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
