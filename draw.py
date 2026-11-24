#!/usr/bin/env python3
"""news-23 b63 front-page-dense: THE WORLD TODAY, Monday 23 November 2026 (31 stories)."""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = "entry.png"

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def F(path, size):
    return ImageFont.truetype(path, size)


img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (17, 17, 17)
GOLD = (201, 162, 39)
GOLD_L = (232, 184, 0)
RED = (178, 34, 34)
RED_D = (192, 57, 43)
TEAL = (14, 124, 123)
NAVY = (11, 31, 58)
BLUE = (31, 78, 156)
OCHRE = (183, 121, 31)
PURPLE = (107, 79, 161)
GRAY = (85, 85, 85)
CREAM = (245, 237, 216)
GREEN = (168, 208, 141)
GREEN_L = (190, 220, 165)


def wrap(text, font, maxw):
    words = text.split()
    lines, cur = [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if d.textlength(t, font=font) <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


def txt(x, y, s, font, fill, anchor="la"):
    d.text((x, y), s, font=font, fill=fill, anchor=anchor)


def chip(x, y, label, color):
    f = F(SANS_B, 9)
    w_ = d.textlength(label, font=f) + 10
    d.rounded_rectangle([x, y, x + w_, y + 14], radius=2, fill=color)
    d.text((x + 5, y + 2), label, font=f, fill="white")
    return w_


# ---------- masthead ----------
d.rectangle([0, 0, W, 54], fill=BLACK)
txt(12, 8, "THE WORLD TODAY", F(SERIF_B, 40), "white")
txt(W - 12, 18, "MONDAY 23 NOVEMBER 2026", F(SANS_B, 16), GOLD_L, anchor="ra")

# ---------- kicker ----------
txt(12, 58, "AI rout hits Asia  ·  UN chief urges AI rules  ·  US lead over China at record low  ·  Anthropic IPO $107.3B",
    F(SANS_B, 13), RED)

# ---------- number strip: 5 cols x 2 rows ----------
nums = [
    ("-3.3%", "KOSPI", RED_D), ("5.3", "US-CHINA POWER GAP", BLUE),
    ("11,762", "EBOLA CASES, DRC", (0, 120, 60)), ("10T won", "SEOUL STABILISATION FUND", OCHRE),
    ("2%", "BILLIONAIRE TAX IN PARIS", PURPLE),
    ("$450M", "SKUBAL DEAL", PURPLE), ("165", "RUSSIAN MISSILES/WEEK", RED_D),
    ("12,000", "CLEARED IN MANCHESTER", BLUE), ("264 kg", "EXPLOSIVES SEIZED", OCHRE),
    ("$107.3B", "ANTHROPIC IPO", PURPLE),
]
colw = (W - 24) // 5
for i, (v, lab, col) in enumerate(nums):
    cx = 12 + (i % 5) * colw
    cy = 78 + (i // 5) * 32
    txt(cx, cy, v, F(SANS_B, 19), col)
    txt(cx, cy + 21, lab, F(SANS_B, 8), BLACK)

# ---------- region bar ----------
regions = [("ASIA-PACIFIC 7", TEAL), ("AMERICAS 8", BLUE), ("MIDDLE EAST 6", OCHRE),
           ("EUROPE 5", PURPLE), ("AFRICA 3", RED_D), ("WORLD 2", GRAY)]
rx = 8
segw = [250, 200, 210, 160, 120, 76]
for (lab, col), w_ in zip(regions, segw):
    d.rectangle([rx, 146, rx + w_, 164], fill=col)
    txt(rx + w_ // 2, 149, lab, F(SANS_B, 11), "white", anchor="ma")
    rx += w_

# ---------- UTC strip ----------
txt(12, 170, "THE DAY IN UTC   ~00:00 Kospi dives   ~06:30 Guterres opens   ~09:00 Power Index   ~12:00 Paris 2% tax   ~15:00 Kyiv missiles",
    F(SANS, 10), BLACK)
txt(W - 12, 170, "~ APPROX", F(SANS, 10), GRAY, anchor="ra")

# ---------- hero scenes ----------
SY, SH = 186, 112
SW = 328
GAP = 8
xs = [8, 8 + SW + GAP, 8 + 2 * (SW + GAP)]

# scene 1: Kospi chart
x0 = xs[0]
d.rectangle([x0, SY, x0 + SW, SY + SH], fill=NAVY)
# buildings
import random
random.seed(63)
for bx in range(x0 + 10, x0 + SW - 10, 26):
    bh = random.randint(28, 62)
    d.rectangle([bx, SY + SH - 30 - bh, bx + 20, SY + SH - 30], fill=(24, 52, 96))
    for wy in range(SY + SH - 28 - bh, SY + SH - 34, 8):
        for wx in range(bx + 3, bx + 18, 6):
            if random.random() < 0.5:
                d.rectangle([wx, wy, wx + 3, wy + 4], fill=(255, 214, 90))
# chart line
pts = [(x0 + 14, SY + 78), (x0 + 60, SY + 52), (x0 + 110, SY + 66), (x0 + 160, SY + 40),
       (x0 + 210, SY + 50), (x0 + 260, SY + 30), (x0 + 312, SY + 38)]
d.line(pts, fill=(255, 176, 66), width=3)
for p in pts:
    d.ellipse([p[0] - 4, p[1] - 4, p[0] + 4, p[1] + 4], fill=(255, 214, 130))
txt(x0 + 10, SY + 4, "-3.3%", F(SANS_B, 30), (255, 90, 70))
d.rectangle([x0, SY + SH - 20, x0 + SW, SY + SH], fill=BLACK)
txt(x0 + 8, SY + SH - 17, "KOSPI 4,708.54    ·    -161 PTS", F(SANS_B, 11), "white")

# scene 2: Guterres
x0 = xs[1]
d.rectangle([x0, SY, x0 + SW, SY + SH], fill=TEAL)
txt(x0 + 10, SY + 8, "150 DELEGATES", F(SANS_B, 24), GOLD_L)
txt(x0 + 10, SY + 36, "BACK A RISK", F(SANS_B, 24), GOLD_L)
txt(x0 + 10, SY + 64, "FRAMEWORK", F(SANS_B, 24), GOLD_L)
# globe
gx, gy, gr = x0 + SW - 52, SY + SH - 52, 30
d.ellipse([gx - gr, gy - gr, gx + gr, gy + gr], outline="white", width=2)
d.ellipse([gx - gr // 2, gy - gr, gx + gr // 2, gy + gr], outline="white", width=1)
d.line([gx - gr, gy, gx + gr, gy], fill="white", width=1)
d.arc([gx - gr, gy - gr // 2, gx + gr, gy + gr // 2], 0, 360, fill="white", width=1)
d.rectangle([x0, SY + SH - 20, x0 + SW, SY + SH], fill=BLACK)
txt(x0 + 8, SY + SH - 17, "UN   ·   BRIDGETOWN", F(SANS_B, 11), "white")

# scene 3: Power Index bars
x0 = xs[2]
d.rectangle([x0, SY, x0 + SW, SY + SH], fill=CREAM)
txt(x0 + 10, SY + 6, "NARROWEST SINCE 2018", F(SANS_B, 12), BLACK)
txt(x0 + SW - 10, SY + 6, "GAP 5.3", F(SANS_B, 12), OCHRE, anchor="ra")
bars = [("78.9", 46, NAVY, "US"), ("73.6", 43, RED_D, "CHINA"), ("40.5", 24, OCHRE, "INDIA")]
bx = x0 + 30
for val, bh, col, lab in bars:
    txt(bx + 40, SY + 26, val, F(SANS_B, 15), BLACK, anchor="ma")
    d.rectangle([bx, SY + 44, bx + 80, SY + 44 + bh], fill=col)
    txt(bx + 40, SY + 44 + bh // 2 - 6, lab, F(SANS_B, 10), "white", anchor="ma")
    bx += 96
d.rectangle([x0, SY + SH - 20, x0 + SW, SY + SH], fill=BLACK)
txt(x0 + 8, SY + SH - 17, "ASIA POWER INDEX 2026", F(SANS_B, 11), "white")

# ---------- hero text ----------
HY = SY + SH + 8  # 306
heroes = [
    ("1", "AI ROUT HITS ASIA",
     "Kospi closes -3.3% to 4,708.54, sheds 161 pts; intraday -5.8%. Samsung -3.1%, SK Hynix -2.5%.",
     "KOREA EXCHANGE"),
    ("2", "GUTERRES: REGULATE AI BEFORE IT'S TOO LATE",
     "UN chief urges global AI safety rules at the Bridgetown summit; 150 delegates back a risk framework.",
     "UNITED NATIONS"),
    ("3", "US LEAD OVER CHINA AT RECORD LOW",
     "Asia Power Index 2026: US 78.9, China 73.6 — gap 5.3, narrowest since 2018. India third at 40.5.",
     "LOWY INSTITUTE"),
]
for i, (n, head, body, src) in enumerate(heroes):
    x0 = xs[i]
    d.ellipse([x0, HY, x0 + 20, HY + 20], fill=RED_D)
    txt(x0 + 10, HY + 3, n, F(SANS_B, 12), "white", anchor="ma")
    hl = wrap(head, F(SANS_B, 16), SW - 28)
    yy = HY
    for ln in hl[:2]:
        txt(x0 + 26, yy, ln, F(SANS_B, 16), BLACK)
        yy += 19
    by = HY + 40
    bl = wrap(body, F(SANS, 11), SW)
    for ln in bl[:2]:
        txt(x0, by, ln, F(SANS, 11), BLACK)
        by += 14
    txt(x0, HY + 70, src, F(SANS, 9), GRAY)
    chip(x0 + SW - 62, HY + 68, "REPORTED", BLUE)

# ---------- MORE OF THE DAY bar ----------
MY = 394
d.rectangle([0, MY, W, MY + 18], fill=BLACK)
txt(12, MY + 2, "MORE OF THE DAY  —  10 STORIES", F(SANS_B, 12), "white")

# ---------- cards: 5 cols x 2 rows ----------
cards = [
    ("AMERICAS", BLUE, "BESSENT: NVIDIA ANSWERS", "Treasury wants answers.", "Reuters", "REPORTED", BLUE),
    ("FBI", RED_D, "FBI PROBES NCIC HACK", "NCIC database hacked.", "AP", "REPORTED", BLUE),
    ("WHITE HOUSE", OCHRE, "TRUMP: IRAN STRIKES MAY RESUME", "May resume in New Year.", "Reuters", "REPORTED", BLUE),
    ("MARKETS", BLUE, "US FUTURES JUMP 3%", "Holiday rally lifts futures 3%.", "Bloomberg", "REPORTED", BLUE),
    ("SPORT", RED_D, "SKUBAL'S $450M METS DEAL", "Nine-year deal, largest ever.", "AP", "REPORTED", BLUE),
    ("SPORT", RED_D, "TOM JACKSON DIES AT 75", "Broncos LB, ESPN voice, dies.", "ESPN", "REPORTED", BLUE),
    ("LEGAL", PURPLE, "STATES SUE SPACEX", "Ten states challenge AI claims.", "AP", "REPORTED", BLUE),
    ("TECH", TEAL, "ANTHROPIC IPO: $107.3B", "Raised at $83; closes $97.17.", "WSJ", "REPORTED", BLUE),
    ("EUROPE", PURPLE, "POLAND: 3 MISSILES CROSSED AIRSPACE", "Kyiv: three Kh-101s crossed.", "AP", "CLAIM", RED_D),
    ("SPACE", GRAY, "RUSSIAN NUCLEAR SATELLITE", "May carry a nuke.", "Reuters", "CLAIM", RED_D),
]
CW, CH = 196, 68
for i, (cat, ccol, head, body, src, clab, chipcol) in enumerate(cards):
    cx = 8 + (i % 5) * (CW + 8)
    cy = MY + 18 + 6 + (i // 5) * (CH + 8)
    d.rectangle([cx, cy, cx + CW, cy + 14], fill=ccol)
    txt(cx + 5, cy + 2, cat, F(SANS_B, 9), "white")
    txt(cx + CW - 5, cy + 2, str(i + 1), F(SANS_B, 9), "white", anchor="ra")
    hl = wrap(head, F(SANS_B, 11), CW - 4)
    yy = cy + 17
    for ln in hl[:2]:
        txt(cx, yy, ln, F(SANS_B, 11), BLACK)
        yy += 13
    txt(cx, cy + 44, body, F(SANS, 9), BLACK)
    txt(cx, cy + 56, src, F(SANS, 8), GRAY)
    chip(cx + CW - 62, cy + 54, clab, chipcol)

# ---------- map / ALSO bar ----------
AY = MY + 18 + 6 + 2 * CH + 8 + 6  # 570
d.rectangle([0, AY, W, AY + 18], fill=BLACK)
txt(12, AY + 2, "WHERE IT HAPPENED", F(SANS_B, 12), "white")
txt(330, AY + 2, "ALSO ON MONDAY", F(SANS_B, 12), "white")

# ---------- map ----------
MX, MY0, MW, MH = 8, AY + 26, 306, 216
d.rectangle([MX, MY0, MX + MW, MY0 + MH], outline=(200, 200, 200), width=1)
for gx_ in range(MX, MX + MW, 17):
    d.line([gx_, MY0, gx_, MY0 + MH], fill=(232, 232, 232), width=1)
for gy_ in range(MY0, MY0 + MH, 17):
    d.line([MX, gy_, MX + MW, gy_], fill=(232, 232, 232), width=1)
# stylised continents
d.ellipse([MX + 6, MY0 + 20, MX + 108, MY0 + 190], fill=GREEN)
d.ellipse([MX + 150, MY0 + 10, MX + 296, MY0 + 170], fill=GREEN)
d.ellipse([MX + 60, MY0 + 160, MX + 160, MY0 + 216], fill=GREEN_L)
pins = {  # (x, y) inside map box
    1: (262, 50), 2: (30, 150), 3: (278, 28), 4: (46, 84), 5: (74, 108),
    6: (196, 116), 7: (30, 52), 8: (22, 112), 9: (56, 128), 10: (88, 148),
    11: (168, 46), 12: (190, 62), 13: (252, 70),
}
for n, (px, py) in pins.items():
    d.ellipse([MX + px - 8, MY0 + py - 8, MX + px + 8, MY0 + py + 8], fill=RED_D, outline="white", width=1)
    txt(MX + px, MY0 + py - 6, str(n), F(SANS_B, 9), "white", anchor="ma")
txt(MX, MY0 + MH + 4, "Pins 1–13:  1 Seoul  ·  2 Bridgetown  ·  3 Beijing", F(SANS, 9), BLACK)
txt(MX, MY0 + MH + 16, "4 Washington  ·  5 New York  ·  6 Tehran  ·  7 Chicago", F(SANS, 9), BLACK)
txt(MX, MY0 + MH + 28, "8 SF  ·  9 Denver  ·  10 Austin  ·  11 Warsaw  ·  12 Kyiv  ·  13 Moscow", F(SANS, 9), BLACK)

# ---------- ALSO list: 2 columns x 9 ----------
also = [
    "14. Paris: 100+ back 2% billionaire tax", "15. Manchester: 12,000 cleared",
    "16. Zelenskyy: 165 missiles in a week", "17. COP31: the day after pact rejected",
    "18. Benghazi: UN demands port probe", "19. Israel unity talks resume",
    "20. Gaza: two killed in Israeli strike", "21. West Bank settler attacks",
    "22. Iran war: no deal in sight",
    "23. Lebanon seizes 264 kg explosives", "24. Bahrain: strike hits plant, 2 hurt",
    "25. Sudan: defences down drones", "26. DRC: fighting traps Ebola teams",
    "27. Bangladesh: Hasina jailed if she returns", "28. Seoul minister quits in exam row",
    "29. SK Telecom -7.3% as hype cools", "30. China eases margin rules",
    "31. Seoul readies 10T-won fund",
]
for i, a in enumerate(also):
    ax = 330 + (i // 9) * 348
    ay_ = MY0 + 4 + (i % 9) * 19
    txt(ax, ay_, a, F(SANS, 11), BLACK)

# ---------- DATE CHECK ----------
DY = MY0 + MH + 44  # 812
d.rectangle([8, DY, W - 8, DY + 62], outline=RED, width=2)
txt(14, DY + 4, "DATE CHECK", F(SANS_B, 11), RED)
txt(W - 14, DY + 4, "READ 23 NOV 2026, 23:59 UTC — STORIES DATED 23 NOV ONLY", F(SANS_B, 9), RED, anchor="ra")
txt(14, DY + 22, "LEFT OUT — NOT 23 NOV:  Dems 258 seats (22 Nov)  ·  Sparta II fire (22 Nov)  ·  El Chapo captured (22 Nov)  ·  EU–Indonesia pact (21 Nov)  ·  Nigeria boat (21 Nov)  ·  ICJ Myanmar (19 Nov)",
    F(SANS, 10), BLACK)
txt(14, DY + 40, "NOT YET:  Dymer search continues (14 missing)  ·  4 House races uncalled  ·  COP32 venue not set  ·  WHO evacuating trapped Ebola staff",
    F(SANS, 10), BLACK)

# ---------- footer ----------
FY = DY + 70
txt(12, FY, "Sources: Reuters · AP · Bloomberg · AFP · Yonhap · BBC · WSJ · NYT · ESPN · Lowy Institute (Asia Power Index 2026).",
    F(SANS, 9), GRAY)
txt(12, FY + 13, "CHIPS: REPORTED = confirmed by wires.  CLAIM = one side's claim, not independently confirmed.  ONGOING = still developing.",
    F(SANS, 9), GRAY)
txt(12, FY + 26, "All times UTC. Figures as reported 23 Nov 2026. Scenes are drawn illustrations, not photographs.",
    F(SANS, 9), GRAY)

# ---------- bottom bar ----------
d.rectangle([0, H - 34, W, H], fill=BLACK)
txt(W // 2, H - 26, "THE WORLD TODAY  —  Monday 23 November 2026  ·  31 stories  ·  6 regions",
    F(SANS_B, 13), GOLD_L, anchor="ma")

img.save(OUT)
print("saved", OUT, img.size)
