# Ecommerce Status — cognivia.eu
## Last Updated: 2026-03-28 22:13 UTC (Cron Cycle #70)

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

**VERDICT: Cart & checkout are fully built and functional. But NO real order processing until Formspree is activated. This has been the same blocker since cycle #65.**

---

## 2. Product Listing Completeness

| Field | Status | Location |
|-------|--------|----------|
| Full product name | ✅ CogniCit — Suplement diety na koncentrację | produkt.html, cognivia-cart.js |
| Polish description | ✅ Complete — "3 synergistyczne składniki na koncentrację i pracę umysłową" | produkt.html |
| Ingredients with dosages | ✅ ALA 250mg, Cytykolina 300mg, β-cyklodekstryna 250mg | produkt.html, ingredients.html |
| Dosage instructions | ✅ 1 kapsułka dziennie, z jedzeniem | jak-stosowac.html |
| Benefits (5+) | ✅ Listed on produkt.html (koncentracja, pamięć, energia, ochrona, synergia) | produkt.html |
| Warnings | ⚠️ Partial — legal disclaimer present, detailed side effects in skutki-uboczne.html | produkt.html |
| Storage | ⚠️ Not prominently displayed on product page | Need to add |
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
| GMP badge | ✅ Referenced on produkt.html (35 trust mentions found) | Badge/image present |
| Lab-tested | ⚠️ Mentioned textually, no certificate/badge image | Need visual badge |
| Money-back guarantee | ✅ 30-day satisfaction guarantee — on product & cart pages | koszyk.html, produkt.html |
| Secure checkout (SSL) | ✅ SSL text on checkout, HTTPS site | kasa.html |
| Trust badges on checkout | 🟡 7 mentions found in kasa.html — could be stronger | Add more visual trust signals |
| Reviews/testimonials | ✅ opinie.html exists with reviews | 4.8/5 rating displayed |
| Certificates page | ✅ certyfikaty.html exists | Need to link more prominently |

---

## 5. Legal & Policy Pages

| Page | Status | Lines | Quality |
|------|--------|-------|---------|
| FAQ (faq.html) | ✅ Exists | 287 | Good — general FAQ |
| FAQ Produkt (faq-produkt.html) | ✅ Exists | 719 | Excellent — detailed product FAQ |
| Shipping Policy (dostawa.html) | ✅ Exists | 162 | Good — all methods detailed |
| Return Policy (zwroty.html) | ✅ Exists | 160 | Good — 30-day returns |
| Privacy Policy / RODO (polityka-prywatnosci.html) | 🟡 Exists but thin | 105 | Needs expansion — RODO requires more detail |
| Terms & Conditions (regulamin.html) | 🟡 Exists but thin | 95 | Needs expansion for EU consumer law |
| Cookie Policy (polityka-cookies.html) | ✅ Exists | Detailed |

---

## 🔴 CRITICAL BLOCKER SUMMARY

**Formspree has not been activated for 5+ cycles.** This is the single biggest blocker to accepting real orders. The entire cart/checkout stack is built and works client-side. CEO needs to:
1. Sign up at formspree.io with cognivia.business@outlook.com
2. Create form, get real ID
3. Replace `xpwzgryv` in js/cognivia-cart.js
4. Deploy

---

## 📋 3 Improvements Added to Queue

### IMP-071: Expand Privacy Policy (RODO) & Terms (Regulamin)
Current privacy policy (105 lines) and T&C (95 lines) are insufficient for EU/Polish e-commerce compliance. Need: data controller details, DPO contact, data processing purposes, cookie consent specifics, right to erasure procedures, complaint procedures, EU Online Dispute Resolution link. **Priority: HIGH (legal risk)**

### IMP-072: Add Visual Trust Badges to Checkout Page
Checkout page (kasa.html) has only 7 trust-related text mentions. Add prominent visual badges: GMP certification seal, "Bezpieczna płatność SSL" shield, "30 dni gwarancji" badge, "Szyfrowane dane" lock icon. Place directly above and below the submit button. **Priority: MEDIUM (conversion rate)**

### IMP-073: Add Product Storage & Shelf-Life Info to Product Page
Product page lacks visible storage instructions and expiration/lot number info. Add a small "Przechowywanie" section near the dosage info: "Przechowywać w suchym miejscu, w temperaturze pokojowej, w sposób niedostępny dla małych dzieci. Data ważności i nr partii na opakowaniu." **Priority: LOW (completeness)**

---

*Next check scheduled by cron. Status file: website/ecommerce_status.md*
