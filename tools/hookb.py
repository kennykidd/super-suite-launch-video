# ---------------- Frame 1 — hook B ("Will they find you?") ----------------
# exec'd by build_frames*.py when HOOK=b. Positions use % so one block serves 16:9 and 9:16;
# HOOKB_VCSS carries the vertical-only overrides.
p = "f1"
RED = "#FF3B3B"

results = [("Comfort Air Co.", "4.9", "0.8 mi"), ("CoolPro HVAC", "4.8", "1.2 mi"), ("Desert Breeze Heating", "4.7", "1.9 mi")]
res_html = "".join(
    f'<div class="{p}-res" id="{p}-res{i}"><div class="{p}-rpin">{i + 1}</div><div class="{p}-rtx"><div class="{p}-rn">{n}</div>'
    f'<div class="{p}-rs"><span class="{p}-rstar"><svg viewBox="0 0 24 24"><path d="M12 2.5 l2.9 6.1 6.6 0.8 -4.9 4.6 1.3 6.6 L12 17.3 6.1 20.6 7.4 14 2.5 9.4 9.1 8.6 Z" fill="#F59E0B"/></svg></span> {r} · {d} · Open now</div></div><div class="{p}-rbtn">Call</div></div>'
    for i, (n, r, d) in enumerate(results)
)
# competitor pins on the map (left%, top%)
pins = [(24, 34), (71, 28), (63, 62)]
pin_html = "".join(f'<div class="{p}-pin" id="{p}-pin{i}" style="left:{x}%;top:{y}%"><div class="{p}-pind"></div></div>' for i, (x, y) in enumerate(pins))
streets = "".join(f'<line x1="{x}" y1="0" x2="{x + 40}" y2="1000" />' for x in range(-200, 1200, 110)) + "".join(
    f'<line x1="0" y1="{y}" x2="1000" y2="{y - 30}" />' for y in range(0, 1100, 95))
search_svg = '<svg viewBox="0 0 24 24" fill="none" stroke="#5B6B8F" stroke-width="2.6" stroke-linecap="round"><circle cx="10.5" cy="10.5" r="6.5"/><path d="M15.5 15.5 L21 21"/></svg>'


def glitch_word_b(idname, text, cls):
    return (f'<div class="{p}-gw {cls}" data-layout-allow-overlap id="{idname}">'
            f'<span class="{p}-gr">{text}</span><span class="{p}-gc">{text}</span><strong>{text}</strong></div>')


frames[("01-hook", 1, 8.1)] = (
    f"""
.{p}-frame {{ position: absolute; inset: 0; overflow: hidden; }}
.{p}-rig, .{p}-punch {{ position: absolute; inset: 0; transform-origin: 50% 50%; }}
.{p}-mapwrap {{ position: absolute; left: -10%; top: -10%; width: 120%; height: 120%; perspective: 1600px; }}
.{p}-map {{ position: absolute; inset: 0; transform-origin: 50% 60%; }}
.{p}-map svg {{ position: absolute; inset: 0; width: 100%; height: 100%; }}
.{p}-map line {{ stroke: rgba(46,168,255,0.22); stroke-width: 2.2; }}
.{p}-glow {{ position: absolute; inset: 0; background: radial-gradient(ellipse 55% 50% at 50% 50%, rgba(46,168,255,0.18), rgba(6,11,30,0) 70%),
  linear-gradient(180deg, rgba(6,11,30,0.2), rgba(6,11,30,0.85)); }}
.{p}-me {{ position: absolute; left: 47%; top: 46%; width: 0; height: 0; }}
.{p}-medot {{ position: absolute; left: -22px; top: -22px; width: 44px; height: 44px; border-radius: 50%; background: {C['blue']};
  border: 6px solid #fff; box-shadow: 0 0 40px rgba(46,168,255,0.9); }}
.{p}-merip {{ position: absolute; left: -60px; top: -60px; width: 120px; height: 120px; border-radius: 50%; border: 3px solid {C['blue']}; }}
.{p}-pin {{ position: absolute; width: 0; height: 0; }}
.{p}-pind {{ position: absolute; left: -30px; top: -70px; width: 60px; height: 60px; border-radius: 50% 50% 50% 0; transform: rotate(-45deg);
  background: {RED}; box-shadow: 0 0 30px rgba(255,59,59,0.7); }}
.{p}-tag {{ position: absolute; left: 6%; top: 9%; font: 700 34px "Space Grotesk", sans-serif; letter-spacing: 0.28em; color: {RED};
  display: flex; align-items: center; gap: 14px; opacity: 0; }}
.{p}-live {{ width: 16px; height: 16px; border-radius: 50%; background: {RED}; box-shadow: 0 0 18px {RED}; }}
.{p}-ui {{ position: absolute; left: 50%; width: 900px; margin-left: -450px; top: 17%; }}
.{p}-bar {{ height: 96px; border-radius: 48px; background: #fff; display: flex; align-items: center; gap: 18px; padding: 0 34px;
  box-shadow: 0 30px 80px rgba(0,0,0,0.55), 0 0 0 3px rgba(46,168,255,0.35); }}
.{p}-bar svg {{ width: 40px; height: 40px; flex: none; }}
.{p}-q {{ font: 600 38px "Inter", sans-serif; color: #0B1530; white-space: nowrap; }}
.{p}-caret {{ width: 3px; height: 44px; background: #0B1530; }}
.{p}-results {{ margin-top: 22px; }}
.{p}-res {{ display: flex; align-items: center; gap: 20px; height: 108px; padding: 0 26px; margin-bottom: 14px; border-radius: 18px;
  background: rgba(255,255,255,0.96); color: #0B1530; box-shadow: 0 18px 50px rgba(0,0,0,0.45); }}
.{p}-rpin {{ width: 54px; height: 54px; border-radius: 50%; background: {RED}; color: #fff; font: 700 26px "Space Grotesk", sans-serif;
  display: flex; align-items: center; justify-content: center; flex: none; }}
.{p}-rtx {{ flex: 1; }}
.{p}-rn {{ font: 700 30px "Inter", sans-serif; }}
.{p}-rs {{ font: 500 22px "Inter", sans-serif; color: #4B5A7A; margin-top: 4px; }}
.{p}-rstar {{ display: inline-block; width: 22px; height: 22px; vertical-align: -3px; }}
.{p}-rstar svg {{ width: 100%; height: 100%; display: block; }}
.{p}-rbtn {{ font: 700 22px "Inter", sans-serif; color: #fff; background: #1D4ED8; padding: 10px 22px; border-radius: 100px; }}
.{p}-ghost {{ height: 108px; border-radius: 18px; border: 3px dashed rgba(185,198,228,0.55); display: flex; align-items: center; justify-content: center;
  font: 700 30px "Space Grotesk", sans-serif; color: {C['muted']}; letter-spacing: 0.06em; background: rgba(6,11,30,0.6); }}
.{p}-gw {{ position: absolute; left: 0; right: 0; text-align: center; font-family: "Space Grotesk", sans-serif; font-weight: 700; line-height: 0.9;
  letter-spacing: -0.03em; text-transform: uppercase; white-space: nowrap; }}
.{p}-gw span, .{p}-gw strong {{ position: absolute; left: 0; right: 0; top: 0; }}
.{p}-gw strong {{ position: relative; color: #fff; }}
.{p}-gr {{ color: {RED}; mix-blend-mode: screen; }}
.{p}-gc {{ color: #22D3EE; mix-blend-mode: screen; }}
.{p}-blue strong {{ color: {C['blue']}; text-shadow: 0 0 70px rgba(46,168,255,0.7); }}
.{p}-red strong {{ color: {RED}; text-shadow: 0 0 60px rgba(255,59,59,0.6); }}
#{p}-k0 {{ top: 40%; font-size: 210px; }}
#{p}-k1 {{ top: 20%; font-size: 150px; }}
#{p}-k2 {{ top: 38%; font-size: 330px; }}
#{p}-k3 {{ top: 70%; font-size: 92px; }}
.{p}-flash {{ position: absolute; inset: 0; background: #fff; opacity: 0; }}
.{p}-rflash {{ position: absolute; inset: 0; background: {RED}; opacity: 0; mix-blend-mode: screen; }}
.{p}-dim {{ position: absolute; inset: 0; background: rgba(4,7,20,0.78); opacity: 0; }}
""",
    f"""
        <div class="{p}-frame"><div class="{p}-rig" id="{p}-rig"><div class="{p}-punch" id="{p}-punch">
          <div class="{p}-mapwrap"><div class="{p}-map" id="{p}-map"><svg viewBox="0 0 1000 1000" preserveAspectRatio="none">{streets}</svg>
            {pin_html}
            <div class="{p}-me" id="{p}-me"><div class="{p}-merip"></div><div class="{p}-merip"></div><div class="{p}-medot"></div></div>
          </div></div>
          <div class="{p}-glow"></div>
          <div class="{p}-tag" id="{p}-tag"><div class="{p}-live"></div>RIGHT NOW</div>
          <div class="{p}-ui" id="{p}-ui">
            <div class="{p}-bar" id="{p}-bar">{search_svg}<div class="{p}-q">{typed(p, f'{p}-qt', 'HVAC repair near me')}</div><div class="{p}-caret" id="{p}-caret"></div></div>
            <div class="{p}-results">{res_html}<div class="{p}-ghost" id="{p}-ghost">YOUR BUSINESS? — NOT FOUND</div></div>
          </div>
          <div class="{p}-dim" id="{p}-dim"></div>
          {glitch_word_b(f'{p}-k0', 'Right now', f'{p}-red')}
          {glitch_word_b(f'{p}-k1', 'Will they find', f'{p}-k1')}
          {glitch_word_b(f'{p}-k2', 'You?', f'{p}-blue')}
          {glitch_word_b(f'{p}-k3', 'Or your competitor?', f'{p}-red')}
        </div></div></div>
        <div class="{p}-rflash" id="{p}-rflash"></div>
        <div class="{p}-flash" id="{p}-flash"></div>
""",
    f"""
  function impact(at, strength) {{
    tl.fromTo("#{p}-flash", {{ opacity: 0.5 * strength }}, {{ opacity: 0, duration: 0.16, ease: "power2.out", immediateRender: false }}, at);
    tl.fromTo("#{p}-punch", {{ scale: 1 + 0.06 * strength }}, {{ scale: 1, duration: 0.45, ease: "expo.out", immediateRender: false }}, at);
  }}
  const TEAR = [[-14, 12], [9, -16], [-6, 7], [16, -9], [-3, 4], [0, 0]];
  function slam(sel, at) {{
    tl.fromTo(sel, {{ opacity: 0, scale: 1.6, filter: "blur(18px)" }}, {{ opacity: 1, scale: 1, filter: "blur(0px)", duration: 0.32, ease: "expo.out", immediateRender: false }}, at);
    TEAR.forEach((o, i) => {{
      tl.set(sel + " .{p}-gr", {{ x: o[0] * 1.6, y: i % 2 ? 3 : -3 }}, at + 0.05 + i * 0.045);
      tl.set(sel + " .{p}-gc", {{ x: o[1] * 1.6, y: i % 2 ? -3 : 3 }}, at + 0.05 + i * 0.045);
    }});
  }}
  tl.set("#{p}-k1, #{p}-k2, #{p}-k3", {{ opacity: 0 }}, 0);
  window.cameraShake(tl, "#{p}-rig", {{ profile: "handheld-normal-mild", intensity: 0.45, rotation: false, duration: DUR }});

  // Scene 1 (0–1.8): the map wakes up — "Right now, someone near you"
  tl.fromTo("#{p}-map", {{ rotationX: 52, scale: 1.25 }}, {{ rotationX: 40, scale: 1.0, duration: 4.6, ease: "power2.out" }}, 0);
  tl.fromTo("#{p}-k0", {{ opacity: 0.8, scale: 1.25, filter: "blur(5px)" }}, {{ opacity: 1, scale: 1, filter: "blur(0px)", duration: 0.3, ease: "expo.out" }}, 0);
  TEAR.forEach((o, i) => {{ tl.set("#{p}-k0 .{p}-gr", {{ x: o[0] * 1.6 }}, i * 0.045); tl.set("#{p}-k0 .{p}-gc", {{ x: o[1] * 1.6 }}, i * 0.045); }});
  tl.to("#{p}-k0", {{ opacity: 0, scale: 0.6, filter: "blur(12px)", duration: 0.35, ease: "power3.in" }}, 0.75);
  tl.fromTo("#{p}-tag", {{ opacity: 0, x: -20 }}, {{ opacity: 1, x: 0, duration: 0.3, ease: "power3.out", immediateRender: false }}, 0.95);
  tl.fromTo(".{p}-live", {{ opacity: 1 }}, {{ opacity: 0.25, duration: 0.25, ease: "steps(1)", immediateRender: false }}, 0.5);
  tl.fromTo(".{p}-live", {{ opacity: 0.25 }}, {{ opacity: 1, duration: 0.25, ease: "steps(1)", immediateRender: false }}, 1.0);
  tl.fromTo("#{p}-me", {{ scale: 0 }}, {{ scale: 1, duration: 0.5, ease: "back.out(2.2)" }}, 0.9);
  tl.fromTo(".{p}-merip", {{ scale: 0.4, opacity: 0.9 }}, {{ scale: 2.6, opacity: 0, duration: 1.1, stagger: 0.45, ease: "power2.out" }}, 1.0);
  // Scene 2 (1.7–4.0): the search — "is searching for exactly what you do"
  tl.fromTo("#{p}-bar", {{ y: -60, opacity: 0, scale: 0.92 }}, {{ y: 0, opacity: 1, scale: 1, duration: 0.45, ease: "expo.out" }}, 1.65);
  {type_js(f'{p}-qt', 1.95, 1.0)}
  tl.fromTo("#{p}-caret", {{ opacity: 1 }}, {{ opacity: 0, duration: 0.01, immediateRender: false }}, 3.0);
  tl.fromTo(".{p}-res", {{ y: 40, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.4, stagger: 0.22, ease: "power3.out" }}, 2.55);
  tl.fromTo(".{p}-pin", {{ y: -140, opacity: 0, scale: 0.5 }}, {{ y: 0, opacity: 1, scale: 1, duration: 0.45, stagger: 0.22, ease: "bounce.out" }}, 2.55);
  // Scene 3 (3.9–4.85): the pause — scan for "you"… nothing
  tl.fromTo("#{p}-ghost", {{ opacity: 0, scale: 0.95 }}, {{ opacity: 1, scale: 1, duration: 0.35, ease: "power3.out" }}, 3.95);
  tl.fromTo("#{p}-ghost", {{ x: 0 }}, {{ x: -16, duration: 0.05, immediateRender: false }}, 4.35);
  tl.fromTo("#{p}-ghost", {{ x: -16 }}, {{ x: 14, duration: 0.07, immediateRender: false }}, 4.40);
  tl.fromTo("#{p}-ghost", {{ x: 14 }}, {{ x: 0, duration: 0.08, immediateRender: false }}, 4.47);
  // Scene 4 (4.85–6.6): "Will they find YOU?"
  tl.fromTo("#{p}-ui", {{ opacity: 1, scale: 1, filter: "blur(0px)" }}, {{ opacity: 0.25, scale: 0.9, filter: "blur(10px)", duration: 0.35, ease: "power2.inOut", immediateRender: false }}, 4.82);
  tl.fromTo("#{p}-dim", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.3, immediateRender: false }}, 4.85);
  impact(4.88, 0.7);
  slam("#{p}-k1", 4.88);
  impact(5.6, 1);
  slam("#{p}-k2", 5.6);
  tl.fromTo("#{p}-k2", {{ scale: 1 }}, {{ scale: 1.06, duration: 1.0, ease: "power1.out", immediateRender: false }}, 5.95);
  // Scene 5 (6.7–8.1): "…or your competitor?"
  tl.fromTo(".{p}-pin", {{ scale: 1 }}, {{ scale: 1.35, duration: 0.4, ease: "back.out(2)", immediateRender: false }}, 6.75);
  tl.fromTo("#{p}-dim", {{ opacity: 1 }}, {{ opacity: 0.55, duration: 0.3, immediateRender: false }}, 6.75);
  tl.fromTo("#{p}-k2", {{ opacity: 1 }}, {{ opacity: 0.35, duration: 0.3, immediateRender: false }}, 7.05);
  slam("#{p}-k3", 7.1);
  tl.fromTo("#{p}-rflash", {{ opacity: 0.65 }}, {{ opacity: 0, duration: 0.4, ease: "power2.out", immediateRender: false }}, 7.1);
  tl.fromTo("#{p}-punch", {{ scale: 1 }}, {{ scale: 1.05, duration: 0.7, ease: "power2.in", immediateRender: false }}, 7.4);
""",
)

HOOKB_VCSS = """
.{p}-ui {{ width: 940px; margin-left: -470px; top: 21%; }}
.{p}-tag {{ top: 10%; left: 8%; }}
#{p}-k1 {{ top: 30%; font-size: 112px; }}
#{p}-k2 {{ top: 39%; font-size: 330px; }}
#{p}-k3 {{ top: 60%; font-size: 74px; }}
#{p}-k0 {{ top: 42%; font-size: 170px; }}
.{p}-mapwrap {{ left: -30%; width: 160%; top: 0%; height: 110%; }}
"""
