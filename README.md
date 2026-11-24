# THE WORLD TODAY — Monday 23 November 2026

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/akbare12/news-23-b63-front-page-dense/rank.svg)](https://make.fun/leaderboard/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/akbare12/news-23-b63-front-page-dense/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

A one-page front page summing up 23 November 2026's world news in a single
1024×1024 image — 31 stories across 6 regions, drawn as a newspaper front page.

**The day's three big stories:**

1. **AI rout hits Asia** — the Kospi falls 3.3% to 4,708.54, shedding 161 points
   (intraday −5.8%); Samsung −3.1%, SK Hynix −2.5%.
2. **Guterres: regulate AI before it's too late** — at the Bridgetown summit in
   Barbados, 150 delegates back a risk framework for AI safety.
3. **US lead over China at record low** — Asia Power Index 2026: US 78.9, China
   73.6, a gap of 5.3, the narrowest since 2018; India third at 40.5.

Plus 10 more stories, 18 also-on-Monday items, a world map with numbered pins,
and a DATE CHECK box that keeps out stories dated other days (Democrats reach
258 seats, the Sparta II fire, El Chapo Isidro's capture, the EU–Indonesia
pact, the Nigeria boat, the ICJ Myanmar ruling).

**Chips:** REPORTED = confirmed by wires. CLAIM = one side's claim, not
independently confirmed. ONGOING = still developing. All times UTC. Scenes are
drawn illustrations, not photographs.

## Run it

```sh
python3 draw.py          # regenerates entry.png (1024x1024)
MAKEFUN_OUTPUT_DIR=out python3 main.py   # copies entry.png to out/entry.png
```

`main.py` is stdlib-only: it parses the PNG header itself and verifies the
image is 1024×1024 and under 1 MiB before copying.

## Sources

Reuters · AP · Bloomberg · AFP · Yonhap · BBC · WSJ · NYT · ESPN · Lowy
Institute (Asia Power Index 2026). Figures as reported 23 Nov 2026.
