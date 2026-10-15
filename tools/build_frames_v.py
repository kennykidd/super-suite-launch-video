#!/usr/bin/env python3
"""Generate the nine frame sub-compositions for super-suite-promo.

Every frame shares the same font faces, background layer and (for frames 3-7)
the left-column system template. Class names are prefixed per frame (fN-).
"""
import os
import sys

PROJECT = sys.argv[1]
OUT = os.path.join(PROJECT, "compositions", "frames")
os.makedirs(OUT, exist_ok=True)

GSAP = '<script src="assets/vendor/gsap.min.js"></script><script src="assets/vendor/camera-shake.js"></script>'

C = {
    "bg": "#060B1E", "surface": "#0E1A3A", "blue": "#2EA8FF", "text": "#FFFFFF",
    "muted": "#B9C6E4", "light": "#6E7DA3", "cta": "#7B3FF2", "star": "#FBBF24",
    "leads": "#2E8BFF", "rec": "#22C55E", "rep": "#8B5CF6", "soc": "#F97316", "web": "#38BDF8",
    "green": "#22C55E", "gold": "#C9A227",
}

FONTS = """
@font-face { font-family: "Space Grotesk"; font-weight: 400; src: url("assets/fonts/space-grotesk-latin-400-normal.woff2") format("woff2"); }
@font-face { font-family: "Space Grotesk"; font-weight: 700; src: url("assets/fonts/space-grotesk-latin-700-normal.woff2") format("woff2"); }
@font-face { font-family: "Inter"; font-weight: 500; src: url("assets/fonts/inter-latin-500-normal.woff2") format("woff2"); }
@font-face { font-family: "Inter"; font-weight: 600; src: url("assets/fonts/inter-latin-600-normal.woff2") format("woff2"); }
@font-face { font-family: "Inter"; font-weight: 700; src: url("assets/fonts/inter-latin-700-normal.woff2") format("woff2"); }
@font-face { font-family: "Inter"; font-weight: 900; src: url("assets/fonts/inter-latin-900-normal.woff2") format("woff2"); }
"""

# ---------- icons (white line icons, 64x64 viewBox) ----------
ICONS = {
    "target": '<svg viewBox="0 0 64 64" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round"><circle cx="30" cy="34" r="22"/><circle cx="30" cy="34" r="13"/><circle cx="30" cy="34" r="4" fill="#fff"/><path d="M30 34 L54 10"/><path d="M46 8 L56 8 L56 18"/></svg>',
    "phone": '<svg viewBox="0 0 64 64" fill="none" stroke="#fff" stroke-width="4" stroke-linejoin="round"><path d="M18 8 h9 l5 13 -7 5 c3 7 8 12 15 15 l5 -7 13 5 v9 c0 4 -3 7 -7 7 C29 55 9 35 9 15 c0 -4 3 -7 9 -7 z"/></svg>',
    "star": '<svg viewBox="0 0 64 64" fill="none" stroke="#fff" stroke-width="4" stroke-linejoin="round"><path d="M32 7 L39.6 23.4 57 25.3 44 37.4 47.6 55 32 46.2 16.4 55 20 37.4 7 25.3 24.4 23.4 Z"/></svg>',
    "camera": '<svg viewBox="0 0 64 64" fill="none" stroke="#fff" stroke-width="4"><rect x="9" y="9" width="46" height="46" rx="14"/><circle cx="32" cy="32" r="11"/><circle cx="45.5" cy="18.5" r="2.5" fill="#fff" stroke="none"/></svg>',
    "globe": '<svg viewBox="0 0 64 64" fill="none" stroke="#fff" stroke-width="4"><circle cx="32" cy="32" r="23"/><ellipse cx="32" cy="32" rx="10" ry="23"/><path d="M9 32 h46 M13 20 h38 M13 44 h38"/></svg>',
    "check": '<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5 l4.5 4.5 L19 7.5"/></svg>',
    "lock": '<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.4"><rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11 V8 a4 4 0 0 1 8 0 v3"/></svg>',
    "cal": '<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.2"><rect x="3.5" y="5" width="17" height="15.5" rx="2.5"/><path d="M3.5 10 h17 M8 3 v4 M16 3 v4"/></svg>',
    "headset": '<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round"><path d="M4 14 v-2 a8 8 0 0 1 16 0 v2"/><rect x="3" y="13" width="4" height="6" rx="1.5"/><rect x="17" y="13" width="4" height="6" rx="1.5"/><path d="M19 19 c0 2 -2 3 -5 3"/></svg>',
    "cursor": '<svg viewBox="0 0 32 32"><path d="M5 3 L5 26 L11 20 L15.5 29 L19.5 27 L15 18.5 L23 18.5 Z" fill="#fff" stroke="#060B1E" stroke-width="1.6" stroke-linejoin="round"/></svg>',
}

SYSTEMS = {
    3: ("leads", "target", "01 / 05", "Lead<br>Generation"),
    4: ("rec", "phone", "02 / 05", "AI<br>Receptionist"),
    5: ("rep", "star", "03 / 05", "Reputation<br>Management"),
    6: ("soc", "camera", "04 / 05", "Social Media<br>Manager"),
    7: ("web", "globe", "05 / 05", "AI<br>Website"),
}


def base_css(p):
    return f"""
{FONTS}
#root {{ position: absolute; inset: 0; overflow: hidden; font-family: "Inter", sans-serif; color: {C['text']}; }}
.{p}-bg {{ position: absolute; inset: 0; background:
  radial-gradient(ellipse 70% 60% at 50% 42%, rgba(46,168,255,0.16), rgba(46,168,255,0) 70%),
  radial-gradient(ellipse 45% 40% at 85% 85%, rgba(123,63,242,0.14), rgba(123,63,242,0) 70%),
  linear-gradient(180deg, #08102A 0%, {C['bg']} 70%); }}
.{p}-grid {{ position: absolute; inset: 0; opacity: 0.35; background-image:
  linear-gradient(rgba(46,168,255,0.07) 1px, transparent 1px),
  linear-gradient(90deg, rgba(46,168,255,0.07) 1px, transparent 1px);
  background-size: 80px 80px; }}
.{p}-stage {{ position: absolute; inset: 0; }}
.{p}-cam {{ position: absolute; inset: 0; transform-origin: 50% 45%; }}
.{p}-sg {{ font-family: "Space Grotesk", sans-serif; }}
.{p}-glass {{ background: linear-gradient(160deg, rgba(30,52,110,0.55), rgba(10,20,48,0.72));
  border: 1.5px solid rgba(46,168,255,0.24); border-radius: 22px; box-shadow: 0 30px 80px rgba(0,0,0,0.45); }}
.{p}-chip {{ display: inline-block; font-family: "Space Grotesk", sans-serif; font-weight: 700; font-size: 24px;
  letter-spacing: 0.08em; text-transform: uppercase; padding: 14px 26px; border-radius: 100px; white-space: nowrap; }}
.{p}-check {{ width: 34px; height: 34px; border-radius: 50%; background: {C['green']}; padding: 6px; }}
.{p}-check svg, .{p}-disc svg {{ width: 100%; height: 100%; display: block; }}
"""


def left_css(p, color):
    return f"""
.{p}-left {{ position: absolute; left: 140px; top: 230px; width: 660px; }}
.{p}-disc {{ width: 128px; height: 128px; border-radius: 50%; padding: 30px; background: {color};
  box-shadow: 0 0 0 10px {color}26, 0 0 60px {color}88; }}
.{p}-eyebrow {{ margin-top: 40px; font-family: "Space Grotesk", sans-serif; font-weight: 700; font-size: 24px;
  letter-spacing: 0.24em; color: {color}; }}
.{p}-titlewrap {{ margin-top: 14px; overflow: hidden; padding-bottom: 6px; }}
.{p}-title {{ font-family: "Space Grotesk", sans-serif; font-weight: 700; font-size: 78px; line-height: 1.0;
  text-transform: uppercase; letter-spacing: -0.01em; }}
.{p}-benefit {{ margin-top: 40px; color: {C['text']}; border: 1.5px solid {color}; background: {color}22; }}
"""


def left_html(p, n):
    key, icon, eyebrow, title = SYSTEMS[n]
    return f"""
      <div class="{p}-left">
        <div class="{p}-disc" id="{p}-disc">{ICONS[icon]}</div>
        <div class="{p}-eyebrow" id="{p}-eyebrow">{eyebrow}</div>
        <div class="{p}-titlewrap"><div class="{p}-title" id="{p}-title">{title}</div></div>
        <div class="{p}-chip {p}-benefit" id="{p}-benefit">__BENEFIT__</div>
      </div><!--/left-->"""


def left_js(p, benefit_at):
    return f"""
  tl.fromTo("#{p}-disc", {{ scale: 0.4, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.55, ease: "back.out(1.7)" }}, 0.05);
  tl.fromTo("#{p}-eyebrow", {{ x: -24, opacity: 0 }}, {{ x: 0, opacity: 1, duration: 0.5, ease: "power3.out" }}, 0.2);
  tl.fromTo("#{p}-title", {{ yPercent: 105 }}, {{ yPercent: 0, duration: 0.7, ease: "power3.out" }}, 0.25);
  tl.fromTo("#{p}-benefit", {{ y: 20, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.5, ease: "power3.out" }}, {benefit_at});
  tl.fromTo(".{p}-cam", {{ scale: 1 }}, {{ scale: 1.035, duration: DUR, ease: "none" }}, 0);"""


def counter_js(sel, frm, to, at, dur, decimals=0, suffix=""):
    # Seek-safe: a property setter on a tweened driver runs on every render, including seek().
    dn = "drv_" + "".join(c for c in sel if c.isalnum())
    return f"""
  (function () {{ const el = document.querySelector("{sel}"); let v = {frm}; const {dn} = {{}}; const d = {dn};
    Object.defineProperty(d, "v", {{ get: () => v, set: (n) => {{ v = n; el.textContent = n.toFixed({decimals}) + "{suffix}"; }} }});
    tl.fromTo({dn}, {{ v: {frm} }}, {{ v: {to}, duration: {dur}, ease: "power2.out" }}, {at}); }})();"""


def typed(p, idname, text, cls=""):
    spans = "".join(f'<span class="{p}-ch">{ "&nbsp;" if c == " " else c}</span>' for c in text)
    return f'<span id="{idname}" class="{cls}">{spans}</span>'


def type_js(idname, at, dur):
    return f"""
  tl.fromTo("#{idname} span", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.01, stagger: {dur} / document.querySelectorAll("#{idname} span").length }}, {at});"""


def wrap(fid, n, dur, css, html, js):
    p = f"f{n}"
    return f"""<template id="{fid}-template">
  <style>
{base_css(p)}
{css}
  </style>
  <div id="root" data-composition-id="{fid}" data-width="1080" data-height="1920" data-duration="{dur}">
    <div id="{p}-bg" class="clip {p}-bg" data-start="0" data-duration="{dur}" data-track-index="0"><div class="{p}-grid"></div></div>
    <div id="{p}-stage" class="clip {p}-stage" data-start="0" data-duration="{dur}" data-track-index="1">
      <div class="{p}-cam">
{html}
      </div>
    </div>
  </div>
  {GSAP}
  <script>
  (function () {{
  const DUR = {dur};
  const tl = gsap.timeline({{ paused: true }});
  function pulse(sel, vars0, vars1, at, d) {{ tl.fromTo(sel, vars0, Object.assign({{ duration: d, ease: "power2.out", immediateRender: false }}, vars1), at); tl.fromTo(sel, vars1, Object.assign({{ duration: d, ease: "power2.in", immediateRender: false }}, vars0), at + d); }}
{js}
  window.__timelines["{fid}"] = tl;
  }})();
  </script>
</template>
"""


frames = {}

# ---------------- Frame 1 — hook (cinematic rebuild) ----------------
# Spliced into build_frames.py in place of the original Frame 1 block.
p = "f1"
RED = "#FF3B3B"


def glitch_word(idname, text, cls):
    """Three stacked copies (red, cyan, solid) — the rgb-glitch-text registry primitive."""
    return (f'<div class="{p}-gw {cls}" data-layout-allow-overlap id="{idname}">'
            f'<span class="{p}-gr">{text}</span><span class="{p}-gc">{text}</span><strong>{text}</strong></div>')


calls = [
    ("Missed call", "(480) 555-0142"), ("Missed call", "(602) 555-0199"), ("Missed call", "Unknown caller"),
    ("Voicemail", "New voicemail · 0:42"), ("Missed call", "(623) 555-0117"), ("Missed call", "(480) 555-0170"),
    ("Missed call", "(602) 555-0188"),
]
notif_html = "".join(
    f'<div class="{p}-nt" id="{p}-nt{i}"><div class="{p}-nic">{ICONS["phone"]}</div>'
    f'<div class="{p}-ntx"><div class="{p}-nh">{h}</div><div class="{p}-ns">{s}</div></div><div class="{p}-nw">now</div></div>'
    for i, (h, s) in enumerate(calls)
)
days = ["MON", "TUE", "WED", "THU", "FRI"]
cal_html = "".join(
    f'<div class="{p}-day"><div class="{p}-dh">{d}</div>' + "".join(f'<div class="{p}-slot"></div>' for _ in range(6)) + "</div>"
    for d in days
)
gold = ICONS["star"].replace('fill="none" stroke="#fff"', 'fill="#FBBF24" stroke="#FBBF24"')
grey = ICONS["star"].replace('fill="none" stroke="#fff"', 'fill="none" stroke="#4B5675"')
stars_html = "".join(f'<div class="{p}-bs">{grey}<div class="{p}-bsg">{gold}</div></div>' for _ in range(5))
person = '<svg viewBox="0 0 64 64" fill="#fff"><circle cx="32" cy="21" r="11"/><path d="M12 56 c0 -13 9 -21 20 -21 s20 8 20 21 z"/></svg>'

frames[("01-hook", 1, 7.95)] = (
    f"""
.{p}-frame {{ position: absolute; inset: 0; overflow: hidden; }}
.{p}-rig {{ position: absolute; inset: 0; transform-origin: 50% 50%; }}
.{p}-punch {{ position: absolute; inset: 0; transform-origin: 50% 50%; }}
.{p}-alarm {{ position: absolute; inset: 0; background: radial-gradient(ellipse 60% 55% at 70% 45%, rgba(255,59,59,0.42), rgba(255,59,59,0) 70%); }}
.{p}-sc {{ position: absolute; inset: 0; }}
/* glitch word */
.{p}-gw {{ position: absolute; font-family: "Space Grotesk", sans-serif; font-weight: 700; line-height: 0.9; letter-spacing: -0.03em;
  text-transform: uppercase; white-space: nowrap; }}
.{p}-gw span, .{p}-gw strong {{ position: absolute; left: 0; top: 0; }}
.{p}-gw strong {{ position: relative; color: #fff; }}
.{p}-gr {{ color: {RED}; mix-blend-mode: screen; }}
.{p}-gc {{ color: #22D3EE; mix-blend-mode: screen; }}
.{p}-big {{ font-size: 210px; left: 150px; }}
#{p}-w1a, #{p}-w2a, #{p}-w3a {{ top: 230px; }}
#{p}-w1b, #{p}-w2b, #{p}-w3b {{ top: 450px; }}
#{p}-w2b {{ font-size: 140px; top: 470px; }}
#{p}-w3b {{ font-size: 160px; top: 465px; }}
.{p}-red strong {{ color: {RED}; text-shadow: 0 0 60px rgba(255,59,59,0.6); }}
/* scene A — phone */
.{p}-phone {{ position: absolute; left: 1180px; top: 110px; width: 450px; height: 770px; border-radius: 64px; background: #05070F;
  border: 12px solid #1A2033; box-shadow: 0 0 0 2px rgba(255,59,59,0.5), 0 50px 120px rgba(0,0,0,0.7), 0 0 140px rgba(255,59,59,0.35); overflow: hidden; }}
.{p}-time {{ position: absolute; left: 0; right: 0; top: 70px; text-align: center; font: 700 110px "Space Grotesk", sans-serif; color: #E8ECF8; }}
.{p}-date {{ position: absolute; left: 0; right: 0; top: 200px; text-align: center; font: 600 24px "Inter", sans-serif; color: #8D97B5; }}
.{p}-stack {{ position: absolute; left: 22px; right: 22px; top: 260px; height: 560px; }}
.{p}-nt {{ position: absolute; left: 0; right: 0; top: 0; height: 92px; border-radius: 22px; background: rgba(40,46,66,0.92);
  display: flex; align-items: center; gap: 14px; padding: 0 18px; border: 1px solid rgba(255,255,255,0.08); }}
.{p}-nic {{ width: 52px; height: 52px; border-radius: 14px; background: {RED}; padding: 12px; flex: none; }}
.{p}-nic svg {{ width: 100%; height: 100%; display: block; }}
.{p}-ntx {{ flex: 1; }}
.{p}-nh {{ font: 700 22px "Inter", sans-serif; color: #fff; }}
.{p}-ns {{ font: 500 19px "Inter", sans-serif; color: #A9B2CC; margin-top: 2px; }}
.{p}-nw {{ font: 500 17px "Inter", sans-serif; color: #8D97B5; align-self: flex-start; margin-top: 18px; }}
.{p}-count {{ position: absolute; left: 1560px; top: 70px; width: 130px; height: 130px; border-radius: 50%; background: {RED};
  font: 700 64px "Space Grotesk", sans-serif; display: flex; align-items: center; justify-content: center; box-shadow: 0 0 60px rgba(255,59,59,0.8); }}
/* scene B — calendar */
.{p}-calwrap {{ position: absolute; left: 900px; top: 120px; width: 900px; height: 700px; perspective: 1400px; }}
.{p}-cal {{ position: absolute; inset: 0; display: flex; gap: 14px; transform-origin: 50% 60%; }}
.{p}-day {{ flex: 1; display: flex; flex-direction: column; gap: 12px; }}
.{p}-dh {{ font: 700 26px "Space Grotesk", sans-serif; color: #8D97B5; letter-spacing: 0.14em; text-align: center; padding-bottom: 6px; }}
.{p}-slot {{ flex: 1; border-radius: 12px; border: 2px dashed rgba(141,151,181,0.35); background: rgba(141,151,181,0.04); }}
.{p}-stamp {{ position: absolute; left: 1060px; top: 380px; padding: 18px 40px; border: 8px solid {RED}; border-radius: 18px; color: {RED};
  font: 700 92px "Space Grotesk", sans-serif; letter-spacing: 0.04em; white-space: nowrap; background: rgba(6,11,30,0.6); opacity: 0; }}
/* scene C — stars */
.{p}-stars {{ position: absolute; left: 930px; top: 300px; width: 900px; display: flex; justify-content: space-between; }}
.{p}-bs {{ position: relative; width: 160px; height: 160px; }}
.{p}-bs svg {{ position: absolute; inset: 0; width: 160px; height: 160px; display: block; }}
.{p}-bsg {{ position: absolute; inset: 0; filter: drop-shadow(0 0 30px rgba(251,191,36,0.7)); }}
.{p}-zero {{ position: absolute; left: 930px; top: 520px; width: 900px; text-align: center; font: 700 40px "Space Grotesk", sans-serif;
  letter-spacing: 0.12em; color: {RED}; }}
/* scene D — the gap */
.{p}-gap {{ font-size: 190px; left: 0; right: 0; top: 330px; text-align: center; }}
.{p}-gap span, .{p}-gap strong {{ left: 0; right: 0; }}
.{p}-lost {{ font-size: 100px; left: 0; right: 0; top: 210px; text-align: center; }}
.{p}-lost span, .{p}-lost strong {{ left: 0; right: 0; }}
.{p}-cust {{ position: absolute; left: 370px; top: 470px; width: 320px; text-align: center; }}
.{p}-cdisc {{ width: 170px; height: 170px; margin: 0 auto; border-radius: 50%; background: {C['blue']}; padding: 34px;
  box-shadow: 0 0 0 12px rgba(46,168,255,0.18), 0 0 80px rgba(46,168,255,0.8); }}
.{p}-cdisc svg {{ width: 100%; height: 100%; display: block; }}
.{p}-cl, .{p}-sl {{ white-space: nowrap; margin-top: 22px; font: 700 30px "Space Grotesk", sans-serif; letter-spacing: 0.16em; }}
.{p}-store {{ position: absolute; left: 1250px; top: 450px; width: 260px; text-align: center; }}
.{p}-store svg {{ width: 210px; height: 190px; display: block; margin: 0 auto; filter: drop-shadow(0 0 30px rgba(255,59,59,0.7)); }}
.{p}-sl {{ color: {RED}; }}
.{p}-path {{ position: absolute; left: 650px; top: 548px; width: 600px; height: 20px; }}
.{p}-flash {{ position: absolute; inset: 0; background: #fff; opacity: 0; }}
.{p}-rflash {{ position: absolute; inset: 0; background: {RED}; opacity: 0; mix-blend-mode: screen; }}
""",
    f"""
        <div class="{p}-frame"><div class="{p}-rig" id="{p}-rig"><div class="{p}-punch" id="{p}-punch">
          <div class="{p}-alarm" id="{p}-alarm"></div>
          <div class="{p}-sc" id="{p}-sa">
            <div class="{p}-phone" id="{p}-phone"><div class="{p}-time">9:41</div><div class="{p}-date">Monday, slow week</div><div class="{p}-stack">{notif_html}</div></div>
            <div class="{p}-count" id="{p}-count"><span id="{p}-cnum">1</span></div>
            {glitch_word(f'{p}-w1a', 'Missed', f'{p}-big')}
            {glitch_word(f'{p}-w1b', 'calls.', f'{p}-big {p}-red')}
          </div>
          <div class="{p}-sc" id="{p}-sb">
            <div class="{p}-calwrap"><div class="{p}-cal" id="{p}-cal">{cal_html}</div></div>
            <div class="{p}-stamp" id="{p}-stamp">0 BOOKINGS</div>
            {glitch_word(f'{p}-w2a', 'Quiet', f'{p}-big')}
            {glitch_word(f'{p}-w2b', 'calendar.', f'{p}-big {p}-red')}
          </div>
          <div class="{p}-sc" id="{p}-sc3">
            <div class="{p}-stars">{stars_html}</div>
            <div class="{p}-zero" id="{p}-zero">0 NEW REVIEWS THIS MONTH</div>
            {glitch_word(f'{p}-w3a', 'No new', f'{p}-big')}
            {glitch_word(f'{p}-w3b', 'reviews.', f'{p}-big {p}-red')}
          </div>
          <div class="{p}-sc" id="{p}-sd">
            {glitch_word(f'{p}-gapw', 'Every gap', f'{p}-gap')}
            {glitch_word(f'{p}-lostw', 'Lost to your competitor', f'{p}-lost {p}-red')}
            <svg class="{p}-path" viewBox="0 0 600 20"><path id="{p}-pl" d="M10 10 H590" stroke="#FF3B3B" stroke-width="6" stroke-dasharray="18 14" fill="none"/></svg>
            <div class="{p}-cust" id="{p}-cust"><div class="{p}-cdisc">{person}</div><div class="{p}-cl" id="{p}-cl">A CUSTOMER</div></div>
            <div class="{p}-store" id="{p}-store"><svg viewBox="0 0 150 120" fill="none" stroke="#FF3B3B" stroke-width="6" stroke-linejoin="round"><path d="M12 40 L24 10 H126 L138 40 Z"/><path d="M20 40 V112 H130 V40"/><rect x="58" y="66" width="34" height="46"/></svg><div class="{p}-sl">COMPETITOR</div></div>
          </div>
        </div></div></div>
        <div class="{p}-rflash" id="{p}-rflash"></div>
        <div class="{p}-flash" id="{p}-flash"></div>
""",
    f"""
  const hidden = {{ opacity: 0 }};
  // ---- helpers ------------------------------------------------------------
  // Impact: white flash + scale punch on the inner wrapper (the rig belongs to camera-shake).
  function impact(at, strength) {{
    if (at > 0) tl.fromTo("#{p}-flash", {{ opacity: 0.5 * strength }}, {{ opacity: 0, duration: 0.16, ease: "power2.out", immediateRender: false }}, at);
    tl.fromTo("#{p}-punch", {{ scale: 1 + 0.06 * strength }}, {{ scale: 1, duration: 0.45, ease: "expo.out", immediateRender: false }}, at);
  }}
  // Slam a glitch word in: oversized + blurred → crisp, then an RGB tear burst.
  const TEAR = [[-14, 12], [9, -16], [-6, 7], [16, -9], [-3, 4], [0, 0]];
  function slam(sel, at) {{
    tl.fromTo(sel, {{ opacity: 0, scale: 1.6, filter: "blur(18px)" }}, {{ opacity: 1, scale: 1, filter: "blur(0px)", duration: 0.32, ease: "expo.out", immediateRender: false }}, at);
    TEAR.forEach((o, i) => {{
      tl.set(sel + " .{p}-gr", {{ x: o[0] * 1.6, y: i % 2 ? 3 : -3 }}, at + 0.05 + i * 0.045);
      tl.set(sel + " .{p}-gc", {{ x: o[1] * 1.6, y: i % 2 ? -3 : 3 }}, at + 0.05 + i * 0.045);
    }});
  }}
  // Whip: outgoing scene smears left, incoming scene smears in from the right.
  function whip(outSel, inSel, at) {{
    tl.fromTo(outSel, {{ x: 0, filter: "blur(0px)", opacity: 1 }}, {{ x: -420, filter: "blur(26px)", opacity: 0, duration: 0.16, ease: "power2.in", immediateRender: false }}, at);
    tl.fromTo(inSel, {{ x: 420, filter: "blur(26px)", opacity: 0 }}, {{ x: 0, filter: "blur(0px)", opacity: 1, duration: 0.22, ease: "power3.out", immediateRender: false }}, at + 0.12);
  }}
  // Seek-safe number driver (property setter, like the camera-shake registry helper).
  function countTo(sel, from, to, at, dur, fmt) {{
    const el = document.querySelector(sel); let v = from; const d = {{}};
    Object.defineProperty(d, "v", {{ get: () => v, set: (n) => {{ v = n; el.textContent = fmt(n); }} }});
    tl.fromTo(d, {{ v: from }}, {{ v: to, duration: dur, ease: "power1.in" }}, at);
  }}

  tl.set("#{p}-sb, #{p}-sc3, #{p}-sd", hidden, 0);
  tl.set("#{p}-w1b, #{p}-w2a, #{p}-w2b, #{p}-w3a, #{p}-w3b, #{p}-gapw, #{p}-lostw", hidden, 0);

  // ---- camera: strong handheld for the whole frame --------------------------
  window.cameraShake(tl, "#{p}-rig", {{ profile: "handheld-normal-strong", intensity: 0.3, frequency: 1.4, rotation: false, duration: DUR }});

  // ---- Scene A (0–1.42): missed calls ----------------------------------------
  tl.fromTo("#{p}-phone", {{ y: 120, rotation: 5, opacity: 0.7 }}, {{ y: 0, rotation: -3, opacity: 1, duration: 0.5, ease: "expo.out" }}, 0);
  tl.fromTo("#{p}-alarm", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.1 }}, 0);
  impact(0.0, 1);
  tl.fromTo("#{p}-w1a", {{ opacity: 0.75, scale: 1.25, filter: "blur(6px)" }}, {{ opacity: 1, scale: 1, filter: "blur(0px)", duration: 0.3, ease: "expo.out" }}, 0);
  TEAR.forEach((o, i) => {{ tl.set("#{p}-w1a .{p}-gr", {{ x: o[0] * 1.6 }}, i * 0.045); tl.set("#{p}-w1a .{p}-gc", {{ x: o[1] * 1.6 }}, i * 0.045); }});
  impact(0.48, 0.8);
  slam("#{p}-w1b", 0.48);
  // notifications pile up, accelerating; each new card pushes the stack down
  const ARR = [0.12, 0.42, 0.66, 0.85, 1.0, 1.12, 1.22];
  ARR.forEach((t, i) => {{
    tl.fromTo("#{p}-nt" + i, {{ y: -110, opacity: 0, scale: 0.9 }}, {{ y: 0, opacity: 1, scale: 1, duration: 0.18, ease: "back.out(1.6)" }}, t);
    for (let j = 0; j < i; j++) {{
      tl.to("#{p}-nt" + j, {{ y: (i - j) * 78, scale: 1 - (i - j) * 0.03, opacity: 1 - (i - j) * 0.1, duration: 0.18, ease: "power3.out" }}, t);
    }}
  }});
  tl.fromTo("#{p}-count", {{ scale: 0 }}, {{ scale: 1, duration: 0.3, ease: "back.out(2.5)" }}, 0.15);
  countTo("#{p}-cnum", 1, 12, 0.15, 1.15, (n) => String(Math.round(n)));
  tl.fromTo("#{p}-alarm", {{ opacity: 1 }}, {{ opacity: 0.55, duration: 0.2, immediateRender: false }}, 0.2);
  tl.fromTo("#{p}-alarm", {{ opacity: 1 }}, {{ opacity: 0.55, duration: 0.2, immediateRender: false }}, 0.68);

  // ---- Scene B (1.42–2.92): quiet calendar ------------------------------------
  whip("#{p}-sa", "#{p}-sb", 1.34);
  slam("#{p}-w2a", 1.46);
  slam("#{p}-w2b", 1.98);
  tl.fromTo("#{p}-cal", {{ rotationX: 38, rotationY: -14, scale: 0.92 }}, {{ rotationX: 22, rotationY: -8, scale: 1.06, duration: 1.6, ease: "power1.out" }}, 1.4);
  tl.fromTo(".{p}-slot", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.2, stagger: 0.012 }}, 1.48);
  tl.set("#{p}-alarm", {{ opacity: 0.2 }}, 1.42);
  tl.fromTo("#{p}-stamp", {{ opacity: 0, scale: 2.6, rotation: -2 }}, {{ opacity: 1, scale: 1, rotation: -9, duration: 0.24, ease: "power4.in", immediateRender: false }}, 2.3);
  impact(2.54, 0.7);
  tl.fromTo("#{p}-alarm", {{ opacity: 0.9 }}, {{ opacity: 0.35, duration: 0.4, immediateRender: false }}, 2.54);

  // ---- Scene C (2.92–5.05): no new reviews ------------------------------------
  whip("#{p}-sb", "#{p}-sc3", 2.86);
  slam("#{p}-w3a", 2.98);
  slam("#{p}-w3b", 3.4);
  tl.fromTo(".{p}-bs", {{ y: -60, opacity: 0, rotation: -20 }}, {{ y: 0, opacity: 1, rotation: 0, duration: 0.4, stagger: 0.06, ease: "back.out(1.8)" }}, 3.0);
  // on "never come": the gold drains out of each star and it drops
  tl.fromTo(".{p}-bsg", {{ opacity: 1 }}, {{ opacity: 0, duration: 0.12, stagger: 0.14, immediateRender: false }}, 3.85);
  tl.to(".{p}-bs", {{ y: 34, rotation: (i) => (i % 2 ? 9 : -9), duration: 0.35, stagger: 0.14, ease: "power2.in" }}, 3.85);
  tl.fromTo("#{p}-zero", {{ opacity: 0, y: 20 }}, {{ opacity: 1, y: 0, duration: 0.35, ease: "power3.out" }}, 4.55);
  impact(4.58, 0.5);

  // ---- Scene D (5.05–7.95): every gap = a customer lost ------------------------
  tl.fromTo("#{p}-sc3", {{ opacity: 1, scale: 1 }}, {{ opacity: 0, scale: 1.25, filter: "blur(20px)", duration: 0.14, ease: "power2.in", immediateRender: false }}, 5.0);
  tl.set("#{p}-sd", {{ opacity: 1 }}, 5.1);
  tl.set("#{p}-alarm", {{ opacity: 0 }}, 5.1);
  impact(5.12, 1);
  slam("#{p}-gapw", 5.12);
  tl.to("#{p}-gapw", {{ y: -130, scale: 0.6, duration: 0.5, ease: "power3.inOut" }}, 5.75);
  tl.fromTo("#{p}-cust", {{ scale: 0, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.45, ease: "back.out(2)" }}, 6.0);
  tl.fromTo("#{p}-store", {{ x: 160, opacity: 0 }}, {{ x: 0, opacity: 1, duration: 0.4, ease: "power3.out" }}, 6.5);
  tl.fromTo("#{p}-pl", {{ strokeDashoffset: 600, opacity: 0 }}, {{ strokeDashoffset: 0, opacity: 1, duration: 0.4, ease: "none" }}, 6.55);
  tl.to("#{p}-cl", {{ opacity: 0, duration: 0.15 }}, 6.85);
  tl.to("#{p}-cust", {{ x: 700, scale: 0.35, duration: 0.5, ease: "power3.in" }}, 6.85);
  tl.to("#{p}-cust", {{ opacity: 0, duration: 0.08 }}, 7.33);
  tl.set("#{p}-gapw", {{ opacity: 0 }}, 7.3);
  slam("#{p}-lostw", 7.3);
  tl.fromTo("#{p}-rflash", {{ opacity: 0.7 }}, {{ opacity: 0, duration: 0.4, ease: "power2.out", immediateRender: false }}, 7.3);
  tl.fromTo("#{p}-store", {{ scale: 1.25 }}, {{ scale: 1, duration: 0.4, ease: "expo.out", immediateRender: false }}, 7.32);
  tl.fromTo("#{p}-alarm", {{ opacity: 0 }}, {{ opacity: 0.8, duration: 0.3, immediateRender: false }}, 7.3);
  tl.fromTo("#{p}-punch", {{ scale: 1 }}, {{ scale: 1.05, duration: 0.6, ease: "power2.in", immediateRender: false }}, 7.35);
""",
)

# ---------------- Frame 2 — intro ----------------
p = "f2"
disc_keys = [("leads", "target"), ("rec", "phone"), ("rep", "star"), ("soc", "camera"), ("web", "globe")]
discs = "".join(
    f'<div class="{p}-rd" style="left:{115 + i * 170}px; background:{C[k]}; box-shadow: 0 0 0 8px {C[k]}26, 0 0 40px {C[k]}88;">{ICONS[ic]}</div>'
    for i, (k, ic) in enumerate(disc_keys)
)
frames[("02-intro", 2, 8.65)] = (
    f"""
.{p}-bloom {{ position: absolute; left: 360px; top: 80px; width: 1200px; height: 800px; border-radius: 50%;
  background: radial-gradient(circle, rgba(46,168,255,0.35) 0%, rgba(46,168,255,0) 65%); }}
.{p}-eyebrow {{ position: absolute; left: 0; right: 0; top: 250px; text-align: center; font: 700 50px "Space Grotesk", sans-serif;
  letter-spacing: 0.02em; text-transform: uppercase; }}
.{p}-title {{ position: absolute; left: 0; right: 0; top: 320px; text-align: center; font: 700 200px "Space Grotesk", sans-serif;
  letter-spacing: -0.01em; line-height: 1; color: {C['blue']}; text-shadow: 0 0 60px rgba(46,168,255,0.55), 0 6px 0 rgba(10,60,140,0.6); }}
.{p}-chips {{ position: absolute; left: 0; right: 0; top: 560px; display: flex; justify-content: center; gap: 22px; }}
.{p}-c {{ color: {C['text']}; border: 1.5px solid rgba(46,168,255,0.5); background: rgba(46,168,255,0.12); font-size: 30px; }}
.{p}-rd {{ position: absolute; top: 700px; width: 110px; height: 110px; border-radius: 50%; padding: 26px; }}
.{p}-rd svg {{ width: 100%; height: 100%; display: block; }}
.{p}-line {{ position: absolute; left: 615px; top: 755px; width: 680px; height: 3px; background: linear-gradient(90deg, {C['leads']}, {C['rec']}, {C['rep']}, {C['soc']}, {C['web']}); transform-origin: 50% 50%; opacity: 0.6; }}
""",
    f"""
        <div class="{p}-bloom" id="{p}-bloom"></div>
        <div class="{p}-eyebrow">{typed(p, f'{p}-eb', 'Meet your A.I. Client Acquisition')}</div>
        <div class="{p}-title" id="{p}-title">SUPER SUITE</div>
        <div class="{p}-chips">
          <div class="{p}-chip {p}-c" id="{p}-c1">Attract</div>
          <div class="{p}-chip {p}-c" id="{p}-c2">Convert</div>
          <div class="{p}-chip {p}-c" id="{p}-c3">Retain</div>
        </div>
        <div class="{p}-line" id="{p}-line"></div>
        {discs}
""",
    f"""
  tl.fromTo("#{p}-bloom", {{ scale: 0.2, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.9, ease: "expo.out" }}, 0);
  {type_js(f'{p}-eb', 0.3, 1.5)}
  tl.fromTo("#{p}-title", {{ scale: 0.55, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.7, ease: "back.out(1.6)" }}, 2.55);
  tl.fromTo("#{p}-line", {{ scaleX: 0 }}, {{ scaleX: 1, duration: 0.6, ease: "power3.out" }}, 3.75);
  tl.fromTo(".{p}-rd", {{ scale: 0, opacity: 0, y: -120 }}, {{ scale: 1, opacity: 1, y: 0, duration: 0.6, stagger: 0.12, ease: "back.out(1.8)" }}, 3.8);
  tl.fromTo("#{p}-c1", {{ y: 24, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.45, ease: "power3.out" }}, 5.4);
  tl.fromTo("#{p}-c2", {{ y: 24, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.45, ease: "power3.out" }}, 6.2);
  tl.fromTo("#{p}-c3", {{ y: 24, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.45, ease: "power3.out" }}, 7.05);
  tl.fromTo(".{p}-cam", {{ scale: 1 }}, {{ scale: 1.04, duration: DUR, ease: "none" }}, 0);
""",
)

# ---------------- Frame 3 — leads ----------------
p = "f3"
leads = [("HVAC Repair", "J", "#2E8BFF"), ("Roofing Estimate", "M", "#F97316"), ("Med Spa Inquiry", "A", "#EC4899"), ("Chiropractic Care", "D", "#22C55E")]
cards = "".join(
    f"""<div class="{p}-card" id="{p}-card{i}"><div class="{p}-av" style="background:{col}">{ini}</div>
      <div class="{p}-ct"><div class="{p}-cn">New Lead</div><div class="{p}-cs">{name}</div></div>
      <div class="{p}-q" id="{p}-q{i}">Qualified</div><div class="{p}-check">{ICONS['check']}</div></div>"""
    for i, (name, ini, col) in enumerate(leads)
)
frames[("03-leads", 3, 5.58)] = (
    left_css(p, C["leads"]) + f"""
.{p}-panel {{ position: absolute; left: 960px; top: 150px; width: 780px; height: 700px; padding: 34px 36px; }}
.{p}-ph {{ display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 26px; }}
.{p}-pt {{ font: 700 36px "Space Grotesk", sans-serif; }}
.{p}-pc {{ font: 700 30px "Space Grotesk", sans-serif; color: {C['green']}; }}
.{p}-card {{ display: flex; align-items: center; gap: 22px; background: rgba(255,255,255,0.95); color: #0B1530; border-radius: 16px;
  padding: 18px 24px; margin-bottom: 18px; height: 116px; }}
.{p}-av {{ width: 72px; height: 72px; border-radius: 50%; color: #fff; font: 700 32px "Space Grotesk", sans-serif;
  display: flex; align-items: center; justify-content: center; flex: none; }}
.{p}-ct {{ flex: 1; }}
.{p}-cn {{ font: 700 30px "Inter", sans-serif; }}
.{p}-cs {{ font: 500 24px "Inter", sans-serif; color: #4B5A7A; margin-top: 4px; }}
.{p}-q {{ font: 700 18px "Inter", sans-serif; color: #fff; background: {C['leads']}; padding: 6px 14px; border-radius: 100px; letter-spacing: 0.04em; }}
.{p}-ring {{ position: absolute; left: 204px; top: 294px; width: 0; height: 0; }}
.{p}-r {{ position: absolute; left: -70px; top: -70px; width: 140px; height: 140px; border-radius: 50%; border: 3px solid {C['leads']}; }}
""",
    f"""
        <div class="{p}-ring">{''.join(f'<div class="{p}-r"></div>' for _ in range(3))}</div>
{left_html(p, 3).replace('__BENEFIT__', 'Qualified prospects')}
        <div class="{p}-panel {p}-glass" id="{p}-panel">
          <div class="{p}-ph"><div class="{p}-pt">New Leads</div><div class="{p}-pc">+<span id="{p}-count">0</span> this week</div></div>
          {cards}
        </div>
""",
    left_js(p, 3.9) + f"""
  tl.fromTo("#{p}-panel", {{ x: 80, opacity: 0 }}, {{ x: 0, opacity: 1, duration: 0.7, ease: "power3.out" }}, 0.85);
  tl.fromTo(".{p}-r", {{ scale: 0.6, opacity: 0.9 }}, {{ scale: 5, opacity: 0, duration: 1.2, stagger: 0.3, ease: "power2.out" }}, 1.0);
  tl.fromTo(".{p}-card", {{ y: 40, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.5, stagger: 0.3, ease: "power3.out" }}, 2.5);
  tl.fromTo(".{p}-card .{p}-check", {{ scale: 0 }}, {{ scale: 1, duration: 0.35, stagger: 0.3, ease: "back.out(2.2)" }}, 2.8);
  {counter_js(f'#{p}-count', 0, 24, 2.5, 1.4)}
  tl.fromTo(".{p}-q", {{ scale: 0.5, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.35, stagger: 0.12, ease: "back.out(2)" }}, 4.2);
""",
)

# ---------------- Frame 4 — receptionist ----------------
p = "f4"
frames[("04-receptionist", 4, 6.9)] = (
    left_css(p, C["rec"]) + f"""
.{p}-phone {{ position: absolute; left: 1000px; top: 110px; width: 380px; height: 760px; border-radius: 56px; background: #0A0F22;
  border: 10px solid #1B2547; box-shadow: 0 40px 90px rgba(0,0,0,0.55), 0 0 0 1.5px rgba(46,168,255,0.3); overflow: hidden; }}
.{p}-notch {{ position: absolute; left: 120px; top: 14px; width: 120px; height: 30px; border-radius: 20px; background: #1B2547; }}
.{p}-incoming {{ position: absolute; left: 0; right: 0; top: 90px; text-align: center; font: 600 24px "Inter", sans-serif; color: {C['muted']}; }}
.{p}-avwrap {{ position: absolute; left: 110px; top: 150px; width: 140px; height: 140px; }}
.{p}-rip {{ position: absolute; inset: 0; border-radius: 50%; border: 3px solid {C['rec']}; }}
.{p}-av {{ position: absolute; inset: 0; border-radius: 50%; background: linear-gradient(140deg, #34D399, #059669); padding: 34px; }}
.{p}-av svg {{ width: 100%; height: 100%; display: block; }}
.{p}-name {{ position: absolute; left: 0; right: 0; top: 312px; text-align: center; font: 700 30px "Space Grotesk", sans-serif; }}
.{p}-status {{ position: absolute; left: 0; right: 0; top: 356px; text-align: center; font: 600 22px "Inter", sans-serif; color: {C['rec']}; }}
.{p}-b {{ position: absolute; max-width: 280px; padding: 14px 18px; border-radius: 20px; font: 600 21px "Inter", sans-serif; line-height: 1.3; }}
.{p}-b1 {{ left: 22px; top: 420px; background: #1E2A52; border-bottom-left-radius: 6px; }}
.{p}-b2 {{ right: 22px; top: 510px; background: {C['rec']}; color: #04210F; border-bottom-right-radius: 6px; }}
.{p}-btns {{ position: absolute; left: 0; right: 0; top: 640px; display: flex; justify-content: center; gap: 60px; }}
.{p}-btn {{ width: 72px; height: 72px; border-radius: 50%; padding: 18px; }}
.{p}-btn svg {{ width: 100%; height: 100%; display: block; }}
.{p}-247 {{ position: absolute; left: 1330px; top: 140px; width: 150px; height: 150px; border-radius: 50%; background: {C['rec']};
  color: #04210F; font: 700 48px "Space Grotesk", sans-serif; display: flex; align-items: center; justify-content: center;
  box-shadow: 0 0 50px rgba(34,197,94,0.6); }}
.{p}-book {{ position: absolute; left: 1420px; top: 560px; width: 380px; padding: 24px 26px; background: #fff; color: #0B1530; border-radius: 20px;
  box-shadow: 0 30px 70px rgba(0,0,0,0.5); display: flex; gap: 18px; align-items: center; }}
.{p}-bookic {{ width: 64px; height: 64px; border-radius: 16px; background: {C['rec']}; padding: 14px; flex: none; }}
.{p}-bookic svg {{ width: 100%; height: 100%; display: block; }}
.{p}-bt1 {{ font: 700 26px "Inter", sans-serif; }}
.{p}-bt2 {{ font: 500 22px "Inter", sans-serif; color: #4B5A7A; margin-top: 4px; }}
""",
    f"""
{left_html(p, 4).replace('__BENEFIT__', 'Never miss a call')}
        <div class="{p}-phone" id="{p}-phone">
          <div class="{p}-notch"></div>
          <div class="{p}-incoming" id="{p}-inc">Incoming call…</div>
          <div class="{p}-avwrap"><div class="{p}-rip"></div><div class="{p}-rip"></div><div class="{p}-av">{ICONS['headset']}</div></div>
          <div class="{p}-name">AI Receptionist</div>
          <div class="{p}-status" id="{p}-status">Connected · answering</div>
          <div class="{p}-b {p}-b1" id="{p}-b1">Do you service AC units?</div>
          <div class="{p}-b {p}-b2" id="{p}-b2">Yes! How can I help you today?</div>
          <div class="{p}-btns"><div class="{p}-btn" style="background:#EF4444">{ICONS['phone']}</div><div class="{p}-btn" id="{p}-accept" style="background:{C['rec']}">{ICONS['phone']}</div></div>
        </div>
        <div class="{p}-247" id="{p}-247">24/7</div>
        <div class="{p}-book" id="{p}-book"><div class="{p}-bookic">{ICONS['cal']}</div><div><div class="{p}-bt1">Appointment booked</div><div class="{p}-bt2">Tue · 9:00 AM</div></div><div class="{p}-check" style="margin-left:auto">{ICONS['check']}</div></div>
""",
    left_js(p, 5.5) + f"""
  tl.fromTo("#{p}-phone", {{ y: 160, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.8, ease: "power3.out" }}, 0.6);
  tl.fromTo(".{p}-rip", {{ scale: 1, opacity: 0.9 }}, {{ scale: 1.7, opacity: 0, duration: 0.8, stagger: 0.35, ease: "power2.out" }}, 0.8);
  pulse("#{p}-accept", {{ scale: 1 }}, {{ scale: 1.25 }}, 1.55, 0.15);
  tl.fromTo("#{p}-inc", {{ opacity: 1 }}, {{ opacity: 0, duration: 0.2 }}, 1.6);
  tl.fromTo("#{p}-status", {{ opacity: 0, y: 10 }}, {{ opacity: 1, y: 0, duration: 0.35, ease: "power3.out" }}, 1.65);
  tl.fromTo("#{p}-247", {{ scale: 0, rotation: -20 }}, {{ scale: 1, rotation: 0, duration: 0.55, ease: "back.out(1.9)" }}, 2.9);
  tl.fromTo("#{p}-b1", {{ y: 20, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.4, ease: "power3.out" }}, 3.95);
  tl.fromTo("#{p}-b2", {{ y: 20, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.4, ease: "power3.out" }}, 4.6);
  tl.fromTo("#{p}-book", {{ x: 60, opacity: 0, scale: 0.9 }}, {{ x: 0, opacity: 1, scale: 1, duration: 0.55, ease: "back.out(1.5)" }}, 5.45);
""",
)

# ---------------- Frame 5 — reputation ----------------
p = "f5"
gold_star = ICONS["star"].replace('fill="none" stroke="#fff"', 'fill="#FBBF24" stroke="#FBBF24"')
grey_star = ICONS["star"].replace('fill="none" stroke="#fff"', 'fill="none" stroke="#CBD2E1"')
frames[("05-reputation", 5, 7.12)] = (
    left_css(p, C["rep"]) + f"""
.{p}-review {{ position: absolute; left: 960px; top: 140px; width: 800px; padding: 34px 38px; background: #fff; color: #0B1530;
  border-radius: 24px; box-shadow: 0 40px 90px rgba(0,0,0,0.5), 0 0 60px rgba(139,92,246,0.35); }}
.{p}-rh {{ display: flex; justify-content: space-between; align-items: center; }}
.{p}-src {{ font: 700 26px "Inter", sans-serif; color: #4B5A7A; }}
.{p}-score {{ font: 700 44px "Space Grotesk", sans-serif; color: #0B1530; }}
.{p}-mini {{ display: inline-block; width: 36px; height: 36px; margin-left: 6px; vertical-align: -3px; }}
.{p}-mini svg {{ width: 100%; height: 100%; display: block; }}
.{p}-score small {{ font: 600 22px "Inter", sans-serif; color: #4B5A7A; margin-left: 10px; }}
.{p}-stars {{ position: relative; display: flex; gap: 12px; margin-top: 22px; height: 64px; }}
.{p}-st {{ position: relative; width: 64px; height: 64px; }}
.{p}-st svg {{ position: absolute; inset: 0; width: 64px; height: 64px; }}
.{p}-quote {{ margin-top: 22px; font: 700 40px "Space Grotesk", sans-serif; line-height: 1.2; }}
.{p}-who {{ margin-top: 14px; font: 500 22px "Inter", sans-serif; color: #4B5A7A; }}
.{p}-bad {{ position: absolute; left: 960px; top: 600px; width: 470px; padding: 22px 26px; background: #1A2346; border: 1.5px solid rgba(239,68,68,0.5);
  border-radius: 18px; }}
.{p}-badstars {{ display: flex; gap: 6px; }}
.{p}-badstars svg {{ width: 30px; height: 30px; }}
.{p}-badtxt {{ margin-top: 10px; font: 600 24px "Inter", sans-serif; color: {C['muted']}; }}
.{p}-inbox {{ position: absolute; left: 1520px; top: 590px; width: 240px; height: 170px; border-radius: 20px; background: rgba(139,92,246,0.18);
  border: 2px solid {C['rep']}; text-align: center; padding-top: 26px; }}
.{p}-lock {{ width: 60px; height: 60px; margin: 0 auto; border-radius: 50%; background: {C['rep']}; padding: 14px; }}
.{p}-lock svg {{ width: 100%; height: 100%; display: block; }}
.{p}-ibt {{ margin-top: 14px; font: 700 22px "Space Grotesk", sans-serif; letter-spacing: 0.04em; }}
.{p}-arrow {{ position: absolute; left: 1430px; top: 640px; width: 90px; height: 60px; }}
""",
    f"""
{left_html(p, 5).replace('__BENEFIT__', 'More 5-star reviews')}
        <div class="{p}-review" id="{p}-review">
          <div class="{p}-rh"><div class="{p}-src">Google Reviews</div><div class="{p}-score"><span id="{p}-score">4.1</span><span class="{p}-mini">{gold_star}</span><small><span id="{p}-cnt">38</span> reviews</small></div></div>
          <div class="{p}-stars">{''.join(f'<div class="{p}-st">{grey_star}<span class="{p}-gs">{gold_star}</span></div>' for _ in range(5))}</div>
          <div class="{p}-quote">{typed(p, f'{p}-qt', '“Amazing service! Highly recommend!”')}</div>
          <div class="{p}-who">— Sarah K., homeowner</div>
        </div>
        <div class="{p}-bad" id="{p}-bad"><div class="{p}-badstars">{gold_star*2}{grey_star*3}</div><div class="{p}-badtxt">“Technician was late…”</div></div>
        <svg class="{p}-arrow" id="{p}-arrow" viewBox="0 0 90 60" fill="none" stroke="#8B5CF6" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"><path id="{p}-ap" d="M4 30 H78 M60 12 L80 30 L60 48"/></svg>
        <div class="{p}-inbox" id="{p}-inbox"><div class="{p}-lock">{ICONS['lock']}</div><div class="{p}-ibt">Resolve privately</div></div>
""",
    left_js(p, 6.1) + f"""
  tl.fromTo("#{p}-review", {{ y: 80, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.7, ease: "power3.out" }}, 1.2);
  tl.fromTo(".{p}-gs", {{ opacity: 0, scale: 0.3 }}, {{ opacity: 1, scale: 1, duration: 0.3, stagger: 0.14, ease: "back.out(2.4)", transformOrigin: "50% 50%" }}, 2.0);
  {type_js(f'{p}-qt', 2.75, 0.8)}
  {counter_js(f'#{p}-score', 4.1, 4.9, 2.0, 1.6, 1)}
  {counter_js(f'#{p}-cnt', 38, 127, 2.0, 1.6)}
  tl.fromTo("#{p}-bad", {{ y: 40, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.5, ease: "power3.out" }}, 3.85);
  tl.fromTo("#{p}-inbox", {{ scale: 0.7, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.45, ease: "back.out(1.8)" }}, 4.3);
  tl.fromTo("#{p}-arrow", {{ opacity: 0, x: -20 }}, {{ opacity: 1, x: 0, duration: 0.35, ease: "power3.out" }}, 4.35);
  tl.fromTo("#{p}-bad", {{ x: 0, scale: 1, opacity: 1 }}, {{ x: 600, scale: 0.35, opacity: 0, duration: 0.7, ease: "power3.in", immediateRender: false }}, 5.05);
  pulse("#{p}-inbox", {{ scale: 1 }}, {{ scale: 1.08 }}, 5.72, 0.15);
""",
)

# ---------------- Frame 6 — social ----------------
p = "f6"
posts = [
    ("Spring tune-up special", '<svg viewBox="0 0 200 180"><rect x="30" y="40" width="140" height="120" rx="10" fill="#CBD5E1"/><circle cx="100" cy="100" r="44" fill="#94A3B8"/><g stroke="#E2E8F0" stroke-width="5">' + "".join(f'<line x1="{60+i*16}" y1="62" x2="{60+i*16}" y2="138"/>' for i in range(6)) + '</g><rect x="20" y="152" width="160" height="10" rx="5" fill="#64748B"/></svg>', "#1E3A8A"),
    ("Meet our team", '<svg viewBox="0 0 200 180"><circle cx="100" cy="66" r="34" fill="#F1C7A5"/><path d="M62 52 Q100 18 138 52 L138 46 Q100 10 62 46 Z" fill="#1E3A8A"/><rect x="58" y="40" width="84" height="14" rx="7" fill="#1E3A8A"/><path d="M40 180 Q40 112 100 108 Q160 112 160 180 Z" fill="#2563EB"/><circle cx="88" cy="70" r="3.5" fill="#3B2A1A"/><circle cx="112" cy="70" r="3.5" fill="#3B2A1A"/><path d="M88 84 Q100 94 112 84" stroke="#3B2A1A" stroke-width="3" fill="none"/></svg>', "#0F766E"),
    ("Another happy home", '<svg viewBox="0 0 200 180"><path d="M30 90 L100 34 L170 90 Z" fill="#7C2D12"/><rect x="44" y="88" width="112" height="76" fill="#E7D7C1"/><rect x="88" y="116" width="26" height="48" fill="#7C5A3A"/><rect x="56" y="104" width="22" height="20" fill="#93C5FD"/><rect x="124" y="104" width="22" height="20" fill="#93C5FD"/><rect x="0" y="162" width="200" height="18" fill="#4D7C0F"/></svg>', "#9A3412"),
]
post_html = "".join(
    f"""<div class="{p}-post" style="left:{870 + i * 310}px"><div class="{p}-img" style="background:linear-gradient(160deg,{bg},#0B1530)">{svg}</div>
      <div class="{p}-cap"><div class="{p}-brand"></div>{cap}</div></div>"""
    for i, (cap, svg, bg) in enumerate(posts)
)
plats = [("#1877F2", '<span style="font:900 46px Inter">f</span>'), ("linear-gradient(135deg,#F58529,#DD2A7B,#8134AF)", ICONS["camera"]),
         ("#0A66C2", '<span style="font:700 38px Inter">in</span>'), ("#111111", '<svg viewBox="0 0 24 24"><path d="M14 3 c0.5 2.6 2.3 4.2 5 4.4 v3.2 c-1.9 0 -3.6 -0.6 -5 -1.6 V16 a5 5 0 1 1 -5 -5 v3.3 a1.8 1.8 0 1 0 1.8 1.8 V3 Z" fill="#fff"/></svg>'),
         ("#FF0000", '<svg viewBox="0 0 24 24"><path d="M9 7 L17 12 L9 17 Z" fill="#fff"/></svg>')]
plat_html = "".join(
    f'<div class="{p}-pl" style="left:{900 + i * 170}px"><div class="{p}-plic" style="background:{bg}">{ic}</div><div class="{p}-tick"><div class="{p}-check">{ICONS["check"]}</div></div></div>'
    for i, (bg, ic) in enumerate(plats)
)
frames[("06-social", 6, 5.92)] = (
    left_css(p, C["soc"]) + f"""
.{p}-post {{ position: absolute; top: 150px; width: 290px; height: 400px; border-radius: 20px; overflow: hidden; background: #fff;
  box-shadow: 0 30px 70px rgba(0,0,0,0.5); }}
.{p}-img {{ height: 300px; padding: 30px 30px 0; }}
.{p}-img svg {{ width: 100%; height: 100%; display: block; }}
.{p}-cap {{ height: 100px; padding: 18px 20px; color: #0B1530; font: 700 22px "Inter", sans-serif; line-height: 1.25; display: flex; gap: 12px; align-items: center; }}
.{p}-brand {{ width: 14px; height: 54px; border-radius: 7px; background: {C['blue']}; flex: none; }}
.{p}-pl {{ position: absolute; top: 620px; width: 110px; height: 150px; }}
.{p}-plic {{ width: 100px; height: 100px; border-radius: 26px; display: flex; align-items: center; justify-content: center; color: #fff; padding: 22px; }}
.{p}-plic svg {{ width: 100%; height: 100%; display: block; }}
.{p}-tick {{ position: absolute; left: 70px; top: -10px; }}
""",
    f"""
{left_html(p, 6).replace('__BENEFIT__', 'Builds trust')}
        {post_html}
        {plat_html}
""",
    left_js(p, 5.05) + f"""
  tl.fromTo(".{p}-post", {{ y: 70, opacity: 0, rotation: 3 }}, {{ y: 0, opacity: 1, rotation: 0, duration: 0.6, stagger: 0.3, ease: "power3.out" }}, 1.6);
  tl.fromTo(".{p}-plic", {{ scale: 0, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.4, stagger: 0.12, ease: "back.out(2)" }}, 2.75);
  tl.fromTo(".{p}-tick", {{ scale: 0 }}, {{ scale: 1, duration: 0.3, stagger: 0.18, ease: "back.out(2.4)" }}, 3.65);
""",
)

# ---------------- Frame 7 — website ----------------
p = "f7"
svc = "".join(
    f'<div class="{p}-svc"><div class="{p}-svcic">{ic}</div>{name}</div>'
    for name, ic in [
        ("HVAC", '<svg viewBox="0 0 24 24" fill="none" stroke="#1D4ED8" stroke-width="2.2" stroke-linecap="round"><path d="M12 2 v20 M3.3 7 l17.4 10 M3.3 17 l17.4 -10"/></svg>'),
        ("Plumbing", '<svg viewBox="0 0 24 24"><path d="M12 2 C8 8 5.5 11 5.5 14.5 a6.5 6.5 0 0 0 13 0 C18.5 11 16 8 12 2 Z" fill="#1D4ED8"/></svg>'),
        ("Electrical", '<svg viewBox="0 0 24 24"><path d="M13 2 L4 14 h7 l-1 8 9 -12 h-7 Z" fill="#1D4ED8"/></svg>'),
        ("Roofing", '<svg viewBox="0 0 24 24" fill="none" stroke="#1D4ED8" stroke-width="2.2" stroke-linejoin="round"><path d="M3 11 L12 3 L21 11 M6 9 V21 H18 V9"/></svg>'),
    ]
)
frames[("07-website", 7, 6.86)] = (
    left_css(p, C["web"]) + f"""
.{p}-browser {{ position: absolute; left: 860px; top: 150px; width: 940px; height: 640px; border-radius: 20px; overflow: hidden; background: #fff;
  box-shadow: 0 40px 90px rgba(0,0,0,0.55), 0 0 0 1.5px rgba(56,189,248,0.4); }}
.{p}-bar {{ height: 50px; background: #E8EDF5; display: flex; align-items: center; gap: 10px; padding: 0 18px; }}
.{p}-dot {{ width: 14px; height: 14px; border-radius: 50%; }}
.{p}-url {{ margin-left: 18px; flex: 1; height: 30px; border-radius: 8px; background: #fff; font: 500 18px "Inter", sans-serif; color: #4B5A7A; padding: 4px 14px; }}
.{p}-view {{ position: absolute; left: 0; right: 0; top: 50px; bottom: 0; overflow: hidden; }}
.{p}-page {{ position: absolute; left: 0; right: 0; top: 0; }}
.{p}-nav {{ height: 70px; display: flex; align-items: center; padding: 0 30px; gap: 26px; border-bottom: 1px solid #E2E8F0; }}
.{p}-logo {{ font: 700 26px "Space Grotesk", sans-serif; color: #0B1530; margin-right: auto; }}
.{p}-tab {{ font: 600 19px "Inter", sans-serif; color: #334155; padding: 6px 12px; border-radius: 8px; }}
.{p}-hero {{ height: 330px; background: linear-gradient(120deg, #0B2A5B, #1D4ED8); display: flex; align-items: center; padding: 0 40px; gap: 20px; }}
.{p}-ht {{ width: 470px; color: #fff; font: 700 40px "Space Grotesk", sans-serif; line-height: 1.12; }}
.{p}-cta {{ display: inline-block; margin-top: 24px; background: #F59E0B; color: #1F1300 !important; color: #fff; font: 700 22px "Inter", sans-serif; padding: 14px 28px; border-radius: 10px; }}
.{p}-van {{ width: 340px; height: 200px; }}
.{p}-svcs {{ display: flex; gap: 18px; padding: 30px; }}
.{p}-svc {{ flex: 1; height: 140px; border: 1.5px solid #E2E8F0; border-radius: 14px; text-align: center; font: 700 22px "Inter", sans-serif; color: #0B1530; padding-top: 22px; }}
.{p}-svcic {{ width: 44px; height: 44px; margin: 0 auto 12px; }}
.{p}-svcic svg {{ width: 100%; height: 100%; display: block; }}
.{p}-badge {{ position: absolute; left: 1640px; color: #04121F; background: {C['web']}; box-shadow: 0 0 40px rgba(56,189,248,0.6); display: flex; gap: 10px; align-items: center; }}
.{p}-badge .{p}-check {{ width: 30px; height: 30px; padding: 5px; background: #04121F; }}
.{p}-cursor {{ position: absolute; left: 0; top: 0; width: 44px; height: 44px; }}
.{p}-cursor svg {{ width: 100%; height: 100%; display: block; }}
.{p}-toast {{ position: absolute; left: 1290px; top: 808px; padding: 18px 24px; background: #0B1530; border: 1.5px solid {C['green']}; border-radius: 14px;
  font: 700 22px "Inter", sans-serif; display: flex; gap: 12px; align-items: center; box-shadow: 0 20px 50px rgba(0,0,0,0.5); }}
""",
    f"""
{left_html(p, 7).replace('__BENEFIT__', 'Designed to convert')}
        <div class="{p}-browser" id="{p}-browser">
          <div class="{p}-bar"><div class="{p}-dot" style="background:#F87171"></div><div class="{p}-dot" style="background:#FBBF24"></div><div class="{p}-dot" style="background:#34D399"></div><div class="{p}-url">yourbusiness.com</div></div>
          <div class="{p}-view" data-layout-allow-overflow data-layout-allow-occlusion><div class="{p}-page" id="{p}-page">
            <div class="{p}-nav"><div class="{p}-logo">ComfortPro</div>{''.join(f'<div class="{p}-tab">{t}</div>' for t in ['Home','Services','About','Reviews','Contact'])}</div>
            <div class="{p}-hero"><div><div class="{p}-ht">Trusted Local Experts for a More Comfortable Home.</div><div class="{p}-cta" id="{p}-cta">Get a Quote</div></div>
              <svg class="{p}-van" viewBox="0 0 340 200"><rect x="20" y="40" width="210" height="110" rx="12" fill="#F8FAFC"/><path d="M230 70 H285 L320 110 V150 H230 Z" fill="#E2E8F0"/><rect x="246" y="80" width="40" height="30" rx="4" fill="#93C5FD"/><rect x="40" y="70" width="150" height="14" rx="7" fill="#2EA8FF"/><rect x="40" y="94" width="100" height="10" rx="5" fill="#94A3B8"/><circle cx="80" cy="155" r="22" fill="#0B1530"/><circle cx="270" cy="155" r="22" fill="#0B1530"/><circle cx="80" cy="155" r="9" fill="#94A3B8"/><circle cx="270" cy="155" r="9" fill="#94A3B8"/></svg>
            </div>
            <div class="{p}-svcs">{svc}</div>
          </div></div>
        </div>
        <div class="{p}-chip {p}-badge" id="{p}-seo" style="top:330px"><div class="{p}-check">{ICONS['check']}</div>SEO ready</div>
        <div class="{p}-chip {p}-badge" id="{p}-aeo" style="top:420px"><div class="{p}-check">{ICONS['check']}</div>AEO ready</div>
        <div class="{p}-toast" id="{p}-toast"><div class="{p}-check">{ICONS['check']}</div>New quote request</div>
        <div class="{p}-cursor" id="{p}-cursor">{ICONS['cursor']}</div>
""",
    left_js(p, 5.9) + f"""
  tl.fromTo("#{p}-browser", {{ y: 90, opacity: 0, rotationX: 8 }}, {{ y: 0, opacity: 1, rotationX: 0, duration: 0.8, ease: "power3.out" }}, 0.9);
  tl.fromTo(".{p}-tab", {{ backgroundColor: "rgba(46,168,255,0)", color: "#334155" }}, {{ backgroundColor: "rgba(46,168,255,0.16)", color: "#1D4ED8", duration: 0.25, stagger: 0.25 }}, 1.75);
  tl.fromTo("#{p}-seo", {{ scale: 0, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.45, ease: "back.out(2)" }}, 3.4);
  tl.fromTo("#{p}-aeo", {{ scale: 0, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.45, ease: "back.out(2)" }}, 4.0);
  tl.fromTo("#{p}-cursor", {{ x: 1700, y: 900, opacity: 0 }}, {{ x: 975, y: 500, opacity: 1, duration: 0.7, ease: "power3.out" }}, 5.0);
  pulse("#{p}-cursor", {{ scale: 1 }}, {{ scale: 0.85 }}, 5.8, 0.1);
  pulse("#{p}-cta", {{ scale: 1 }}, {{ scale: 0.93 }}, 5.8, 0.1);
  tl.fromTo("#{p}-toast", {{ y: 30, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.45, ease: "back.out(1.6)" }}, 6.0);
""",
)

# ---------------- Frame 8 — CTA ----------------
p = "f8"
row = "".join(
    f'<div class="{p}-d" style="left:{115 + i * 170}px; background:{C[k]}; box-shadow: 0 0 0 8px {C[k]}26, 0 0 40px {C[k]}88;">{ICONS[ic]}</div>'
    for i, (k, ic) in enumerate(disc_keys)
)
frames[("08-cta", 8, 4.32)] = (
    f"""
.{p}-banner {{ position: absolute; left: 260px; top: 110px; width: 1400px; height: 690px; background: url("assets/super-suite-banner.png") center / cover; border-radius: 24px; filter: blur(3px); }}
.{p}-label {{ position: absolute; left: 0; right: 0; top: 280px; text-align: center; font: 700 64px "Space Grotesk", sans-serif; letter-spacing: 0.06em; }}
.{p}-l2 {{ color: {C['blue']}; }}
.{p}-d {{ position: absolute; top: 420px; width: 110px; height: 110px; border-radius: 50%; padding: 26px; }}
.{p}-d svg {{ width: 100%; height: 100%; display: block; }}
.{p}-pill {{ position: absolute; left: 540px; top: 410px; width: 840px; height: 140px; border-radius: 100px;
  background: linear-gradient(90deg, #6D28D9, #8B5CF6); box-shadow: 0 0 0 2px rgba(255,255,255,0.25) inset, 0 0 80px rgba(123,63,242,0.7);
  display: flex; align-items: center; justify-content: center; font: 700 58px "Space Grotesk", sans-serif; white-space: nowrap; }}
.{p}-arr {{ width: 54px; height: 54px; margin-left: 22px; flex: none; }}
.{p}-rip {{ position: absolute; left: 1150px; top: 500px; width: 0; height: 0; }}
.{p}-ripc {{ position: absolute; left: -60px; top: -60px; width: 120px; height: 120px; border-radius: 50%; border: 4px solid #fff; opacity: 0; }}
.{p}-cursor {{ position: absolute; left: 0; top: 0; width: 56px; height: 56px; }}
.{p}-cursor svg {{ width: 100%; height: 100%; display: block; }}
.{p}-url {{ position: absolute; left: 0; right: 0; top: 640px; text-align: center; font: 600 34px "Inter", sans-serif; color: {C['muted']}; letter-spacing: 0.02em; }}
""",
    f"""
        <div class="{p}-banner" id="{p}-banner"></div>
        <div class="{p}-label" data-layout-allow-overlap id="{p}-l1">5 SYSTEMS</div>
        <div class="{p}-label {p}-l2" data-layout-allow-overlap id="{p}-l2">1 SUITE</div>
        {row}
        <div class="{p}-pill" id="{p}-pill">{typed(p, f'{p}-pt', 'Discover the Suite')}<svg class="{p}-arr" id="{p}-arr" viewBox="0 0 40 40" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"><path d="M6 20 H32 M22 9 L33 20 L22 31"/></svg></div>
        <div class="{p}-rip"><div class="{p}-ripc" id="{p}-ripc"></div></div>
        <div class="{p}-url" id="{p}-url">TrainorMediaNetwork.com</div>
        <div class="{p}-cursor" id="{p}-cursor">{ICONS['cursor']}</div>
""",
    f"""
  tl.fromTo(".{p}-d", {{ y: 60, opacity: 0, scale: 0.6 }}, {{ y: 0, opacity: 1, scale: 1, duration: 0.5, stagger: 0.09, ease: "back.out(1.8)" }}, 0.0);
  tl.fromTo("#{p}-l1", {{ y: 20, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.4, ease: "power3.out" }}, 0.3);
  // condense five → one
  tl.to(".{p}-d", {{ x: (i) => (2 - i) * 170, scale: 0.4, opacity: 0, duration: 0.5, ease: "power3.in" }}, 1.25);
  tl.set("#{p}-l1", {{ opacity: 0 }}, 1.4);
  tl.fromTo("#{p}-l2", {{ opacity: 0, scale: 1.2 }}, {{ opacity: 1, scale: 1, duration: 0.35, ease: "power3.out" }}, 1.4);
  tl.fromTo("#{p}-pill", {{ scale: 0.2, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.6, ease: "back.out(1.6)" }}, 1.6);
  {type_js(f'{p}-pt', 2.2, 0.7)}
  tl.fromTo("#{p}-arr", {{ opacity: 0, x: -16 }}, {{ opacity: 1, x: 0, duration: 0.3, ease: "power3.out" }}, 2.85);
  tl.fromTo("#{p}-url", {{ opacity: 0, y: 14 }}, {{ opacity: 1, y: 0, duration: 0.4, ease: "power3.out" }}, 2.6);
  tl.fromTo("#{p}-cursor", {{ x: 900, y: 1500, opacity: 0 }}, {{ x: 690, y: 832, opacity: 1, duration: 0.9, ease: "power3.out" }}, 2.75);
  pulse("#{p}-pill", {{ scale: 1 }}, {{ scale: 0.95 }}, 3.8, 0.1);
  pulse("#{p}-cursor", {{ scale: 1 }}, {{ scale: 0.85 }}, 3.8, 0.1);
  tl.fromTo("#{p}-ripc", {{ scale: 0.3, opacity: 0.9 }}, {{ scale: 3, opacity: 0, duration: 0.6, ease: "power2.out", immediateRender: false }}, 3.85);
  tl.fromTo("#{p}-banner", {{ opacity: 0 }}, {{ opacity: 0.16, duration: 0.8, ease: "power2.out" }}, 3.3);
""",
)

# ---------------- Frame 9 — brand (final) ----------------
p = "f9"
frames[("09-brand", 9, 6.2)] = (
    f"""
.{p}-plate {{ position: absolute; left: 410px; top: 110px; width: 1100px; height: 640px; border-radius: 36px; background: #F7F5EF;
  box-shadow: 0 50px 120px rgba(0,0,0,0.55), 0 0 0 1px rgba(201,162,39,0.4); }}
.{p}-mark {{ position: absolute; left: 810px; top: 160px; width: 300px; height: 260px; }}
.{p}-n1 {{ position: absolute; left: 550px; top: 456px; width: 820px; }}
.{p}-n2 {{ position: absolute; left: 631px; top: 548px; width: 657px; }}
.{p}-tag {{ position: absolute; left: 643px; top: 676px; width: 635px; }}
.{p}-mark, .{p}-n1, .{p}-n2, .{p}-tag {{ display: block; }}
.{p}-nwrap {{ position: absolute; inset: 0; }}
.{p}-url {{ position: absolute; left: 0; right: 0; top: 790px; text-align: center; font: 700 52px "Space Grotesk", sans-serif; letter-spacing: 0.01em; }}
.{p}-ul {{ position: absolute; left: 640px; top: 862px; width: 640px; height: 5px; border-radius: 3px; background: linear-gradient(90deg, {C['gold']}, {C['blue']}); transform-origin: 0 50%; }}
""",
    f"""
        <div class="{p}-plate" id="{p}-plate"></div>
        <img class="{p}-mark" id="{p}-mark" src="assets/tmn-mark.png" alt="">
        <img class="{p}-n1" id="{p}-n1" src="assets/tmn-name1.png" alt="">
        <img class="{p}-n2" id="{p}-n2" src="assets/tmn-name2.png" alt="">
        <img class="{p}-tag" id="{p}-tag" src="assets/tmn-tagline.png" alt="">
        <div class="{p}-url">{typed(p, f'{p}-u', 'TrainorMediaNetwork.com')}</div>
        <div class="{p}-ul" id="{p}-ul"></div>
""",
    f"""
  tl.fromTo("#{p}-plate", {{ y: 60, opacity: 0, scale: 0.96 }}, {{ y: 0, opacity: 1, scale: 1, duration: 0.8, ease: "power3.out" }}, 0);
  tl.fromTo("#{p}-mark", {{ clipPath: "inset(100% 0% 0% 0%)" }}, {{ clipPath: "inset(0% 0% 0% 0%)", duration: 1.0, ease: "power3.out" }}, 0.45);
  tl.fromTo("#{p}-mark", {{ y: 30 }}, {{ y: 0, duration: 1.0, ease: "power3.out" }}, 0.45);
  tl.fromTo("#{p}-n1", {{ y: 30, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.6, ease: "power3.out" }}, 0.9);
  tl.fromTo("#{p}-n2", {{ y: 30, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.6, ease: "power3.out" }}, 1.25);
  tl.fromTo("#{p}-tag", {{ opacity: 0, y: 12 }}, {{ opacity: 1, y: 0, duration: 0.8, ease: "power3.out" }}, 2.1);
  {type_js(f'{p}-u', 3.0, 0.9)}
  tl.fromTo("#{p}-ul", {{ scaleX: 0 }}, {{ scaleX: 1, duration: 0.7, ease: "power3.inOut" }}, 3.8);
  tl.fromTo(".{p}-cam", {{ scale: 1 }}, {{ scale: 1.025, duration: DUR, ease: "none" }}, 0);
""",
)

import os as _os
if _os.environ.get("HOOK") == "b":
    frames = {k: v for k, v in frames.items() if k[0] != "01-hook"}
    exec(open(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "hookb.py")).read())
VCSS = {1: '\n.{p}-big {{ font-size: 180px; left: 70px; }}\n#{p}-w1a, #{p}-w2a, #{p}-w3a {{ top: 250px; }}\n#{p}-w1b, #{p}-w2b, #{p}-w3b {{ top: 440px; }}\n#{p}-w2b {{ font-size: 140px; top: 450px; }}\n#{p}-w3b {{ font-size: 160px; top: 445px; }}\n.{p}-phone {{ left: 315px; top: 720px; width: 450px; height: 770px; }}\n.{p}-count {{ left: 700px; top: 680px; }}\n.{p}-calwrap {{ left: 90px; top: 760px; width: 900px; height: 720px; }}\n.{p}-stamp {{ left: 230px; top: 1040px; }}\n.{p}-stars {{ left: 130px; top: 900px; width: 820px; }}\n.{p}-bs, .{p}-bs svg {{ width: 136px !important; height: 136px !important; }}\n.{p}-zero {{ left: 90px; top: 1130px; width: 900px; }}\n.{p}-gap {{ font-size: 170px; top: 520px; }}\n.{p}-lost {{ font-size: 68px; top: 430px; }}\n.{p}-cust {{ left: 50px; top: 900px; width: 260px; }}\n.{p}-cdisc {{ width: 150px; height: 150px; padding: 30px; }}\n.{p}-store {{ left: 720px; top: 880px; }}\n.{p}-path {{ left: 300px; top: 968px; width: 430px; }}\n.{p}-alarm {{ background: radial-gradient(ellipse 80% 45% at 50% 60%, rgba(255,59,59,0.42), rgba(255,59,59,0) 70%); }}\n', 2: '\n.{p}-bloom {{ left: -60px; top: 360px; width: 1200px; height: 1000px; }}\n.{p}-eyebrow {{ top: 400px; left: 90px; right: 90px; font-size: 54px; line-height: 1.15; }}\n.{p}-title {{ top: 560px; font-size: 230px; line-height: 0.92; }}\n.{p}-chips {{ top: 1060px; }}\n.{p}-rd {{ top: 1220px; }}\n.{p}-line {{ left: 170px; top: 1275px; width: 740px; }}\n', 8: '\n.{p}-banner {{ left: 40px; top: 560px; width: 1000px; height: 500px; }}\n.{p}-label {{ top: 600px; }}\n.{p}-d {{ top: 760px; }}\n.{p}-pill {{ left: 90px; top: 750px; width: 900px; }}\n.{p}-rip {{ left: 700px; top: 840px; }}\n.{p}-url {{ top: 960px; }}\n', 3: '\n.{p}-left {{ left: 80px; top: 200px; width: 920px; }}\n.{p}-title {{ font-size: 104px; }}\n.{p}-disc {{ width: 140px; height: 140px; padding: 33px; }}\n.{p}-vstage {{ position: absolute; left: 0; top: 0; width: 1920px; height: 1080px; transform-origin: 0 0; transform: translate(-743px, 655px) scale(0.95); }}\n.{p}-ring {{ left: 150px; top: 270px; }}\n', 4: '\n.{p}-left {{ left: 80px; top: 200px; width: 920px; }}\n.{p}-title {{ font-size: 104px; }}\n.{p}-disc {{ width: 140px; height: 140px; padding: 33px; }}\n.{p}-vstage {{ position: absolute; left: 0; top: 0; width: 1920px; height: 1080px; transform-origin: 0 0; transform: translate(-743px, 655px) scale(0.95); }}\n', 5: '\n.{p}-left {{ left: 80px; top: 200px; width: 920px; }}\n.{p}-title {{ font-size: 104px; }}\n.{p}-disc {{ width: 140px; height: 140px; padding: 33px; }}\n.{p}-vstage {{ position: absolute; left: 0; top: 0; width: 1920px; height: 1080px; transform-origin: 0 0; transform: translate(-743px, 655px) scale(0.95); }}\n', 6: '\n.{p}-left {{ left: 80px; top: 200px; width: 920px; }}\n.{p}-title {{ font-size: 104px; }}\n.{p}-disc {{ width: 140px; height: 140px; padding: 33px; }}\n.{p}-vstage {{ position: absolute; left: 0; top: 0; width: 1920px; height: 1080px; transform-origin: 0 0; transform: translate(-743px, 655px) scale(0.95); }}\n', 7: '\n.{p}-left {{ left: 80px; top: 200px; width: 920px; }}\n.{p}-title {{ font-size: 104px; }}\n.{p}-disc {{ width: 140px; height: 140px; padding: 33px; }}\n.{p}-vstage {{ position: absolute; left: 0; top: 0; width: 1920px; height: 1080px; transform-origin: 0 0; transform: translate(-743px, 655px) scale(0.95); }}\n', 9: '.{p}-vstage {{ position: absolute; left: 0; top: 0; width: 1920px; height: 1080px; transform-origin: 0 0; transform: translate(-324px, 470px) scale(0.9); }}\n'}
if _os.environ.get("HOOK") == "b":
    VCSS[1] = HOOKB_VCSS
for (fid, n, dur), (css, html, js) in list(frames.items()):
    p = f"f{n}"
    if n in VCSS:
        css = css + VCSS[n].replace("{p}", p).replace("{{", "{").replace("}}", "}")
    if n in (3, 4, 5, 6, 7):
        a, b = html.split("<!--/left-->", 1)
        html = a + f'<div class="{p}-vstage">' + b + "</div>"
    if n == 9:
        html = f'<div class="{p}-vstage">' + html + "</div>"
    with open(os.path.join(OUT, f"{fid}.html"), "w") as f:
        f.write(wrap(fid, n, dur, css, html, js))
    print("wrote", fid)
