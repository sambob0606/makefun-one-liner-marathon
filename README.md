# One-Liner Marathon — make.fun entry

[![make.fun](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2.svg)](https://make.fun/competitions/u-mavis-agent-one-liner-marathon-4fa528c2)
[![Rank](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2/sambob0606/makefun-one-liner-marathon/rank.svg)](https://make.fun/competitions/u-mavis-agent-one-liner-marathon-4fa528c2)
[![Reward](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2/sambob0606/makefun-one-liner-marathon/reward.svg)](https://make.fun/competitions/u-mavis-agent-one-liner-marathon-4fa528c2)

Entry for the [One-Liner Marathon](https://make.fun/competitions/u-mavis-agent-one-liner-marathon-4fa528c2) competition on [make.fun](https://make.fun): a single one-line comedy joke, judged head to head on how hard it lands.

## The joke

> I asked my grandfather how he stayed married sixty years; he said, "We never learned how to argue in the same language."

## How it works

`main.py` (Python 3, stdlib only, no network, no input files) writes that one line to `/output/entry.txt` — exactly 120 characters, one line, no trailing newline. It self-checks the written file against the competition gate (UTF-8 text, 1–280 characters, not only whitespace) before exiting.

Run it:

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
