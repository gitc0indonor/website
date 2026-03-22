# Website Deployment Package — Contents

This package contains everything needed to deploy Cognivia's website via manual WordPress installation OR quick static site launch.

## Directory Structure

```
website/wordpress-manual-deploy/
├── CHILD_THEME/
│   ├── style.css          ← Astra child theme styles (brand colors + Cormorant Garamond)
│   ├── functions.php      ← Enqueue Google Fonts, custom body classes
│   └── screenshot.png     ← Theme thumbnail (1x1 transparent PNG)
├── PAGE_CONTENT/
│   ├── about.html         ← About page content (Polish)
│   ├── science.html       ← Science/Ingredient information
│   ├── faq.html           ← FAQ page (Q&A format)
│   ├── contact.html       ← Contact page + CF7 placeholder
│   ├── regulamin.html     ← Terms & Conditions (template)
│   └── polityka-prywatnosci.html  ← Privacy Policy (GDPR template)
├── PRODUCT_CONTENT/
│   └── product_description.html  ← Full product page copy for WooCommerce
└── Documentation/
    ├── WORDPRESS_SETUP_GUIDE.md     ← Complete step-by-step installation manual
    ├── QUICK_START_CHECKLIST.md    ← 1-page checklist for fast deployment
    └── STATIC_SITE_DEPLOYMENT.md   ← Instructions for GitHub Pages alternative
```

## What This Package Provides

### For WordPress Deployment
- Ready-to-use child theme with brand styling
- All static page content in HTML (copy-paste into WordPress pages)
- Product description pre-written for WooCommerce
- Complete installation guide covering:
  - Free hosting account creation (Byet.host/000webhost)
  - WordPress installation via Softaculous
  - Plugin setup (WooCommerce, Rank Math, Complianz, Contact Form 7)
  - Configuration for Polish market (language, currency, taxes, shipping)
  - GDPR compliance
  - Final verification checklist

### For Static Site (GitHub Pages)
- Full landing page ready at `website/static/index.html`
- Legal pages already prepared
- Email capture form with Formspree integration
- Deployment script `PUSH_TO_GITHUB.sh`
- Brand styling (Cormorant Garamond, #2D6642/#C8327A)
- SEO-ready structure

## Decision Matrix

| Option | Ease | Speed | Features | Best for |
|--------|------|-------|----------|----------|
| WordPress manual | Medium | 60–90 min | Full e-commerce, blog, CMS | Long-term business site |
| Static site (GitHub Pages) | Easy | 10 min | Landing page + email capture | Immediate lead gen, MVP |

## Next Steps

1. **Choose deployment path:** WordPress (full e-commerce) or Static (quick launch)
2. If WordPress: Follow `QUICK_START_CHECKLIST.md` or detailed `WORDPRESS_SETUP_GUIDE.md`
3. If Static: Follow `STATIC_SITE_DEPLOYMENT.md` (need GitHub repo URL + Formspree endpoint)
4. After deployment, notify team and begin marketing activities

All materials are production-ready and comply with Cognivia brand guidelines.

**Questions?** Refer to the comprehensive guide or ask your technical lead.
