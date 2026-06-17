import os
import re
import random

lp_dir = "landing_pages/landing_pages"
all_files = [f for f in os.listdir(lp_dir) if f.startswith("variation_") and f.endswith(".html")]

# Select 30 random pages (or all if less than 30)
sample_size = min(30, len(all_files))
selected_files = random.sample(all_files, sample_size)

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Image Quality Audit - 30 Random Pages</title>
    <style>
        body { font-family: 'Segoe UI', sans-serif; padding: 40px; background: #f0f2f5; color: #1c1e21; }
        h1 { text-align: center; color: #606C38; margin-bottom: 10px; }
        .subtitle { text-align: center; color: #666; margin-bottom: 40px; }
        .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(350px, 1fr)); gap: 30px; }
        .card { background: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); transition: transform 0.2s; }
        .card:hover { transform: translateY(-5px); }
        .card-header { font-weight: bold; margin-bottom: 15px; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #eee; padding-bottom: 10px; }
        .filename { color: #D4A373; font-size: 0.9em; }
        .image-container { position: relative; width: 100%; aspect-ratio: 16/9; overflow: hidden; border-radius: 8px; background: #eee; }
        img { width: 100%; height: 100%; object-fit: cover; display: block; }
        .image-label { position: absolute; bottom: 0; left: 0; right: 0; background: rgba(0,0,0,0.6); color: white; padding: 5px 10px; font-size: 0.8em; }
        .btn-link { display: block; margin-top: 15px; text-align: center; color: #606C38; text-decoration: none; font-size: 0.9em; font-weight: 600; }
        .btn-link:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <h1>Visual Quality Audit</h1>
    <p class="subtitle">Showing hero images from 30 random landing page variations. All images should be sharp and high-resolution.</p>
    <div class="grid">
"""

img_pattern = r'<img src="([^"]+)" class="hero-img"'

for filename in selected_files:
    path = os.path.join(lp_dir, filename)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Find the first image (hero image)
    match = re.search(img_pattern, content)
    if match:
        cdn_url = match.group(1)
        # Convert CDN URL back to local path for previewing
        # Example: https://cdn.jsdelivr.net/gh/cukaawye/healthy-eating@main/assets/images/food_5.webp
        # Becomes: assets/images/food_5.webp
        img_src = cdn_url.split('/assets/images/')[-1]
        img_src = f"assets/images/{img_src}"
    else:
        img_src = "https://via.placeholder.com/600x400?text=No+Image+Found"
    
    # Get the variation ID from filename
    var_id = filename.replace("variation_", "").replace(".html", "")
    
    html_content += f"""
        <div class="card">
            <div class="card-header">
                <span>Variation #{var_id}</span>
                <span class="filename">{filename}</span>
            </div>
            <div class="image-container">
                <img src="{img_src}" alt="Preview">
                <div class="image-label">{img_src.split('/')[-1]}</div>
            </div>
            <a href="{path}" target="_blank" class="btn-link">View Full Page</a>
        </div>
    """

html_content += """
    </div>
    <div style="text-align:center; margin-top: 50px; color: #888; font-size: 0.8em;">
        &copy; 2026 Visual Audit Tool
    </div>
</body>
</html>
"""

with open("preview_audit.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Audit report generated: preview_audit.html with {sample_size} random pages.")
