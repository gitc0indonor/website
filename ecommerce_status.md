# Ecommerce Status — cognivia.eu
## Last Updated: 2026-03-29 10:45 UTC (Cron Cycle #83)

## 🟡 OVERALL: Cart/Checkout FUNCTIONAL — Orders NOT arriving (Formspree placeholder)

---

## 1. Is Cognicit Buyable? Cart Working? Checkout Working?

| Component | Status | Details |
|-----------|--------|---------|
| Cart (koszyk.html) | ✅ Working | JS cart with add/remove/update qty, localStorage persistence |
| Checkout (kasa.html) | ✅ Working | Full form: name, email, phone, address, shipping, payment |
| Order Confirmation (potwierdzenie.html) | ✅ Working | Tracking status bar, order ID display |
| Add to Cart buttons | ✅ Working | 18+ buttons on produkt.html, bundle selectors, floating mobile CTA |
| Real orders arriving? | 🔴 NO | Formspree ID `xpwzgryv` is placeholder — orders only save to localStorage (lost on refresh) + mailto fallback |
| reCAPTCHA v3 | ⚠️ Test key | Using Google's test site key — works on localhost, needs production key for live site |

**VERDICT: Cart & checkout are fully built and functional client-side. But NO real order processing until Formspree is activated. Same blocker since cycle #65. CEO ACTION REQUIRED: Sign up at formspree.io, create form, replace ID in cognivia-cart.js line 368.**

---

## 2. Product Listing Completeness

| Field | Status | Location |
|-------|--------|----------|
| Full product name | ✅ CogniCit — Suplement diety na koncentrację | produkt.html, cognivia-cart.js |
| Polish description | ✅ Complete — "3 synergistyczne składniki na koncentrację i pracę umysłową" | produkt.html |
| Ingredients with dosages | ✅ ALA 250mg, Cytykolina 300mg, β-cyklodekstryna 250mg | produkt.html, ingredients.html |
| Dosage instructions | ✅ 1 kapsułka dziennie, z jedzeniem | jak-stosowac.html |
| Benefits (5+) | ✅ 5 benefits: cognitive support, antioxidant, energy metabolism, synergistic formula, bioavailability | produkt.html |
| Warnings | ✅ 7 warnings including pregnancy, medication interactions | produkt.html |
| Storage | ✅ 5 storage instructions + freshness guarantee + batch tracking | produkt.html |
| Images | ✅ OG image, product gallery, product assets referenced | assets/, produkt.html gallery |
| Category | ✅ Nootropic / suplement diety | meta tags, structured data |
| Tags | ✅ SEO tags present | produkt.html |
| SEO (title, desc, OG) | ✅ Complete with Product JSON-LD + Offer schema | produkt.html |
| Related content | ✅ **NEW** — 3-card cross-sell section: cytykolina, skladniki-deep-dive, jak-stosowac | produkt.html (bottom) |

---

## 3. Shipping & Payment for Poland

### Shipping ✅
| Method | Price | Free From | Delivery |
|--------|-------|-----------|----------|
| InPost Paczkomat | 12.99 zł | 120 zł | 1-2 dni |
| InPost Kurier | 15.99 zł | 120 zł | 1-2 dni |
| DPD Kurier | 16.99 zł | 150 zł | 1-2 dni |
| Poczta Polska | 11.99 zł | 120 zł | 2-3 dni |

### Payment Methods ✅ (defined in JS, NOT integrated with real gateways)
| Method | Status |
|--------|--------|
| PayU | 🔴 Defined only — no gateway integration |
| Przelewy24 | 🔴 Defined only — no gateway integration |
| BLIK | 🔴 Defined only — no gateway integration |
| PayPal | 🔴 Defined only — no gateway integration |
| Przelew tradycyjny | 🟡 Works as manual bank transfer |
| Pobranie (COD) | 🟡 Works if shipping supports it |

### VAT ✅
- 23% VAT rate configured in cognivia-cart.js (`vatRate: 0.23`)

---

## 4. Trust Elements

| Element | Status | Notes |
|---------|--------|-------|
| GMP badge | ✅ Referenced on produkt.html + certyfikaty.html | Badge/image present |
| Lab-tested | ✅ Batch tracking section with lab test links | produkt.html przechowywanie section |
| Money-back guarantee | ✅ 30-day satisfaction guarantee — on product, cart, checkout, regulamin §9 | Multi-page |
| Secure checkout (SSL) | ✅ SSL text on checkout, HTTPS site, reCAPTCHA | kasa.html |
| Trust badges on checkout | ✅ 7 trust indicators found | kasa.html |
| Reviews/testimonials | ✅ opinie.html + dodaj-opinie.html | 4.8/5 rating displayed |
| Certificates page | ✅ certyfikaty.html exists | Linked from produkt.html, footer |
| Pre-purchase FAQ | ✅ Accordion on checkout page | kasa.html |

---

## 5. Legal & Policy Pages

| Page | Status | Lines | Quality |
|------|--------|-------|---------|
| FAQ (faq.html) | ✅ Exists | 287 | Good — general FAQ |
| FAQ Produkt (faq-produkt.html) | ✅ Exists | 719 | Excellent — detailed product FAQ |
| Shipping Policy (dostawa.html) | ✅ Exists | 162 | Good — all methods detailed |
| Return Policy (zwroty.html) | ✅ Exists | 160 | Good — 30-day returns |
| Privacy Policy / RODO (polityka-prywatnosci.html) | ✅ Expanded | ~245 | RODO-compliant: data controller, processing purposes, legal bases, retention periods, data subject rights, PUODO contact |
| Terms & Conditions (regulamin.html) | ✅ Expanded | ~236 | EU-compliant: consumer rights, 14-day withdrawal, complaint procedure, ODR link, satisfaction guarantee |
| Cookie Policy (polityka-cookies.html) | ✅ Exists | Detailed | GDPR cookie consent |

---

## 🔴 CRITICAL BLOCKER SUMMARY

**Formspree has not been activated for 10+ cycles.** This is the single biggest blocker to accepting real orders. CEO needs to:
1. Sign up at formspree.io with cognivia.business@outlook.com
2. Create form, get real ID
3. Replace `xpwzgryv` in js/cognivia-cart.js line 368
4. Deploy

**Payment gateways (PayU/Przelewy24/BLIK) require merchant accounts** — defined in UI but not connected to real processors.

---

## 📋 Recent Changes (Cycle #82)

- ✅ IMP-385: Added "Powiązane artykuły" (Related articles) cross-sell section to produkt.html — 3 cards linking to cytykolina.html, skladniki-deep-dive.html, jak-stosowac.html with hover animations

---

## 📋 Improvement Queue Status

### Recently Completed (Cycles #76-82)
- ✅ IMP-071: Expanded Privacy Policy (RODO) — full GDPR compliance
- ✅ IMP-071b: Expanded Terms & Conditions — EU consumer law compliance
- ✅ IMP-372: Satisfaction guarantee progress bar on koszyk.html
- ✅ IMP-373: "Porównaj skład" comparison widget on produkt.html
- ✅ IMP-375: Pre-purchase FAQ accordion on kasa.html
- ✅ IMP-378: "Ostatnie zamówienia" counter on index.html footer
- ✅ IMP-385: "Powiązane artykuły" cross-sell section on produkt.html

### Pending (key items)
- IMP-386: Order confirmation email template for Formspree
- IMP-387: "Gwarancja świeżości" badge on produkt.html buy section
- IMP-382: "Opinie klientów" mini-carousel on index.html hero
- IMP-384: "Napisz opinię" CTA on potwierdzenie.html

See improvement_queue.md for full list (387 items, ~15 active).

---

## 📋 Recent Changes (Cycle #83)

- ✅ IMP-384: Added "Napisz opinię" CTA button to potwierdzenie.html
- ✅ IMP-387: Added "Gwarancja świeżości" badges to produkt.html buy section
- ✅ IMP-391: Added "Jak to działa?" animated GIF to produkt.html
- ✅ IMP-392: Added Google Search Console verification to index.html
- ✅ IMP-393: Updated dziekuje-za-zapis.html with discount delivery
- ✅ IMP-394: Added review widgets to landing pages
- ✅ IMP-395: Created seasonal timing blog post
- ✅ IMP-396: Added interactive quiz widget to index.html

### Cycle #83 Added to Queue (397-399)
- IMP-397: "Gwarancja satysfakcji — jak to działa?" explainer section on produkt.html
- IMP-398: "Porównanie CogniCit z kawą" blog post (high-volume Polish SEO target)
- IMP-399: FAQPage JSON-LD schema for faq-produkt.html (rich results enablement)

---

*Next check scheduled by cron. Status file: website/ecommerce_status.md*
