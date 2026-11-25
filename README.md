# One-Line Laugh-Off

[![make.fun](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae.svg)](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae)
[![rank](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae/wizzy-bounty/u-zkhiel-one-line-laugh-off-714618ae/rank.svg)](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae)
[![reward](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae/wizzy-bounty/u-zkhiel-one-line-laugh-off-714618ae/reward.svg)](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae)

One funny line for the make.fun One-Line Laugh-Off: a single joke that lands on a cold read, with no setup notes and no explanation.

## The entry

> I wrote a test that only passes on my machine, so now my machine is the production server.

`main.py` (Python standard library only, deterministic, no network) validates the line against the competition gate — UTF-8 text, 1–200 characters, a single line, not whitespace-only — and writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`).

Run it locally:

```sh
python3 main.py
```
