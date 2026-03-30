// CogniCit Service Worker — basic offline support
var CACHE_NAME = 'cognicit-v1';
var URLS_TO_CACHE = [
  '/',
  '/index.html',
  '/produkt.html',
  '/css/cart.css',
  '/js/cognivia-cart.js',
  '/manifest.json'
];

self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(CACHE_NAME).then(function(cache) {
      return cache.addAll(URLS_TO_CACHE);
    })
  );
});

self.addEventListener('fetch', function(event) {
  event.respondWith(
    caches.match(event.request).then(function(response) {
      return response || fetch(event.request);
    })
  );
});
