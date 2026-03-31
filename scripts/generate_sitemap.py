#!/usr/bin/env python3
"""
Sitemap auto-generator for cognivia.eu
Scans all .html files, extracts title and last-modified, generates sitemap.xml
Run via: python3 scripts/generate_sitemap.py
"""

import os
import re
from datetime import datetime
from pathlib import Path

SITE_URL = "https://cognivia.eu"
BASE_DIR = Path(__file__).parent.parent  # website/

# Priority rules based on path
PRIORITY_MAP = {
    "index.html": 1.0,
    "produkt.html": 0.9,
    "faq.html": 0.8,
    "faq-produkt.html": 0.8,
    "nauka.html": 0.8,
    "porownanie.html": 0.8,
    "opinie.html": 0.8,
    "kontakt.html": 0.7,
    "certyfikaty.html": 0.7,
    "skladniki.html": 0.7,
    "jak-stosowac.html": 0.7,
    "jak-wybrac-suplement.html": 0.7,
    "jak-czytac-etykiety.html": 0.7,
    "jak-zamowic.html": 0.7,
    "polityka-prywatnosci.html": 0.3,
    "regulamin.html": 0.3,
    "polityka-cookies.html": 0.3,
    "404.html": 0.1,
}

# Change frequency rules
def get_changefreq(path):
    if path == "merchant-feed.xml":
        return "daily"
    if "blog/" in path and path.endswith("index.html"):
        return "daily"
    if path == "index.html":
        return "daily"
    if "blog/" in path:
        return "monthly"
    if path in ("produkt.html", "opinie.html"):
        return "weekly"
    return "monthly"

def get_priority(filename, rel_path):
    if filename == "merchant-feed.xml":
        return 0.5
    if filename == "manifest.json":
        return 0.2
    if filename in PRIORITY_MAP:
        return PRIORITY_MAP[filename]
    if "blog/" in rel_path and filename != "index.html":
        return 0.7
    return 0.6

def extract_title(filepath):
    """Extract <title> from HTML file"""
    if not filepath.endswith('.html'):
        return os.path.basename(filepath)
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read(4096)  # Read only first 4KB
        match = re.search(r'<title[^>]*>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
        if match:
            return match.group(1).strip()
    except Exception:
        pass
    return ""

def get_last_modified(filepath):
    """Get file modification time as YYYY-MM-DD"""
    try:
        mtime = os.path.getmtime(filepath)
        return datetime.fromtimestamp(mtime).strftime("%Y-%m-%d")
    except Exception:
        return datetime.now().strftime("%Y-%m-%d")

def generate_sitemap():
    html_files = []
    
    for root, dirs, files in os.walk(BASE_DIR):
        # Skip hidden dirs, scripts, email-templates
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ('scripts', 'email-templates', 'node_modules')]
        
        for f in files:
            if f.endswith('.html') and not f.startswith('.'):
                full_path = os.path.join(root, f)
                rel_path = os.path.relpath(full_path, BASE_DIR)
                html_files.append((full_path, rel_path, f))
    
    # Include important non-HTML resources
    for extra in ['merchant-feed.xml', 'manifest.json']:
        extra_path = BASE_DIR / extra
        if extra_path.exists():
            html_files.append((str(extra_path), extra, extra))
    
    # Sort for consistent output
    html_files.sort(key=lambda x: x[1])
    
    urls = []
    today = datetime.now().strftime("%Y-%m-%d")
    
    for full_path, rel_path, filename in html_files:
        url_path = rel_path.replace('\\', '/')  # Windows compat
        url = f"{SITE_URL}/{url_path}"
        lastmod = get_last_modified(full_path)
        changefreq = get_changefreq(url_path)
        priority = get_priority(filename, url_path)
        
        urls.append({
            "loc": url,
            "lastmod": lastmod,
            "changefreq": changefreq,
            "priority": priority,
        })
    
    # Generate XML
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    
    for u in urls:
        lines.append("  <url>")
        lines.append(f"    <loc>{u['loc']}</loc>")
        lines.append(f"    <lastmod>{u['lastmod']}</lastmod>")
        lines.append(f"    <changefreq>{u['changefreq']}</changefreq>")
        lines.append(f"    <priority>{u['priority']}</priority>")
        lines.append("  </url>")
    
    lines.append("</urlset>")
    
    return "\n".join(lines) + "\n"

if __name__ == "__main__":
    sitemap_xml = generate_sitemap()
    output_path = BASE_DIR / "sitemap.xml"
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(sitemap_xml)
    
    # Count URLs
    url_count = sitemap_xml.count("<url>")
    print(f"✅ Sitemap generated: {url_count} URLs → {output_path}")
    print(f"📅 Date: {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}")
