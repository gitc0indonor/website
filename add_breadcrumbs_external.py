#!/usr/bin/env python3
"""Add breadcrumbs to pages with external CSS (no </style> tag)."""
import json, os

WEB = "/root/.openclaw/workspace/website"

PAGES = {
    "ingredients.html": {
        "trail": [("Strona główna", "/"), ("Składniki", "/ingredients.html")],
        "css_type": "eb"
    },
    "koszyk.html": {
        "trail": [("Strona główna", "/"), ("Koszyk", "/koszyk.html")],
        "css_type": "eb"
    },
    "kasa.html": {
        "trail": [("Strona główna", "/"), ("Kasa", "/kasa.html")],
        "css_type": "eb"
    },
}

BREADCRUMB_CSS_EB = """<style>
    .breadcrumb {
      max-width: 900px;
      margin: 100px auto 0;
      padding: 0 5%;
      font-size: 12px;
      color: #888;
    }
    .breadcrumb a { color: #2D6642; text-decoration: none; }
    .breadcrumb a:hover { text-decoration: underline; }
    .breadcrumb span { margin: 0 6px; opacity: 0.4; }
</style>"""

def make_breadcrumb_jsonld(trail, base="https://cognivia.eu"):
    items = []
    for i, (name, path) in enumerate(trail, 1):
        items.append({
            "@type": "ListItem",
            "position": i,
            "name": name,
            "item": base + path if path != "/" else base
        })
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}

def make_breadcrumb_html(trail):
    parts = ['<nav class="breadcrumb" aria-label="Nawigacja okruszkowa">']
    for i, (name, path) in enumerate(trail):
        if i > 0:
            parts.append('<span>›</span>')
        if i < len(trail) - 1:
            parts.append(f'<a href="{path}">{name}</a>')
        else:
            parts.append(f'<span>{name}</span>')
    parts.append('</nav>')
    return '\n'.join(parts)

for filepath, cfg in PAGES.items():
    full = os.path.join(WEB, filepath)
    if not os.path.exists(full):
        print(f"MISSING: {filepath}")
        continue
    
    with open(full, 'r') as f:
        content = f.read()
    
    if 'breadcrumb' in content:
        print(f"ALREADY HAS: {filepath}")
        continue
    
    # Add CSS + JSON-LD before </head>
    jsonld = make_breadcrumb_jsonld(cfg["trail"])
    jsonld_str = json.dumps(jsonld, ensure_ascii=False, indent=2)
    
    insert = BREADCRUMB_CSS_EB + '\n' + f'<script type="application/ld+json">\n{jsonld_str}\n</script>'
    
    head_close = content.find('</head>')
    if head_close == -1:
        print(f"NO </head>: {filepath}")
        continue
    content = content[:head_close] + insert + '\n' + content[head_close:]
    
    # Add HTML after <body>
    breadcrumb_html = make_breadcrumb_html(cfg["trail"])
    body_open = content.find('<body>')
    if body_open == -1:
        print(f"NO <body>: {filepath}")
        continue
    insert_pos = content.find('\n', body_open) + 1
    content = content[:insert_pos] + breadcrumb_html + '\n' + content[insert_pos:]
    
    with open(full, 'w') as f:
        f.write(content)
    print(f"OK: {filepath}")
