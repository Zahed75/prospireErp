# VexaNext Multi-Company Setup Runbook

Everything needed to run VexaNext (vexanext.com) as a second branded company
on the same Odoo instance as ProspireNext.

- ERP entry point: `https://hq.vexanext.com` → same Odoo (ports 8070/8074),
  same database (`dbfilter = ^prospire_hq$`). Users pick the company after login.
- Mail: VexaNext sends AS `vexanext@gmail.com` through its own Gmail login.

---

## 1. Cloudflare / DNS (vexanext.com)

Already done: `hq.vexanext.com A → 217.216.58.129`, SSL on the aaPanel site.

**Important — DMARC is `p=reject` with an empty DKIM record:**
as long as mail is sent **From: @gmail.com addresses**, this is fine (Gmail
authenticates its own domain). But **never** configure Odoo/templates to send
`From: anything@vexanext.com` — receivers will hard-reject it because no DKIM
signing exists for vexanext.com. If you later want branded `@vexanext.com`
senders, sign up a transactional ESP (SendGrid/Brevo/Mailgun), add their DKIM
keys to the `*_domainkey.vexanext.com` TXT record (currently empty — delete it
or fill it), and add the ESP to SPF. Until then, remove any `@vexanext.com`
addresses from Odoo user/company email fields.

The existing SPF `v=spf1 ip4:217.216.58.129 include:vexanext.com ~all` is
harmless; no mail is sent directly from the VPS.

## 2. aaPanel nginx for hq.vexanext.com

1. aaPanel → Website → add site `hq.vexanext.com` → apply SSL.
2. Website → Config → replace the proxy section with the contents of
   `nginx/hq.vexanext.com.proxy.conf` (same pattern as the hq.prospirenext.com
   proxy file — see its header comment for the exact target path).
3. `nginx -t && systemctl reload nginx`
4. Verify: `https://hq.vexanext.com/web/login` shows the Odoo login page.

Do **not** add upstream/map blocks for this domain — they already exist in the
edu/hq full vhost and duplicates break `nginx -t`.

## 3. Server / Docker (mail fixes + pending fixes)

1. Get a Gmail app password for **vexanext@gmail.com**
   (myaccount.google.com → Security → 2-Step Verification → App passwords).
2. On the server, add to `.env`:
   ```
   VEXA_SMTP_USER=vexanext@gmail.com
   VEXA_SMTP_PASSWORD=<16-char app password>
   ```
   (`MAIL_CATCHALL_DOMAIN` stays empty — replies go to the sender.)
3. Deploy:
   ```bash
   cd /opt/odoo && git pull
   docker compose up -d --build
   ```
   This same rebuild also activates the two earlier fixes:
   - `workers = 2` → websocket works → Discuss "Real-time connection lost" gone.
   - spreadsheet xlsx-import crash patch.

## 4. Odoo settings (in the UI — fixes the broken quotation/invoice PDF)

The PDF header/letterhead is **per company**. VexaNext never got a document
layout, so reports render bare.

1. Switch to the **VexaNext** company (top-right company selector).
2. Settings → General Settings → **Companies** → open **VexaNext**:
   - fill address, phone, email (`vexanext@gmail.com`), website (`www.vexanext.com`);
   - upload the company logo.
3. On the company form (or General Settings → Business Documents) click
   **Document Layout** → choose a layout (e.g. Boxed) → set colors/fonts →
   confirm with the print preview.
4. Settings → General Settings → **Email Content** (or user form) → set the
   email signature for VexaNext users (the "Engineering Manager, VexaNext /
   vexanext@gmail.com | www.vexanext.com" block).
5. Settings → Technical → **Outgoing Mail Servers**: expect two entries —
   `Prospire SMTP` (From Filtering = prospirenext@gmail.com) and
   `Vexa SMTP` (From Filtering = vexanext@gmail.com), both tested OK.
6. Send a test quotation from the VexaNext company and confirm the PDF has the
   VexaNext letterhead and the mail arrives in the inbox, not spam.

## 5. Known limitations

- Links inside VexaNext emails (buttons, documents) point to
  `hq.prospirenext.com` because `web.base.url` is frozen to a single value.
  Cosmetic; everything still works after login.
- Mail sent with a *different* personal Gmail as From (employees' own
  addresses) still routes through the Prospire SMTP login. If that gets
  spam-flagged too, either standardize sender addresses per company or move to
  an ESP per domain (see step 1).
