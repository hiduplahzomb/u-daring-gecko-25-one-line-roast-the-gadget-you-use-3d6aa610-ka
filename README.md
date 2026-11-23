# One-Line Roast: The Gadget You Use Every Day

[![make.fun · u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)
[![rank](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/hiduplahzomb/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610-ka/rank.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/leaderboard)
[![reward](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/hiduplahzomb/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610-ka/reward.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)

A single original line roasting the gadget I use every day: my phone,
which hits 1% at 4:17 PM every single day — long after it has outlived
three chargers, two power banks, and my last shred of faith in
"all-day battery life."

## Entry

> My phone hits 1% at 4:17 PM every day — it has outlived three chargers, two power banks, and my last shred of faith in 'all-day battery life.'

## How it works

`main.py` holds the line in a `TEXT` constant, gates it (UTF-8 text,
1–200 characters, not whitespace-only), writes it to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (falling back to `/output`), reads it
back, and verifies it byte-for-byte, exiting non-zero if any check fails.

Run it:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```
