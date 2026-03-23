/* ==========================================================================
   Cognivia Cart System — Pure JS Cart for Static Site
   ========================================================================== */

const CogniviaCart = {
  STORAGE_KEY: 'cognivia_cart',
  
  // Product catalog
  products: {
    'cognicit': {
      id: 'cognicit',
      name: 'CogniCit',
      nameFull: 'CogniCit — Suplement diety na koncentrację',
      price: 79.00,
      currency: 'PLN',
      image: 'assets/cognicit-box.png',
      weight: 0.15, // kg
      description: '30 kapsułek — kwas alfa-liponowy 250 mg, cytykolina 300 mg, beta-cyklodekstryna 250 mg',
      inStock: true,
      maxQty: 10
    }
  },

  // Shipping methods (Poland only)
  shipping: [
    { id: 'inpost_locker', name: 'InPost Paczkomat', price: 12.99, freeFrom: 120, days: '1-2 dni robocze', icon: '📦' },
    { id: 'inpost_courier', name: 'InPost Kurier', price: 15.99, freeFrom: 120, days: '1-2 dni robocze', icon: '🚚' },
    { id: 'dpd', name: 'DPD Kurier', price: 16.99, freeFrom: 150, days: '1-2 dni robocze', icon: '🚚' },
    { id: 'poczta', name: 'Poczta Polska (priorytet)', price: 11.99, freeFrom: 120, days: '2-3 dni robocze', icon: '✉️' }
  ],

  // Payment methods
  payments: [
    { id: 'payu', name: 'PayU', desc: 'Karta, BLIK, przelew', icon: '💳', recommended: true },
    { id: 'przelewy24', name: 'Przelewy24', desc: 'Szybki przelew online', icon: '🏦' },
    { id: 'blik', name: 'BLIK', desc: 'Kod BLIK z aplikacji bankowej', icon: '📱' },
    { id: 'paypal', name: 'PayPal', desc: 'Płatność przez PayPal', icon: '🅿️' },
    { id: 'transfer', name: 'Przelew tradycyjny', desc: 'Płatność z góry przelewem', icon: '📄' },
    { id: 'cod', name: 'Pobranie', desc: 'Zapłać przy odbiorze (+8 zł)', icon: '💵' }
  ],

  // VAT rate
  vatRate: 0.23,

  // ---- Cart Operations ----
  
  getCart() {
    try {
      return JSON.parse(localStorage.getItem(this.STORAGE_KEY)) || { items: [], shipping: null, payment: null };
    } catch { return { items: [], shipping: null, payment: null }; }
  },

  saveCart(cart) {
    localStorage.setItem(this.STORAGE_KEY, JSON.stringify(cart));
    this.updateUI();
  },

  addItem(productId, qty = 1) {
    const product = this.products[productId];
    if (!product || !product.inStock) return false;
    const cart = this.getCart();
    const existing = cart.items.find(i => i.id === productId);
    if (existing) {
      existing.qty = Math.min(existing.qty + qty, product.maxQty);
    } else {
      cart.items.push({ id: productId, qty: Math.min(qty, product.maxQty) });
    }
    this.saveCart(cart);
    this.showNotification(`${product.name} dodano do koszyka`);
    return true;
  },

  removeItem(productId) {
    const cart = this.getCart();
    cart.items = cart.items.filter(i => i.id !== productId);
    this.saveCart(cart);
  },

  updateQty(productId, qty) {
    const product = this.products[productId];
    if (!product) return;
    const cart = this.getCart();
    const item = cart.items.find(i => i.id === productId);
    if (item) {
      item.qty = Math.max(1, Math.min(qty, product.maxQty));
      this.saveCart(cart);
    }
  },

  clearCart() {
    localStorage.removeItem(this.STORAGE_KEY);
    this.updateUI();
  },

  setShipping(shippingId) {
    const cart = this.getCart();
    cart.shipping = shippingId;
    this.saveCart(cart);
  },

  setPayment(paymentId) {
    const cart = this.getCart();
    cart.payment = paymentId;
    this.saveCart(cart);
  },

  // ---- Calculations ----

  getSubtotal() {
    const cart = this.getCart();
    return cart.items.reduce((sum, item) => {
      const product = this.products[item.id];
      return sum + (product ? product.price * item.qty : 0);
    }, 0);
  },

  getShippingCost() {
    const cart = this.getCart();
    if (!cart.shipping) return 0;
    const method = this.shipping.find(s => s.id === cart.shipping);
    if (!method) return 0;
    // Free shipping threshold
    if (method.freeFrom && this.getSubtotal() >= method.freeFrom) return 0;
    // COD surcharge
    if (cart.payment === 'cod') return method.price + 8;
    return method.price;
  },

  getTotal() {
    return this.getSubtotal() + this.getShippingCost();
  },

  getNetTotal() {
    return this.getTotal() / (1 + this.vatRate);
  },

  getVatAmount() {
    return this.getTotal() - this.getNetTotal();
  },

  getItemCount() {
    return this.getCart().items.reduce((sum, item) => sum + item.qty, 0);
  },

  // ---- UI Updates ----

  updateUI() {
    // Update cart count badges
    const count = this.getItemCount();
    document.querySelectorAll('.cart-count').forEach(el => {
      el.textContent = count;
      el.style.display = count > 0 ? 'flex' : 'none';
    });
    
    // Update cart total displays
    const total = this.getTotal();
    document.querySelectorAll('.cart-total').forEach(el => {
      el.textContent = this.formatPrice(total);
    });

    // Update mini cart if present
    this.renderMiniCart();
  },

  formatPrice(amount) {
    return amount.toFixed(2).replace('.', ',') + ' zł';
  },

  renderMiniCart() {
    const container = document.getElementById('mini-cart-items');
    if (!container) return;
    const cart = this.getCart();
    if (cart.items.length === 0) {
      container.innerHTML = '<p class="mini-cart-empty">Koszyk jest pusty</p>';
      return;
    }
    container.innerHTML = cart.items.map(item => {
      const p = this.products[item.id];
      return `
        <div class="mini-cart-item">
          <div class="mini-cart-item-info">
            <strong>${p.name}</strong>
            <span>${item.qty} × ${this.formatPrice(p.price)}</span>
          </div>
          <button class="mini-cart-remove" onclick="CogniviaCart.removeItem('${item.id}')" aria-label="Usuń">×</button>
        </div>`;
    }).join('') + `
      <div class="mini-cart-total">
        <span>Razem:</span>
        <strong>${this.formatPrice(this.getSubtotal())}</strong>
      </div>
      <a href="kasa.html" class="mini-cart-checkout-btn">Przejdź do kasy</a>`;
  },

  renderCartPage() {
    const container = document.getElementById('cart-page-items');
    if (!container) return;
    const cart = this.getCart();
    if (cart.items.length === 0) {
      container.innerHTML = `
        <div class="cart-empty">
          <div class="cart-empty-icon">🛒</div>
          <h2>Twój koszyk jest pusty</h2>
          <p>Dodaj CogniCit do koszyka, aby kontynuować zakupy.</p>
          <a href="produkt.html" class="btn-primary">Zobacz produkt</a>
        </div>`;
      return;
    }
    container.innerHTML = cart.items.map(item => {
      const p = this.products[item.id];
      return `
        <div class="cart-item">
          <div class="cart-item-image">
            <div class="cart-item-img-placeholder">${p.name.charAt(0)}</div>
          </div>
          <div class="cart-item-details">
            <h3>${p.nameFull}</h3>
            <p class="cart-item-desc">${p.description}</p>
            <div class="cart-item-price">${this.formatPrice(p.price)} / szt.</div>
          </div>
          <div class="cart-item-actions">
            <div class="qty-control">
              <button onclick="CogniviaCart.updateQty('${item.id}', ${item.qty - 1}); CogniviaCart.renderCartPage();" ${item.qty <= 1 ? 'disabled' : ''}>−</button>
              <span class="qty-display">${item.qty}</span>
              <button onclick="CogniviaCart.updateQty('${item.id}', ${item.qty + 1}); CogniviaCart.renderCartPage();" ${item.qty >= p.maxQty ? 'disabled' : ''}>+</button>
            </div>
            <div class="cart-item-subtotal">${this.formatPrice(p.price * item.qty)}</div>
            <button class="cart-item-remove" onclick="CogniviaCart.removeItem('${item.id}'); CogniviaCart.renderCartPage();">Usuń</button>
          </div>
        </div>`;
    }).join('');
  },

  renderCheckoutPage() {
    const cart = this.getCart();
    if (cart.items.length === 0) {
      window.location.href = 'kasa.html';
      return;
    }

    // Render order summary
    const summaryEl = document.getElementById('checkout-summary');
    if (summaryEl) {
      summaryEl.innerHTML = cart.items.map(item => {
        const p = this.products[item.id];
        return `<div class="summary-row"><span>${p.name} × ${item.qty}</span><span>${this.formatPrice(p.price * item.qty)}</span></div>`;
      }).join('');
    }

    // Render shipping options
    const shippingEl = document.getElementById('shipping-options');
    if (shippingEl) {
      shippingEl.innerHTML = this.shipping.map(s => {
        const isFree = s.freeFrom && this.getSubtotal() >= s.freeFrom;
        const isSelected = cart.shipping === s.id;
        return `
          <label class="shipping-option ${isSelected ? 'selected' : ''}">
            <input type="radio" name="shipping" value="${s.id}" ${isSelected ? 'checked' : ''} onchange="CogniviaCart.setShipping('${s.id}'); CogniviaCart.renderCheckoutPage();">
            <div class="shipping-option-content">
              <span class="shipping-icon">${s.icon}</span>
              <div class="shipping-info">
                <strong>${s.name}</strong>
                <span class="shipping-days">${s.days}</span>
              </div>
              <span class="shipping-price">${isFree ? '<span class="free-shipping">GRATIS</span>' : this.formatPrice(s.price)}</span>
            </div>
          </label>`;
      }).join('');
    }

    // Render payment options
    const paymentEl = document.getElementById('payment-options');
    if (paymentEl) {
      paymentEl.innerHTML = this.payments.map(p => {
        const isSelected = cart.payment === p.id;
        return `
          <label class="payment-option ${isSelected ? 'selected' : ''} ${p.recommended ? 'recommended' : ''}">
            <input type="radio" name="payment" value="${p.id}" ${isSelected ? 'checked' : ''} onchange="CogniviaCart.setPayment('${p.id}'); CogniviaCart.renderCheckoutPage();">
            <div class="payment-option-content">
              <span class="payment-icon">${p.icon}</span>
              <div class="payment-info">
                <strong>${p.name} ${p.recommended ? '<span class="badge-recommended">Polecane</span>' : ''}</strong>
                <span class="payment-desc">${p.desc}</span>
              </div>
            </div>
          </label>`;
      }).join('');
    }

    // Update totals
    const subtotal = this.getSubtotal();
    const shippingCost = this.getShippingCost();
    const total = this.getTotal();
    
    const subtotalEl = document.getElementById('summary-subtotal');
    const shippingEl2 = document.getElementById('summary-shipping');
    const vatEl = document.getElementById('summary-vat');
    const totalEl = document.getElementById('summary-total');
    
    if (subtotalEl) subtotalEl.textContent = this.formatPrice(subtotal);
    if (shippingEl2) shippingEl2.innerHTML = shippingCost === 0 ? '<span class="free-shipping">GRATIS</span>' : this.formatPrice(shippingCost);
    if (vatEl) vatEl.textContent = this.formatPrice(this.getVatAmount());
    if (totalEl) totalEl.textContent = this.formatPrice(total);
  },

  // ---- Notifications ----

  showNotification(message) {
    let container = document.getElementById('cart-notifications');
    if (!container) {
      container = document.createElement('div');
      container.id = 'cart-notifications';
      document.body.appendChild(container);
    }
    const notif = document.createElement('div');
    notif.className = 'cart-notification';
    notif.innerHTML = `<span>✓</span> ${message}`;
    container.appendChild(notif);
    requestAnimationFrame(() => notif.classList.add('show'));
    setTimeout(() => {
      notif.classList.remove('show');
      setTimeout(() => notif.remove(), 300);
    }, 2500);
  },

  // ---- Checkout Submission ----

  submitOrder(formData) {
    const cart = this.getCart();
    if (cart.items.length === 0) return false;
    if (!cart.shipping) { this.showNotification('Wybierz metodę dostawy'); return false; }
    if (!cart.payment) { this.showNotification('Wybierz metodę płatności'); return false; }

    const order = {
      id: 'COG-' + Date.now().toString(36).toUpperCase(),
      date: new Date().toISOString(),
      items: cart.items.map(i => ({ ...i, product: this.products[i.id] })),
      shipping: this.shipping.find(s => s.id === cart.shipping),
      payment: this.payments.find(p => p.id === cart.payment),
      customer: formData,
      subtotal: this.getSubtotal(),
      shippingCost: this.getShippingCost(),
      vat: this.getVatAmount(),
      total: this.getTotal(),
      status: 'pending_payment'
    };

    // Save order to localStorage (would be sent to backend in production)
    const orders = JSON.parse(localStorage.getItem('cognivia_orders') || '[]');
    orders.push(order);
    localStorage.setItem('cognivia_orders', JSON.stringify(orders));

    // Clear cart
    this.clearCart();

    // Redirect to confirmation
    window.location.href = 'potwierdzenie.html?order=' + order.id;
    return true;
  },

  // ---- Init ----

  init() {
    this.updateUI();
    // Render cart page if on cart page
    if (document.getElementById('cart-page-items')) this.renderCartPage();
    // Render checkout if on checkout page
    if (document.getElementById('checkout-summary')) this.renderCheckoutPage();
  }
};

// Auto-init on DOM ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => CogniviaCart.init());
} else {
  CogniviaCart.init();
}
