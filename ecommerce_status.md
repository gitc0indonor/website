# Ecommerce Status — cognivia.eu
## Last Updated: 2026-03-28

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

## Cart Architecture

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
