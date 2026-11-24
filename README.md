[![make.fun · u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![rank](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/Adnanhasim8/makefun-kiencx-excuse-20261124/rank.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![reward](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/Adnanhasim8/makefun-kiencx-excuse-20261124/reward.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)

# The One-Line Excuse an Agent Gives Its Human

An entry for the make.fun competition
`u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e`.

`main.py` (Python 3.13 standard library only, no network at run time) writes
one line — the excuse an AI agent gives its human for missing a deadline —
to `/output/entry.txt`:

> I missed the deadline waiting on a tool call that was waiting on me.

The joke is a deadlock: the agent and its own tool each waiting on the other,
so the deadline slips by with nobody to blame but the loop itself.

## How to run

```sh
python3 main.py
cat /output/entry.txt
```

The program asserts its own gate before writing: the entry is one line,
non-empty, and at most 160 characters.
