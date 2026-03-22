# WordPress + WooCommerce Build Report for Cognivia

**Date:** 2026-03-19  
**Status:** Pending hosting registration (CAPTCHA blocker)

---

## 1. Hosting Selection

- **Provider:** InfinityFree (https://infinityfree.net)
- **Rationale:** 5 GB disk, unlimited bandwidth, PHP 8.3, MySQL 8.0, Softaculous installer, no ads, free SSL, 99.9% uptime. Supports WordPress one‑click install.
- **Registration URL:** https://dash.infinityfree.com/register
- **Planned credentials:**
  - Email: cognivia.co@gmail.com
  - Password: `C0gn!v!aInfinity2025` (stored in vault)

**Blocker:** Cloudflare CAPTCHA (Turnstile) presented on the registration page, requiring human interaction. Automated signup is not possible due to this challenge.

---

## 2. Credentials Vault

Updated `credentials_vault.md` with hosting details and noted pending manual completion.

---

## 3. Prepared Assets

- ✅ Child theme directory `website/astra-child/` created.
- ✅ `style.css` with:
  - Brand colors (#2D6642, #C8327A, #F4F8F5)
  - Cormorant Garamond font for headings
  - Basic Astra customizations
- ✅ All required page content files generated in `website/pages/`:
  - `home.md` (provided)
  - `about.md` (provided)
  - `contact.md` (provided)
  - `shop.md` (created)
  - `cart.md` (created)
  - `checkout.md` (created)
  - `blog.md` (created)
  - `regulamin.md` (created)
  - `polityka-prywatnosci.md` (created)

---

## 4. Remaining Tasks (once hosting is active)

1. **Complete registration** (manual CAPTCHA solve by user/CEO).
2. Log into InfinityFree control panel and create database (if not automatically via Softaculous).
3. Install WordPress via Softaculous (recommended) or manually.
4. Install and activate:
   - Astra theme (parent)
   - Upload Astra child theme and activate it
   - WooCommerce
   - Rank Math SEO
   - W3 Total Cache
   - Contact Form 7
   - Complianz GDPR
   - Przelewy24 (plugin for Polish payments)
5. **Configure WordPress settings:**
   - Language: Polish
   - Timezone: Europe/Warsaw
   - discourage search engines (noindex) – via Settings > Reading or Rank Math
   - Permalinks: Post name
   - Currency: PLN
   - Tax: 23% (WooCommerce > Settings > Tax)
6. **Create pages** (using markdown content from `website/pages/*.md`):
   - Home, Shop, Cart, Checkout, About, Contact, Blog, Regulamin, Polityka Prywatności
7. **Set up WooCommerce:**
   - Add product `CogniCit` with price 79,00 zł, category `Suplementy Diety`, stock enabled.
   - Configure Przelewy24 payment gateway.
   - Set shipping zone to Poland and shipping method (InPost courier, 15 zł, free over 100 zł).
8. **SEO configuration:**
   - Verify titles/meta via Rank Math (noindex on front page initially, sitemap blocked from public until launch).
9. **Write final report** with admin URL, username, password, and status.

---

## 5. Notes

- SEO elements will be configured to discourage public indexing until launch, as requested.
- All plugin choices align with Polish market and GDPR compliance.
- Child theme enforces brand colors and typography.
- Ready to proceed immediately once hosting account credentials are available.

---

**Prepared by:** Jan (subagent)  
**Next actions:** Await manual completion of InfinityFree registration and credentials to continue with installation & configuration.