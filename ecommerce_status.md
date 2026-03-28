# Ecommerce Status — cognivia.eu
## Last Updated: 2026-03-28 18:43 UTC (Power Cycle #69)

## 🔴 CRITICAL BLOCKER: Formspree STILL NOT ACTIVATED
Last checked: 2026-03-28 18:43 UTC. Form ID still placeholder `xpwzgryv`.
**Orders CANNOT be received until CEO activates Formspree.** This has been flagged in every cycle since #65.

## Current State
The site has a **fully functional client-side JavaScript cart** (cognivia-cart.js) with:
- ✅ Add to cart (product page, bundle selectors, calculators)
- ✅ Cart page (koszyk.html) with quantity controls + remove
- ✅ Checkout form (kasa.html) with customer details + shipping + payment selection
- ✅ Order confirmation page (potwierdzenie.html) with tracking status bar
- ✅ Shipping page (dostawa.html) + Return policy (zwroty.html)
- ✅ Savings calculator vs pharmacy prices
- ✅ Mailto fallback (if Formspree fails, opens email client with order details)
- ✅ reCAPTCHA v3 anti-spam protection on checkout

## 🔴 BLOCKER: Formspree Not Activated

**The site cannot receive real orders until Formspree is activated.**

Currently using placeholder form ID `xpwzgryv`. Orders save to localStorage only (vanish on page refresh) and trigger a mailto: fallback.

### Step-by-Step: Activate Formspree (5 minutes)

1. **Go to** [formspree.io](https://formspree.io)
2. **Sign up** using `cognivia.business@outlook.com`
3. **Create a new form** — name it "CogniCit Orders"
4. **Copy the Form ID** from the dashboard (looks like `xpwzgryv` or `mpzbkndw`)
5. **Open** `/website/js/cognivia-cart.js`
6. **Find** the line: `const FORMSPREE_ORDER_ID = 'xpwzgryv';`
7. **Replace** `'xpwzgryv'` with your new form ID
8. **Commit and push** the change
9. **Test**: Place a test order on the site → check `cognivia.business@outlook.com` inbox

### What Happens After Activation
- Every order POSTs JSON to Formspree
- Formspree emails order details to `cognivia.business@outlook.com`
- Customer sees confirmation page with order ID
- Mailto fallback still works as backup

### Free Tier Limits
- 50 submissions/month (sufficient for pre-launch)
- Upgrade to $10/month for 1,000 submissions when needed

## 🧪 Test Order Notification (Quick Verification)

After activating Formspree, verify it works with this 3-minute test:

1. **Open** the live site → `produkt.html`
2. **Add** 1× CogniCit to cart (click "Dodaj do koszyka")
3. **Go to** `koszyk.html` → verify item shows at 79,00 zł
4. **Click** "Przejdź do kasy" → `kasa.html`
5. **Fill in** test data:
   - Imię i nazwisko: `Test Testowy`
   - Email: `cognivia.business@outlook.com` (or your personal email)
   - Telefon: `123456789`
   - Ulica: `Testowa 1`
   - Miasto: `Gdańsk`
   - Kod pocztowy: `80-001`
   - Shipping: InPost Paczkomat
   - Payment: Przelew bankowy
6. **Click** "Zamawiam i płacę"
7. **Check inbox** for email from Formspree with order JSON
8. **Verify** confirmation page (`potwierdzenie.html`) shows order ID

### Expected Email Content
```json
{
  "subject": "🛒 Nowe zamówienie CogniCit — Test Testowy",
  "body": "imię: Test Testowy, email: ..., produkty: CogniCit × 1, suma: 79,00 zł"
}
```

### Troubleshooting
| Problem | Fix |
|---------|-----|
| No email received | Check spam folder; verify form ID matches |
| Formspree 403 error | Form may be disabled in dashboard — re-enable |
| "Form not found" | Wrong form ID — double-check the string in cognivia-cart.js |
| reCAPTCHA error | Production site key needed — test key only works on localhost |

## 📊 Order Flow Diagram

```
cognivia-cart.js (377 lines)
├── CogniviaCart class
│   ├── addItem(id, name, price, qty)
│   ├── removeItem(id)
│   ├── updateQuantity(id, qty)
│   ├── getTotal()
│   └── submitOrder() → Formspree POST + localStorage save + mailto fallback
├── FORMSPREE_ORDER_ID = 'xpwzgryv' ← CEO MUST REPLACE
├── _mailtoFallback(order, formData) ← backup: opens email client
└── reCAPTCHA v3 integration (site key configured)
```

## Pages Involved
| Page | Purpose | Status |
|------|---------|--------|
| produkt.html | Product display + 18+ add-to-cart buttons | ✅ Live |
| koszyk.html | Cart page with savings calculator | ✅ Live |
| kasa.html | Checkout form + reCAPTCHA v3 | ✅ Live |
| potwierdzenie.html | Order confirmation + tracking bar | ✅ Live |
| dostawa.html | Shipping info | ✅ Live |
| zwroty.html | Return policy | ✅ Live |

## Price
- **79,00 zł** per box (30 capsules, 30-day supply)
- Free shipping from 120 zł (InPost/Poczta) / 150 zł (DPD)
- 30-day satisfaction guarantee
