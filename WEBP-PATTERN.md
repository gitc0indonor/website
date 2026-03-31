# WebP Image Pattern

Use `<picture>` elements for automatic WebP optimization.

## Pattern

```html
<picture>
  <source srcset="/img/photo.webp" type="image/webp">
  <img src="/img/photo.png" alt="..." loading="lazy">
</picture>
```

## Benefits
- 25-40% smaller file sizes vs PNG/JPG
- Automatic format negotiation (browser picks best)
- PNG/JPG fallback for older browsers
- `loading="lazy"` for below-fold images

## CSS
Add `css/webp.css` to pages when real product photos arrive.
