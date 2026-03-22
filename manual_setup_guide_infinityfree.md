# Manual WordPress Setup Guide — InfinityFree

**Prepared for:** Cognivia CEO  
**Date:** 2026-03-19  
**Goal:** Complete WordPress + WooCommerce setup on InfinityFree after manual registration.

## Step 1: Complete Registration

1. Go to https://dash.infinityfree.com/register
2. Fill form:
   - Email: `cognivia.business@outlook.com`
   - Password: `C0gn!v!aInfinity2025` (use this or choose another and store it)
3. Solve Cloudflare CAPTCHA (Turnstile) – human required.
4. Verify email via link sent by InfinityFree.
5. Log into dashboard: https://dash.infinityfree.com/

## Step 2: Create Database (via Softaculous)

1. In dashboard, find **“Softaculous Apps Installer”** (or “Site Software” → “Softaculous”).
2. Click **WordPress**.
3. Click **“Install Now”**.
4. Choose **“https://”** protocol.
5. **Domain:** select your free subdomain (e.g., `cognivia.epizy.com` or similar).
6. **Site Name:** Cognivia
7. **Site Description:** Nootropic supplement CogniCit
8. **Admin Username:** (choose, e.g., `cognivia_admin`)
9. **Admin Password:** strong password (store in credentials_vault.md)
10. **Admin Email:** cognivia.business@outlook.com
11. Select **“WP + WooCommerce”** if available, otherwise plain WordPress.
12. Click **Install**.
13. Note the **Admin URL** (e.g., `https://cognivia.epizy.com/wp-admin`).

## Step 3: Install Required Plugins

1. Log into WordPress admin (`/wp-admin`).
2. Go to **Plugins → Add New**.
3. Search and install (click “Install Now”, then “Activate”):
   - **WooCommerce**
   - **Rank Math SEO**
   - **W3 Total Cache**
   - **Contact Form 7**
   - **Complianz – GDPR Cookie Consent** (or “Cookie Notice for GDPR”)
   - **Przelewy24 for WooCommerce** (search “Przelewy24”)
4. After activation, run WooCommerce setup wizard:
   - Set **Currency** to PLN
   - Set **Tax** → 23% VAT
   - Shipping zone: Poland; add shipping method (e.g., Flat rate: 15 zł, free shipping over 100 zł)
   - Payments: enable Przelewy24 (you’ll configure merchant ID later)

## Step 4: Upload Astra Child Theme

1. On your computer, ensure the folder `website/astra-child/` is ready (contains `style.css` and `functions.php` if any).
2. In WordPress admin: **Appearance → Themes → Add New → Upload Theme**.
3. Choose `website/astra-child/style.css` (ZIP the folder first) and upload.
4. Activate the child theme.
5. If the parent Astra theme is not present, WordPress will prompt to install it — accept.

## Step 5: Create Pages

1. Go to **Pages → Add New** for each page.
2. Use the content from `website/pages/*.md` files.
   - Copy the Markdown text and paste into the WordPress editor (Gutenberg “Paragraph” blocks or use “Classic Editor” plugin if easier).
   - Set page template as needed (e.g., “Home” as front page).
3. Create these pages (Slug in parentheses):
   - Strona główna (home) – set as **Front page** (Settings → Reading)
   - Sklep (shop) – WooCommerce will auto-create shop page; you can assign.
   - Koszyk (cart)
   - Zamówienie (checkout)
   - O nas (about)
   - Kontakt (contact) – use Contact Form 7 shortcode
   - Regulamin (regulamin)
   - Polityka Prywatności (polityka-prywatnosci)
   - Blog (blog) – posts page (Settings → Reading)
4. Publish each page.

## Step 6: WooCommerce Product

1. Go to **Products → Add New**.
2. Title: **CogniCit**
3. Description: use content from `website/pages/home.md` or create product description.
4. Short description: brief tagline.
5. Price: **79,00 zł**
6. Categories: add “Suplementy Diety”
7. Inventory: enable stock management; SKU `COG-001`; allow backorders? no.
8. Shipping: weight ~0.05 kg; dimensions appropriate for 30‑capsule box.
9. Image: upload product placeholder image (to be replaced later).
10. Publish.

## Step 7: SEO & Noindex

1. In Rank Math SEO:
   - Global settings → “Links” → remove `?replytocom` etc.
   - Sitemap settings: enable but do NOT submit to Google yet.
   - Titles & Meta:
     - Home page: set “noindex, nofollow” (Advanced tab in Rank Math meta box).
     - Other pages: leave indexable for now or also noindex until launch.
2. In **Settings → Reading**, check “Discourage search engines from indexing this site” (adds robots meta).

## Step 8: Additional Settings

- **Permalinks**: Settings → Permalinks → “Post name”.
- **Timezone**: Settings → General → Timezone “Warsaw”.
- **Language**: Polish (install if not present).
- **W3 Total Cache**: enable minify, cache, but test carefully.

## Step 9: Verify & Report

1. Visit the site frontend; ensure child theme styles applied (colors, fonts).
2. Test checkout flow (use test payment mode in WooCommerce).
3. Note admin credentials and site URL in `credentials_vault.md`.
4. Reply to this guide that setup is complete; I will generate final report.

## Troubleshooting

- If Softaculous not available: use “File Manager” to upload WordPress manually (download from wordpress.org, extract, upload, run installer).
- If Przelewy24 plugin fails: skip for now; configure after launch.
- If CAPTCHA prevents registration at all, contact InfinityFree support or switch to 000webhost (see alternative_000webhost_setup.md).

**Done.** Report completion via session_send to main.
