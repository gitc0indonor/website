# WordPress Deployment Quick Start Checklist

## Pre-deployment
- [ ] Create free hosting account (Byet.host or 000webhost)
- [ ] Receive login credentials via email
- [ ] Download / prepare this deployment package on your computer

## Installation Phase
- [ ] Log into hosting control panel
- [ ] Install WordPress via Softaculous (Polish language)
- [ ] Create admin account with strong password
- [ ] Note: login URL, username, password

## Plugins
- [ ] Install & Activate: WooCommerce
- [ ] Install & Activate: Rank Math SEO
- [ ] Install & Activate: W3 Total Cache
- [ ] Install & Activate: Contact Form 7
- [ ] Install & Activate: Complianz GDPR
- [ ] Install & Activate: Polylang (if multilingual)
- [ ] Install Przelewy24 plugin (upload ZIP if not in repo)

## WordPress Settings
- [ ] Settings → General: Language=Polish, Timezone=Europa/Warszawa, Currency=zł
- [ ] Settings → Reading: Discourage search engines (uncheck later at launch)
- [ ] Settings → Permalinks: Post name
- [ ] Settings → Tax: Standard rate = 23%

## Theme
- [ ] Upload & Activate Astra Child theme (ZIP or FTP)
- [ ] Verify Cormorant Garamond font loads on headings
- [ ] Verify brand colors (green #2D6642, pink #C8327A) visible

## Pages
- [ ] Create Home page → paste `PAGE_CONTENT/home.html` → Publish
- [ ] Create About page → paste `PAGE_CONTENT/about.html` → Publish
- [ ] Create Science page → paste `PAGE_CONTENT/science.html` → Publish
- [ ] Create FAQ page → paste `PAGE_CONTENT/faq.html` → Publish
- [ ] Create Contact page → paste `PAGE_CONTENT/contact.html` → add CF7 shortcode
- [ ] Create Regulamin → paste `PAGE_CONTENT/regulamin.html` → Publish
- [ ] Create Polityka Prywatności → paste `PAGE_CONTENT/polityka-prywatnosci.html` → Publish
- [ ] Set Home page as "Front page" (Settings → Reading)

## WooCommerce
- [ ] Run setup wizard: Store location=Poland, Currency=PLN, Taxes=Yes
- [ ] Add Product:
  - Name: CogniCit
  - SKU: COG-001
  - Price: 79 zł
  - Inventory: Enable stock, quantity 100
  - Description: paste `PRODUCT_CONTENT/product_description.html`
  - Short description: "Nootropic supplement with ALA, CDP-Choline, Beta-Cyclodextrin. 30 capsules."
  - Category: create "Suplementy Diety"
  - Images: upload product mockup
- [ ] Shipping zones: Poland → Flat rate (15 zł, InPost) + Free shipping >100 zł
- [ ] Payments: Enable Przelewy24 + Bank transfer + COD

## Contact & Lead Capture
- [ ] Create Contact Form 7 form for contact page (email fields)
- [ ] Insert CF7 shortcode into Contact page
- [ ] Create lead capture form (email only) for Home page
- [ ] Configure email notifications to cognivia.business@outlook.com

## GDPR
- [ ] Run Complianz configuration wizard
- [ ] Generate Privacy Policy and Cookie Policy
- [ ] Verify cookie banner appears

## Final Verification
- [ ] All pages load without errors
- [ ] Product appears in shop with correct price
- [ ] Test checkout flow (use sandbox if available)
- [ ] Test contact form submission
- [ ] Test email capture on home page
- [ ] Check mobile responsiveness
- [ ] SSL certificate active (HTTPS)
- [ ] Email sending works (contact forms, order notifications)

## Launch
- [ ] Settings → Reading: Uncheck "Discourage search engines"
- [ ] Remove "noindex" from Home page in Rank Math
- [ ] Announce launch to test users
- [ ] Begin marketing campaigns

---

**Time estimate:** 60–90 minutes with focused effort.

**If stuck:** Refer to full `WORDPRESS_SETUP_GUIDE.md` for detailed explanations of each step.

Good luck!
