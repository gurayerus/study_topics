"""Exact titration curves (charge balance, solved by bisection) -> static SVG figures.

Usage: python3 make_curves.py [output_dir]   (default: this folder)
No third-party packages needed.
"""
import os, sys
from math import log10
Kw = 1.0e-14
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))

def solve(f):
    lo, hi = -15.0, 1.0           # log10[H3O+]
    for _ in range(200):
        mid = (lo + hi) / 2
        if f(10**mid) > 0: hi = mid
        else: lo = mid
    return -((lo + hi) / 2)       # pH

def acid_with_naoh(Va, Ca, Cb, Ka, v):          # monoprotic acid + NaOH, volumes mL
    V = Va + v; CA = Ca*Va/V; Na = Cb*v/V
    return solve(lambda h: Na + h - CA*Ka/(Ka+h) - Kw/h)

def base_with_hcl(Vb, Cb, Ca, KaBH, v):         # weak base + HCl
    V = Vb + v; CB = Cb*Vb/V; Cl = Ca*v/V
    return solve(lambda h: h + CB*h/(h+KaBH) - Cl - Kw/h)

def diprotic_with_naoh(Va, Ca, Cb, K1, K2, v):
    V = Va + v; CA = Ca*Va/V; Na = Cb*v/V
    def f(h):
        D = h*h + K1*h + K1*K2
        return Na + h - CA*(K1*h + 2*K1*K2)/D - Kw/h
    return solve(f)

# ---------- SVG helpers ----------
W, H = 680, 420
ML, MR, MT, MB = 60, 28, 56, 56
PW, PH = W-ML-MR, H-MT-MB
INK1, INK2, INK3 = "#0b0b0b", "#52514e", "#8a8984"
GRID, SURF = "#e6e5e0", "#fcfcfb"
BLUE, ORANGE = "#2a78d6", "#eb6834"

def frame(title, subtitle, xmax, xlabel, xstep):
    sx = lambda v: ML + v/xmax*PW
    sy = lambda p: MT + (14-p)/14*PH
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
         f'font-family="system-ui, -apple-system, Segoe UI, Helvetica, Arial, sans-serif" role="img" aria-label="{title}">',
         f'<rect width="{W}" height="{H}" fill="{SURF}"/>',
         f'<text x="{ML}" y="24" font-size="16" font-weight="600" fill="{INK1}">{title}</text>',
         f'<text x="{ML}" y="42" font-size="12.5" fill="{INK2}">{subtitle}</text>']
    for p in range(0, 15, 2):
        y = sy(p)
        s.append(f'<line x1="{ML}" x2="{ML+PW}" y1="{y:.1f}" y2="{y:.1f}" stroke="{GRID}" stroke-width="1"/>')
        s.append(f'<text x="{ML-8}" y="{y+4:.1f}" font-size="12" fill="{INK2}" text-anchor="end">{p}</text>')
    v = 0
    while v <= xmax + 1e-9:
        x = sx(v)
        s.append(f'<line x1="{x:.1f}" x2="{x:.1f}" y1="{MT+PH}" y2="{MT+PH+5}" stroke="{INK3}" stroke-width="1"/>')
        s.append(f'<text x="{x:.1f}" y="{MT+PH+19}" font-size="12" fill="{INK2}" text-anchor="middle">{v:g}</text>')
        v += xstep
    s.append(f'<line x1="{ML}" x2="{ML+PW}" y1="{MT+PH}" y2="{MT+PH}" stroke="{INK3}" stroke-width="1"/>')
    s.append(f'<text x="{ML+PW/2}" y="{H-12}" font-size="13" fill="{INK2}" text-anchor="middle">{xlabel}</text>')
    s.append(f'<text transform="translate(18 {MT+PH/2}) rotate(-90)" font-size="13" fill="{INK2}" text-anchor="middle">pH</text>')
    return s, sx, sy

def path(pts, sx, sy, color):
    d = " ".join(("M" if i == 0 else "L") + f"{sx(v):.1f},{sy(p):.1f}" for i, (v, p) in enumerate(pts))
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="2.25" stroke-linejoin="round" stroke-linecap="round"/>'

def dot(x, y, color):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="{color}" stroke="{SURF}" stroke-width="2"/>'

def label(x, y, text, anchor="start", size=12, color=INK1, weight="400"):
    return f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{color}" text-anchor="{anchor}" font-weight="{weight}">{text}</text>'

def vguide(x, color=INK3):
    return f'<line x1="{x:.1f}" x2="{x:.1f}" y1="{MT}" y2="{MT+PH}" stroke="{color}" stroke-width="1" stroke-dasharray="4 4"/>'

def hguide(y, color=INK3):
    return f'<line x1="{ML}" x2="{ML+PW}" y1="{y:.1f}" y2="{y:.1f}" stroke="{color}" stroke-width="1" stroke-dasharray="4 4"/>'

def legend(items, x, y):
    out = []
    for i, (c, t) in enumerate(items):
        yy = y + i*20
        out.append(f'<line x1="{x}" x2="{x+22}" y1="{yy}" y2="{yy}" stroke="{c}" stroke-width="2.5" stroke-linecap="round"/>')
        out.append(label(x+30, yy+4, t, size=12.5))
    return out

def volumes(vmax, n=1400):
    return [vmax*i/n for i in range(n+1)]

# ---------- Figure 1: strong vs weak acid, titrated with NaOH ----------
Ka = 1.8e-5
vs = volumes(50)
strong = [(v, acid_with_naoh(25.0, 0.100, 0.100, 1e8, v)) for v in vs]
weak   = [(v, acid_with_naoh(25.0, 0.100, 0.100, Ka, v)) for v in vs]
s, sx, sy = frame("Titrating 25.00 mL of 0.100 M acid with 0.100 M NaOH",
                  "Strong acid (HCl) vs. weak acid (CH₃COOH, Ka = 1.8 × 10⁻⁵)",
                  50, "Volume of NaOH added (mL)", 5)
# buffer region band (weak acid)
s.append(f'<rect x="{sx(2.5):.1f}" y="{MT}" width="{sx(22.5)-sx(2.5):.1f}" height="{PH}" fill="{ORANGE}" fill-opacity="0.07"/>')
s.append(label(sx(12.5), MT+16, "buffer region (weak acid)", "middle", 12, INK2))
s.append(vguide(sx(25)))
s.append(label(sx(25)+6, MT+PH-8, "equivalence: 25.00 mL", size=12, color=INK2))
s.append(hguide(sy(7)))
s.append(path(strong, sx, sy, BLUE))
s.append(path(weak, sx, sy, ORANGE))
ph_half = acid_with_naoh(25.0, 0.100, 0.100, Ka, 12.5)
ph_eqw  = acid_with_naoh(25.0, 0.100, 0.100, Ka, 25.0)
s.append(dot(sx(12.5), sy(ph_half), ORANGE))
s.append(label(sx(11.5), sy(5.95), "half-equivalence", "end"))
s.append(label(sx(11.5), sy(5.35), "pH = pKa = 4.74", "end"))
s.append(dot(sx(25), sy(ph_eqw), ORANGE))
s.append(label(sx(25)-9, sy(ph_eqw)-6, f"pH {ph_eqw:.2f}", "end"))
s.append(dot(sx(25), sy(7.0), BLUE))
s.append(label(sx(25)+9, sy(7.0)+16, "pH 7.00", "start"))
s.append(label(sx(3.0), sy(1.55), "HCl", size=12.5, weight="600"))
s.append(label(sx(3.0), sy(3.1), "CH₃COOH", size=12.5, weight="600"))
s.append(label(sx(49), sy(10.3), "curves match after equivalence (excess OH⁻)", "end", 12, INK2))
s += legend([(BLUE, "strong acid: HCl"), (ORANGE, "weak acid: CH₃COOH")], sx(31), sy(4.6))
s.append("</svg>")
open(f"{OUT}/titration_weak_vs_strong_acid.svg", "w").write("\n".join(s))

# ---------- Figure 2: weak base titrated with HCl ----------
KaNH4 = Kw/1.8e-5
wb = [(v, base_with_hcl(25.0, 0.100, 0.100, KaNH4, v)) for v in vs]
s, sx, sy = frame("Titrating 25.00 mL of 0.100 M NH₃ with 0.100 M HCl",
                  "Weak base: the curve falls, and the equivalence point is acidic",
                  50, "Volume of HCl added (mL)", 5)
s.append(f'<rect x="{sx(2.5):.1f}" y="{MT}" width="{sx(22.5)-sx(2.5):.1f}" height="{PH}" fill="{BLUE}" fill-opacity="0.07"/>')
s.append(label(sx(12.5), MT+PH-10, "buffer region (NH₃ / NH₄⁺)", "middle", 12, INK2))
s.append(vguide(sx(25)))
s.append(label(sx(25)+6, MT+16, "equivalence: 25.00 mL", size=12, color=INK2))
s.append(hguide(sy(7)))
s.append(path(wb, sx, sy, BLUE))
h1 = base_with_hcl(25.0, 0.100, 0.100, KaNH4, 12.5); e1 = base_with_hcl(25.0, 0.100, 0.100, KaNH4, 25.0)
s.append(dot(sx(12.5), sy(h1), BLUE))
s.append(label(sx(14.0), sy(8.2), "half-equivalence", "end"))
s.append(label(sx(14.0), sy(7.55), "pH = pKa of NH₄⁺ = 9.26", "end"))
s.append(dot(sx(25), sy(e1), BLUE))
s.append(label(sx(25)+10, sy(e1)+4, f"equivalence: pH {e1:.2f}", "start"))
s.append(label(sx(50)-4, sy(7)-6, "pH 7", "end", 12, INK2))
s.append("</svg>")
open(f"{OUT}/titration_weak_base.svg", "w").write("\n".join(s))

# ---------- Figure 3: diprotic acid ----------
K1, K2 = 1e-4, 1e-8
vs2 = volumes(70)
dp = [(v, diprotic_with_naoh(25.0, 0.100, 0.100, K1, K2, v)) for v in vs2]
s, sx, sy = frame("Titrating a diprotic acid, H₂A, with NaOH",
                  "25.00 mL of 0.100 M H₂A with 0.100 M NaOH · pKa₁ = 4.00, pKa₂ = 8.00",
                  70, "Volume of NaOH added (mL)", 10)
for v in (25, 50): s.append(vguide(sx(v)))
s.append(path(dp, sx, sy, BLUE))
pts = {}
for v in (12.5, 25, 37.5, 50):
    pts[v] = diprotic_with_naoh(25.0, 0.100, 0.100, K1, K2, v)
    s.append(dot(sx(v), sy(pts[v]), BLUE))
s.append(label(sx(12.5), sy(pts[12.5])+22, f"½ eq. 1: pH ≈ pKa₁", "middle"))
s.append(label(sx(25)+9, sy(pts[25])+18, f"1st equivalence (HA⁻)", "start"))
s.append(label(sx(37.5), sy(pts[37.5])+22, f"½ eq. 2: pH ≈ pKa₂", "middle"))
s.append(label(sx(50)+9, sy(pts[50])+18, f"2nd equivalence (A²⁻)", "start"))
# species bands along the top
for a, b, t in ((0, 25, "mostly H₂A → HA⁻"), (25, 50, "mostly HA⁻ → A²⁻"), (50, 70, "A²⁻ + excess OH⁻")):
    s.append(label((sx(a)+sx(b))/2, MT+16, t, "middle", 12, INK2))
s.append("</svg>")
open(f"{OUT}/titration_diprotic.svg", "w").write("\n".join(s))
