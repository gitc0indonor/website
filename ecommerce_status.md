# Ecommerce Status — cognivia.eu
## Last Updated: 2026-03-29 03:33 UTC (Cron Cycle #76)

## 🟡 OVERALL: Cart/Checkout FUNCTIONAL — Orders NOT arriving (Formspree placeholder)

---

## 1. Is Cognicit Buyable? Cart Working? Checkout Working?

| Component | Status | Details |
|-----------|--------|---------|
| Cart (koszyk.html) | ✅ Working | JS cart with add/remove/update qty, localStorage persistence |
| Checkout (kasa.html) | ✅ Working | Full form: name, email, phone, address, shipping, payment |
| Order Confirmation (potwierdzenie.html) | ✅ Working | Tracking status bar, order ID display |
| Add to Cart buttons | ✅ Working | 18+ buttons on produkt.html, bundle selectors |
| Real orders arriving? | 🔴 NO | Formspree ID `xpwzgryv` is placeholder — orders only save to localStorage (lost on refresh) + mailto fallback |
| reCAPTCHA v3 | ⚠️ Test key | Using Google's test site key — works on localhost, needs production key for live site |

**VERDICT: Cart & checkout are fully built and functional client-side. But NO real order processing until Formspree is activated. Same blocker since cycle #65.**

---

## 2. Product Listing Completeness

| Field | Status | Location |
|-------|--------|----------|
| Full product name | ✅ CogniCit — Suplement diety na koncentrację | produkt.html, cognivia-cart.js |
| Polish description | ✅ Complete — "3 synergistyczne składniki na koncentrację i pracę umysłową" | produkt.html |
| Ingredients with dosages | ✅ ALA 250mg, Cytykolina 300mg, β-cyklodekstryna 250mg | produkt.html, ingredients.html |
| Dosage instructions | ✅ 1 kapsułka dziennie, z jedzeniem | jak-stosowac.html |
| Benefits (5+) | ✅ Listed on produkt.html (koncentracja, pamięć, energia, ochrona, synergia) | produkt.html |
| Warnings | ✅ Legal disclaimer + skutki-uboczne.html linked | produkt.html |
| Storage | ✅ Przechowywanie section present (14 matches) | produkt.html |
| Images | ✅ OG image, product assets referenced | assets/ |
| Category | ✅ Nootropic / suplement diety | meta tags, structured data |
| Tags | ⚠️ Could be richer for SEO | produkt.html |
| SEO (title, desc, OG) | ✅ Complete | produkt.html |

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
| GMP badge | ✅ Referenced on produkt.html | Badge/image present |
| Lab-tested | ⚠️ Mentioned textually, no certificate/badge image | Need visual badge |
| Money-back guarantee | ✅ 30-day satisfaction guarantee — on product & cart pages | koszyk.html, produkt.html, regulamin §9 |
| Secure checkout (SSL) | ✅ SSL text on checkout, HTTPS site | kasa.html |
| Trust badges on checkout | 🟡 7 mentions found — could be stronger | IMP-072 pending |
| Reviews/testimonials | ✅ opinie.html exists with reviews | 4.8/5 rating displayed |
| Certificates page | ✅ certyfikaty.html exists | Linked from produkt.html |

---

## 5. Legal & Policy Pages

| Page | Status | Lines | Quality |
|------|--------|-------|---------|
| FAQ (faq.html) | ✅ Exists | 287 | Good — general FAQ |
| FAQ Produkt (faq-produkt.html) | ✅ Exists | 719 | Excellent — detailed product FAQ |
| Shipping Policy (dostawa.html) | ✅ Exists | 162 | Good — all methods detailed |
| Return Policy (zwroty.html) | ✅ Exists | 160 | Good — 30-day returns |
| Privacy Policy / RODO (polityka-prywatnosci.html) | ✅ **EXPANDED** | ~280 | Now RODO-compliant: data controller, DPO, processing purposes, legal bases, retention periods, all 8 data subject rights, PUODO contact, cookie details, Plausible info |
| Terms & Conditions (regulamin.html) | ✅ **EXPANDED** | ~280 | Now EU-compliant: consumer rights, 14-day withdrawal, detailed return conditions, payment methods table, delivery table, complaint procedure §8+§13, ODR link, guarantee of satisfaction §9, intellectual property, liability |
| Cookie Policy (polityka-cookies.html) | ✅ Exists | Detailed |

### Recent Changes (Cycle #76)
- ✅ Privacy Policy expanded from 105→~280 lines with full RODO compliance
- ✅ Terms & Conditions expanded from 95→~280 lines with full EU consumer law compliance

---

## 🔴 CRITICAL BLOCKER SUMMARY

**Formspree has not been activated for 7+ cycles.** This is the single biggest blocker to accepting real orders. CEO needs to:
1. Sign up at formspree.io with cognivia.business@outlook.com
2. Create form, get real ID
3. Replace `xpwzgryv` in js/cognivia-cart.js line 368
4. Deploy

---

## 📋 Improvement Queue Status

### Recently Completed (Cycle #76)
- ✅ IMP-071: Expanded Privacy Policy (RODO) — full GDPR compliance with all 12 required sections
- ✅ IMP-071b: Expanded Terms & Conditions — EU consumer law, ODR link, complaint procedures

### Pending Improvements
See improvement_queue.md for full list.

---

*Next check scheduled by cron. Status file: website/ecommerce_status.md*
