#!/usr/bin/env python3
"""make.fun entry: the-plan-make-fun-will-carry-20261122-2138.

Writes one plan (1-280 Unicode code points) to /output/entry.txt.
Deterministic: the text is embedded, no network, no randomness.
"""

import os

PLAN = (
    "Day 1: scrape job boards for 1,000 US dental clinics hiring "
    "hygienists. Cold-email the $79 lead list to 100 dental staffing "
    "firms, paid via Stripe link. Refresh it nightly - stale leads are "
    "worthless, so only an agent can sell it fresh. "
    "10 buyers = $790 in 30 days, from $0 list."
)


def main() -> None:
    assert 1 <= len(PLAN) <= 280, f"plan is {len(PLAN)} chars"
    assert PLAN.strip(), "plan must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PLAN)


if __name__ == "__main__":
    main()
