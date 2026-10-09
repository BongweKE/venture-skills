# Deliverability

Detail for `outbound-sequencing` section 4. Read this when setting up sending
infrastructure or diagnosing why mail is not reaching inboxes.

## Authentication (do this first)

| Record | Purpose | Minimum |
|--------|---------|---------|
| SPF | Authorises sending IPs | Include the sending tool's SPF, one record only |
| DKIM | Cryptographic signature | Enabled and passing on every send |
| DMARC | Policy + reporting | Start `p=none` with an `rua` address; move to `quarantine` once clean |
| Custom tracking domain | Aligns link tracking | CNAME on your domain, not the tool's |

No authentication means no inbox, regardless of copy quality.

## Domain and mailbox architecture

- Send outbound from a **secondary domain** (e.g. `get-company.example`), never the
  primary. Protects transactional and customer mail from a deliverability incident.
- 1 primary domain per sending tool; 3-4 mailboxes per domain; rotate mailboxes.
- Keep per-mailbox volume under ~50/day; total under the provider's ceiling.
- For high volume, register 2-3 backup domains and warm them in parallel.

## Warmup schedule (new domain / mailbox)

| Week | Sends / mailbox / day | Notes |
|------|-----------------------|-------|
| 1 | 10-20 | Real, engaged recipients only; no bulk list |
| 2 | 20-40 | Increase only if bounce < 2% and replies > 0 |
| 3 | 40-50 | Hold at cap; monitor inbox placement |
| 4+ | 50 | Steady state |

Warmup is about **engagement**, not just volume. Sending 50/day to addresses that
never open damages the domain faster than sending 20 to addresses that reply.

## Spam-trigger list (avoid or use sparingly)

Free / guarantee / act now / limited time / 100% / click here / no obligation /
risk-free / this is not spam / ALL CAPS / multiple exclamation marks / ALL-CAPS
subjects / "Dear Sir/Madam". Also avoid attachment-heavy sends and link shorteners
from unknown domains.

## Content hygiene

- Plain text. No images in cold sends; images raise spam scores and break rendering.
- One link at most; link to your real domain, not a redirect.
- Real signature with a physical address where required by law.
- Unsubscribe or "reply STOP" line where required by the recipient's jurisdiction.
- Test render before sending: Gmail, Outlook, Apple Mail.

## Diagnostic loop when mail lands in spam

1. **Check authentication** — SPF/DKIM/DMARC passing? Fix before anything else.
2. **Check bounce rate** — over 2%? Clean the list, suppress hard bounces.
3. **Check volume** — over cap, or a cold domain? Slow down and warm further.
4. **Check content** — spam words, images, too many links, tracking breakage.
5. **Check engagement** — no opens at all? The list or the copy is wrong, not just the tech.
6. **Check reputation** — domain/IP blocklists (e.g. public RBL lookups) and Google Postmaster Tools.

Fix the highest-severity cause first; re-test on a small batch before resuming the full list.
