---
name: cold-offer
description: "Draft a give-first cold offer — a leak (one finding the buyer did not ask for), a prototype (a short trial of the fix), and email one that hands both over without selling. Use when the user asks for a cold email, first-touch outbound, a give-first or value-first opener, or a cold offer, and email one must not pitch the paid product or ask for a meeting. Scores the draft with a local script; never sends."
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

If the user gave a URL and the page can be read, find the leak there. Do not invent a finding the page does not show. If you cannot see the page, ask the user for the finding.

## Workflow

Copy this list and tick it in order.

- [ ] 1. Choose one finding the buyer did not request. One, not a list.
- [ ] 2. Fill the shell below: `leak`, `prototype`, `email_one`. Write it to a scratch file, not the user's repo.
- [ ] 3. Run `python3 scripts/score.py --file draft.json --json` from this skill's directory.
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
python3 scripts/score.py --file examples/offer-good.json    # exits 0, prints the three parts
python3 scripts/score.py --file examples/offer-sells.json   # exits 1, names "retainer", "book a demo"
```

Python 3 standard library only. No network. No send.
