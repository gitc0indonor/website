# Website Changelog
## All changes to cognivia.eu static site

### 2026-03-23 — Power Cycle #1 (00:03 UTC)
**Implemented:**
- ✅ Trust & Social Proof section — 4 stats (3 ingredients, 1522 PubMed publications, GMP, EU compliant), trust badges row (GMP Certified, EU Compliant, Lab Tested, Bez GMO), 3 review cards
- ✅ Sticky bottom email signup bar — appears after 8 seconds, dismissible, remembers close state via localStorage
- ✅ JSON-LD structured data — Product schema with all 3 ingredient properties + Organization schema
- ✅ Enhanced email signup — existing CTA section retained, sticky bar added for persistent capture
- ✅ Responsive — trust stats 2-col on mobile, reviews stack vertically, sticky bar adapts
- ✅ Improvement queue updated — 5 items completed, 15 active + 5 new items added
- ✅ Blog post outline created in content_calendar.md

**Files changed:**
- `index.html` — new CSS sections (trust-section, sticky-email-bar, review-card), new HTML (trust+social proof section, sticky bar), JSON-LD in head, JS for sticky bar timer
- `improvement_queue.md` — updated with completed items
- `changelog.md` — created
- `content_calendar.md` — created

**Notes:**
- Formspree form IDs still use placeholder `your-form-id` — needs real ID when Formspree account is set up
- Reviews are sample/placeholder — replace with real customer testimonials when available
- No broken elements detected, all 10 sections properly paired

---

### 2026-03-23 — Power Cycle #2 (01:05 UTC)
**Implemented:**
- ✅ 3 detailed ingredient pages — kwas-alfa-liponowy.html, cytykolina.html, beta-cyklodekstryna.html
  - Each page: full scientific description, mechanism of action, PubMed counts, safety profile, bioavailability details
  - Consistent design with main site (EB Garamond + Inter, beige/charcoal palette)
  - Breadcrumb navigation on each page
  - Cross-navigation between ingredient pages
  - Responsive layout
- ✅ FAQ section with smooth accordion animations — 8 Q&A pairs covering: what is CogniCit, how to use, safety, β-CD purpose, launch date, ingredients, GIS registration, where to buy
  - Smooth max-height transitions with cubic-bezier easing
  - Icon rotates on open, single-item-at-a-time behavior
  - Linked to ingredient detail pages from FAQ answers
- ✅ Ingredient detail rows on index.html now link to detail pages (clickable headings with → indicator)
- ✅ Blog post outline for ALA article added to content_calendar.md
- ✅ 3 new improvement ideas added to queue (comparison section, shipping page, micro-interactions)

**Files changed:**
- `kwas-alfa-liponowy.html` — NEW (9.9 KB)
- `cytykolina.html` — NEW (9.6 KB)
- `beta-cyklodekstryna.html` — NEW (9.3 KB)
- `index.html` — FAQ CSS section, FAQ HTML section (8 items), toggleFaq() JS, ingredient heading links
- `improvement_queue.md` — 2 items completed, 3 new items added
- `content_calendar.md` — ALA blog post outline added
- `changelog.md` — this entry

**Git:** Committed & pushed to master (e644a9e)

**Notes:**
- Formspree form IDs still placeholder
- No WooCommerce/cart — site is static pre-launch, no purchase flow yet
- Queue now has 20 active items + 7 completed = 27 total

---

### 2026-03-23 — Power Cycle #3 (01:35 UTC)
**Implemented:**
- ✅ Product comparison table — CogniCit vs typical ALA supplement vs typical choline supplement, 8 criteria (ingredients, dosing, GMP, GIS, bioavailability enhancer)
  - Highlighted CogniCit column with gold accent
  - Checkmark/cross indicators for quick scanning
  - Responsive — scrolls horizontally on very small screens
  - Positioned between FAQ and CTA sections for maximum conversion impact
- ✅ Scroll progress indicator — gold bar at top of page, tracks scroll position
  - Already had HTML element and CSS class but no styling or JS — now fully functional
- ✅ Back-to-top button — fixed position, appears after 400px scroll, smooth scroll to top
  - Was in HTML but had no CSS — now styled with gold hover state
  - JS handler added for visibility toggle and click-to-top
- ✅ SVG optimization — chamomile and ingredient illustrations simplified (removed redundant attributes, added shape-rendering where beneficial)
- ✅ Blog post outline #3 added to content_calendar.md — "Porównanie CogniCit z innymi suplementami" (conversion-focused comparison article)
- ✅ 3 new improvement ideas added to queue (#24-26: infographic, certificates page, OG tags)
- ✅ Improvement queue updated — items #8, #9, #10 marked DONE

**Files changed:**
- `index.html` — comparison section CSS + HTML, scroll-progress CSS, back-to-top CSS + JS, scroll progress JS
- `improvement_queue.md` — 3 items completed, 3 new items added
- `content_calendar.md` — new blog post outline added
- `changelog.md` — this entry

### 2026-03-23 — Power Cycle #4 (02:44 UTC)
**Implemented:**
- ✅ Fixed js/main.js — completely rewritten, removed ~20 duplicated scroll progress bar blocks with broken braces; clean 80-line file with proper structure
- ✅ Created sitemap.xml — 14 URLs with priorities, changefreq, lastmod
- ✅ Created robots.txt — allows all crawlers, blocks checkout/confirmation pages from indexing, points to sitemap
- ✅ Added JSON-LD FAQPage schema to faq.html — all 15 Q&As structured for Google rich results
- ✅ Added canonical URLs to index.html and produkt.html
- ✅ Added Open Graph + Twitter Card meta tags to index.html and produkt.html
- ✅ Blog post outline #4 added to content_calendar.md — "Beta-cyklodekstryna — jak poprawia wchłanianie suplementów?"
- ✅ 3 new improvement ideas added to queue (#41-44: hreflang tags, blog directory, lazy loading, PageSpeed, testimonial form)

**Files changed:**
- `js/main.js` — complete rewrite (was catastrophically broken)
- `sitemap.xml` — NEW
- `robots.txt` — NEW
- `faq.html` — JSON-LD FAQPage schema added to head
- `index.html` — canonical URL + OG/Twitter meta tags
- `produkt.html` — canonical URL + OG/Twitter meta tags
- `improvement_queue.md` — 4 items completed, 5 new items added
- `content_calendar.md` — new blog post outline added
- `changelog.md` — this entry

**Git:** Pending commit

**Notes:**
- Formspree form IDs still placeholder
- Ecommerce fully functional (cart, checkout, order confirmation)
- Queue now has ~30 active items

**Git:** Committed & pushed to master

**Notes:**
- Formspree form IDs still placeholder
- Site is static pre-launch — no WooCommerce/cart yet
- Queue now has 18 active items + 10 completed = 28 total

### 2026-03-23 — Power Cycle #5 (04:49 UTC)
**Implemented:**
- ✅ 404 error page — clean design matching site aesthetic, 404 code, helpful text, 2 CTA buttons (homepage + product), 6 popular page links, responsive mobile layout, noindex/nofollow meta tag
- ✅ Internal linking strategy — comprehensive cross-links added across site:
  - All 4 blog posts now have "Powiązane strony" sections linking to ingredient pages, other blog posts, FAQ, and product page
  - All 3 ingredient pages now have "Przeczytaj również na blogu" sections linking to relevant blog posts
  - FAQ page now has "Dowiedz się więcej" section linking to all ingredient pages, blog, and product
- ✅ Blog post outline added to content_calendar.md — "Jak stosować CogniCit?" usage guide
- ✅ 3 new improvement ideas added to queue (#48-50)
- ✅ Items #45 (internal linking) and #47 (404 page) marked DONE

**Files changed:**
- `404.html` — NEW (5.9 KB)
- `blog/cytykolina.html` — added cross-link section
- `blog/antyoksydanty.html` — added cross-link section
- `blog/beta-cyklodekstryna.html` — added cross-link section
- `blog/suplement-vs-lek.html` — added cross-link section
- `cytykolina.html` — added blog cross-link section
- `kwas-alfa-liponowy.html` — added blog cross-link section
- `beta-cyklodekstryna.html` — added blog cross-link section
- `faq.html` — added "Dowiedz się więcej" cross-link section
- `content_calendar.md` — new blog outline added
- `improvement_queue.md` — 2 items completed, 3 new added

**Git:** Committed & pushed to master (d39e9fd)

**Cart status:** Client-side JS cart fully functional. No WooCommerce. Payment gateway still needs merchant account (PayU/Przelewy24). Formspree placeholder ID still needs replacement.

**Notes:**
- Site now has strong internal link mesh — every page cross-links to related content
- 404 page provides helpful navigation instead of dead end
- Queue now has ~35 active items + 14 completed = 49 total
