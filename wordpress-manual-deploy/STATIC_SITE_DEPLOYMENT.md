# Static Site Deployment — GitHub Pages

Deploy Cognivia landing page instantly (5–10 minutes). No hosting signup required.

## Requirements

- GitHub account
- Public repository (can be username.github.io for user site, or any repo)
- Formspree account (free) for email capture

---

## Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. Repository name:
   - For user site: `username.github.io` (replace `username` with your GitHub username)
   - Or any name: `cognivia-landing`
3. Check **Public** (GitHub Pages requires public for free hosting)
4. Do NOT initialize with README, .gitignore, or license
5. Click "Create repository"

---

## Step 2: Get Formspree Endpoint

1. Go to https://formspree.io/ and sign up (free)
2. Click "New form"
3. Form name: "Cognivia Lead Capture"
4. Add your email: cognivia.business@outlook.com (must verify)
5. Complete verification email
6. Copy the form endpoint URL, e.g.: `https://formspree.io/f/xvnyqaez`
7. Keep this URL handy

---

## Step 3: Configure Form Action

Edit `website/static/index.html`:

Find line around ~180:
```html
<form action="https://formspree.io/f/your-form-id" method="POST">
```

Replace `your-form-id` with your actual Formspree ID (the path after `/f/`)

Example:
```html
<form action="https://formspree.io/f/xvnyqaez" method="POST">
```

Save the file.

---

## Step 4: Deploy to GitHub Pages

Open terminal in `website/static/` directory and run:

```bash
# Initialize git
git init

# Add all files
git add .

# Commit
git commit -m "Deploy Cognivia landing page - 2026-03-20"

# Create main branch
git branch -M main

# Add remote (replace with your repo URL)
git remote add origin https://github.com/yourusername/cognivia-landing.git

# Push
git push -u origin main
```

**Note:** If `website/PUSH_TO_GITHUB.sh` exists, you can run it instead:
```bash
bash PUSH_TO_GITHUB.sh
```
It will prompt for repo URL.

---

## Step 5: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** → **Pages** (left sidebar)
3. "Build and deployment" → Source: **Deploy from a branch**
4. Branch: `main` → `/root` folder
5. Click "Save"
6. Wait ~2 minutes; site will be live at:
   - User site: `https://username.github.io/`
   - Project site: `https://yourusername.github.io/cognivia-landing/`

---

## Step 6: Verify

- Visit your site URL
- Check that email capture form appears
- Submit test email (check cognivia.co@gmail.com inbox)
- Test on mobile
- Check that legal pages (Regulamin, Polityka Prywatności) load

---

## Optional: Custom Domain

1. Buy domain (e.g., cognivia.co)
2. Create CNAME file in `/static` with domain: `cognivia.co`
3. In repository Settings → Pages → Custom domain → enter domain
4. Configure DNS at registrar:
   - `A` records → `185.199.108.153` (or GitHub's current IPs)
   - or `CNAME` → `username.github.io`
5. Save; GitHub will issue free SSL certificate automatically

---

## Post-Deployment

- Set up email notifications in Formspree dashboard
- Add social media links in footer
- Update meta tags with real description if needed
- Prepare to launch marketing campaigns

---

**Problems?** Check GitHub Pages docs or Formspree help. Static site requires no server maintenance and runs forever on GitHub's free infrastructure.
