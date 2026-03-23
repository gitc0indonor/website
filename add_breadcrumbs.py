#!/usr/bin/env python3
"""Add breadcrumbs and social share buttons to cognivia.eu pages."""
import re, os

WEB = "/root/.openclaw/workspace/website"

# Page -> breadcrumb trail
BREADCRUMBS = {
    "produkt.html": [("Strona główna", "/"), ("Produkt", "/produkt.html")],
    "faq.html": [("Strona główna", "/"), ("FAQ", "/faq.html")],
    "nauka.html": [("Strona główna", "/"), ("Nauka", "/nauka.html")],
    "o-nas.html": [("Strona główna", "/"), ("O nas", "/o-nas.html")],
    "jak-stosowac.html": [("Strona główna", "/"), ("Jak stosować", "/jak-stosowac.html")],
    "dostawa.html": [("Strona główna", "/"), ("Dostawa i płatność", "/dostawa.html")],
    "zwroty.html": [("Strona główna", "/"), ("Zwroty i reklamacje", "/zwroty.html")],
    "regulamin.html": [("Strona główna", "/"), ("Regulamin", "/regulamin.html")],
    "polityka-prywatnosci.html": [("Strona główna", "/"), ("Polityka prywatności", "/polityka-prywatnosci.html")],
    "ingredients.html": [("Strona główna", "/"), ("Składniki", "/ingredients.html")],
    "koszyk.html": [("Strona główna", "/"), ("Koszyk", "/koszyk.html")],
    "kasa.html": [("Strona główna", "/"), ("Kasa", "/kasa.html")],
    "blog/index.html": [("Strona główna", "/"), ("Blog", "/blog/")],
    "blog/cytykolina.html": [("Strona główna", "/"), ("Blog", "/blog/"), ("Cytykolina", "/blog/cytykolina.html")],
    "blog/antyoksydanty.html": [("Strona główna", "/"), ("Blog", "/blog/"), ("Antyoksydanty", "/blog/antyoksydanty.html")],
    "blog/beta-cyklodekstryna.html": [("Strona główna", "/"), ("Blog", "/blog/"), ("Beta-cyklodekstryna", "/blog/beta-cyklodekstryna.html")],
    "blog/suplement-vs-lek.html": [("Strona główna", "/"), ("Blog", "/blog/"), ("Suplement vs lek", "/blog/suplement-vs-lek.html")],
}

# Pages that already have breadcrumbs
SKIP = {"kwas-alfa-liponowy.html", "cytykolina.html", "beta-cyklodekstryna.html", "404.html", "potwierdzenie.html"}

def make_breadcrumb_jsonld(trail, base="https://cognivia.eu"):
    items = []
    for i, (name, path) in enumerate(trail, 1):
        items.append({
            "@type": "ListItem",
            "position": i,
            "name": name,
            "item": base + path if path != "/" else base
        })
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": items
    }

import json

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

# CSS for EB Garamond pages (produkt, faq, dostawa, zwroty, regulamin, polityka, ingredients, koszyk, kasa)
BREADCRUMB_CSS_EB = """
    .breadcrumb {
      max-width: 900px;
      margin: 100px auto 0;
      padding: 0 5%;
      font-size: 12px;
      color: #888;
    }
    .breadcrumb a { color: var(--cognivia-green); text-decoration: none; }
    .breadcrumb a:hover { text-decoration: underline; }
    .breadcrumb span { margin: 0 6px; opacity: 0.4; }
"""

# CSS for Playfair Display pages (o-nas, nauka, blog)
BREADCRUMB_CSS_PF = """
    .breadcrumb {
      max-width: 900px;
      margin: 100px auto 0;
      padding: 0 6%;
      font-size: 12px;
      color: var(--soft-text, #5a5a58);
    }
    .breadcrumb a { color: var(--gold, #c9a96e); text-decoration: none; }
    .breadcrumb a:hover { text-decoration: underline; }
    .breadcrumb span { margin: 0 6px; opacity: 0.4; }
"""

PLAYFAIR_PAGES = {"o-nas.html", "nauka.html", "blog/index.html", "blog/cytykolina.html",
                  "blog/antyoksydanty.html", "blog/beta-cyklodekstryna.html", "blog/suplement-vs-lek.html"}

count = 0
for filepath, trail in BREADCRUMBS.items():
    if filepath in SKIP:
        continue
    
    full = os.path.join(WEB, filepath)
    if not os.path.exists(full):
        print(f"MISSING: {filepath}")
        continue
    
    with open(full, 'r') as f:
        content = f.read()
    
    if 'breadcrumb' in content:
        print(f"ALREADY HAS: {filepath}")
        continue
    
    # Choose CSS
    css = BREADCRUMB_CSS_PF if filepath in PLAYFAIR_PAGES else BREADCRUMB_CSS_EB
    
    # Insert CSS before </style> (last </style> tag)
    last_style = content.rfind('</style>')
    if last_style == -1:
        print(f"NO </style>: {filepath}")
        continue
    content = content[:last_style] + css + content[last_style:]
    
    # Insert JSON-LD before </head>
    jsonld = make_breadcrumb_jsonld(trail)
    jsonld_str = json.dumps(jsonld, ensure_ascii=False, indent=2)
    jsonld_html = f'<script type="application/ld+json">\n{jsonld_str}\n</script>'
    
    head_close = content.find('</head>')
    if head_close == -1:
        print(f"NO </head>: {filepath}")
        continue
    content = content[:head_close] + jsonld_html + '\n' + content[head_close:]
    
    # Insert HTML after <body>
    breadcrumb_html = make_breadcrumb_html(trail)
    body_open = content.find('<body>')
    if body_open == -1:
        print(f"NO <body>: {filepath}")
        continue
    insert_pos = content.find('\n', body_open) + 1
    content = content[:insert_pos] + breadcrumb_html + '\n' + content[insert_pos:]
    
    with open(full, 'w') as f:
        f.write(content)
    
    count += 1
    print(f"OK: {filepath}")

print(f"\nBreadcrumbs added to {count} pages")
