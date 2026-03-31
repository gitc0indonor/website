#!/usr/bin/env python3
"""
Google Merchant Center Product Feed Auto-Generator
Run weekly via cron to keep merchant-feed.xml fresh.
Usage: python3 scripts/update_merchant_feed.py
"""

from datetime import datetime
import os

SITE_URL = "https://cognivia.eu"
FEED_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "merchant-feed.xml")

now = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

PRODUCTS = [
    {
        "id": "cognicit-1box",
        "title": "CogniCit — Suplement nootropowy (30 kapsułek)",
        "description": "CogniCit to synergiczny suplement nootropowy z cytykoliną (300 mg), kwasem alfa-liponowym (250 mg) i beta-cyklodekstryną (250 mg). Certyfikat GMP, zgłoszony do GIS. Zero kofeiny.",
        "price": "79.00 PLN",
        "weight": "0.15 kg",
    },
    {
        "id": "cognicit-2pack",
        "title": "CogniCit — 2× opakowanie (60 kapsułek, -5%)",
        "description": "Zestaw 2 opakowań CogniCit z rabatem 5%. 60 dni suplementacji. Cytykolina 300 mg + ALA 250 mg + β-CD 250 mg. GMP, GIS.",
        "price": "150.00 PLN",
        "sale_price": "150.00 PLN",
        "weight": "0.30 kg",
    },
    {
        "id": "cognicit-3pack",
        "title": "CogniCit — 3× opakowanie (90 kapsułek, -10%)",
        "description": "Zestaw 3 opakowań CogniCit z rabatem 10%. 90 dni suplementacji. Cytykolina 300 mg + ALA 250 mg + β-CD 250 mg. GMP, GIS.",
        "price": "213.00 PLN",
        "sale_price": "213.00 PLN",
        "weight": "0.45 kg",
    },
]

def xml_item(p):
    sale = ""
    if p.get("sale_price"):
        sale = f"    <g:sale_price>{p['sale_price']}</g:sale_price>\n"
    return f"""  <item>
    <g:id>{p['id']}</g:id>
    <g:title>{p['title']}</g:title>
    <g:description>{p['description']}</g:description>
    <g:link>{SITE_URL}/produkt.html</g:link>
    <g:image_link>{SITE_URL}/assets/produkt-front.webp</g:image_link>
    <g:availability>in stock</g:availability>
    <g:price>{p['price']}</g:price>
{sale}    <g:brand>Cognivia</g:brand>
    <g:condition>new</g:condition>
    <g:google_product_category>Health &amp; Beauty &gt; Health Care &gt; Vitamins &amp; Supplements</g:google_product_category>
    <g:product_type>Suplement diety &gt; Nootropowy</g:product_type>
    <g:shipping_weight>{p['weight']}</g:shipping_weight>
    <g:mpn>{p['id'].upper()}</g:mpn>
    <g:identifier_exists>no</g:identifier_exists>
    <g:shipping>
      <g:service>InPost</g:service>
      <g:price>12.99 PLN</g:price>
      <g:country>PL</g:country>
    </g:shipping>
    <g:shipping>
      <g:service>DPD</g:service>
      <g:price>15.99 PLN</g:price>
      <g:country>PL</g:country>
    </g:shipping>
    <g:shipping>
      <g:service>Poczta Polska</g:service>
      <g:price>10.99 PLN</g:price>
      <g:country>PL</g:country>
    </g:shipping>
    <g:shipping_label>Darmowa dostawa od 120 zł</g:shipping_label>
    <g:custom_label_0>nootropowy</g:custom_label_0>
    <g:custom_label_1>cognicit</g:custom_label_1>
    <g:custom_label_2>standard</g:custom_label_2>
    <g:custom_label_3>direct</g:custom_label_3>
    <g:custom_label_4>bestseller</g:custom_label_4>
  </item>"""

items_xml = "\n".join(xml_item(p) for p in PRODUCTS)

feed = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:g="http://base.google.com/ns/1.0">
  <channel>
    <title>Cognivia — CogniCit</title>
    <link>{SITE_URL}</link>
    <description>Feed produktów Cognivia dla Google Merchant Center</description>
    <lastBuildDate>{now}</lastBuildDate>
{items_xml}
  </channel>
</rss>"""

with open(FEED_PATH, "w", encoding="utf-8") as f:
    f.write(feed)

print(f"✅ Merchant feed updated: {FEED_PATH}")
print(f"   Generated: {now}")
print(f"   Products: {len(PRODUCTS)}")
