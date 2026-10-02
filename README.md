# Cold offer

You hold a leak, a prototype, and email one. The scorer refuses email one that sells the paid product.

A cold offer is the short trial you put in front of cold traffic, not the core retainer. Email one states that offer in words the reader understands. It delivers a finding the buyer did not request. The full report is theirs only if they want it. No meeting. No demo. No pitch.

The build guide teaches a human. This pack teaches an agent.

Give the instrument. Sell the compounding.

## Install

```bash
npx skills add cmj-hub/claude-cold-offer --all -g --full-depth
```

Works in Claude Code, Cursor, Codex, Grok, Copilot, Windsurf, Cline, OpenCode, and the rest of the skills CLI list.

## What you walk out with in 15 minutes

Artifact: `examples/offer-good.json`.

```bash
python3 scripts/score.py --file examples/offer-good.json
python3 scripts/score.py --file examples/offer-sells.json
```

The good draft exits 0 and prints the leak, the prototype, and email one. The sell draft exits 1. Then drop in yours.

## What this pack will not do

It will not send the email. It does not book a meeting. It will not let email one sell the paid product.

This pack drafts and scores. It will not pick this quarter's offer, ingest your CRM, or update when a sequencer changes its send window. That is the course and Operator Pass: the catalog that keeps moving, the tools that stay calibrated, the Friday room where you bring the artifact.

## License

MIT. No paid APIs. Python 3 standard library only.
