/* ==========================================================================
   GA4 Ecommerce Event Tracking for Cognivia
   Pushes standard ecommerce events to dataLayer.
   Requires GA4 Measurement ID — set window.GA4_ID before this script loads.
   Falls back gracefully if gtag is not loaded.
   ========================================================================== */

(function() {
  'use strict';

  // Safe dataLayer push — works even without gtag
  function dlPush(event, params) {
    try {
      window.dataLayer = window.dataLayer || [];
      window.dataLayer.push(Object.assign({ event: event }, params || {}));
    } catch(e) { /* silent */ }
  }

  // GA4 ecommerce events API
  window.CogniviaAnalytics = {

    // view_item — fire on produkt.html page load
    viewItem: function(product) {
      dlPush('view_item', {
        currency: 'PLN',
        value: product.price || 79,
        items: [{
          item_id: product.id || 'cognicit',
          item_name: product.name || 'CogniCit',
          item_category: 'Suplement diety',
          item_brand: 'Cognivia',
          price: product.price || 79,
          quantity: 1
        }]
      });
    },

    // add_to_cart — fire when addItem is called
    addToCart: function(productId, qty, price) {
      dlPush('add_to_cart', {
        currency: 'PLN',
        value: (price || 79) * (qty || 1),
        items: [{
          item_id: productId || 'cognicit',
          item_name: 'CogniCit',
          item_category: 'Suplement diety',
          item_brand: 'Cognivia',
          price: price || 79,
          quantity: qty || 1
        }]
      });
    },

    // view_cart — fire on koszyk.html load
    viewCart: function(cart) {
      if (!cart || !cart.items || cart.items.length === 0) return;
      var totalValue = 0;
      var items = cart.items.map(function(i) {
        var price = 79;
        var val = price * i.quantity;
        totalValue += val;
        return {
          item_id: i.id,
          item_name: 'CogniCit',
          item_category: 'Suplement diety',
          item_brand: 'Cognivia',
          price: price,
          quantity: i.quantity
        };
      });
      dlPush('view_cart', { currency: 'PLN', value: totalValue, items: items });
    },

    // begin_checkout — fire on kasa.html load
    beginCheckout: function(cart) {
      if (!cart || !cart.items || cart.items.length === 0) return;
      var totalValue = 0;
      var items = cart.items.map(function(i) {
        var price = 79;
        var val = price * i.quantity;
        totalValue += val;
        return {
          item_id: i.id,
          item_name: 'CogniCit',
          item_category: 'Suplement diety',
          item_brand: 'Cognivia',
          price: price,
          quantity: i.quantity
        };
      });
      dlPush('begin_checkout', { currency: 'PLN', value: totalValue, items: items });
    },

    // purchase — fire on successful order
    purchase: function(order) {
      if (!order) return;
      var items = (order.items || []).map(function(i) {
        return {
          item_id: i.id || 'cognicit',
          item_name: 'CogniCit',
          item_category: 'Suplement diety',
          item_brand: 'Cognivia',
          price: 79,
          quantity: i.quantity || 1
        };
      });
      dlPush('purchase', {
        transaction_id: order.id || ('COG-' + Date.now()),
        value: order.total || 0,
        currency: 'PLN',
        shipping: order.shippingCost || 0,
        items: items
      });
    }
  };

})();
