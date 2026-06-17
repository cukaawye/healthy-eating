import cv2
import os

image_dir = "landing_pages/Healthy Food Ideas"
output_dir = "assets/images"
os.makedirs(output_dir, exist_ok=True)

# Get sorted list of images (same order as used in upload_to_cloudinary.py)
images = sorted([f for f in os.listdir(image_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))])

# Load cloudinary links
cloudinary_links = []
if os.path.exists("landing_pages/cloudinary_links.txt"):
    with open("landing_pages/cloudinary_links.txt", "r") as f:
        cloudinary_links = [line.strip() for line in f if line.strip()]

repo = "cukaawye/healthy-eating"
base_cdn_url = f"https://cdn.jsdelivr.net/gh/{repo}@main/assets/images"

github_links = []
mapping = {} # cloudinary_url -> github_url

good_count = 0
for i, img_name in enumerate(images):
    img_path = os.path.join(image_dir, img_name)
    img = cv2.imread(img_path)
    
    if img is not None:
        h, w, _ = img.shape
        if w >= 600:
            good_count += 1
            new_name = f"food_{good_count}.webp"
            new_path = os.path.join(output_dir, new_name)
            
            # Save as WebP with high quality
            cv2.imwrite(new_path, img, [int(cv2.IMWRITE_WEBP_QUALITY), 90])
            
            github_url = f"{base_cdn_url}/{new_name}"
            github_links.append(github_url)
            
            if i < len(cloudinary_links):
                mapping[cloudinary_links[i]] = github_url
            
            print(f"Processed: {img_name} ({w}x{h}) -> {new_name}")
        else:
            print(f"Skipped (Low Res): {img_name} ({w}x{h})")
    else:
        print(f"Could not read: {img_name}")

# Write the new github links
with open("landing_pages/github_image_links.txt", "w") as f:
    for link in github_links:
        f.write(link + "\n")

# Write the mapping for later replacement
import json
with open("landing_pages/image_mapping.json", "w") as f:
    json.dump(mapping, f, indent=4)

print(f"\nFinished. {good_count} high-quality images prepared in 'assets/images'.")
print("New links saved to 'landing_pages/github_image_links.txt'.")
print("Mapping saved to 'landing_pages/image_mapping.json'.")
