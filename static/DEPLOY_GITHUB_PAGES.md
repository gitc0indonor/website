# Deploy Cognivia Static Landing Page on GitHub Pages

## Prerequisites
- GitHub account
- Git installed on your machine (or use GitHub web UI)

## Steps

1. **Create a new repository**
   - Name: `cognivia.github.io` (or any name if using a project page)
   - Set to **Public** (GitHub Pages requires public for free hosting)
   - Do not initialize with README.

2. **Push the static site**
   - Clone the repository to your local machine.
   - Copy all files from `website/static/` into the repo root.
   - Commit and push:
     ```
     git add .
     git commit -m "Initial Cognivia landing page"
     git branch -M main
     git remote add origin https://github.com/yourusername/cognivia.github.io.git
     git push -u origin main
     ```

3. **Enable GitHub Pages**
   - Go to repository Settings → Pages.
   - Source: Deploy from a branch.
   - Branch: `main`, folder: `/ (root)`.
   - Save. GitHub will publish at `https://yourusername.github.io/`.

4. **Custom domain (optional)**
   - In Pages settings, add custom domain `cognivia.pl` (or `www.cognivia.pl`).
   - Create DNS records:
     - A records → 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153
     - Or CNAME to `yourusername.github.io`.
   - Enable HTTPS after DNS propagation (GitHub provides free certificate).

5. **Update links**
   - Ensure all internal links point to `index.html` or other local files.
   - The contact email is `cognivia.business@outlook.com` — replace with a contact form later if desired.

6. **SEO**
   - The page includes basic meta description.
   - Add `sitemap.xml` and `robots.txt` later if needed.

Need any changes to content or styling? Let me know and I’ll adjust before you deploy.
