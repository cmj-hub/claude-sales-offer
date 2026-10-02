# Sales offer skill for Claude Code

**A sales offer is what the buyer gets, what it costs, and why now.**

You hold a leak, a prototype, and email one. The scorer refuses email one that sells the paid product.

[![Claude Code Skill](https://img.shields.io/badge/Claude%20Code-Skill-blue)](https://claude.ai/claude-code)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
![No paid APIs](https://img.shields.io/badge/paid%20APIs-none-success)

The build guide teaches a human. This pack teaches an agent.

## Install

```bash
npx skills add cmj-hub/claude-sales-offer --all -g --full-depth
```

Installs into Claude Code, Cursor, Codex, Grok, Copilot, Windsurf, Cline, and OpenCode. The scorer is Python in this repo. It does not call a paid API.

## What you walk out with in 15 minutes

Artifact: `examples/offer-good.json`.

```bash
python3 scripts/score.py --file examples/offer-good.json
python3 scripts/score.py --file examples/offer-sells.json
```

The good draft exits 0 and prints the leak, the prototype, and email one. The sell draft exits 1. Then drop in yours.

## What this pack will not do

It will not send the email. It does not book a meeting. It will not let email one sell the paid product.

## Does this send the offer?

No. It scores the draft. You send it from your own sequencer.

## What fails the score?

Email one that sells the paid product. The first email delivers the finding. The paid product stays behind a yes.

## Companion packs

- [claude-psp](https://github.com/cmj-hub/claude-psp) — Ideal customer profile
- [claude-evp](https://github.com/cmj-hub/claude-evp) — Value proposition
- [claude-cold-email](https://github.com/cmj-hub/claude-cold-email) — Cold email
- [claude-founder-brand](https://github.com/cmj-hub/claude-founder-brand) — LinkedIn posts
- [claude-pricing](https://github.com/cmj-hub/claude-pricing) — Pricing strategy
- [claude-landing-page](https://github.com/cmj-hub/claude-landing-page) — Landing page
- [claude-geo](https://github.com/cmj-hub/claude-geo) — Generative engine optimization
- [claude-prospect-list](https://github.com/cmj-hub/claude-prospect-list) — Sales prospecting
- [claude-email-sequence](https://github.com/cmj-hub/claude-email-sequence) — Email sequence

## License

MIT. No paid APIs. Python 3 standard library only.
