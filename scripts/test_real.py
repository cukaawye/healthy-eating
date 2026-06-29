import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from watermark_processor import WatermarkProcessor

def test_real_image():
    image_path = "2026-03-31_13-27-39_UTC_3.jpg"
    output_path = "branded_real_test.jpg"
    
    if not os.path.exists(image_path):
        print(f"Error: {image_path} not found.")
        return
        
    processor = WatermarkProcessor()
    
    print(f"Processing real image: {image_path}...")
    processor.process(
        image_path=image_path,
        domain="HealthyRecipes.com",
        cta="Get the full recipe!",
        output_path=output_path
    )
    
    print(f"Success! Branded image saved to: {output_path}")

if __name__ == "__main__":
    test_real_image()
