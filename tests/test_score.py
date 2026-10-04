#!/usr/bin/env python3
"""score.py prints a cold offer or refuses email one that sells the paid product."""

import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CELL = "super-secret-cell"


def run(args, stdin=None):
    return subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "score.py"), *args],
        input=stdin,
        capture_output=True,
        text=True,
    )


class ScoreColdOffer(unittest.TestCase):
    def test_good_draft_prints_three(self):
        result = run(["--file", str(ROOT / "examples" / "offer-good.json")])
        self.assertEqual(result.returncode, 0)
        self.assertIn("leak: The homepage asks for a meeting before it shows any work.", result.stdout)
        self.assertIn("prototype: A one-page sample that leads with one finding", result.stdout)
        self.assertIn("email one: Your homepage asks for a meeting before it shows any work.", result.stdout)
        self.assertIn("price: Example price, replace this before you send: 0 for the one-page sample.", result.stdout)
        self.assertIn("scope: One page. One finding. The short trial stops there.", result.stdout)
        self.assertIn("deadline: 2026-12-15", result.stdout)
        self.assertNotIn("email one that sells the paid product", result.stdout)

    def test_sell_exits_1(self):
        result = run(["--file", str(ROOT / "examples" / "offer-sells.json")])
        self.assertEqual(result.returncode, 1)
        self.assertIn("email one that sells the paid product", result.stdout)
        self.assertNotIn("leak:", result.stdout)

    def test_bad_json_hides_input(self):
        bad = run(["--stdin"], stdin='{"email_one": "' + CELL)
        self.assertNotEqual(bad.returncode, 0)
        self.assertNotIn(CELL, bad.stdout + bad.stderr)
        self.assertIn("invalid JSON", bad.stderr)
        array = run(["--stdin"], stdin='["' + CELL + '"]')
        self.assertNotEqual(array.returncode, 0)
        self.assertNotIn(CELL, array.stdout + array.stderr)
        self.assertIn("JSON must be an object", array.stderr)

    def test_price_scope_and_deadline(self):
        import json
        payload = {
            "leak": "The homepage asks for a meeting before it shows any work.",
            "prototype": "A one-page sample that leads with one finding and the short trial, and stops there.",
            "price": "500 for the sample.",
            "scope": "One page. One finding. The short trial stops there.",
            "deadline": "2026-12-15",
            "email_one": "Your homepage asks for a meeting before it shows any work. I wrote one page that leads with that finding. The full report is yours if you want it.",
        }
        unlabeled = run(["--stdin"], stdin=json.dumps(payload))
        self.assertEqual(unlabeled.returncode, 1)
        self.assertEqual(unlabeled.stdout.strip(), "price is not labeled example")
        payload["price"] = "Example price, replace this before you send: 0 for the one-page sample."
        payload["scope"] = "The whole engagement, unbounded."
        wide = run(["--stdin"], stdin=json.dumps(payload))
        self.assertEqual(wide.returncode, 1)
        self.assertEqual(wide.stdout.strip(), "scope is not one bound")
        payload["scope"] = "One page. One finding. The short trial stops there."
        payload["deadline"] = "next week"
        late = run(["--stdin"], stdin=json.dumps(payload))
        self.assertEqual(late.returncode, 1)
        self.assertEqual(late.stdout.strip(), "deadline is not a date")
        payload["deadline"] = "2026-12-15"
        payload["price"] = "Example price, replace this: buy the retainer."
        sold = run(["--stdin"], stdin=json.dumps(payload))
        self.assertEqual(sold.returncode, 1)
        self.assertEqual(sold.stdout.strip(), "the offer sells the paid product")


if __name__ == "__main__":
    unittest.main()
