import numpy as np
import cv2
from watermark_processor import WatermarkProcessor
import os

def create_sample_image(path):
    # Create a 800x600 image with some "content" (circles/shapes)
    # to simulate a "busy" and "empty" areas
    img = np.ones((600, 800, 3), dtype=np.uint8) * 255
    
    # Simulate a "subject" in the middle and top-left
    cv2.circle(img, (400, 300), 150, (100, 150, 200), -1) # Middle
    cv2.rectangle(img, (50, 50), (300, 250), (150, 100, 100), -1) # Top-left busy area
    
    # Add some text to simulate detail
    cv2.putText(img, "RECIPE CONTENT", (100, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    
    cv2.imwrite(path, img)
    print(f"Created sample image: {path}")

def main():
    sample_path = "sample_food.jpg"
    output_path = "branded_food.jpg"
    
    # 1. Create a dummy image for testing
    create_sample_image(sample_path)
    
    # 2. Initialize the processor
    processor = WatermarkProcessor()
    
    # 3. Process the image
    print("Finding best placement and adding watermark...")
    processor.process(
        image_path=sample_path,
        domain="HealthyEats.com",
        cta="Click for full recipe!",
        output_path=output_path
    )
    
    print(f"Done! Watermarked image saved to: {output_path}")
    print(f"Best corner found was likely bottom_right because top_left was 'busy'.")

if __name__ == "__main__":
    main()
