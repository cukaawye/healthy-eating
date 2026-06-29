import os
import glob

GA_TAG = """<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-RRXQSNCRWX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-RRXQSNCRWX');
</script>"""

WRAP_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
""" + GA_TAG + "\n</head>\n<body>\n"

ROOT = r"C:\Users\hp\healthy-eating"
count_head = 0
count_wrap = 0
count_skip = 0

for filepath in glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True):
    if ".git" in filepath:
        continue
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    if "G-RRXQSNCRWX" in content:
        count_skip += 1
        print(f"SKIP (already has GA): {os.path.relpath(filepath, ROOT)}")
        continue

    if "<head>" in content:
        content = content.replace("<head>", "<head>\n    " + GA_TAG)
        count_head += 1
        print(f"HEAD: {os.path.relpath(filepath, ROOT)}")
    else:
        content = WRAP_HTML + content + "\n</body>\n</html>\n"
        count_wrap += 1
        print(f"WRAP: {os.path.relpath(filepath, ROOT)}")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print(f"\nDone! {count_head} files got GA in <head>, {count_wrap} files got wrapped, {count_skip} files skipped (already had GA).")
