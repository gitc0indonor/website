# Website Improvement Queue
## Last Updated: 2026-03-23 (Power Cycle #8)

### ✅ Completed (this session — ecommerce build)

1. ~~Build JavaScript cart system (cognivia-cart.js)~~ ✅
   - Full cart with localStorage persistence
   - Add/remove/update quantities
   - Shipping options (InPost, DPD, Poczta Polska)
   - Payment methods (PayU, Przelewy24, BLIK, PayPal, przelew, pobranie)
   - VAT calculation (23%)
   - Order submission & confirmation
   - Cart notification toasts
   - Mini cart UI

2. ~~Create checkout page (kasa.html)~~ ✅
   - 4-step checkout: customer data → shipping → payment → notes
   - Form validation
   - Invoice fields (optional VAT invoice)
   - Terms acceptance checkbox
   - Trust badges sidebar
   - Order summary with live totals

3. ~~Create cart page (koszyk.html)~~ ✅
   - Full cart view with quantity controls
   - Order summary sidebar
   - Empty state with CTA back to product

4. ~~Create order confirmation page (potwierdzenie.html)~~ ✅
   - Thank you page with order ID
   - Next steps info
   - Contact information

5. ~~Create shipping & delivery page (dostawa.html)~~ ✅
   - All shipping methods with prices
   - Free shipping thresholds
   - Payment methods table
   - Tracking information
   - Delivery times

6. ~~Create return policy page (zwroty.html)~~ ✅
   - 14-day statutory right of withdrawal
   - 30-day satisfaction guarantee
   - Return process instructions
   - Refund timeline
   - Complaint procedure

7. ~~Create FAQ page (faq.html)~~ ✅
   - 15 Q&As organized by category
   - Smooth accordion animations
   - Navigation pills by topic
   - Product, ingredients, usage, purchase, safety sections

8. ~~Update index.html with ecommerce~~ ✅
   - Added cart icon to header navigation
   - Updated CTA section with "Dodaj do koszyka" button
   - Added price display (79,00 zł)
   - Added trust indicators (secure payment, free shipping, 30-day return)
   - Added cart CSS and JS
   - Added footer links to new pages

9. ~~Update produkt.html with buy section~~ ✅
   - Added buy section with price, quantity selector, add-to-cart button
   - Payment methods display
   - Shipping methods display
   - Trust features (GMP, lab-tested, 30-day return)

10. ~~Fix company name in policies~~ ✅
    - Changed "Przedwiośnie" → "Cognivia" in regulamin.html and polityka-prywatnosci.html

11. ~~Create cart CSS (css/cart.css)~~ ✅
    - Cart icon, mini cart, notifications
    - Cart page layout
    - Checkout page layout
    - Buy section
    - Responsive design

---

### 🔄 Active Items

12. [URGENT] Integrate real payment gateway (PayU/Przelewy24 — requires merchant account)
13. [URGENT] Set up backend for order processing (email confirmations, inventory)
14. [URGENT] Replace Formspree placeholder ID with real form ID
15. Set up SSL certificate for cognivia.eu
16. Add product images (currently using placeholders)
17. Create "How to Order" interactive guide
18. Add breadcrumb navigation to subpages
19. Polish footer with newsletter signup
20. Add loading animations for scroll-triggered elements
21. Improve mobile hamburger menu animation
22. [DONE] ~~Add exit-intent popup with email capture~~ ✅ — Exit-intent popup on index.html: triggers on mouse leave (desktop) or 45s timer (mobile), 15% discount CTA, localStorage persistence, dismissible, responsive
23. Add Google PageSpeed optimization (lazy loading, preloading)
24. Create Polish-language blog post: "Czym jest cytykolina?"
25. Add real photos of product/packaging
26. [NEW] Set up Google Analytics / Plausible for conversion tracking
27. [NEW] Add order confirmation email template
28. [NEW] Create /certyfikaty page showing GMP certificate, lab results, GIS registration proof
29. [NEW] Add social sharing meta tags (Open Graph + Twitter Card) for blog post promotion
30. [NEW] Integrate customer review system (Trustpilot or self-hosted)
31. [NEW] Add structured data (JSON-LD for FAQPage) on faq.html
32. [NEW] Add canonical URLs and hreflang tags to all pages
33. [NEW] Create sitemap.xml and robots.txt
34. [DONE] ~~Fix js/main.js — duplicate scroll progress bar code~~ ✅
35. [NEW] Add Google Tag Manager for conversion tracking
36. [DONE] ~~Create sitemap.xml and robots.txt~~ ✅
37. [DONE] ~~Add structured data (JSON-LD for FAQPage) on faq.html~~ ✅
38. [DONE] ~~Add canonical URLs and Open Graph meta tags to index.html and produkt.html~~ ✅
39. [DONE] ~~Add hreflang="pl" tags to all pages for Polish SEO~~ ✅ — added to all 16 HTML pages
40. [NEW] Create /blog/ directory with first published post
41. [DONE] ~~Add breadcrumb JSON-LD schema to ingredient pages~~ ✅ — BreadcrumbList added to all 3 ingredient pages
42. [DONE] ~~Implement lazy loading for images site-wide~~ ✅ — only 2 images on site, both already optimized
43. [DONE] ~~Add Google PageSpeed optimization (preloading critical CSS, defer non-critical JS)~~ ✅ — Added `<link rel="preload">` for Google Fonts to 11 key pages (index, produkt, nauka, jak-stosowac, jak-wybrac-suplement, faq, all 5 blog pages). Added `defer` to cognivia-cart.js on index.html. Added missing preconnect to faq.html.
44. [NEW] Create customer testimonial collection form/page
45. [DONE] ~~Add internal linking strategy — cross-link blog posts, ingredient pages, FAQ, and product page more aggressively~~ ✅ — Added cross-link sections to all 4 blog posts, all 3 ingredient pages, and FAQ page
46. [DONE] ~~Create "Jak stosować CogniCit?" usage guide page with dosage, timing, stacking info~~ ✅ — Full guide page with dosage, timing table, stacking advice, contraindications, storage, FAQ. Added to jak-stosowac.html
47. [DONE] ~~Add 404 error page with navigation back to homepage~~ ✅ — Created 404.html with popular page links and navigation
48. [NEW] Add "Recently viewed" or "Customers also viewed" section on product page
49. [NEW] Create /certyfikaty page with downloadable GMP certificate and lab test PDFs
50. [DONE] ~~Add trust bar to blog pages — "CogniCit — 3 synergistyczne składniki, GMP certified" banner with CTA~~ ✅ — Added to all 5 blog pages (cytykolina, antyoksydanty, beta-cyklodekstryna, suplement-vs-lek, blog index)
51. [NEW] Add breadcrumb navigation to all subpages (produkt, faq, nauka, o-nas, jak-stosowac, etc.)
52. [NEW] Add "Share this article" social buttons to blog post pages (Facebook, Twitter/X, LinkedIn)
53. [DONE] ~~Create "Jak wybrać suplement?" consumer guide page — checklist-based, conversion-focused~~ ✅ — Created jak-wybrac-suplement.html: full checklist (safety, GMP, GIS, CoA, transparency), red flags table, CogniCit example, JSON-LD Article schema, cross-links, email CTA
54. [NEW] Add Product JSON-LD schema with Offer to produkt.html — DONE 2026-03-23 ✅
55. [NEW] Add 5 korzyści (benefits) section to produkt.html — DONE 2026-03-23 ✅
56. [NEW] Add przechowywanie (storage) section to produkt.html — DONE 2026-03-23 ✅
57. [NEW] Replace localStorage order submission with Formspree or backend API — URGENT, orders currently lost on page refresh
58. [NEW] Add product images — currently only 1 placeholder, need 4-6 professional product photos (front, back, ingredients closeup, lifestyle)
59. [NEW] Create /certyfikaty page with downloadable GMP certificate PDF and lab test results — builds trust, currently only mentioned as text badge
60. [NEW] Add live chat widget (Tidio/Crisp) for pre-launch questions — capture leads from visitors with questions
61. [DONE] ~~Create "Jak czytać etykiety suplementów?" educational page~~ ✅ — Created jak-czytac-etykiety.html (27KB): 7-element label anatomy diagram, 5 label traps (proprietary blends, doses, fillers, forms, certifications), red/green flag comparisons, 10-point purchase checklist, CogniCit comparison table, Article + BreadcrumbList JSON-LD, cross-links, email CTA, trust bar, responsive. Added to sitemap.xml.
62. [NEW] Add A/B test variants for hero CTA text — test "Powiadom mnie" vs "Chcę zniżkę" vs "Zapisz się"
63. [NEW] Add "Co mówią klienci?" section to produkt.html — embed Trustpilot widget or self-hosted star ratings, builds conversion trust
64. [NEW] Create /kalkulator-dawkowania interactive page — user inputs weight/age/goal, gets personalized dosage recommendation, lead capture via email gate
65. [NEW] Add hreflang + canonical to jak-czytac-etykiety.html and all newer pages missing them (jak-stosowac, jak-wybrac-suplement)
