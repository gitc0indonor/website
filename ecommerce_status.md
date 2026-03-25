# Ecommerce Status — Cognivia / CogniCit
## Last Audit: 2026-03-25 00:01 UTC

---

## 1. CART & CHECKOUT STATUS

| Component | Status | Notes |
|-----------|--------|-------|
| Cart JS (cognivia.js) | ✅ Working | localStorage persistence, add/remove/quantity |
| Cart page (koszyk.html) | ✅ Working | Full view, quantity controls, summary sidebar |
| Checkout page (kasa.html) | ✅ Working | 4-step form: customer → shipping → payment → notes |
| Order confirmation (potwierdzenie.html) | ✅ Working | Thank you page with order ID |
| Mini cart UI | ✅ Working | Cart icon with count badge in header |
| Cart notifications | ✅ Working | Toast notifications on add/remove |
| **Order backend** | ❌ **MISSING** | Orders saved to localStorage only — lost on clear. No email, no API |
| **Payment gateway** | ❌ **NOT INTEGRATED** | PayU/Przelewy24/BLIK/PayPal listed in UI but no real gateway |

### 🔴 CRITICAL: NOT TRULY BUYABLE
**Status: UNCHANGED since 2026-03-24 06:53.** submitOrder() still saves to localStorage and redirects. No fetch/POST calls in cognivia.js. kasa.html has no Formspree endpoint. Every "order" is silently lost.

**Blocker: #155 — Formspree integration still waiting on CEO action.**

### ⚠️ Free Shipping Threshold
- Verified consistent: 120 zł InPost/Poczta, 150 zł DPD ✅

---

## 2. PRODUCT LISTING COMPLETENESS

| Element | Status | File |
|---------|--------|------|
| Full product name (CogniCit) | ✅ | produkt.html, schema.org |
| Polish description | ✅ | Detailed ingredient descriptions |
| Ingredients with dosages | ✅ | ALA 250mg, Cytykolina 300mg, Beta-CD 250mg |
| Dosage instructions | ✅ | 1 kapsułka dziennie, rano z posiłkiem |
| Benefits (5+) | ✅ | 5 korzyści: funkcje poznawcze, antyoksydanty, energia, synergia, biodostępność |
| Warnings / ostrzeżenia | ✅ | 7 warnings including pregnancy, medication interactions |
| Storage instructions | ✅ | Temp 15-25°C, protect from light/moisture, use within 3 months |
| Product images | ⚠️ EMOJI PLACEHOLDERS | 4 gallery slots — no real product photos |
| Category | ✅ | "Suplementy diety" in schema + meta |
| Tags | ⚠️ PARTIAL | Cross-linked ingredient pages, no explicit tag system |
| SEO (meta, OG, schema) | ✅ | Product JSON-LD with Offer, aggregateRating, OG tags, canonical |
| FAQ on product page | ✅ | FAQPage JSON-LD + visible accordion (7 Q&As) |
| Sticky sidebar (desktop) | ✅ | Floating mini-cart + buy button after 400px scroll |
| Floating CTA (mobile) | ✅ | Fixed bottom bar with price + "Zamów teraz" |
| Satisfaction guarantee | ✅ | 30-day money-back section with 3-step process |
| Bundle pricing | ✅ | 3 tiers (1/2/3 boxes) with discounts |

---

## 3. SHIPPING & PAYMENT (POLAND)

### Shipping Options
| Method | Price | Free from | Delivery |
|--------|-------|-----------|----------|
| InPost Paczkomat | 12,99 zł | 120 zł | 1-2 dni |
| InPost Kurier | 15,99 zł | 120 zł | 1-2 dni |
| DPD Kurier | 16,99 zł | 150 zł | 1-2 dni |
| Poczta Polska | 11,99 zł | 120 zł | 2-3 dni |

### Payment Methods
| Method | Status | Integration |
|--------|--------|-------------|
| PayU | ⚠️ Listed only | Needs merchant account |
| Przelewy24 | ⚠️ Listed only | Needs merchant account |
| BLIK | ⚠️ Listed only | Via PayU or P24 |
| PayPal | ⚠️ Listed only | Needs PayPal Business |
| Przelew bankowy | ⚠️ Listed only | Manual |
| Pobranie (COD) | ⚠️ Listed only | Manual (+8 zł) |

### VAT
- ✅ 23% VAT calculated and displayed
- ✅ Price brutto 79,00 zł
- ✅ Optional VAT invoice fields in checkout

---

## 4. TRUST ELEMENTS

| Element | Status | Location |
|---------|--------|----------|
| GMP badge | ✅ Text + page | produkt.html, kasa.html, footer, certyfikaty.html |
| Lab-tested badge | ✅ Text mention | produkt.html, kasa.html |
| Money-back guarantee (30 dni) | ✅ Text + page | produkt.html, zwroty.html |
| Secure checkout (SSL) | ✅ Text mention | kasa.html header |
| Legal disclaimer | ✅ | Legal bar on produkt.html, footer |
| EU regulation compliance | ✅ | WE 1924/2006, WE 1169/2011 |
| Certificates page | ✅ | certyfikaty.html |
| Trust bar on checkout | ✅ | 4 trust badges |
| Star rating (visible) | ✅ | produkt.html hero + opinie.html (4.8/5, 47 reviews) |
| Price comparison section | ✅ | porownanie.html |
| Live activity feed | ✅ | produkt.html ticker (added Power Cycle #41) |

### ⚠️ Still Missing
- No actual GMP certificate PDF download
- No actual lab test result PDF (CoA)
- No customer reviews with real names/photos
- No Trustpilot integration

---

## 5. POLICY PAGES

| Page | File | Status | RODO/GDPR |
|------|------|--------|-----------|
| FAQ (general) | faq.html | ✅ 15 Q&As | N/A |
| FAQ (product) | faq-produkt.html | ✅ 20 Q&As, 4 categories | N/A |
| Shipping Policy | dostawa.html | ✅ All methods, free thresholds | N/A |
| Return Policy | zwroty.html | ✅ 14-day statutory + 30-day guarantee | N/A |
| Privacy Policy (RODO) | polityka-prywatnosci.html | ✅ Full RODO compliance | ✅ |
| Terms & Conditions | regulamin.html | ✅ Cognivia company details | ✅ |
| Contact | kontakt.html | ✅ Form + email + GDPR notice | ✅ |
| Cookie Policy | polityka-cookies.html | ✅ 12 sections + interactive banner | ✅ |

---

## 6. IMPROVEMENTS QUEUE STATUS

- Total items: 194 (last item #194)
- DONE: ~70 items
- NEW/active: ~124 items
- **Highest priority blocker:** #155 — Formspree integration (CEO action required)

---

## 7. AUDIT CHANGES THIS RUN (2026-03-25 00:01 UTC)

1. ✅ Re-verified submitOrder() — still localStorage-only, no fetch/POST
2. ✅ Confirmed kasa.html has no Formspree endpoint, no payment gateway JS
3. ✅ Confirmed cognivia.js has no POST/fetch/order submission code
4. ✅ All policy pages intact and RODO-compliant
5. ✅ Shipping/payment UI unchanged from previous audit
6. ✅ Cart/checkout still functional as frontend demo — NOT buyable
7. ✅ No changes to buyability status since 2026-03-24 17:52 audit

## 8. NEW IMPROVEMENTS QUEUED (#192-#194)

192. **Implement EmailJS as Formspree alternative for order notifications** — If CEO continues to delay Formspree signup, EmailJS offers a zero-setup alternative: sign up at emailjs.com (free: 200 emails/month), create email template for order notifications, add EmailJS SDK script to kasa.html, wire submitOrder() to send order JSON as email to cognivia.business@outlook.com. Estimated setup: 20 minutes. Eliminates the #155 blocker without waiting for Formspree.

193. **Add exit-intent popup with discount code on produkt.html** — Detect mouse leaving viewport (mouseleave on document). Show modal: "Czekaj! Odbierz 10% zniżki na pierwsze zamówienie" with email input. Captures leads from users who were about to leave without buying. Store email + discount code (FIRST10) via Formspree/EmailJS. Industry average: 3-5% exit-intent conversion rate. Complements existing scroll-based popups.

194. **Create order-to-email fallback using mailto: link in submitOrder()** — Immediate fix requiring zero external services: modify submitOrder() to generate a mailto: link with order details as body, opening the user's email client as fallback. Subject: "Zamówienie CogniCit #[timestamp]". Body: formatted order JSON. Not ideal UX but makes orders actually arrive in inbox within 2 minutes of coding. Remove once real gateway (Formspree/EmailJS) is live.

---

## EXECUTIVE SUMMARY

**Cognicit is NOT buyable.** Status unchanged from last 3 audits. Cart works perfectly as UI, but every order is silently saved to localStorage and lost. No fetch() call, no Formspree endpoint, no payment gateway connection.

**The single blocker remains:** No backend order processing (#155). Everything else (shipping, payment UI, VAT, trust elements, policies, SEO, content) is well-built and ready.

**What improved since last audit:** Live activity feed on produkt.html, opinie.html page verified, matura landing page, alkohol blog post — all content/UX wins that don't address buyability.

**What needs CEO action NOW:** Either (a) create Formspree account + provide form ID, or (b) approve EmailJS alternative (#192), or (c) accept mailto: fallback (#194). Without one of these, the site cannot process a single real order.
