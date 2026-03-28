#!/usr/bin/env python3
"""Add missing satisfaction guarantee badges and cross-links to blog posts."""

import re

GUARANTEE_HTML = '''
<!-- Satisfaction Guarantee -->
<div style="background: linear-gradient(135deg, #e8f5e9, #f1f8e9); border-radius: 14px; padding: 28px 24px; margin: 32px 0; display: flex; align-items: center; gap: 20px; flex-wrap: wrap; border: 1px solid rgba(45,102,66,0.15);">
  <div style="flex-shrink: 0; width: 56px; height: 56px; background: #2D6642; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #fff; font-size: 22px; font-weight: 700; box-shadow: 0 4px 12px rgba(45,102,66,0.3);">30</div>
  <div style="flex: 1; min-width: 200px;">
    <div style="font-family: 'EB Garamond', serif; font-size: 18px; font-weight: 700; color: #2a2a27; margin-bottom: 4px;">30-dniowa gwarancja satysfakcji</div>
    <p style="font-size: 13px; color: #555; line-height: 1.6; margin: 0;">Nie jesteś zadowolony? Zwrócimy pieniądze za pierwsze opakowanie. Zero ryzyka.</p>
    <a href="produkt.html" style="display: inline-block; margin-top: 8px; font-size: 13px; color: #2D6642; font-weight: 600; text-decoration: none;">Zamów bez ryzyka →</a>
  </div>
</div>
'''

CROSS_LINKS_HTML = '''
<!-- Cross-links -->
<div style="margin: 32px 0; padding: 24px; background: #faf8f5; border-radius: 14px; border: 1px solid #e8e0d0;">
  <div style="font-family: 'EB Garamond', serif; font-size: 18px; font-weight: 700; color: #2a2a27; margin-bottom: 16px;">📚 Powiązane artykuły</div>
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px;">
    <a href="suplementy-a-kofeina.html" style="text-decoration: none; background: white; border-radius: 10px; padding: 14px; border: 1px solid #e8e0d0; transition: transform 0.2s, box-shadow 0.2s;">
      <div style="font-size: 20px; margin-bottom: 6px;">☕</div>
      <div style="font-family: 'EB Garamond', serif; font-size: 14px; font-weight: 600; color: #2a2a27;">Suplementy a kofeina</div>
      <div style="font-size: 12px; color: #888; margin-top: 4px;">Porównanie mechanizmów działania</div>
    </a>
    <a href="cytykolina-przewodnik-kompletny.html" style="text-decoration: none; background: white; border-radius: 10px; padding: 14px; border: 1px solid #e8e0d0; transition: transform 0.2s, box-shadow 0.2s;">
      <div style="font-size: 20px; margin-bottom: 6px;">🧠</div>
      <div style="font-family: 'EB Garamond', serif; font-size: 14px; font-weight: 600; color: #2a2a27;">Przewodnik po cytykolinie</div>
      <div style="font-size: 12px; color: #888; margin-top: 4px;">Kompletna analiza CDP-choliny</div>
    </a>
    <a href="produkt.html" style="text-decoration: none; background: white; border-radius: 10px; padding: 14px; border: 1px solid #e8e0d0; transition: transform 0.2s, box-shadow 0.2s;">
      <div style="font-size: 20px; margin-bottom: 6px;">💊</div>
      <div style="font-family: 'EB Garamond', serif; font-size: 14px; font-weight: 600; color: #2a2a27;">CogniCit — poznaj produkt</div>
      <div style="font-size: 12px; color: #888; margin-top: 4px;">3 synergistyczne składniki</div>
    </a>
  </div>
</div>
'''

# Files missing guarantee
guarantee_files = [
    'blog/kiedy-zaczac-suplementacje.html',
    'blog/koszt-suplementacji.html',
]

# Files missing cross-links
crosslink_files = [
    'blog/chroniczne-zmeczenie-umyslowe.html',
    'blog/czy-suplementy-dzialaja.html',
    'blog/ranking-nootropikow-2026.html',
    'blog/suplementy-a-kofeina.html',
]

def add_before_footer(filepath, html_block):
    with open(filepath, 'r') as f:
        content = f.read()
    if 'gwarancja satysfakcji' in content.lower() and html_block == GUARANTEE_HTML:
        print(f"  SKIP {filepath} (already has guarantee)")
        return False
    # Insert before <footer>
    content = content.replace('<footer>', html_block + '\n<footer>', 1)
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"  OK {filepath}")
    return True

def add_before_trust_bar_or_footer(filepath, html_block):
    with open(filepath, 'r') as f:
        content = f.read()
    if 'powiązane' in content.lower() or 'polecane artykuły' in content.lower():
        print(f"  SKIP {filepath} (already has cross-links)")
        return False
    # Try trust-bar first, then footer
    if '<div class="trust-bar' in content:
        content = content.replace('<div class="trust-bar', html_block + '\n<div class="trust-bar', 1)
    elif '<footer>' in content:
        content = content.replace('<footer>', html_block + '\n<footer>', 1)
    else:
        print(f"  WARN {filepath} (no insertion point found)")
        return False
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"  OK {filepath}")
    return True

print("Adding satisfaction guarantee to blog posts:")
for f in guarantee_files:
    add_before_footer(f, GUARANTEE_HTML)

print("\nAdding cross-links to blog posts:")
for f in crosslink_files:
    add_before_trust_bar_or_footer(f, CROSS_LINKS_HTML)

print("\nDone!")
