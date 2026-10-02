# -*- coding: utf-8 -*-
"""Rebuilds assets/fonts/phosphor-*.woff2 + fonts.css with only the icons the site uses.

    pip install fonttools brotli
    python _src/icons.py
"""
import io, os, re, glob, urllib.request
from fontTools import subset

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONTS = os.path.join(ROOT, "assets", "fonts")
CDN = "https://unpkg.com/@phosphor-icons/web@2.1.1/src/"
TMP = os.path.join(FONTS, "_tmp")
os.makedirs(TMP, exist_ok=True)

text = ""
for f in glob.glob(os.path.join(ROOT, "*.html")) + [os.path.join(ROOT, "assets", "site.js")] + glob.glob(os.path.join(ROOT, "_src", "*.py")):
    text += io.open(f, encoding="utf-8").read()
names = sorted(set(re.findall(r"ph-([a-z0-9-]+)", text)) - {"fill"})
# icons swapped in by site.js at runtime
names = sorted(set(names) | {"list", "x"})
print("icons:", len(names), " ".join(names))

def fetch(path, dst):
    urllib.request.urlretrieve(CDN + path, dst)

out = {}
for weight, fontfile, prefix in [("regular", "Phosphor.woff2", "ph"), ("fill", "Phosphor-Fill.woff2", "ph-fill")]:
    css_p = os.path.join(TMP, weight + ".css"); font_p = os.path.join(TMP, weight + ".woff2")
    fetch(weight + "/style.css", css_p); fetch(weight + "/" + fontfile, font_p)
    css = io.open(css_p, encoding="utf-8").read()
    wanted = names if weight == "regular" else ["whatsapp-logo"]
    cps = {}
    for n in wanted:
        m = re.search(r"\." + re.escape(prefix) + r"\.ph-" + re.escape(n) + r':before\s*\{\s*content:\s*"\\([0-9a-f]+)";', css)
        if not m:
            raise SystemExit("missing icon in Phosphor " + weight + ": " + n)
        cps[n] = m.group(1)
    subset.main([font_p, "--unicodes=" + ",".join("U+" + c for c in cps.values()), "--flavor=woff2",
                 "--output-file=" + os.path.join(FONTS, "phosphor-" + weight + ".woff2"), "--no-hinting", "--notdef-outline"])
    out[weight] = cps

BS = "\\"
css = """/* Self-hosted fonts. Geist: SIL Open Font License 1.1 (OFL.txt).
   Phosphor Icons 2.1.1: MIT License (LICENSE-phosphor.txt), subset by _src/icons.py. */
@font-face{font-family:"Geist";font-style:normal;font-weight:400 700;font-display:swap;src:url(geist-latin-ext.woff2) format("woff2");unicode-range:U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+0304,U+0308,U+0329,U+1D00-1DBF,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF}
@font-face{font-family:"Geist";font-style:normal;font-weight:400 700;font-display:swap;src:url(geist-latin.woff2) format("woff2");unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}
@font-face{font-family:"Phosphor";src:url(phosphor-regular.woff2) format("woff2");font-weight:normal;font-style:normal;font-display:block}
@font-face{font-family:"Phosphor-Fill";src:url(phosphor-fill.woff2) format("woff2");font-weight:normal;font-style:normal;font-display:block}
.ph,.ph-fill{speak:never;font-style:normal;font-weight:normal;font-variant:normal;text-transform:none;line-height:1;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;display:inline-block}
.ph{font-family:"Phosphor"!important}
.ph-fill{font-family:"Phosphor-Fill"!important}
"""
css += "".join('.ph.ph-%s:before{content:"%s%s"}\n' % (n, BS, c) for n, c in out["regular"].items())
css += "".join('.ph-fill.ph-%s:before{content:"%s%s"}\n' % (n, BS, c) for n, c in out["fill"].items())
io.open(os.path.join(FONTS, "fonts.css"), "w", encoding="utf-8", newline="\n").write(css)
for f in glob.glob(os.path.join(TMP, "*")):
    os.remove(f)
os.rmdir(TMP)
print("fonts.css written")
