/* Abandoned Cart Recovery Banner — #330
 * Detects items in cart from previous session and shows recovery banner.
 * Non-intrusive: appears after 10s if cart has items, dismissible, localStorage persistence.
 */
(function() {
  'use strict';
  
  var DISMISSED_KEY = 'cartRecoveryDismissed';
  var PAGE_LOAD_TIME = Date.now();
  var DELAY_BEFORE_SHOW = 10000; // 10 seconds
  
  // Check if already dismissed today
  var dismissed = localStorage.getItem(DISMISSED_KEY);
  if (dismissed) {
    var dismissedDate = new Date(parseInt(dismissed)).toDateString();
    if (dismissedDate === new Date().toDateString()) return;
  }
  
  function checkCart() {
    try {
      var cart = JSON.parse(localStorage.getItem('cognivia_cart') || '[]');
      if (!Array.isArray(cart) || cart.length === 0) return false;
      
      // Check if order was recently completed (within 24h)
      var lastOrder = localStorage.getItem('lastOrderId');
      if (lastOrder) return false;
      
      return cart;
    } catch(e) { return false; }
  }
  
  function getCartSummary(cart) {
    var total = 0;
    var items = [];
    for (var i = 0; i < cart.length; i++) {
      var qty = cart[i].quantity || 1;
      var price = cart[i].price || 7900;
      total += qty * price;
      items.push(cart[i].name + ' ×' + qty);
    }
    return { total: total, items: items, count: cart.reduce(function(s,c){ return s + (c.quantity||1); }, 0) };
  }
  
  function formatPrice(cents) {
    return (cents / 100).toFixed(2).replace('.', ',') + ' zł';
  }
  
  function createBanner(cart) {
    var summary = getCartSummary(cart);
    
    // Create banner element
    var banner = document.createElement('div');
    banner.id = 'cart-recovery-banner';
    banner.innerHTML = 
      '<button class="cr-close" aria-label="Zamknij">&times;</button>' +
      '<div class="cr-title">🛒 Masz coś w koszyku!</div>' +
      '<div class="cr-items">' + summary.count + ' produkt' + (summary.count > 1 ? 'y' : '') + ' · ' + formatPrice(summary.total) + '</div>' +
      '<a href="koszyk.html" class="cr-btn">Dokończ zamówienie →</a>';
    
    document.body.appendChild(banner);
    
    // Show after delay
    setTimeout(function() {
      banner.style.display = 'block';
    }, DELAY_BEFORE_SHOW);
    
    // Close handler
    banner.querySelector('.cr-close').addEventListener('click', function() {
      banner.style.display = 'none';
      localStorage.setItem(DISMISSED_KEY, Date.now().toString());
    });
  }
  
  // Don't show on cart or checkout pages
  var path = window.location.pathname;
  if (path.indexOf('koszyk') > -1 || path.indexOf('kasa') > -1 || path.indexOf('potwierdzenie') > -1) return;
  
  // Load CSS
  var link = document.createElement('link');
  link.rel = 'stylesheet';
  link.href = path.indexOf('/blog/') > -1 ? '../css/cart-recovery.css' : 'css/cart-recovery.css';
  document.head.appendChild(link);
  
  // Check cart on load
  var cart = checkCart();
  if (cart) {
    createBanner(cart);
  }
})();
