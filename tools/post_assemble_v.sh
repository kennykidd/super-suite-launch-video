#!/usr/bin/env bash
# Re-apply project-local patches after assemble-index.mjs + transitions inject regenerate index.html.
set -e
cd "$1"
sed -i 's#<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"[^>]*></script>#<script src="assets/vendor/gsap.min.js"></script>#' index.html compositions/captions.html
sed -i 's/\(id="el-[0-9a-z-]*-voice"\)/\1 data-audio-group="voiceover"/' index.html
python3 -I - <<'PY'
s = open("index.html").read()
s = s.replace('id="el-captions"', 'id="el-captions"\n        data-track-kind="captions"', 1)
fx = '''      <div
        id="el-fx-overlay"
        data-composition-id="fx-overlay"
        data-composition-src="compositions/fx-overlay.html"
        data-start="0"
        data-duration="59.5"
        data-track-index="3"
        data-width="1080"
        data-height="1920"
      ></div>

      <!-- captions -->'''
assert "<!-- captions -->" in s
s = s.replace("      <!-- captions -->", fx, 1)
open("index.html", "w").write(s)
PY
node /home/user/.agents/skills/hyperframes-audio/scripts/carve.mjs --comp ./index.html | tail -1
