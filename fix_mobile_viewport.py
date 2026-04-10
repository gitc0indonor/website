#!/usr/bin/env python3
import os

viewport_tag = '<meta name="viewport" content="width=device-width, initial-scale=1.0">'

fixed = 0
skipped = 0

for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.html'):
            path = os.path.join(root, file)
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if 'viewport' not in content:
                    if '</head>' in content:
                        content = content.replace('</head>', f'  {viewport_tag}\n</head>')
                        with open(path, 'w', encoding='utf-8') as f:
                            f.write(content)
                        fixed +=1
                    else:
                        skipped +=1
            except Exception as e:
                print(f"Error {path}: {e}")

print(f"✅ Fixed: {fixed} pages added mobile viewport")
print(f"⚠️  Skipped: {skipped} pages")
