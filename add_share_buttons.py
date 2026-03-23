#!/usr/bin/env python3
"""Add social share buttons to blog post pages."""
import os

WEB = "/root/.openclaw/workspace/website"

BLOG_POSTS = [
    "blog/cytykolina.html",
    "blog/antyoksydanty.html", 
    "blog/beta-cyklodekstryna.html",
    "blog/suplement-vs-lek.html",
]

SHARE_CSS = """
    .share-section {
      max-width: 800px;
      margin: 48px auto;
      padding: 24px 0;
      border-top: 1px solid rgba(26,26,26,0.08);
      border-bottom: 1px solid rgba(26,26,26,0.08);
      text-align: center;
    }
    .share-section p {
      font-size: 13px;
      color: #999;
      text-transform: uppercase;
      letter-spacing: 1.5px;
      margin-bottom: 16px;
    }
    .share-buttons {
      display: flex;
      gap: 12px;
      justify-content: center;
      flex-wrap: wrap;
    }
    .share-btn {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 10px 20px;
      border-radius: 4px;
      font-size: 13px;
      font-weight: 500;
      text-decoration: none;
      color: white;
      transition: opacity 0.2s, transform 0.2s;
    }
    .share-btn:hover { opacity: 0.85; transform: translateY(-1px); }
    .share-btn.fb { background: #1877F2; }
    .share-btn.tw { background: #1a1a1a; }
    .share-btn.li { background: #0A66C2; }
    .share-btn svg { width: 16px; height: 16px; fill: currentColor; }
"""

SHARE_HTML = """    <div class="share-section">
      <p>Udostępnij artykuł</p>
      <div class="share-buttons">
        <a class="share-btn fb" href="https://www.facebook.com/sharer/sharer.php?u={url}" target="_blank" rel="noopener" aria-label="Udostępnij na Facebook">
          <svg viewBox="0 0 24 24"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
          Facebook
        </a>
        <a class="share-btn tw" href="https://twitter.com/intent/tweet?url={url}&text={title}" target="_blank" rel="noopener" aria-label="Udostępnij na X/Twitter">
          <svg viewBox="0 0 24 24"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
          X / Twitter
        </a>
        <a class="share-btn li" href="https://www.linkedin.com/sharing/share-offsite/?url={url}" target="_blank" rel="noopener" aria-label="Udostępnij na LinkedIn">
          <svg viewBox="0 0 24 24"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
          LinkedIn
        </a>
      </div>
    </div>
"""

BASE_URL = "https://cognivia.eu"

for filepath in BLOG_POSTS:
    full = os.path.join(WEB, filepath)
    if not os.path.exists(full):
        print(f"MISSING: {filepath}")
        continue
    
    with open(full, 'r') as f:
        content = f.read()
    
    if 'share-section' in content:
        print(f"ALREADY HAS: {filepath}")
        continue
    
    # Get page URL
    url = BASE_URL + "/" + filepath
    
    # Get title from <title> tag
    import re
    title_match = re.search(r'<title>([^<]+)</title>', content)
    title = title_match.group(1) if title_match else "Cognivia Blog"
    
    # URL encode
    from urllib.parse import quote
    url_enc = quote(url, safe='')
    title_enc = quote(title, safe='')
    
    share_html = SHARE_HTML.replace("{url}", url_enc).replace("{title}", title_enc)
    
    # Insert CSS before last </style>
    last_style = content.rfind('</style>')
    if last_style == -1:
        print(f"NO </style>: {filepath}")
        continue
    content = content[:last_style] + SHARE_CSS + content[last_style:]
    
    # Insert share buttons before <footer>
    footer_pos = content.find('<footer>')
    if footer_pos == -1:
        # Try before </body>
        footer_pos = content.find('</body>')
        if footer_pos == -1:
            print(f"NO <footer> or </body>: {filepath}")
            continue
    
    content = content[:footer_pos] + share_html + '\n' + content[footer_pos:]
    
    with open(full, 'w') as f:
        f.write(content)
    print(f"OK: {filepath}")

print("\nDone!")
