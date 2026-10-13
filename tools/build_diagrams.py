#!/usr/bin/env python3
"""Build the editorial SVG diagrams in docs/assets/diagrams/.

The Mermaid blocks in the public docs stay the diffable source of meaning; these
SVGs are the hand-laid editorial rendering of the same content, drawn with the
diagram-design conventions (https://github.com/cathrynlavery/diagram-design):
one accent per figure, orthogonal rounded connectors, masked arrow labels,
hairline borders, no shadows, 4px grid. Each SVG carries its own light and dark
skin via ``prefers-color-scheme`` so it reads on either GitHub theme.

Run ``python tools/build_diagrams.py`` after editing a diagram below, and keep
the matching Mermaid block in the same change.
"""

from __future__ import annotations

from html import escape
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "docs" / "assets" / "diagrams"

SANS = "system-ui, -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
SERIF = "'Iowan Old Style', Georgia, 'Times New Roman', serif"

# Brand skin derived from docs/assets/landing-banner.svg (navy ink, slate blue,
# gold gate). The light accent is the gold darkened until it clears 4.5:1 on paper.
STYLE = f"""
.bg{{fill:#F7F6F2}} .ink{{fill:#0E1A30}} .muted{{fill:#46536B}} .soft{{fill:#5A6680}}
.acc{{fill:#8A5A00}} .lnk{{fill:#2F4F94}}
.n-step{{fill:#FFFFFF;stroke:#0E1A30}} .n-store{{fill:rgba(14,26,48,0.05);stroke:#46536B}}
.n-focal{{fill:rgba(255,210,77,0.22);stroke:#8A5A00}} .n-ext{{fill:rgba(14,26,48,0.03);stroke:rgba(14,26,48,0.32)}}
.n-opt{{fill:rgba(14,26,48,0.02);stroke:rgba(14,26,48,0.36);stroke-dasharray:4 3}}
.n-indep{{fill:rgba(47,79,148,0.07);stroke:#2F4F94}}
.grp{{fill:none;stroke:rgba(14,26,48,0.22);stroke-dasharray:4 4}}
.band{{fill:rgba(14,26,48,0.035);stroke:rgba(14,26,48,0.10)}}
.ln{{fill:none;stroke:#46536B}} .ln-acc{{fill:none;stroke:#8A5A00}} .ln-lnk{{fill:none;stroke:#2F4F94}}
.life{{stroke:rgba(14,26,48,0.25);stroke-dasharray:3 4}}
.mask{{fill:#F7F6F2}} .rule{{stroke:rgba(14,26,48,0.14)}}
.name{{font-family:{SANS};font-size:13px;font-weight:600}}
.sub{{font-family:{MONO};font-size:10px}}
.eye{{font-family:{MONO};font-size:9.5px;font-weight:600;letter-spacing:0.16em}}
.lbl{{font-family:{MONO};font-size:9.5px;letter-spacing:0.04em}}
.ttl{{font-family:{SERIF};font-size:22px}}
.call{{font-family:{SERIF};font-style:italic;font-size:14px}}
@media (prefers-color-scheme: dark){{
.bg{{fill:#0E1A30}} .ink{{fill:#F4F7FC}} .muted{{fill:#B3C2DA}} .soft{{fill:#9DB0CE}}
.acc{{fill:#FFD24D}} .lnk{{fill:#8FB0E6}}
.n-step{{fill:#16263F;stroke:#D7E0EE}} .n-store{{fill:rgba(244,247,252,0.05);stroke:#9DB0CE}}
.n-focal{{fill:rgba(255,210,77,0.14);stroke:#FFD24D}} .n-ext{{fill:rgba(244,247,252,0.03);stroke:rgba(244,247,252,0.34)}}
.n-opt{{fill:rgba(244,247,252,0.02);stroke:rgba(244,247,252,0.40)}}
.n-indep{{fill:rgba(143,176,230,0.10);stroke:#8FB0E6}}
.grp{{stroke:rgba(244,247,252,0.26)}} .band{{fill:rgba(244,247,252,0.035);stroke:rgba(244,247,252,0.10)}}
.ln{{stroke:#9DB0CE}} .ln-acc{{stroke:#FFD24D}} .ln-lnk{{stroke:#8FB0E6}}
.life{{stroke:rgba(244,247,252,0.28)}} .mask{{fill:#0E1A30}} .rule{{stroke:rgba(244,247,252,0.16)}}
}}
"""

CHAR_SANS = 7.4  # avg advance at 13px, 600 weight
CHAR_MONO = 6.0  # advance at 9.5-10px mono


class Fig:
    def __init__(self, name: str, w: int, h: int, title: str, desc: str, eyebrow: str):
        self.name, self.w, self.h = name, w, h
        self.title, self.desc, self.eyebrow = title, desc, eyebrow
        self.lines: list[str] = []  # connectors, drawn first
        self.nodes: list[str] = []  # boxes and text, drawn on top
        self.labels: list[str] = []  # arrow labels, drawn last
        self.under: list[str] = []  # bands and groups, drawn beneath everything

    # ---- text -----------------------------------------------------------
    def text(self, x, y, s, cls="name", fill="ink", anchor="middle", layer=None):
        (layer if layer is not None else self.nodes).append(
            f'<text x="{x}" y="{y}" class="{cls} {fill}" text-anchor="{anchor}">{escape(s)}</text>'
        )

    # ---- nodes ----------------------------------------------------------
    def box(self, x, y, w, h, name, sub=None, kind="step", shape="rect", eyebrow=None):
        """Box at top-left (x, y). Returns dict of ports."""
        cls = f"n-{kind}"
        sw = 1.4 if kind in ("focal", "indep") else 1
        if shape == "pill":
            r = h / 2
        elif shape == "oval":
            r = 20
        else:
            r = 6
        if shape == "diamond":
            cx, cy = x + w / 2, y + h / 2
            self.nodes.append(
                f'<polygon class="{cls}" stroke-width="{sw}" points="{cx},{y} {x + w},{cy} {cx},{y + h} {x},{cy}"/>'
            )
        else:
            self.nodes.append(
                f'<rect class="{cls}" stroke-width="{sw}" x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}"/>'
            )
        lines = name.split("\n")
        subs = sub.split("\n") if sub else []
        total = len(lines) * 16 + len(subs) * 13 + (10 if eyebrow else 0)
        ty = y + h / 2 - total / 2 + 12
        cx = x + w / 2
        if eyebrow:
            fill = "acc" if kind == "focal" else ("lnk" if kind == "indep" else "soft")
            self.text(cx, ty - 2, eyebrow.upper(), "eye", fill)
            ty += 12
        for ln in lines:
            self.text(cx, ty, ln, "name", "ink")
            ty += 16
        for s in subs:
            self.text(cx, ty - 1, s, "sub", "soft")
            ty += 13
        return {
            "t": (x + w / 2, y), "b": (x + w / 2, y + h), "l": (x, y + h / 2), "r": (x + w, y + h / 2),
            "x": x, "y": y, "w": w, "h": h, "cx": x + w / 2, "cy": y + h / 2,
        }

    def group(self, x, y, w, h, label, cls="grp", label_fill="soft"):
        self.under.append(f'<rect class="{cls}" x="{x}" y="{y}" width="{w}" height="{h}" rx="8"/>')
        self.text(x + 14, y + 18, label.upper(), "eye", label_fill, anchor="start", layer=self.under)

    # ---- connectors -----------------------------------------------------
    def arrow(self, pts, style="ln", dashed=False, label=None, at=None, head=True, r=8):
        d = _rounded(pts, r)
        mk = {"ln": "m-muted", "ln-acc": "m-acc", "ln-lnk": "m-lnk"}[style]
        dash = ' stroke-dasharray="5 4"' if dashed else ""
        end = f' marker-end="url(#{mk})"' if head else ""
        self.lines.append(f'<path class="{style}" stroke-width="1.2" d="{d}"{dash}{end}/>')
        if label:
            if at is None:
                (x1, y1), (x2, y2) = pts[len(pts) // 2 - 1], pts[len(pts) // 2]
                at = ((x1 + x2) / 2, (y1 + y2) / 2)
            self.label(at[0], at[1], label, "acc" if style == "ln-acc" else "muted")

    def label(self, x, y, s, fill="muted"):
        w = len(s) * CHAR_MONO + 10
        self.labels.append(f'<rect class="mask" x="{x - w / 2:.1f}" y="{y - 8}" width="{w:.1f}" height="15" rx="2"/>')
        self.labels.append(f'<text x="{x}" y="{y + 3.5}" class="lbl {fill}" text-anchor="middle">{escape(s)}</text>')

    # ---- output ---------------------------------------------------------
    def render(self) -> str:
        head = (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" width="{self.w}" '
            f'height="{self.h}" role="img" aria-labelledby="t d">\n'
            f"<title id=\"t\">{escape(self.title)}</title>\n<desc id=\"d\">{escape(self.desc)}</desc>\n"
            f"<style>{STYLE}</style>\n<defs>\n"
            + "".join(
                f'<marker id="{i}" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">'
                f'<polygon class="{c}" points="0 0, 8 3, 0 6"/></marker>\n'
                for i, c in (("m-muted", "muted"), ("m-acc", "acc"), ("m-lnk", "lnk"))
            )
            + "</defs>\n"
            f'<rect class="bg" width="{self.w}" height="{self.h}" rx="10"/>\n'
            f'<text x="28" y="34" class="eye soft">{escape(self.eyebrow.upper())}</text>\n'
            f'<line class="rule" x1="28" y1="44" x2="{self.w - 28}" y2="44"/>\n'
        )
        body = "\n".join(self.under + self.lines + self.nodes + self.labels)
        return head + body + "\n</svg>\n"

    def save(self):
        OUT.mkdir(parents=True, exist_ok=True)
        (OUT / f"{self.name}.svg").write_text(self.render(), encoding="utf-8")


def _rounded(pts, r):
    """Orthogonal polyline with quarter-arc corners of radius r."""
    if len(pts) == 2:
        return f"M{pts[0][0]},{pts[0][1]} L{pts[1][0]},{pts[1][1]}"
    out = [f"M{pts[0][0]},{pts[0][1]}"]
    for i in range(1, len(pts) - 1):
        (x0, y0), (x1, y1), (x2, y2) = pts[i - 1], pts[i], pts[i + 1]
        d1 = max(abs(x1 - x0), abs(y1 - y0))
        d2 = max(abs(x2 - x1), abs(y2 - y1))
        rr = min(r, d1 / 2, d2 / 2)
        ax = x1 - rr * _sgn(x1 - x0)
        ay = y1 - rr * _sgn(y1 - y0)
        bx = x1 + rr * _sgn(x2 - x1)
        by = y1 + rr * _sgn(y2 - y1)
        out.append(f"L{ax},{ay} Q{x1},{y1} {bx},{by}")
    out.append(f"L{pts[-1][0]},{pts[-1][1]}")
    return " ".join(out)


def _sgn(v):
    return (v > 0) - (v < 0)


# =========================================================================
# 1. Lifecycle (README short form, and docs/diagrams.md with clearance gate)
# =========================================================================
def lifecycle(clearance: bool):
    name = "lifecycle-cleared" if clearance else "lifecycle"
    f = Fig(name, 1000, 360 if clearance else 300,
            "Nuclear-grade lifecycle",
            "Question, Discover, Specify, Plan, Execute, Verify, Review, then the Decide gate. "
            "Ship or defer leads to Baseline, Operate, Learn; block returns to Plan; "
            "Learn feeds the next Question." + (" A separate Cleared-to-apply-now gate sits between "
                                                "Decide and Baseline and holds while clearance is lapsed." if clearance else ""),
            "The change lifecycle · eleven beats")
    W, H, G, y = 92, 44, 20, 104
    names = ["Question", "Discover", "Specify", "Plan", "Execute", "Verify", "Review"]
    x = 36
    n = []
    for nm in names:
        n.append(f.box(x, y, W, H, nm))
        x += W + G
    dec = f.box(x, y - 14, 112, 72, "Decide", kind="focal", shape="diamond")
    for a, b in zip(n, n[1:]):
        f.arrow([a["r"], b["l"]])
    f.arrow([n[-1]["r"], dec["l"]])
    # block: Decide -> Plan, over the top
    f.arrow([dec["t"], (dec["cx"], 68), (n[3]["cx"], 68), n[3]["t"]], "ln-acc", dashed=True,
            label="block", at=((dec["cx"] + n[3]["cx"]) / 2, 68))
    y2 = 220 if not clearance else 252
    xs = dec["cx"]
    if clearance:
        clr = f.box(xs - 64, 192, 128, 64, "Cleared to\napply now?", kind="focal", shape="diamond")
        f.arrow([dec["b"], clr["t"]], "ln-acc", label="ship / defer", at=(xs, 166))
        # hold / lapsed self-loop on the right
        f.arrow([clr["r"], (clr["r"][0] + 40, clr["cy"]), (clr["r"][0] + 40, clr["y"] - 4),
                 (clr["cx"] + 18, clr["y"] - 4), (clr["cx"] + 18, clr["y"] + 9)],
                dashed=True, r=6)
        f.label(clr["r"][0] + 4, clr["y"] - 4, "hold / lapsed")
        src = clr
        y2 = 316
    else:
        src = dec
    bx = xs - W / 2
    base = f.box(bx, y2 - H / 2, W, H, "Baseline", kind="store")
    op = f.box(bx - W - 48, y2 - H / 2, W, H, "Operate", kind="store")
    le = f.box(bx - 2 * (W + 48), y2 - H / 2, W, H, "Learn", kind="store")
    if clearance:
        f.arrow([src["b"], base["t"]], "ln-acc", label="yes")
    else:
        f.arrow([src["b"], base["t"]], "ln-acc", label="ship / defer")
    f.arrow([base["l"], op["r"]])
    f.arrow([op["l"], le["r"]])
    f.arrow([le["l"], (n[0]["cx"], le["cy"]), n[0]["b"]], dashed=True,
            label="feeds future basis", at=((n[0]["cx"] + le["x"]) / 2, le["cy"]))
    f.save()


# =========================================================================
# 2. PRO and PROVE bands
# =========================================================================
def bands(name, title, eyebrow, rows, links, desc):
    """rows: list of (band label, [(id, label, kind, shape)]). Band rows stack."""
    BW, BH, W, H, G = 960, 92, 112, 40, 28
    f = Fig(name, 1040, 72 + len(rows) * (BH + 20) + 8, title, desc, eyebrow)
    pos = {}
    y = 64
    for i, (lab, items) in enumerate(rows):
        f.group(40, y, BW, BH, lab, cls="band", label_fill="acc" if "VERDICT" in lab else "soft")
        x = 220 + i * 60 if len(rows) > 3 else 220 + i * 120
        for (nid, nm, kind, shape) in items:
            if shape == "diamond":
                pos[nid] = f.box(x, y + BH / 2 - 30, 128, 60, nm, kind=kind, shape="diamond")
                x += 128 + G
            else:
                pos[nid] = f.box(x, y + BH / 2 - H / 2, W, H, nm, kind=kind, shape="pill")
                x += W + G
        for (a, *_), (b, *_) in zip(items, items[1:]):
            f.arrow([pos[a]["r"], pos[b]["l"]])
        y += BH + 20
    for spec in links:
        f.arrow(**spec(pos))
    f.save()
    return pos


def pro():
    rows = [
        ("P — Plan", [("q", "Question", "step", "pill"), ("d", "Discover", "step", "pill"),
                     ("s", "Specify", "step", "pill"), ("p", "Plan", "step", "pill")]),
        ("R — Run", [("e", "Execute", "step", "pill"), ("v", "Verify", "step", "pill"),
                    ("rv", "Review", "step", "pill"), ("dec", "Decide", "focal", "diamond")]),
        ("O — Operate", [("b", "Baseline", "store", "pill"), ("o", "Operate", "store", "pill"),
                        ("l", "Learn", "store", "pill")]),
    ]
    links = [
        lambda P: dict(pts=[P["p"]["b"], (P["p"]["cx"], P["e"]["y"] - 26), (P["e"]["cx"], P["e"]["y"] - 26), P["e"]["t"]]),
        lambda P: dict(pts=[P["dec"]["b"], (P["dec"]["cx"], P["b"]["y"] - 30), (P["b"]["cx"], P["b"]["y"] - 30), P["b"]["t"]],
                       style="ln-acc", label="ship / defer", at=((P["dec"]["cx"] + P["b"]["cx"]) / 2 + 120, P["b"]["y"] - 30)),
        lambda P: dict(pts=[P["dec"]["r"], (P["dec"]["r"][0] + 32, P["dec"]["cy"]), (P["dec"]["r"][0] + 32, P["p"]["cy"]), P["p"]["r"]],
                       style="ln-acc", dashed=True, label="block", at=(P["dec"]["r"][0] + 32, (P["dec"]["cy"] + P["p"]["cy"]) / 2)),
        lambda P: dict(pts=[P["l"]["r"], (P["l"]["r"][0] + 40, P["l"]["cy"]), (P["l"]["r"][0] + 40, P["l"]["y"] + 52),
                            (180, P["l"]["y"] + 52), (180, P["q"]["cy"]), P["q"]["l"]],
                       dashed=True, label="lessons feed the next basis", at=(400, P["l"]["y"] + 52)),
    ]
    bands("pro", "PRO: Plan · Run · Operate", "PRO · the path in three moves", rows, links,
          "Three bands. Plan: Question, Discover, Specify, Plan. Run: Execute, Verify, Review, Decide. "
          "Operate: Baseline, Operate, Learn. Decide ships or defers to Baseline, blocks back to Plan; "
          "lessons feed the next Question.")


def prove():
    """Staircase: each band starts under the beat that hands off to it, so band-to-band arrows run straight down."""
    f = Fig("prove", 1280, 620, "PROVE: Plan · Run · Observe · Verdict · Educate",
            "Five bands. Plan: Question, Discover, Specify, Plan. Run: Execute. Observe: Verify, Review. "
            "Verdict: Decide, then Cleared to apply now, which holds while clearance is lapsed. "
            "Educate: Baseline, Operate, Learn. Block returns to Plan; lessons feed the next Question.",
            "PROVE · the path in five moves")
    W, H, C, BH = 104, 40, 124, 84
    x0 = 176

    def cx(col):
        return x0 + col * C + W / 2

    rows = [
        ("P — Plan", [(0, "q", "Question"), (1, "d", "Discover"), (2, "s", "Specify"), (3, "p", "Plan")]),
        ("R — Run", [(3, "e", "Execute")]),
        ("O — Observe", [(3, "v", "Verify"), (4, "rv", "Review")]),
        ("V — Verdict", [(4, "dec", "Decide"), (5.7, "clr", "Cleared to\napply now?")]),
        ("E — Educate", [(5.7, "b", "Baseline"), (6.7, "o", "Operate"), (7.7, "l", "Learn")]),
    ]
    P = {}
    y = 64
    for lab, items in rows:
        f.group(32, y, 1216, BH, lab, cls="band", label_fill="acc" if "Verdict" in lab else "soft")
        for col, nid, nm in items:
            if nid in ("dec", "clr"):
                P[nid] = f.box(cx(col) - 60, y + BH / 2 - 32, 120, 64, nm, kind="focal", shape="diamond")
            else:
                kind = "store" if "Educate" in lab else "step"
                P[nid] = f.box(cx(col) - W / 2, y + BH / 2 - H / 2, W, H, nm, kind=kind, shape="pill")
        ids = [i[1] for i in items]
        for a, b in zip(ids, ids[1:]):
            f.arrow([P[a]["r"], P[b]["l"]], "ln-acc" if a == "dec" else "ln",
                    label="ship / defer" if a == "dec" else None)
        y += BH + 16
    f.arrow([P["p"]["b"], P["e"]["t"]])
    f.arrow([P["e"]["b"], P["v"]["t"]])
    f.arrow([P["rv"]["b"], P["dec"]["t"]])
    f.arrow([P["clr"]["b"], P["b"]["t"]], "ln-acc", label="yes")
    c = P["clr"]
    f.arrow([c["r"], (c["r"][0] + 36, c["cy"]), (c["r"][0] + 36, c["y"] - 8), (c["cx"] + 20, c["y"] - 8),
             (c["cx"] + 20, c["y"] + 10)], dashed=True, r=6)
    f.label(c["r"][0] + 36, c["y"] - 8, "hold / lapsed")
    d, pl = P["dec"], P["p"]
    gx = (cx(2) + cx(3)) / 2
    f.arrow([d["l"], (gx, d["cy"]), (gx, pl["b"][1] + 14), (pl["x"] + 20, pl["b"][1] + 14), (pl["x"] + 20, pl["b"][1])],
            "ln-acc", dashed=True, label="block", at=(gx, P["e"]["cy"]))
    lo, q = P["l"], P["q"]
    f.arrow([lo["r"], (lo["r"][0] + 24, lo["cy"]), (lo["r"][0] + 24, 596), (148, 596), (148, q["cy"]), q["l"]],
            dashed=True, label="lessons feed the next basis", at=(600, 596))
    f.save()


# =========================================================================
# 3. Mode selection
# =========================================================================
def modes():
    f = Fig("mode-selection", 960, 560, "Choosing a rigor mode",
            "Start from a change request. Purely administrative and instantly reversible: administrative floor. "
            "Local, reversible, obvious proof: Quick packet. User, data, dependency, permission, AI authority or "
            "release consequence: Standard packet. Severe, silent, irreversible or external trust: human-reviewed "
            "stronger mode. Already went wrong: incident pattern.", "Mode selection · lightest honest mode")
    cx = 360
    st = f.box(cx - 80, 64, 160, 40, "Change request", shape="oval", kind="ext")
    q0 = f.box(cx - 120, 128, 240, 92, "Purely administrative?", "instantly reversible ·\nno new trust boundary", shape="diamond")
    q1 = f.box(cx - 120, 248, 240, 92, "Local & reversible?", "obvious proof ·\nno new trust boundary", shape="diamond")
    q2 = f.box(cx - 120, 368, 240, 92, "Real consequence?", "user · data · dep · permission\nAI authority · release", shape="diamond")
    ox, ow = 600, 320
    fl = f.box(ox, 150, ow, 48, "Administrative floor", "no packet — the commit message is the record", kind="ext")
    qk = f.box(ox, 270, ow, 48, "Quick packet", "risk.md + proof.md")
    sd = f.box(ox, 390, ow, 48, "Standard packet", "6 files")
    sg = f.box(cx - 120, 496, 240, 48, "Human-reviewed stronger mode", kind="focal")
    inc = f.box(28, 496, 168, 48, "Incident pattern", kind="store")
    f.arrow([st["b"], q0["t"]])
    f.arrow([q0["r"], fl["l"]], label="yes")
    f.arrow([q0["b"], q1["t"]], label="no")
    f.arrow([q1["r"], qk["l"]], label="yes")
    f.arrow([q1["b"], q2["t"]], label="no")
    f.arrow([q2["r"], sd["l"]], label="yes")
    f.arrow([q2["b"], sg["t"]], "ln-acc", label="severe · silent · irreversible · external trust")
    f.arrow([q2["l"], (inc["cx"], q2["cy"]), inc["t"]], label="already went wrong", at=(inc["cx"], q2["cy"] + 40))
    f.save()


# =========================================================================
# 4. Sequence: you, agent, record, reviewer
# =========================================================================
def sequence():
    f = Fig("one-change-sequence", 960, 560, "One change, end to end",
            "Sequence between You, the AI agent, the change record and a reviewer: you set the goal, the agent drafts "
            "risk and acceptance, you approve limits, the agent builds inside them and writes claims with evidence, "
            "the reviewer decides on purpose, and the approved version is saved as the baseline.",
            "One change · who does what, in order")
    actors = [("You", "person", "ext"), ("AI agent", "", "step"), ("Change record", "", "focal"), ("Reviewer", "person", "ext")]
    xs = [140, 380, 620, 840]
    top, bot = 64, 500
    for (nm, sub, kind), x in zip(actors, xs):
        f.box(x - 72, top, 144, 40, nm, kind=kind, shape="oval" if sub else "rect")
        f.lines.append(f'<line class="life" x1="{x}" y1="{top + 40}" x2="{x}" y2="{bot}" stroke-width="1"/>')
    msgs = [
        (0, 1, "Ask the hard question, set the goal", False),
        (1, 2, "Draft the risk and what “good” means", False),
        (2, 0, "You read the draft", True),
        (0, 1, "Approve the limits (may / may not do)", False),
        (1, 1, "Build only inside the limits", False),
        (1, 2, "Write each claim with its evidence", False),
        (2, 3, "Show evidence, gaps, decision", True),
        (3, 2, "Decide on purpose — ship / defer / block", False),
        (2, 2, "Save the approved version (baseline)", False),
    ]
    y = 136
    for a, b, text, ret in msgs:
        style = "ln-acc" if text.startswith("Decide") else "ln"
        if a == b:
            x = xs[a]
            f.arrow([(x, y - 6), (x + 36, y - 6), (x + 36, y + 10), (x + 4, y + 10)], style, r=6)
            f.text(x + 46, y + 6, text, "lbl", "muted", anchor="start", layer=f.labels)
        else:
            x1, x2 = xs[a], xs[b]
            d = 1 if x2 > x1 else -1
            f.arrow([(x1 + 3 * d, y), (x2 - 4 * d, y)], style, dashed=ret)
            f.label((x1 + x2) / 2, y - 12, text, "acc" if style == "ln-acc" else "muted")
        y += 40
    f.under.append(f'<rect class="band" x="{xs[0] - 72}" y="{y - 8}" width="{xs[3] - xs[0] + 144}" height="32" rx="6"/>')
    f.text((xs[0] + xs[3]) / 2, y + 13, "Lessons from real use feed the next change", "call", "muted", layer=f.under)
    f.save()


# =========================================================================
# 5. Configuration-control loop
# =========================================================================
def control_loop(clearance: bool):
    name = "control-loop-cleared" if clearance else "control-loop"
    f = Fig(name, 1040, 300, "Configuration control loop",
            "Controlled items (code, prompts, models, dependencies, docs, releases) receive a change; evidence names "
            "pass or gap; Decide on purpose. Ship or defer saves the baseline, which is operated and yields lessons "
            "that feed the next change. Block returns to the change."
            + (" A Cleared-to-apply-now gate holds while clearance is lapsed." if clearance else ""),
            "Configuration control · the loop")
    y = 92
    ci = f.box(36, y, 188, 64, "Controlled items", "code · prompts · models\ndeps · docs · releases", kind="store")
    ch = f.box(272, y + 10, 132, 44, "A change")
    ev = f.box(452, y + 4, 168, 56, "Evidence", "pass or gap, named")
    dec = f.box(668, y - 6, 140, 76, "Decide", "on purpose", kind="focal", shape="diamond")
    f.arrow([ci["r"], ch["l"]])
    f.arrow([ch["r"], ev["l"]])
    f.arrow([ev["r"], dec["l"]])
    f.arrow([dec["t"], (dec["cx"], 64), (ch["cx"], 64), ch["t"]], "ln-acc", dashed=True, label="block",
            at=((dec["cx"] + ch["cx"]) / 2, 64))
    y2 = 220
    if clearance:
        clr = f.box(852, y - 2, 128, 68, "Cleared to\napply now?", kind="focal", shape="diamond")
        f.arrow([dec["r"], clr["l"]], "ln-acc", label="ship / defer", at=(838, dec["cy"] - 14))
        f.arrow([clr["r"], (clr["r"][0] + 20, clr["cy"]), (clr["r"][0] + 20, clr["y"] - 14), (clr["cx"], clr["y"] - 14), clr["t"]],
                dashed=True, r=6)
        f.label(clr["cx"] + 30, clr["y"] - 14, "hold / lapsed")
        bl = f.box(min(clr["cx"] - 96, 820), y2, 192, 52, "Saved baseline", "the approved version", kind="store")
        f.arrow([clr["b"], bl["t"]], "ln-acc", label="yes")
    else:
        bl = f.box(dec["cx"] - 96, y2, 192, 52, "Saved baseline", "the approved version", kind="store")
        f.arrow([dec["b"], bl["t"]], "ln-acc", label="ship / defer")
    op = f.box(bl["x"] - 180, y2 + 4, 132, 44, "Operate")
    le = f.box(op["x"] - 200, y2 + 4, 152, 44, "Lessons learned")
    f.arrow([bl["l"], op["r"]])
    f.arrow([op["l"], le["r"]])
    f.arrow([le["l"], (ci["cx"], le["cy"]), ci["b"]], dashed=True, label="feed the next change",
            at=(ci["cx"], (ci["b"][1] + le["cy"]) / 2 + 4))
    f.save()


# =========================================================================
# 6. Skill map
# =========================================================================
def skill_map(name, overlays_on):
    """overlays_on: dict spine-id -> list of overlay chains; each chain is [(label, edge label), ...]."""
    spine = [
        ("ung", "using-nuclear-grade", "router · entry point"),
        ("qa", "questioning-attitude", None),
        ("ccr", "rating-change-risk", None),
        ("ccp", "creating-change-records", None),
        ("pc", "proving-claims", None),
        ("rsr", "checking-release-readiness", None),
        ("bc", "recording-a-known-good-version", None),
        ("lfo", "learning-from-experience", None),
    ]
    ROW = 52
    rows_for = {sid: max(1, len(overlays_on.get(sid, []))) for sid, *_ in spine}
    total_rows = sum(rows_for.values())
    h = 96 + total_rows * ROW + 40
    f = Fig(name, 1200, h, "Skill map",
            "The core path runs from using-nuclear-grade through questioning-attitude, rating-change-risk, "
            "creating-change-records, proving-claims, checking-release-readiness, recording-a-known-good-version and "
            "learning-from-experience, which feeds back to questioning-attitude. Rating-change-risk branches to "
            "choosing-what-to-control and checking-what-a-change-affects. Heavier overlays switch on by consequence.",
            "Skill map · core path and consequence overlays")
    SX, SW = 340, 248
    OX = SX + SW + 200
    y = 80
    pos = {}
    f.group(OX - 24, 60, 1200 - OX - 4, total_rows * ROW + 36, "Heavier overlays — switch on by consequence")
    f.group(SX - 24, 60, SW + 48, total_rows * ROW + 36, "Core path", cls="band")
    for sid, nm, sub in spine:
        kind = "focal" if sid == "ung" else "step"
        pos[sid] = f.box(SX, y + 4, SW, 40 if not sub else 44, nm, sub, kind=kind)
        chains = overlays_on.get(sid, [])
        oy = y + 4
        for chain in chains:
            prev = None
            ox = OX
            for lab, edge in chain:
                w = max(150, int(len(lab) * CHAR_SANS + 28) // 4 * 4)
                b = f.box(ox, oy, w, 40, lab, kind="opt" if prev is None else "opt")
                if prev is None:
                    src = pos[sid]
                    sy = oy + 20
                    if abs(sy - src["cy"]) < 1:
                        f.arrow([src["r"], b["l"]], dashed=True, label=edge, at=((SX + SW + 24 + OX) / 2, sy))
                    else:
                        f.arrow([(src["r"][0], src["cy"] + 8), (SX + SW + 24, src["cy"] + 8), (SX + SW + 24, sy), b["l"]],
                                dashed=True, label=edge, at=((SX + SW + 24 + OX) / 2, sy))
                else:
                    f.arrow([prev["r"], b["l"]])
                prev = b
                ox += w + 32
            oy += ROW
        y += rows_for[sid] * ROW
    order = [s[0] for s in spine]
    for a, b in zip(order, order[1:]):
        f.arrow([pos[a]["b"], pos[b]["t"]])
    # side branch: controlled config touched
    ccr, ccp = pos["ccr"], pos["ccp"]
    ici = f.box(28, ccr["y"] + 52, 248, 40, "choosing-what-to-control")
    sci = f.box(28, ici["y"] + 72, 248, 40, "checking-what-a-change-affects")
    f.arrow([ccr["l"], (ici["cx"], ccr["cy"]), ici["t"]], label="controlled config touched",
            at=(ici["cx"] + 24, ccr["cy"]))
    f.arrow([ici["b"], sci["t"]])
    # learning loop back to questioning-attitude, left of the spine
    lfo, qa = pos["lfo"], pos["qa"]
    lx = SX - 16
    f.arrow([(lfo["x"], lfo["cy"]), (lx, lfo["cy"]), (lx, qa["cy"]), qa["l"]], "ln-acc", dashed=True)
    f.text(lx - 12, lfo["cy"] - 10, "durable control", "lbl", "acc", anchor="end", layer=f.labels)
    f.text(lx - 12, lfo["cy"] + 4, "update ↺", "lbl", "acc", anchor="end", layer=f.labels)
    f.save()


FULL_OVERLAYS = {
    "qa": [[("staying-on-mission", "long drifting session")]],
    "ccr": [[("deciding-who-decides", "irreversible action"), ("declaring-intent", None)],
            [("vetting-outside-code-and-models", "outside dep / model")]],
    "ccp": [[("briefing-an-agent", "delegate / resume"), ("handing-off-work", None)],
            [("double-checking-before-acting", "critical action")]],
    "pc": [[("reviewing-code-quality", "standards drift in diff")],
           [("verifying-final-artifacts", "rendered deliverable")]],
    "rsr": [[("stress-testing-agent-changes", "new agent authority")],
            [("recording-what-an-agent-did", "execution path matters")]],
    "lfo": [[("closing-stale-packets", "stale packet sweep")]],
}
SHORT_OVERLAYS = {
    "qa": FULL_OVERLAYS["qa"],
    "ccp": FULL_OVERLAYS["ccp"],
    "pc": FULL_OVERLAYS["pc"][:1],
    "rsr": FULL_OVERLAYS["rsr"],
    "lfo": FULL_OVERLAYS["lfo"],
}


# =========================================================================
# 7. Evidence chain (traceability)
# =========================================================================
def evidence_chain():
    f = Fig("evidence-chain", 1040, 300, "Evidence chain",
            "Change intent, consequence classification, design basis, controlled items, implementation plan, "
            "traceability, verification, baseline record, release readiness, operating signals; OPEX feeds forward "
            "into the design basis.", "Evidence chain · intent to operating signal")
    W, H, G = 168, 52, 30
    row1 = [("Change intent", None, "ext"), ("Consequence", "classification", "step"), ("Design basis", "basis.md", "focal"),
            ("Controlled items", None, "store"), ("Implementation plan", "plan.md", "step")]
    row2 = [("Traceability", "trace.md", "step"), ("Verification", "verification.md", "step"), ("Baseline record", None, "store"),
            ("Release readiness", "ship.md", "step"), ("Operating signals", "opex.md", "step")]
    x0 = 40
    top = [f.box(x0 + i * (W + G), 76, W, H, *r[:2], kind=r[2]) for i, r in enumerate(row1)]
    bot = [f.box(x0 + (4 - i) * (W + G), 204, W, H, *r[:2], kind=r[2]) for i, r in enumerate(row2)]
    for a, b in zip(top, top[1:]):
        f.arrow([a["r"], b["l"]])
    f.arrow([top[-1]["b"], bot[0]["t"]])
    for a, b in zip(bot, bot[1:]):
        f.arrow([a["l"], b["r"]])
    f.arrow([bot[-1]["t"], (bot[-1]["cx"], 168), (top[2]["cx"], 168), top[2]["b"]], "ln-acc", dashed=True,
            label="feeds forward", at=((bot[-1]["cx"] + top[2]["cx"]) / 2, 168))
    f.save()


# =========================================================================
# 8. Independence seam
# =========================================================================
def independence():
    f = Fig("independence-seam", 1040, 500, "The independence seam",
            "Left, coupled: the actor builds the change and also authors the verify evidence, the review narrative "
            "and the decide framing, so every gate input is actor-authored and a confident error ships wrapped in its "
            "own proof. Right, with the seam: an independent verifier or reproducible evidence and a decider "
            "independent of the actor, so a confident error is visible at the gate.",
            "Independence · where a confident error is caught")
    f.group(28, 60, 480, 420, "Coupled — the hole")
    f.group(532, 60, 480, 420, "With the independence seam")
    a = f.box(168, 92, 200, 40, "Actor builds the change", kind="ext", shape="oval")
    xs = [44, 196, 348]
    outs = [f.box(x, 172, 144, 48, t, "actor-authored", kind="ext") for x, t in
            zip(xs, ["Verify evidence", "Review narrative", "Decide framing"])]
    for o in outs:
        f.arrow([a["b"], (a["cx"], 152), (o["cx"], 152), o["t"]] if o["cx"] != a["cx"] else [a["b"], o["t"]])
    g = f.box(208, 260, 120, 64, "Gates", shape="diamond")
    for o in outs:
        f.arrow([o["b"], (o["cx"], 240), (g["cx"], 240), g["t"]] if o["cx"] != g["cx"] else [o["b"], g["t"]])
    bad = f.box(128, 372, 280, 56, "A confident error ships,", "wrapped in its own proof", kind="opt")
    f.arrow([g["b"], bad["t"]], label="every input actor-authored", at=(g["cx"], 350))
    a2 = f.box(672, 92, 200, 40, "Actor builds the change", kind="ext", shape="oval")
    iv = f.box(632, 164, 280, 52, "Independent verifier", "or evidence the reviewer reproduces", kind="indep")
    g2 = f.box(712, 236, 120, 56, "Gates", shape="diamond")
    idc = f.box(652, 308, 240, 40, "Decider independent of the actor", kind="indep")
    good = f.box(632, 404, 280, 56, "A confident error is", "visible at the gate", kind="focal")
    f.arrow([a2["b"], iv["t"]])
    f.arrow([iv["b"], g2["t"]])
    f.arrow([g2["b"], idc["t"]])
    f.arrow([idc["b"], good["t"]], "ln-acc", label="input not solely actor-authored", at=(772, 376))
    f.save()


# =========================================================================
# 9. Control plane vs execution plane
# =========================================================================
def planes():
    f = Fig("control-execution-planes", 1040, 300, "Control plane and execution plane",
            "The stage contract (inputs, process, outputs) in the interpretable control plane scopes and bounds the "
            "agent, tools and CI in the enforced execution plane. Their output reaches an acceptance gate the agent "
            "cannot edit: accept moves to the next stage; reject returns to the stage contract.",
            "Agentic workflow · two planes")
    f.group(28, 64, 280, 200, "Control plane · interpretable", cls="band")
    f.group(340, 64, 672, 200, "Execution plane · enforced", cls="band")
    sc = f.box(64, 136, 208, 56, "Stage contract", "inputs · process · outputs", kind="store")
    run = f.box(400, 140, 176, 48, "Agent / tools / CI")
    gate = f.box(612, 108, 200, 112, "Acceptance gate", "rung the agent\ncannot edit", kind="focal", shape="diamond")
    nxt = f.box(868, 140, 120, 48, "Next stage", kind="ext")
    f.arrow([sc["r"], run["l"]], label="scopes & bounds")
    f.arrow([run["r"], gate["l"]])
    f.arrow([gate["r"], nxt["l"]], "ln-acc", label="accept")
    f.arrow([gate["b"], (gate["cx"], 240), (sc["cx"], 240), sc["b"]], dashed=True, label="reject",
            at=((gate["cx"] + sc["cx"]) / 2 + 60, 240))
    f.save()


def main():
    lifecycle(False)
    lifecycle(True)
    pro()
    prove()
    modes()
    sequence()
    control_loop(False)
    control_loop(True)
    skill_map("skill-map", FULL_OVERLAYS)
    skill_map("skill-map-core", SHORT_OVERLAYS)
    evidence_chain()
    independence()
    planes()
    print(f"wrote {len(list(OUT.glob('*.svg')))} SVGs to {OUT}")


if __name__ == "__main__":
    main()
