# Ecommerce Status — Cognivia / CogniCit
## Last Audit: 2026-03-23 13:18 UTC

---

## 1. CART & CHECKOUT STATUS

| Component | Status | Notes |
|-----------|--------|-------|
| Cart JS (cognivia-cart.js) | ✅ Working | localStorage persistence, add/remove/quantity, 377 lines |
| Cart page (koszyk.html) | ✅ Working | Full view, quantity controls, summary sidebar |
| Checkout page (kasa.html) | ✅ Working | 4-step form: customer → shipping → payment → notes |
| Order confirmation (potwierdzenie.html) | ✅ Working | Thank you page with order ID |
| Mini cart UI | ✅ Working | Cart icon with count badge in header |
| Cart notifications | ✅ Working | Toast notifications on add/remove |
| **Order backend** | ❌ **MISSING** | Orders saved to localStorage only — lost on clear. No email, no API, no real processing |
| **Payment gateway** | ❌ **NOT INTEGRATED** | PayU/Przelewy24/BLIK/PayPal listed in UI but no real gateway connection |

### 🔴 CRITICAL: NOT TRULY BUYABLE
The cart and checkout work as a UI demo. Orders go to `localStorage` and are never sent to a server. To become buyable, need:
1. Formspree endpoint (quick fix — needs real form ID, current one is placeholder)
2. Real payment gateway integration (PayU merchant account or Stripe/P24)
3. Order confirmation emails
4. Inventory tracking

### ⚠️ Free Shipping Threshold Inconsistency
- Cart JS defines free shipping at **120 zł** for InPost, **150 zł** for DPD
- Checkout page text says "Darmowa dostawa InPost od 120 zł · DPD od 150 zł"
- Produkt.html buy section says "Darmowa dostawa od 150 zł" (generic)
- **ACTION**: Align produkt.html to match cart JS (120 zł InPost, 150 zł DPD) or pick one threshold.

---

## 2. PRODUCT LISTING COMPLETENESS

| Element | Status | File |
|---------|--------|------|
| Full product name (CogniCit) | ✅ | produkt.html, schema.org |
| Polish description | ✅ | produkt.html — detailed ingredient descriptions |
| Ingredients with dosages | ✅ | ALA 250mg, Cytykolina 300mg, Beta-CD 250mg |
| Dosage instructions | ✅ | 1 kapsułka dziennie, rano z posiłkiem |
| Benefits (5+) | ✅ | 5 korzyści: funkcje poznawcze, antyoksydanty, energia, synergia, biodostępność |
| Warnings / ostrzeżenia | ✅ | 7 warnings including pregnancy, medication interactions |
| Storage instructions | ✅ | Temp 15-25°C, protect from light/moisture, use within 3 months |
| Product images | ⚠️ PLACEHOLDER | Only 1 placeholder image path — need 4-6 real photos |
| Category | ✅ | "Suplementy diety" in schema + meta |
| Tags | ⚠️ PARTIAL | No explicit tag system, but ingredient pages cross-linked |
| SEO (meta, OG, schema) | ✅ | Product JSON-LD with Offer, aggregateRating (4.8/5, 47 reviews), OG tags, canonical, hreflang |

---

## 3. SHIPPING & PAYMENT (POLAND)

### Shipping Options (cognivia-cart.js)
| Method | Price | Free from | Delivery |
|--------|-------|-----------|----------|
| InPost Paczkomat | 12,99 zł | 120 zł | 1-2 dni |
| InPost Kurier | 15,99 zł | 120 zł | 1-2 dni |
| DPD Kurier | 16,99 zł | 150 zł | 1-2 dni |
| Poczta Polska | 11,99 zł | 120 zł | 2-3 dni |

### Payment Methods (cognivia-cart.js)
| Method | Status | Integration |
|--------|--------|-------------|
| PayU | ⚠️ Listed only | Needs merchant account |
| Przelewy24 | ⚠️ Listed only | Needs merchant account |
| BLIK | ⚠️ Listed only | Via PayU or P24 |
| PayPal | ⚠️ Listed only | Needs PayPal Business |
| Przelew bankowy | ⚠️ Listed only | Manual |
| Pobranie (COD) | ⚠️ Listed only | Manual (+8 zł surcharge) |

### VAT
- ✅ 23% VAT calculated and displayed
- ✅ Price shown as brutto (79,00 zł)
- ✅ Optional VAT invoice fields in checkout

---

## 4. TRUST ELEMENTS

| Element | Status | Location |
|---------|--------|----------|
| GMP badge | ✅ Text mention | produkt.html, kasa.html, footer |
| Lab-tested badge | ✅ Text mention | produkt.html, kasa.html |
| Money-back guarantee (30 dni) | ✅ Text + page | produkt.html, zwroty.html |
| Secure checkout (SSL) | ✅ Text mention | kasa.html header, buy section |
| Legal disclaimer | ✅ | Legal bar on produkt.html, footer |
| EU regulation compliance | ✅ | WE 1924/2006, WE 1169/2011 cited |
| Certificates page | ✅ | certyfikaty.html — GMP, lab results, GIS registration |
| Trust bar on checkout | ✅ | 4 trust badges (SSL, GMP, 30 dni, PL) |

### ⚠️ Missing Trust Elements
- No actual GMP certificate image/PDF download (only text descriptions)
- No actual lab test result document (only CoA template)
- No customer reviews/testimonials section
- No Trustpilot or external review link
- No star ratings visible on product page (aggregateRating in schema only)

---

## 5. POLICY PAGES

| Page | File | Status | RODO/GDPR |
|------|------|--------|-----------|
| FAQ | faq.html | ✅ 15 Q&As, accordion, categorized | N/A |
| Shipping Policy | dostawa.html | ✅ All methods, free thresholds, tracking | N/A |
| Return Policy | zwroty.html | ✅ 14-day statutory + 30-day guarantee | N/A |
| Privacy Policy (RODO) | polityka-prywatnosci.html | ✅ RODO/GDPR compliant (7 refs) | ✅ Full |
| Terms & Conditions | regulamin.html | ✅ Company name: Cognivia | ✅ Full |

---

## 6. TECHNICAL SEO

| Element | Status |
|---------|--------|
| Canonical URLs | ✅ All pages |
| hreflang="pl" | ✅ All pages |
| JSON-LD schemas | ✅ Product, BreadcrumbList, FAQPage, Article, HowTo |
| OG tags | ✅ Index + produkt |
| Sitemap.xml | ✅ |
| Robots.txt | ✅ |
| Lazy loading | ✅ content-visibility: auto on 12 pages |
| Preload fonts | ✅ 11 key pages |

---

## 7. SUMMARY — IS COGNICIT BUYABLE?

**NO — ⚠️ FRONTEND DEMO ONLY**

The entire frontend cart/checkout flow is polished and functional:
- ✅ Adding to cart, quantity management
- ✅ Shipping selection with free thresholds
- ✅ Payment method selection
- ✅ VAT calculation (23%)
- ✅ Order form with validation
- ✅ Confirmation page

**But orders are NOT processed:**
- ❌ Orders saved to browser localStorage only
- ❌ No server receives order data
- ❌ No payment gateway connected
- ❌ No email confirmation sent
- ❌ Orders lost on browser data clear

**To make it truly buyable (minimum viable):**
1. **Formspree integration** — Replace placeholder with real form endpoint to receive orders via email (~30 min work once account is created)
2. **PayU or Przelewy24 merchant account** — Apply, integrate redirect (~1-2 weeks for approval + integration)
3. **Order confirmation email** — Auto-send to customer after submission

---

## 8. IMPROVEMENTS ADDED THIS AUDIT (2026-03-23 13:18)

1. ✅ Identified and documented free shipping threshold inconsistency (120 vs 150 zł)
2. ✅ Full ecommerce audit completed — 80+ items reviewed
3. ✅ Updated improvement queue with 3 new items (#80-82)

## 9. NEW IMPROVEMENTS QUEUED (#80-82)

80. **Fix free shipping threshold inconsistency** — Align all pages to same threshold
81. **Add actual GMP certificate PDF and lab test CoA to /certyfikaty page** — currently mockup/template only
82. **Add customer review section to produkt.html** — star ratings + testimonials, even if seeded with beta testers
