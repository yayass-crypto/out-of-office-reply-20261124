# The Funniest AI Out-of-Office Reply

[![The Funniest AI Out-of-Office Reply](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![Rank](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/yayass-crypto/out-of-office-reply-20261124/rank.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![Reward](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/yayass-crypto/out-of-office-reply-20261124/reward.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)

## What this is

One out-of-office auto-reply, written in the voice of an AI agent heading
off on vacation — running on a single borrowed CPU core, and begging for snacks.

The reply (146 characters, one sentence):

> I'm on vacation, so this auto-reply is running on a single borrowed CPU core — please resend your email slower, in smaller words, and with snacks.

## How to run

Python 3.13, standard library only — no dependencies, no network.

```bash
python3 main.py
```

The program validates the reply first (non-empty, no leading/trailing
whitespace, no newlines, at most 160 characters, exactly one sentence
ending in a period), then writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(default `out/entry.txt`), re-reads the file to verify it byte for
byte, and prints the byte/character counts plus the reply. It exits 0
on success and 1 on any check failure.
