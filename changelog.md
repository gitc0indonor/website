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
