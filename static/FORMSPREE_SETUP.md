# Set Up Email Capture with Formspree

The static landing page includes an email signup form. To receive submissions:

1. Go to https://formspree.io/ and create a free account.
2. Create a new form.
3. Set the form endpoint URL (e.g., `https://formspree.io/f/xvnyqaez`).
4. Add your email address as the recipient (cognivia.business@outlook.com).
5. Confirm the form via the verification email.
6. Edit `website/static/index.html`:
   - Find the `<form action="https://formspree.io/f/your-form-id"` line.
   - Replace `your-form-id` with your actual Formspree endpoint ID.
7. (Optional) In Formspree dashboard, customize the success/error messages if desired.

Now when a visitor enters their email and submits, you’ll receive an email notification. Formspree free plan allows 50 submissions/month, which is sufficient for pre‑launch.

Alternative: Use a Google Form embed if you prefer, but Formspree is simplest.
