/**
 * CogniCit — Core Web Vitals Monitoring
 * Tracks LCP, CLS, INP and logs to console
 * Lightweight: ~1.5KB, no external dependencies
 */
(function() {
  'use strict';

  // Skip if PerformanceObserver not supported
  if (!window.PerformanceObserver) return;

  var vitals = { lcp: null, cls: 0, inp: null, fcp: null, ttfb: null };

  function log(metric, value, rating) {
    var rounded = Math.round(value * 100) / 100;
    console.log('[CWV] ' + metric + ': ' + rounded + 'ms (' + rating + ')');
    vitals[metric.toLowerCase()] = rounded;

    // Optional: send to analytics endpoint
    // navigator.sendBeacon && navigator.sendBeacon('/api/vitals', JSON.stringify({
    //   metric: metric, value: rounded, rating: rating, page: location.pathname, ts: Date.now()
    // }));
  }

  function rateLCP(val) { return val <= 2500 ? 'good' : val <= 4000 ? 'needs-improvement' : 'poor'; }
  function rateCLS(val) { return val <= 0.1 ? 'good' : val <= 0.25 ? 'needs-improvement' : 'poor'; }
  function rateINP(val) { return val <= 200 ? 'good' : val <= 500 ? 'needs-improvement' : 'poor'; }
  function rateTTFB(val) { return val <= 800 ? 'good' : val <= 1800 ? 'needs-improvement' : 'poor'; }
  function rateFCP(val) { return val <= 1800 ? 'good' : val <= 3000 ? 'needs-improvement' : 'poor'; }

  // LCP — Largest Contentful Paint
  try {
    new PerformanceObserver(function(list) {
      var entries = list.getEntries();
      var last = entries[entries.length - 1];
      if (last) log('LCP', last.startTime, rateLCP(last.startTime));
    }).observe({ type: 'largest-contentful-paint', buffered: true });
  } catch(e) {}

  // CLS — Cumulative Layout Shift
  try {
    var clsValue = 0;
    new PerformanceObserver(function(list) {
      list.getEntries().forEach(function(entry) {
        if (!entry.hadRecentInput) clsValue += entry.value;
      });
      log('CLS', clsValue, rateCLS(clsValue));
    }).observe({ type: 'layout-shift', buffered: true });
  } catch(e) {}

  // INP — Interaction to Next Paint
  try {
    new PerformanceObserver(function(list) {
      list.getEntries().forEach(function(entry) {
        if (entry.interactionId) {
          var inp = entry.processingEnd - entry.startTime;
          log('INP', inp, rateINP(inp));
        }
      });
    }).observe({ type: 'event', buffered: true, durationThreshold: 40 });
  } catch(e) {}

  // FCP — First Contentful Paint
  try {
    new PerformanceObserver(function(list) {
      list.getEntries().forEach(function(entry) {
        if (entry.name === 'first-contentful-paint') {
          log('FCP', entry.startTime, rateFCP(entry.startTime));
        }
      });
    }).observe({ type: 'paint', buffered: true });
  } catch(e) {}

  // TTFB — Time to First Byte
  try {
    var nav = performance.getEntriesByType('navigation')[0];
    if (nav) log('TTFB', nav.responseStart, rateTTFB(nav.responseStart));
  } catch(e) {}

  // Summary on page unload
  window.addEventListener('visibilitychange', function() {
    if (document.visibilityState === 'hidden') {
      console.log('[CWV] Summary:', JSON.stringify(vitals));
    }
  });

  // Expose for debugging
  window.__cogniVitals = vitals;
})();
