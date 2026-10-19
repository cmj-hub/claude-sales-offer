# Full offer

The whole offer for one buyer: what they get, proof, what it costs, why now, and one first step. Use it when the user asks for "the offer", "a sales offer", a proposal, or names price, why now or the next step. The give-first touch in [SKILL.md](../SKILL.md) is for a first email that must not sell.

## Inputs

Work only from what the user gave: the seller's product, price, customers and the deals they lose, and the buyer's dated public signals. If the price is missing, ask for it (or take it from `pricing` in `brand-config.json`); never invent one. If no first step was given, use the plainest one the facts support: a short call, or a reply to start.

## The parts

| Part | What goes in | Rule |
| --- | --- | --- |
| Opening | The buyer's own signal, with its source and date | Their words, not yours. Quote marks only around words the source quotes. |
| What you get | What the product does for this buyer, in their nouns | Only capabilities the seller listed. No feature the facts do not name. |
| Proof | One to three customers the seller gave, nearest fit first, each with its number | Never a customer, number or logo the seller did not give. |
| What it costs | The seller's price, exactly. If the buyer's volume is given, show the arithmetic and mark it "estimate" | Never a discount, trial, pilot, guarantee or refund the seller does not offer. |
| Why now | The buyer's dated signals and what they change | No countdown, no "limited time". Inference is labeled as inference. |
| Fit caveat | The case where the seller loses (the stated loses-to), said plainly | One sentence. Optional when the facts give none. |
| First step | One action the buyer can say yes to | One ask. No invented day, time, sample or attachment. |

Length: 300 words or fewer across the parts. Plain salutation and sign-off (`[Your name]` when the sender is not given). No em dashes, no notes to the operator, no tool names.

## Workflow

- [ ] 1. Pick the signal that names the pain in the buyer's words; note its date.
- [ ] 2. Fill `gtm/offer.json` with `what_they_get`, `proof`, `price`, `why_now`, `caveat`, `first_step`, and `facts` (the source facts as given, so the scorer can check every number).
- [ ] 3. Run `python3 ${CLAUDE_SKILL_DIR}/scripts/score.py --mode full --file gtm/offer.json --json`.
- [ ] 4. On exit 1, apply each `fix` and score again until it exits 0.
- [ ] 5. Show the finished offer as the buyer would read it. Do not send it.

## What the scorer checks (`--mode full`)

| Check | Fails when | Fix |
| --- | --- | --- |
| `complete` | `what_they_get`, `price`, `why_now` or `first_step` is empty | Fill all four. |
| `price` | The price line has no number | State the seller's price. |
| `why_now` | Why now has no date, month or number | Tie it to a dated buyer signal. |
| `first_step` | More than one question, an "Or ..." alternative, or over 40 words | One action. |
| `invented_terms` | Guarantee, refund, discount, free trial, pilot or risk-free that `facts` does not contain | Cut it. |
| `hype` | "Act now", "limited time", "ends soon" and similar | Let the dated signal carry it. |
| `numbers` | With `facts`, a dollar amount or percent, or any number in `proof`, that `facts` lacks (the price line is exempt when marked "estimate") | Use only given numbers. |
| `length` | Over 300 words | Cut. |

## Example

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/score.py --mode full --file ${CLAUDE_SKILL_DIR}/examples/offer-full.json   # exits 0, prints each part
```
