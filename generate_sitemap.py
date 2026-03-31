#!/usr/bin/env python3
"""
Sitemap auto-generator for cognivia.eu
Scans all .html files, extracts title and generates fresh sitemap.xml
Run: python3 generate_sitemap.py
"""

import os
import re
from datetime import datetime
from pathlib import Path

SITE_URL = "https://cognivia.eu"
WORKSPACE = Path(__file__).parent
OUTPUT = WORKSPACE / "sitemap.xml"

# Priority rules based on path patterns
PRIORITY_MAP = {
    "index.html": 1.0,
    "produkt.html": 0.9,
    "faq.html": 0.8,
    "faq-produkt.html": 0.8,
    "nauka.html": 0.8,
    "certyfikaty.html": 0.8,
    "kontakt.html": 0.7,
    "opinie.html": 0.7,
    "porownanie.html": 0.8,
    "ranking-nootropikow.html": 0.8,
    "jak-stosowac.html": 0.7,
    "jak-wybrac-suplement.html": 0.7,
    "jak-czytac-etykiety.html": 0.7,
    "jak-zamowic.html": 0.7,
    "skladniki.html": 0.8,
    "o-nas.html": 0.6,
    "dostawa.html": 0.5,
    "zwroty.html": 0.5,
    "regulamin.html": 0.3,
    "polityka-prywatnosci.html": 0.3,
    "polityka-cookies.html": 0.3,
    "merchant-feed.xml": 0.5,
}

CHANGEFREQ_MAP = {
    "index.html": "daily",
    "produkt.html": "weekly",
    "blog/": "weekly",
    "default": "monthly",
}

# Skip these files/dirs
SKIP_PATTERNS = ["404.html", "szukaj.html", "dziekuje-za-zapis.html", "email-templates/", "static/", "scripts/", "copy/", "pages/", "astra-child/", "wordpress-manual-deploy/"]


def get_priority(rel_path):
    """Determine priority based on filename and path. rel_path is relative string."""
    rel_path = str(rel_path)
    name = os.path.basename(rel_path)
    
    if name in PRIORITY_MAP:
        return PRIORITY_MAP[name]
    if rel_path.startswith("blog/") and name != "index.html":
        return 0.7
    # Landing pages
    if name in ["matura.html", "sesja.html", "powrot-do-szkoly.html", "skutki-uboczne-nootropiki.html"]:
        return 0.7
    if "skladniki" in name or "beta-cyklodekstryn" in name or "cytykolina" in name or "kwas-alfa" in name:
        return 0.7
    return 0.6


def get_changefreq(rel_path):
    """Determine change frequency. rel_path is relative string."""
    rel_path = str(rel_path)
    for pattern, freq in CHANGEFREQ_MAP.items():
        if rel_path.startswith(pattern):
            return freq
    return CHANGEFREQ_MAP["default"]


def get_lastmod(filepath):
    """Get file modification date."""
    mtime = os.path.getmtime(filepath)
    return datetime.fromtimestamp(mtime).strftime("%Y-%m-%d")


def extract_title(filepath):
    """Extract <title> from HTML file."""
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read(4096)  # Only read first 4KB
        match = re.search(r"<title[^>]*>(.*?)</title>", content, re.IGNORECASE | re.DOTALL)
        if match:
            return match.group(1).strip()
    except Exception:
        pass
    return None


def should_skip(rel_path):
    """Check if file should be skipped. rel_path is a string relative to WORKSPACE."""
    rel_path = str(rel_path)
    for pattern in SKIP_PATTERNS:
        if rel_path.startswith(pattern) or rel_path == pattern:
            return True
    return False


def scan_files():
    """Scan workspace for .html files and merchant-feed.xml."""
    files = []
    
    # Scan HTML files
    for html_file in sorted(WORKSPACE.rglob("*.html")):
        rel = str(html_file.relative_to(WORKSPACE))
        if should_skip(rel):
            continue
        files.append(html_file)
    
    # Add merchant feed
    merchant = WORKSPACE / "merchant-feed.xml"
    if merchant.exists():
        files.append(merchant)
    
    return files


def generate_sitemap(files):
    """Generate sitemap XML content."""
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    
    for filepath in files:
        rel = str(filepath.relative_to(WORKSPACE))
        
        # Build URL
        if rel == "merchant-feed.xml":
            url = f"{SITE_URL}/merchant-feed.xml"
        elif rel == "index.html":
            url = SITE_URL + "/"
        else:
            url = f"{SITE_URL}/{rel}"
        
        priority = get_priority(rel)
        changefreq = get_changefreq(rel)
        lastmod = get_lastmod(filepath)
        
        lines.append("  <url>")
        lines.append(f"    <loc>{url}</loc>")
        lines.append(f"    <lastmod>{lastmod}</lastmod>")
        lines.append(f"    <changefreq>{changefreq}</changefreq>")
        lines.append(f"    <priority>{priority:.1f}</priority>")
        lines.append("  </url>")
    
    lines.append("</urlset>")
    return "\n".join(lines) + "\n"


def main():
    files = scan_files()
    print(f"Found {len(files)} pages to include in sitemap")
    
    sitemap = generate_sitemap(files)
    
    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write(sitemap)
    
    print(f"Sitemap written to {OUTPUT}")
    print(f"Total URLs: {len(files)}")
    
    # Show sample
    for f in files[:5]:
        rel = f.relative_to(WORKSPACE)
        print(f"  - {rel} (priority={get_priority(rel)}, lastmod={get_lastmod(f)})")
    if len(files) > 5:
        print(f"  ... and {len(files)-5} more")


if __name__ == "__main__":
    main()
