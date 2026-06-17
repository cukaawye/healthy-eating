import os
import json
import random

# Load mapping
mapping_path = "landing_pages/image_mapping.json"
if os.path.exists(mapping_path):
    with open(mapping_path, "r") as f:
        image_mapping = json.load(f)
else:
    image_mapping = {}

# Load new github links
github_links_path = "landing_pages/github_image_links.txt"
if os.path.exists(github_links_path):
    with open(github_links_path, "r") as f:
        github_links = [line.strip() for line in f if line.strip()]
else:
    github_links = []

repo = "cukaawye/healthy-eating"
branch = "high-quality-images"
# Updated to use the specific branch so we can test before merging to main
target_cdn_prefix = f"https://cdn.jsdelivr.net/gh/{repo}@{branch}/assets/images"

def update_html_file(file_path):
    if not os.path.exists(file_path):
        return
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # First, replace the @main with @high-quality-images if they already exist
    new_content = content.replace("@main/assets/images", f"@{branch}/assets/images")
    
    # Replace known mappings (ensuring they use the branch name)
    for old_url, new_url in image_mapping.items():
        branch_url = new_url.replace("@main/", f"@{branch}/")
        new_content = new_content.replace(old_url, branch_url)
    
    # Also handle any other cloudinary links
    import re
    cloudinary_pattern = r'https://res\.cloudinary\.com/dfdqewd46/image/upload/[^"\'\s>]+'
    found_links = re.findall(cloudinary_pattern, new_content)
    
    for link in found_links:
        # Avoid replacing already replaced ones
        if "cdn.jsdelivr.net" not in link:
            random_good_link = random.choice(github_links).replace("@main/", f"@{branch}/")
            new_content = new_content.replace(link, random_good_link)
            print(f"Replaced unknown link in {file_path} with {random_good_link}")

    if new_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated: {file_path}")

# 1. Update existing folders
for item in os.listdir("."):
    if os.path.isdir(item) and item not in ["landing_pages", "assets", ".git", ".gemini"]:
        index_path = os.path.join(item, "index.html")
        if os.path.exists(index_path):
            update_html_file(index_path)

# 2. Update variation files in landing_pages if they exist
lp_dir = "landing_pages/landing_pages"
if os.path.exists(lp_dir):
    for item in os.listdir(lp_dir):
        if item.startswith("variation_") and item.endswith(".html"):
            update_html_file(os.path.join(lp_dir, item))

print(f"\nAll landing pages updated to use the '{branch}' CDN links.")
