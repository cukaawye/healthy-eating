import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

class WatermarkProcessor:
    def __init__(self, font_path="C:\\Windows\\Fonts\\arial.ttf", default_font_size=24):
        self.font_path = font_path
        self.default_font_size = default_font_size

    def _get_corner_roi(self, img_gray, corner, size_percent=0.25):
        h, w = img_gray.shape
        rw, rh = int(w * size_percent), int(h * size_percent)
        
        if corner == "top_left":
            return img_gray[0:rh, 0:rw]
        elif corner == "top_right":
            return img_gray[0:rh, w-rw:w]
        elif corner == "bottom_left":
            return img_gray[h-rh:h, 0:rw]
        elif corner == "bottom_right":
            return img_gray[h-rh:h, w-rw:w]
        return None

    def find_best_corner(self, image_path):
        """Analyzes 4 corners and returns the one with the lowest detail (variance)."""
        img = cv2.imread(image_path)
        if img is None:
            raise ValueError(f"Could not read image at {image_path}")
            
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        corners = ["bottom_right", "bottom_left", "top_right", "top_left"]
        scores = {}
        
        for c in corners:
            roi = self._get_corner_roi(gray, c)
            # Use Laplacian variance to measure detail/busyness
            variance = cv2.Laplacian(roi, cv2.CV_64F).var()
            # Also consider mean brightness to avoid very dark/bright extremes if possible
            mean_val = np.mean(roi)
            
            # Weighted score: low variance is good. 
            # We prefer bottom corners (multiplier 1.0) over top (multiplier 1.2)
            bias = 1.0 if "bottom" in c else 1.2
            scores[c] = variance * bias

        return min(scores, key=scores.get)

    def _draw_rounded_rect(self, draw, coords, radius, fill, outline=None, width=1):
        """Helper to draw a rounded rectangle."""
        x1, y1, x2, y2 = coords
        draw.rectangle([x1 + radius, y1, x2 - radius, y2], fill=fill)
        draw.rectangle([x1, y1 + radius, x2, y2 - radius], fill=fill)
        draw.pieslice([x1, y1, x1 + radius * 2, y1 + radius * 2], 180, 270, fill=fill)
        draw.pieslice([x2 - radius * 2, y1, x2, y1 + radius * 2], 270, 360, fill=fill)
        draw.pieslice([x1, y2 - radius * 2, x1 + radius * 2, y2], 90, 180, fill=fill)
        draw.pieslice([x2 - radius * 2, y2 - radius * 2, x2, y2], 0, 90, fill=fill)
        if outline:
            # Simple outline implementation for rounded rect
            draw.line([x1 + radius, y1, x2 - radius, y1], fill=outline, width=width)
            draw.line([x1 + radius, y2, x2 - radius, y2], fill=outline, width=width)
            draw.line([x1, y1 + radius, x1, y2 - radius], fill=outline, width=width)
            draw.line([x2, y1 + radius, x2, y2 - radius], fill=outline, width=width)

    def process(self, image_path, domain=None, cta=None, output_path=None, padding=40, style="aesthetic"):
        """
        Adds domain and CTA to the best corner.
        Styles: 'dark' (classic), 'aesthetic' (lifestyle/soft white), 'minimal' (no box, soft shadow)
        """
        best_corner = self.find_best_corner(image_path)
        
        with Image.open(image_path) as img:
            img = img.convert("RGBA")
            w, h = img.size
            
            # Lifestyle spacing: slightly larger text and more padding
            base_size = max(20, int(w * 0.028))
            try:
                font_domain = ImageFont.truetype(self.font_path, base_size)
                font_cta = ImageFont.truetype(self.font_path, int(base_size * 0.75 if domain else base_size))
            except:
                font_domain = ImageFont.load_default()
                font_cta = ImageFont.load_default()

            domain_text = domain.lower() if domain else ""
            cta_text = cta.strip() if cta else ""
            
            if not domain_text and not cta_text:
                return img.convert("RGB")

            draw = ImageDraw.Draw(img)
            
            dw, dh = 0, 0
            if domain_text:
                d_bbox = draw.textbbox((0, 0), domain_text, font=font_domain)
                dw, dh = d_bbox[2] - d_bbox[0], d_bbox[3] - d_bbox[1]
            
            cw, ch = 0, 0
            if cta_text:
                c_bbox = draw.textbbox((0, 0), cta_text, font=font_cta)
                cw, ch = c_bbox[2] - c_bbox[0], c_bbox[3] - c_bbox[1]

            # Box configuration based on style
            if style == "aesthetic":
                bg_color = (255, 255, 255, 195)
                text_color = (30, 30, 30, 255)
                cta_color = (30, 30, 30, 255)
                box_radius = 22
            elif style == "minimal":
                bg_color = (0, 0, 0, 0)
                text_color = (255, 255, 255, 255)
                cta_color = (255, 255, 255, 255)
                box_radius = 0
            else: # dark
                bg_color = (0, 0, 0, 160)
                text_color = (255, 255, 255, 255)
                cta_color = (255, 255, 255, 255)
                box_radius = 15

            box_w = max(dw, cw) + 60
            if domain_text and cta_text:
                box_h = dh + ch + 52
            else:
                box_h = (dh if domain_text else ch) + 40
            
            if best_corner == "top_left": bx, by = padding, padding
            elif best_corner == "top_right": bx, by = w - box_w - padding, padding
            elif best_corner == "bottom_left": bx, by = padding, h - box_h - padding
            else: bx, by = w - box_w - padding, h - box_h - padding

            overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
            overlay_draw = ImageDraw.Draw(overlay)
            
            if style != "minimal":
                self._draw_rounded_rect(
                    overlay_draw, 
                    [bx, by, bx + box_w, by + box_h], 
                    radius=box_radius, 
                    fill=bg_color
                )
            
            img = Image.alpha_composite(img, overlay)
            draw = ImageDraw.Draw(img)
            
            def draw_text_with_shadow(draw, pos, text, font, fill, shadow_fill=(0,0,0,80)):
                x, y = pos
                draw.text((x+1, y+1), text, font=font, fill=shadow_fill)
                draw.text((x, y), text, font=font, fill=fill)

            current_y = by + 20
            
            if domain_text:
                domain_x = bx + (box_w - dw) // 2
                if style == "minimal":
                    draw_text_with_shadow(draw, (domain_x, current_y), domain_text, font_domain, text_color)
                else:
                    draw.text((domain_x, current_y), domain_text, font=font_domain, fill=text_color)
                current_y += dh + 12

            if cta_text:
                cta_x = bx + (box_w - cw) // 2
                if not domain_text:
                    cta_y = by + (box_h - ch) // 2 - 2
                else:
                    cta_y = current_y
                
                if style == "minimal":
                    draw_text_with_shadow(draw, (cta_x, cta_y), cta_text, font_cta, cta_color)
                else:
                    draw.text((cta_x, cta_y), cta_text, font=font_cta, fill=cta_color)

            final_img = img.convert("RGB")
            if output_path:
                final_img.save(output_path, quality=95)
            return final_img

if __name__ == "__main__":
    # Test script if run directly
    print("This module is intended to be imported.")
