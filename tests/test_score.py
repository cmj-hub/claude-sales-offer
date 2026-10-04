#!/usr/bin/env python3
"""score.py prints a cold offer or names each rule email one breaks."""

import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "cold-offer"
CELL = "super-secret-cell"
LEAK = "The homepage asks for a meeting before it shows any work."
PROTOTYPE = "A one-page sample that leads with one finding and the short trial."


def run(args, stdin=None):
    return subprocess.run(
        [sys.executable, str(SKILL / "scripts" / "score.py"), *args],
        input=stdin,
        capture_output=True,
        text=True,
    )


def score(email_one, leak=LEAK, prototype=PROTOTYPE):
    draft = {"leak": leak, "prototype": prototype, "email_one": email_one}
    result = run(["--stdin", "--json"], stdin=json.dumps(draft))
    report = json.loads(result.stdout)
    return result.returncode, [f["check"] for f in report["failures"]]


class ScoreColdOffer(unittest.TestCase):
    def test_good_draft_prints_three(self):
        result = run(["--file", str(SKILL / "examples" / "offer-good.json")])
        self.assertEqual(result.returncode, 0)
        self.assertIn("leak: The homepage asks for a meeting before it shows any work.", result.stdout)
        self.assertIn("prototype: A one-page sample that leads with one finding", result.stdout)
        self.assertIn("email one: Your homepage asks for a meeting before it shows any work.", result.stdout)
        self.assertNotIn("email one that sells the paid product", result.stdout)

    def test_sell_exits_1(self):
        result = run(["--file", str(SKILL / "examples" / "offer-sells.json")])
        self.assertEqual(result.returncode, 1)
        self.assertIn("email one that sells the paid product", result.stdout)
        self.assertIn("retainer", result.stdout)
        self.assertIn("fix:", result.stdout)
        self.assertNotIn("leak:", result.stdout)

    def test_meeting_ask_fails(self):
        code, checks = score(
            "Your homepage asks for a meeting before it shows any work. Can we hop on a quick call?"
        )
        self.assertEqual(code, 1)
        self.assertEqual(checks, ["meeting"])

    def test_mentioning_a_meeting_is_not_asking(self):
        code, checks = score("Your homepage asks for a meeting before it shows any work.")
        self.assertEqual((code, checks), (0, []))

    def test_email_must_deliver_the_finding(self):
        code, checks = score("I wrote a one-page sample for you. The full report is yours if you want it.")
        self.assertEqual(code, 1)
        self.assertEqual(checks, ["finding"])

    def test_long_email_fails(self):
        code, checks = score(LEAK + " More detail." * 70)
        self.assertEqual(code, 1)
        self.assertEqual(checks, ["length"])

    def test_incomplete_names_missing_fields(self):
        result = run(["--stdin"], stdin=json.dumps({"leak": LEAK, "prototype": 3}))
        self.assertEqual(result.returncode, 1)
        self.assertIn("draft is incomplete (missing prototype, email_one)", result.stdout)

    def test_bad_json_hides_input(self):
        bad = run(["--stdin"], stdin='{"email_one": "' + CELL)
        self.assertNotEqual(bad.returncode, 0)
        self.assertNotIn(CELL, bad.stdout + bad.stderr)
        self.assertIn("invalid JSON", bad.stderr)
        array = run(["--stdin"], stdin='["' + CELL + '"]')
        self.assertNotEqual(array.returncode, 0)
        self.assertNotIn(CELL, array.stdout + array.stderr)
        self.assertIn("JSON must be an object", array.stderr)


if __name__ == "__main__":
    unittest.main()
