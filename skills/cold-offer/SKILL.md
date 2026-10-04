---
name: cold-offer
description: "Draft a give-first cold offer: a leak (one finding the buyer did not ask for), a prototype (a short trial of the fix), and email one that hands both over without selling. Use when the user asks for a give-first or value-first first touch, a cold offer, or a first email that must not pitch the paid product or ask for a meeting. Not for a standard signal-anchored cold email or follow-up sequence (use cold-email). Scores the draft with a local script; never sends."
models: ""
---

# Cold offer

A cold offer is not the main service. Email one hands over work already done: a finding the buyer did not request, and a short trial of the solution. The full report is offered only if they want it. There is no meeting ask, no demo, and no pitch.

## The three parts

1. Leak. The finding, in words the reader already uses. One concrete miss on their public page or product. They did not ask for it.
2. Prototype. The short trial. One page, one sample, or one worked slice of the fix. It shows the system works. It is not the core retainer.
3. Email one. States that offer in words the reader understands. It delivers the finding. It names the prototype. It offers the full report only if they want it.

## Inputs

Ask for what is missing before drafting:

- The buyer: company, and the public page or product to look at.
- What the user sells, so the prototype is a slice of it and not the whole thing.

If `brand-config.json` is at the project root, read it first. Take the pain from `psp.primary_pain` and write email one in `psp.vocabulary`. Take the outcome the prototype previews from `evp.outcome`, and keep it inside `evp.primary`. Use them as given; do not ask for them again. If a block is missing, say which pack produces it (`/plugin install psp@gtm-operator-skills`, `/plugin install evp@gtm-operator-skills`) and work from the page and the user's answers. Never invent the values.

If the user gave a URL and the page can be read, find the leak there. Do not invent a finding the page does not show. If you cannot see the page, ask the user for the finding.

## Workflow

Copy this list and tick it in order.

- [ ] 1. Choose one finding the buyer did not request. One, not a list.
- [ ] 2. Fill the shell below: `leak`, `prototype`, `email_one`. Write it to a scratch file, not the user's repo.
- [ ] 3. Run `python3 ${CLAUDE_SKILL_DIR}/scripts/score.py --file draft.json --json`.
- [ ] 4. If it exits 1, apply each `fix` and go back to step 2. Repeat until it exits 0.
- [ ] 5. Show the user the leak, the prototype, and email one. Do not send it.

Exit codes: `0` pass, `1` a check failed, `2` bad input (missing file, broken JSON, not an object). Bad input never echoes the raw draft.

## What the scorer checks

| Check | Fails when | Fix |
| --- | --- | --- |
| `sells` | Email one asks the reader to buy, book, or start the paid thing: retainer, demo, purchase, subscribe, checkout, plans, or pricing of the core service. | Cut the ask. Offer the full report only if they want it. |
| `meeting` | Email one asks for time: book a call, quick chat, 15-minute call, calendar link. Mentioning a meeting is fine; asking for one is not. | Hand over the finding and stop. |
| `complete` | `leak`, `prototype`, or `email_one` is missing or empty. | Fill all three with non-empty strings. |
| `finding` | Email one shares too few key words with the leak, so it does not deliver the finding. | State the leak in email one, in the reader's words. |
| `length` | Email one is over 120 words. | Cut to the finding, the prototype, and the offer of the report. |

The output names the phrase that tripped each check. A false positive (for example, "no retainer") is still worth rewording: the reader skims the same way the regex does.

A recruiter note that asks for coffee is a different letter. This pack does not write it.

## Works with the suite

This is step 5 of the GTM operator suite (`/plugin marketplace add cmj-hub/gtm-operator-skills`).

- **Reads:** `psp` (pain, vocabulary) and `evp` (outcome, line) from `brand-config.json` if present.
- **Writes:** nothing outside the draft. Never touches `brand-config.json`.
- **Before this:** psp (`/psp:psp`) and evp (`/evp:evp`), when there is no `psp` or `evp` block; prospect-list (`/prospect-list:who-to-contact`), when you do not yet know who to send it to.
- **Instead of this:** cold-email (`/cold-email:cold-email`), for a signal-anchored first touch with a binary ask and Day 3 / 7 / 14 follow-ups.
- **After this:** landing-page (`/landing-page:page`) for the page the full report points to; pricing (`/pricing:pricing`) when they ask what the core service costs.

If a companion pack is not installed, name it and its install line (`/plugin install <name>@gtm-operator-skills`); do not do its job inline.

## Shell

```json
{
  "leak": "The homepage asks for a meeting before it shows any work.",
  "prototype": "A one-page sample that leads with one finding and the short trial, and stops there.",
  "email_one": "Your homepage asks for a meeting before it shows any work. I wrote one page that leads with that finding. The full report is yours if you want it."
}
```

## Examples

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/score.py --file ${CLAUDE_SKILL_DIR}/examples/offer-good.json    # exits 0, prints the three parts
python3 ${CLAUDE_SKILL_DIR}/scripts/score.py --file ${CLAUDE_SKILL_DIR}/examples/offer-sells.json   # exits 1, names "retainer", "book a demo"
```

Python 3 standard library only. No network. No send.
