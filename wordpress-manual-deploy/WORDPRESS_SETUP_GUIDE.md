# WordPress + WooCommerce Manual Installation Guide

**Purpose:** Deploy Cognivia's e-commerce website for Cognicit nootropic supplement.

**Prerequisites:**
- Free hosting account on Byet.host or 000webhost (see account creation below)
- Domain: free subdomain provided by host
- Email: cognivia.business@outlook.com
- Time: ~60 minutes

---

## Phase 1: Create Free Hosting Account

### Option A: Byet.host (Recommended)
1. Go to https://byet.host/free-hosting/news
2. Fill form:
   - **Sub Domain**: Choose any available (e.g., `cognivia`)
   - **Password**: Strong password (store securely)
   - **Email**: cognivia.co@gmail.com
   - **Site Category**: Business
   - **Site Language**: English
   - **Security Code**: Type characters from image
3. Click "Register"
4. Account activates instantly → check email for login details

### Option B: 000webhost (via Hostinger)
1. Go to https://www.hostinger.com/special/000webhost
2. Complete any Cloudflare verification if shown
3. Click "Sign Up" for free hosting
4. Register with email/password
5. Verify email address

---

## Phase 2: WordPress Installation

1. Log into hosting control panel (cPanel or similar)
2. Locate **Softaculous** or **Website Auto-Installer** (often in "Software" section)
3. Click **WordPress** → "Install"
4. Configure:
   - **Domain**: Select your free subdomain
   - **Site Name**: Cognivia
   - **Admin Username**: Create unique (not "admin")
   - **Admin Password**: Strong password
   - **Admin Email**: cognivia.business@outlook.com
   - **Language**: Polish (pl_PL)
5. Click "Install"
6. Save:
   - WordPress login URL (usually `https://yoursite.byet.host/wp-admin`)
   - Username and password

---

## Phase 3: Install Required Plugins

1. Log into WordPress admin
2. Go to **Plugins → Add New**
3. Search and **Install** → **Activate**:
   - **WooCommerce**
   - **Rank Math SEO**
   - **W3 Total Cache**
   - **Contact Form 7**
   - **Complianz GDPR** (or similar GDPR plugin)
   - **Polylang** or **WPML** (for Polish/English if needed)

4. For **Przelewy24** payment gateway:
   - May not be in repo → download from official site
   - Upload via Plugins → Add New → Upload Plugin
   - Activate after upload

---

## Phase 4: WordPress Configuration

### Settings → General
- Site Language: Polski
- Timezone: Europa/Warszawa
- Currency: zł (PLN)

### Settings → Reading
- Check "Discourage search engines" (noindex) until launch

### Settings → Permalinks
- Select "Post name"

### Settings → Tax → Standard rate
- Set to 23% (Polish VAT)

---

## Phase 5: Install Astra Child Theme

### Upload ZIP (if you have it):
1. Go to **Appearance → Themes → Add New → Upload Theme**
2. Click "Choose File" → select `CHILD_THEME.zip` (from this package)
3. Click "Install Now" → "Activate"

### Manual upload via FTP (if ZIP upload fails):
1. In hosting file manager, navigate to `/wp-content/themes/`
2. Create folder: `astra-child`
3. Upload the three files from `CHILD_THEME/`:
   - `style.css`
   - `functions.php`
   - `screenshot.png`
4. In WordPress admin, go to **Appearance → Themes**
5. Activate "Astra Child"

---

## Phase 6: Create Pages (from Markdown)

For each page below:
1. Pages → Add New
2. Set **Language**: Polski (if using Polylang)
3. Set **Title** as listed
4. Paste content from `PAGE_CONTENT/` files (convert Markdown to HTML)
5. **Publish**

Required pages:
- Home (use `home.html` — contains full hero, product showcase, email capture)
- About (`about.html`)
- Science (`science.html`)
- FAQ (`faq.html`)
- Contact (`contact.html`) — add Contact Form 7 shortcode `[contact-form-7 id="123" title="Contact form 1"]` (create form first)
- Regulamin (`regulamin.html`)
- Polityka Prywatności (`polityka-prywatnosci.html`)
- Blog (will be auto-generated from posts)

**Note:** Product page will be created via WooCommerce in next step.

---

## Phase 7: WooCommerce Configuration

### Run Setup Wizard
1. After activating WooCommerce, you'll see setup prompt → Start
2. **Page setup**: Let WooCommerce create Cart, Checkout, My Account pages (keep default slugs)
3. **Store location**: Poland
4. **Currency**: PLN
5. **Taxes**: Enable (23% standard rate already set in WordPress)

### Add Product: CogniCit
1. **Products → Add New**
2. **Product data**:
   - Type: Simple product
   - SKU: COG-001
   - Regular price: 79
   - Inventory: Enable stock management, stock quantity: 100 (or whatever initial stock)
   - Shipping: Weight 0.1 kg, Dimensions: 5×5×2 cm
3. **Product description**:
   Paste content from `PRODUCT_CONTENT/product_description.html`
4. **Short description**: "Nootropic supplement with ALA, CDP-Choline, Beta-Cyclodextrin. 30 capsules."
5. **Categories**: Add "Suplementy Diety" or create new
6. **Product image**: Upload product mockup (use placeholder from `PRODUCT_IMAGES/` if needed)
7. **Gallery**: Upload additional images if available
8. Publish

### Shipping Zones
1. WooCommerce → Settings → Shipping → Shipping zones
2. Add zone: Poland
3. Add shipping method: Flat rate
   - Name: InPost courier
   - Cost: 15 zł
   - Tax status: Taxable
4. Add another: Free shipping
   - Minimum order amount: 100 zł
   - Method title: Darmowa dostawa

### Payment Gateways
1. WooCommerce → Settings → Payments
2. Enable **Przelewy24** (if installed) → configure with merchant credentials
3. Also enable **Cash on Delivery** (optional) and **Bank transfer** as fallback

---

## Phase 8: Rank Math SEO Configuration

1. Go to **Rank Math → General Settings**
2. In "Links" tab, enable "Remove ?replytocom" from URLs
3. In "Images" tab, add alt text patterns if desired
4. For pages you don't want indexed (Home, Cart, Checkout):
   - Edit page → Rank Math metabox → "No Index" → "Do not Index"
5. Save changes

---

## Phase 9: GDPR Compliance (Complianz)

1. Go to **Complianz → Configuration**
2. Answer wizard questions about your site:
   - Purpose: Commercial, e-commerce (WooCommerce)
   - Collecting data: Yes (contact forms, checkout)
   - Analytics: None (or add Google Analytics later)
3. Generate Privacy Policy and Cookie Policy (use Polish language)
4. The plugin will add cookie banner automatically

---

## Phase 10: Email Capture Form (Homepage)

1. Go to **Contact Form 7 → Add New**
2. Title: "Lead Capture"
3. Form template (pre-filled):

```
[email* your-email placeholder "Twój email"]
[submit "Powiadom mnie!"]
```

4. Copy the form shortcode from "Copy this shortcode"
5. Edit **Home** page → paste shortcode where email capture should appear
6. In Mail tab, set:
   - From: cognivia.co@gmail.com
   - To: cognivia.co@gmail.com
   - Subject: "Nowy zapis na listę mailingową CogniCit"
   - Message body: `Nowy email: [your-email]`

7. Save

---

## Phase 11: Final Verification Checklist

- [ ] All pages load correctly (Home, About, Science, FAQ, Contact, Regulamin, Polityka Prywatności)
- [ ] Polish language set site-wide
- [ ] Astra Child theme active
- [ ] Brand fonts (Cormorant Garamond) loading on headings
- [ ] Brand colors visible in buttons/links
- [ ] Product "CogniCit" added in WooCommerce with price 79 zł
- [ ] Cart → Checkout flow works (test with sandbox if available)
- [ ] Shipping methods: Flat rate (15 zł) and Free shipping over 100 zł
- [ ] Payment gateway configured (Przelewy24 credentials added)
- [ ] Contact form 7 works (test submission)
- [ ] Email capture form on Home page works
- [ ] GDPR cookie banner appears
- [ ] Mobile responsive (check on phone)
- [ ] SSL certificate active (hosting usually provides free SSL)

---

## Phase 12: Launch Readiness

After verification:
1. Settings → Reading → Uncheck "Discourage search engines"
2. Rank Math: remove "noindex" from Home page if set
3. Announce to test users
4. Begin marketing campaigns

---

## Troubleshooting

**Softaculous not found?** → Most free hosts have it; if not, use "QuickInstall" or ask host support. Manual WordPress install via FTP is also possible but more complex.

**Plugin not in repository?** → Download from WordPress.org or official source, then upload via ZIP.

**SSL not working?** → Enable in hosting control panel (often "Let's Encrypt" or "Free SSL").

**Email form not sending?** → Check WordPress email configuration; may need SMTP plugin like WP Mail SMTP with Gmail/third-party SMTP.

---

**Files included in this package:**
- `CHILD_THEME/` — Complete Astra child theme (style.css, functions.php, screenshot.png)
- `PAGE_CONTENT/` — HTML versions of all static pages (from original markdown)
- `PRODUCT_CONTENT/` — Product description HTML for WooCommerce
- `PRODUCT_IMAGES/` — Placeholder product images (add real ones later)
- `FORMSPREE_SETUP.md` — For static site alternative (if you prefer that route)

---

**Need help?** Save this guide as PDF and follow step-by-step. All critical configuration points are covered. Good luck!
