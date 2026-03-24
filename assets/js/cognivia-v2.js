/* Cognivia — Minimal Luxury Botanical JS v2.0 */
(function() {
  'use strict';

  // Scroll progress
  const bar = document.querySelector('.scroll-progress');
  if (bar) {
    window.addEventListener('scroll', function() {
      const h = document.documentElement.scrollHeight - window.innerHeight;
      bar.style.width = h > 0 ? (window.scrollY / h * 100) + '%' : '0%';
    }, { passive: true });
  }

  // Mobile menu
  const btn = document.querySelector('.mobile-menu-btn');
  const menu = document.querySelector('.mobile-menu');
  if (btn && menu) {
    btn.addEventListener('click', function() {
      menu.classList.toggle('open');
      document.body.style.overflow = menu.classList.contains('open') ? 'hidden' : '';
    });
    menu.querySelectorAll('a').forEach(function(a) {
      a.addEventListener('click', function() {
        menu.classList.remove('open');
        document.body.style.overflow = '';
      });
    });
  }

  // Reveal on scroll
  if ('IntersectionObserver' in window) {
    const obs = new IntersectionObserver(function(entries) {
      entries.forEach(function(e) {
        if (e.isIntersecting) { e.target.classList.add('visible'); obs.unobserve(e.target); }
      });
    }, { threshold: 0.08 });
    document.querySelectorAll('.reveal').forEach(function(el) { obs.observe(el); });
  }

  // Smooth anchor scroll
  document.querySelectorAll('a[href^="#"]').forEach(function(a) {
    a.addEventListener('click', function(e) {
      const t = document.querySelector(this.getAttribute('href'));
      if (t) { e.preventDefault(); t.scrollIntoView({ behavior: 'smooth' }); }
    });
  });
})();
