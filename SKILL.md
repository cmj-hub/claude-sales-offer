---
name: cold-offer
description: "Draft a cold offer as a leak, a prototype, a price, a scope, a deadline, and email one. Use when the first outbound email should hand over a finding and a short trial, and when email one must not sell the paid product."
models: ""
---

# Cold offer

A cold offer is not the main service. Email one hands over work already done: a finding the buyer did not request, and a short trial of the solution. The full report is offered only if they want it. There is no meeting ask, no demo, and no pitch.

The build guide teaches a human. This pack teaches an agent.

A sales offer is what the buyer gets, what it costs, and why now. Those three sit on the offer as scope, price, and deadline. Email one delivers the finding. It does not sell the paid product.

You walk out with one cold offer a stranger can send later, from their own sequencer. This pack does not send it. It does not add a paid product. The public next steps already on the site are Friday Signal and the Growth Audit. They are not the offer in email one.

## Inputs

- One concrete miss on their public page or product, in words they already use. They did not ask for it.
- The short trial: one page, one sample, or one worked slice.
- What that trial costs. Not what the retainer costs. If you use a number, label it example and replace it. Do not invent a client price.
- The bound of what they get.
- The date the short trial stops. That is why now.
- The words of email one.

## The six keys

The scorer reads one JSON object. Every value is a string.

1. `leak` — the finding.
2. `prototype` — the short trial.
3. `price` — what the short trial costs.
4. `scope` — what the buyer gets. One bound.
5. `deadline` — why now, as `YYYY-MM-DD`.
6. `email_one` — the letter.

## Decision rules

Leak. One miss. Their words. Not a tour of the whole site.

Prototype. One page, one sample, or one worked slice. It shows the system works. It is not the core retainer.

Price. The cost of the prototype. Free is a cost. Write it in words, or write a number. A number, or a currency mark, must sit in a line that contains the word example. Replace the number before you send. The sample uses 0. That is not a real price. Do not write the retainer's price here.

Scope. What they get. The line must contain the word one, because the bound is one page, one sample, or one slice. Not the core service.

Deadline. A real calendar date, `YYYY-MM-DD`. The day the short trial stops being offered. The sample date is a placeholder. Replace it. It is not a client result.

Email one. States the offer in words the reader understands. It delivers the finding. It names the prototype. It offers the full report only if they want it. It can stay silent on price. The price field already holds the cost. It does not ask the reader to buy, book, or start the paid thing.

Selling means the letter asks for the retainer, a demo, a purchase, a subscription, a checkout, the pricing of the core service, a booked meeting, or a scheduled call. A line that says "book a meeting" or "schedule a call" fails. Naming the finding "your page asks for a meeting" does not fail. That is the leak, not an ask.

A recruiter note that asks for coffee is a different letter. It is not this gate. This gate is selling the paid product.

Price, scope, leak, and prototype fail on the same sell words. The short trial is not a place to hide the retainer.

## Procedure

1. Write the leak in one or two sentences. One miss.
2. Write the prototype. Stop at the short trial.
3. Write the price of that trial. If there is a number, include the word example and plan to replace the number.
4. Write the scope. Use the word one. Say where it stops.
5. Write the deadline as `YYYY-MM-DD`.
6. Write email one. Deliver the leak. Name the page or sample you wrote. Offer the full report only if they want it. Do not ask for the paid product.
7. Save `draft.json`. From the repo root, run `python3 scripts/score.py --file draft.json`.

Exit 0 prints the six lines. Exit 1 prints one reason and does not print the offer.

## Filled example

Example only. Replace every line. The price 0 is not a price you should send. The date is not a client deadline.

The offer, in words:

- What they get: one page that leads with one finding, and stops.
- What it costs: example price, replace this before you send, 0 for that page.
- Why now: the short trial stops on 2026-12-15. Replace that date.

Email one:

Your homepage asks for a meeting before it shows any work. I wrote one page that leads with that finding. The full report is yours if you want it.

```json
{
  "leak": "The homepage asks for a meeting before it shows any work.",
  "prototype": "A one-page sample that leads with one finding and the short trial, and stops there.",
  "price": "Example price, replace this before you send: 0 for the one-page sample.",
  "scope": "One page. One finding. The short trial stops there.",
  "deadline": "2026-12-15",
  "email_one": "Your homepage asks for a meeting before it shows any work. I wrote one page that leads with that finding. The full report is yours if you want it."
}
```

## What exit 1 means

- `email one that sells the paid product` — the letter asks them to buy, book, or start the paid thing.
- `the offer sells the paid product` — the leak, the prototype, the price, or the scope does that instead.
- `draft is incomplete` — a string is blank.
- `price is not labeled example` — a number or currency mark is not marked example.
- `scope is not one bound` — the word one is missing.
- `deadline is not a date` — it is not a real `YYYY-MM-DD`.

## Checklist

Copy this list and tick it in order.

- [ ] 1. Choose the finding the buyer did not request.
- [ ] 2. Fill the offer shell: leak, prototype, price, scope, deadline, email one.
- [ ] 3. From the repo root, run `python3 scripts/score.py --file draft.json`.

Check again until the script exits 0.

Go back to step 2 if step 3 fails.

## Run

```bash
python3 scripts/score.py --file examples/offer-good.json
python3 scripts/score.py --file examples/offer-sells.json
```

The good file exits 0 and prints the leak, the prototype, the price, the scope, the deadline, and email one. The sell file exits 1.

A broken JSON exits non-zero and does not echo the raw input.

Python 3 standard library only. No network. No send.
