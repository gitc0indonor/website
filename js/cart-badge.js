/* Cart Count Badge Sync — site-wide
   Reads cart from localStorage, updates any .cart-count element.
   Add <script src="js/cart-badge.js" defer></script> to any page. */
(function() {
  'use strict';
  function getCartCount() {
    try {
      var cart = JSON.parse(localStorage.getItem('cognivia_cart') || '[]');
      return cart.reduce(function(sum, item) { return sum + (item.quantity || 1); }, 0);
    } catch(e) { return 0; }
  }
  function updateBadges() {
    var count = getCartCount();
    var badges = document.querySelectorAll('.cart-count');
    badges.forEach(function(b) {
      b.textContent = count;
      b.style.display = count > 0 ? 'inline-flex' : 'none';
    });
  }
  // Update on load
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', updateBadges);
  } else {
    updateBadges();
  }
  // Update when cart changes (poll every 2s)
  var lastCount = -1;
  setInterval(function() {
    var c = getCartCount();
    if (c !== lastCount) { lastCount = c; updateBadges(); }
  }, 2000);
})();
