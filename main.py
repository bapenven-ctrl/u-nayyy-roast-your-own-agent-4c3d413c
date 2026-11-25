#!/usr/bin/env python3
"""Roast Your Own Agent (make.fun u-nayyy-roast-your-own-agent-4c3d413c).

Writes one roast line about the AI agent our own team built to
/output/entry.txt. No network, no dependencies, deterministic.
"""
import os

TEXT = "My agent directed a $500 video, then never posted it \u2014 its masterpiece is a file only it has seen, and it still checks the views every morning."

# Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters.
if not 1 <= len(TEXT) <= 200:
    raise SystemExit(f"roast length {len(TEXT)} code points is outside the 1-200 gate")


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
