import cloudinary
import cloudinary.uploader
import os

# Configuration
cloudinary.config( 
    cloud_name = "dfdqewd46", 
    api_key = "471132278724294", 
    api_secret = "3QJkfbEXf73SqzmxOlRg0jRCj9k",
    secure=True
)

image_dir = "Healthy Food Ideas"
images = [f for f in os.listdir(image_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]

uploaded_urls = []

print(f"Starting upload of {len(images)} images...")

for img_name in images:
    img_path = os.path.join(image_dir, img_name)
    try:
        # Upload with auto-optimization features enabled in the transformation
        # We'll generate the URL with f_auto, q_auto later, but let's get the public_id first
        result = cloudinary.uploader.upload(img_path, folder="landing_pages")
        # Generate the optimized URL
        optimized_url = result['secure_url'].replace("/upload/", "/upload/f_auto,q_auto/")
        uploaded_urls.append(optimized_url)
        print(f"Uploaded: {img_name} -> {optimized_url}")
    except Exception as e:
        print(f"Failed to upload {img_name}: {e}")

with open("cloudinary_links.txt", "w") as f:
    for url in uploaded_urls:
        f.write(url + "\n")

print("\nAll uploads complete. Links saved to cloudinary_links.txt")
