#!/usr/bin/env python3
"""Inject Efekty w 30 dni timeline + Porownaj sklad floating button into seasonal pages."""

import re

# Timeline HTML for seasonal pages (condensed, context-aware)
TIMELINE_HTML = '''
  <!-- #694 — EFEKTY W 30 DNI (Seasonal) -->
  <section style="background:#f3f1ec;padding:60px 20px;">
    <div style="max-width:800px;margin:0 auto;">
      <h2 style="font-family:'EB Garamond',serif;font-size:30px;color:#1a3a2a;text-align:center;margin-bottom:8px;">Efekty w 30 dni</h2>
      <p style="text-align:center;font-size:14px;color:#888;margin-bottom:40px;">Kliknij etap, aby zobaczyć co dzieje się w organizmie</p>
      <div style="background:#e0e0e0;border-radius:20px;height:8px;margin-bottom:40px;overflow:hidden;">
        <div id="timeline-progress-s" style="width:0%;height:100%;background:linear-gradient(90deg,#2e7d32,#8f7a3d);border-radius:20px;transition:width .6s ease;"></div>
      </div>
      <div style="position:relative;padding-left:40px;">
        <div style="position:absolute;left:15px;top:0;bottom:0;width:2px;background:linear-gradient(to bottom,#2e7d32,#388e3c,#689f38,#8f7a3d);"></div>
        <div class="timeline-phase-s" data-phase="1" onclick="toggleTP(this)" style="position:relative;margin-bottom:24px;cursor:pointer;">
          <div style="position:absolute;left:-33px;width:14px;height:14px;background:#2e7d32;border-radius:50%;border:3px solid #e8f5e9;z-index:1;"></div>
          <div style="background:#fff;padding:20px 24px;border-radius:12px;box-shadow:0 2px 12px rgba(0,0,0,.04);border-left:3px solid #2e7d32;">
            <div style="display:flex;justify-content:space-between;align-items:center;">
              <div><span style="font-size:11px;color:#2e7d32;text-transform:uppercase;letter-spacing:1.5px;font-weight:600;">Dzień 1–3</span>
              <h3 style="font-family:'EB Garamond',serif;color:#1a3a2a;font-size:20px;margin:4px 0 0;">🔬 Pierwsze wrażenie</h3></div>
              <span class="tp-arrow" style="font-size:18px;color:#2e7d32;transition:transform .3s;">▼</span>
            </div>
            <p style="font-size:14px;color:#555;margin:12px 0 0;">Subtelna „jasność umysłu" — lepsza orientacja w zadaniach.</p>
            <div class="tp-details" style="display:none;margin-top:16px;padding-top:16px;border-top:1px solid #eee;">
              <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
                <div style="background:#f8fdf8;padding:12px;border-radius:8px;"><div style="font-size:12px;color:#2e7d32;font-weight:600;margin-bottom:4px;">Co czujesz</div><div style="font-size:13px;color:#555;">Subtelna poprawa, mniej mgły mózgowej</div></div>
                <div style="background:#fef8f0;padding:12px;border-radius:8px;"><div style="font-size:12px;color:#8f7a3d;font-weight:600;margin-bottom:4px;">W środku</div><div style="font-size:13px;color:#555;">Cytykolina podnosi acetylocholinę. β-CD chroni składniki.</div></div>
              </div>
            </div>
          </div>
        </div>
        <div class="timeline-phase-s" data-phase="2" onclick="toggleTP(this)" style="position:relative;margin-bottom:24px;cursor:pointer;">
          <div style="position:absolute;left:-33px;width:14px;height:14px;background:#388e3c;border-radius:50%;border:3px solid #e8f5e9;z-index:1;"></div>
          <div style="background:#fff;padding:20px 24px;border-radius:12px;box-shadow:0 2px 12px rgba(0,0,0,.04);border-left:3px solid #388e3c;">
            <div style="display:flex;justify-content:space-between;align-items:center;">
              <div><span style="font-size:11px;color:#388e3c;text-transform:uppercase;letter-spacing:1.5px;font-weight:600;">Dzień 4–7</span>
              <h3 style="font-family:'EB Garamond',serif;color:#1a3a2a;font-size:20px;margin:4px 0 0;">⚡ Adaptacja</h3></div>
              <span class="tp-arrow" style="font-size:18px;color:#388e3c;transition:transform .3s;">▼</span>
            </div>
            <p style="font-size:14px;color:#555;margin:12px 0 0;">Codzienne zadania wymagają mniej wysiłku umysłowego.</p>
            <div class="tp-details" style="display:none;margin-top:16px;padding-top:16px;border-top:1px solid #eee;">
              <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
                <div style="background:#f8fdf8;padding:12px;border-radius:8px;"><div style="font-size:12px;color:#2e7d32;font-weight:600;margin-bottom:4px;">Co czujesz</div><div style="font-size:13px;color:#555;">Łatwiejsze skupienie, dłuższe sesje pracy</div></div>
                <div style="background:#fef8f0;padding:12px;border-radius:8px;"><div style="font-size:12px;color:#8f7a3d;font-weight:600;margin-bottom:4px;">W środku</div><div style="font-size:13px;color:#555;">ALA neutralizuje wolne rodniki w mitochondriach.</div></div>
              </div>
            </div>
          </div>
        </div>
        <div class="timeline-phase-s" data-phase="3" onclick="toggleTP(this)" style="position:relative;margin-bottom:24px;cursor:pointer;">
          <div style="position:absolute;left:-33px;width:14px;height:14px;background:#689f38;border-radius:50%;border:3px solid #f0f7f0;z-index:1;"></div>
          <div style="background:#fff;padding:20px 24px;border-radius:12px;box-shadow:0 2px 12px rgba(0,0,0,.04);border-left:3px solid #689f38;">
            <div style="display:flex;justify-content:space-between;align-items:center;">
              <div><span style="font-size:11px;color:#689f38;text-transform:uppercase;letter-spacing:1.5px;font-weight:600;">Dzień 8–14</span>
              <h3 style="font-family:'EB Garamond',serif;color:#1a3a2a;font-size:20px;margin:4px 0 0;">🎯 Stabilizacja</h3></div>
              <span class="tp-arrow" style="font-size:18px;color:#689f38;transition:transform .3s;">▼</span>
            </div>
            <p style="font-size:14px;color:#555;margin:12px 0 0;">Stała energia bez kofeinowych zjazdów. Lepsza pamięć robocza.</p>
            <div class="tp-details" style="display:none;margin-top:16px;padding-top:16px;border-top:1px solid #eee;">
              <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
                <div style="background:#f8fdf8;padding:12px;border-radius:8px;"><div style="font-size:12px;color:#2e7d32;font-weight:600;margin-bottom:4px;">Co czujesz</div><div style="font-size:13px;color:#555;">Wyraźna poprawa koncentracji, mniej rozproszeń</div></div>
                <div style="background:#fef8f0;padding:12px;border-radius:8px;"><div style="font-size:12px;color:#8f7a3d;font-weight:600;margin-bottom:4px;">W środku</div><div style="font-size:13px;color:#555;">Steady-state acetylocholina. Mitochondria działają wydajniej.</div></div>
              </div>
            </div>
          </div>
        </div>
        <div class="timeline-phase-s" data-phase="4" onclick="toggleTP(this)" style="position:relative;margin-bottom:24px;cursor:pointer;">
          <div style="position:absolute;left:-33px;width:14px;height:14px;background:#8f7a3d;border-radius:50%;border:3px solid #f5f0e0;z-index:1;"></div>
          <div style="background:#fff;padding:20px 24px;border-radius:12px;box-shadow:0 2px 12px rgba(0,0,0,.04);border-left:3px solid #8f7a3d;">
            <div style="display:flex;justify-content:space-between;align-items:center;">
              <div><span style="font-size:11px;color:#8f7a3d;text-transform:uppercase;letter-spacing:1.5px;font-weight:600;">Dzień 15–30</span>
              <h3 style="font-family:'EB Garamond',serif;color:#1a3a2a;font-size:20px;margin:4px 0 0;">🏆 Pełny efekt</h3></div>
              <span class="tp-arrow" style="font-size:18px;color:#8f7a3d;transition:transform .3s;">▼</span>
            </div>
            <p style="font-size:14px;color:#555;margin:12px 0 0;">Pełna synergia 3 składników. Stała, niezawodna koncentracja.</p>
            <div class="tp-details" style="display:none;margin-top:16px;padding-top:16px;border-top:1px solid #eee;">
              <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
                <div style="background:#f8fdf8;padding:12px;border-radius:8px;"><div style="font-size:12px;color:#2e7d32;font-weight:600;margin-bottom:4px;">Co czujesz</div><div style="font-size:13px;color:#555;">Stabilna koncentracja, zero spadków, lepszy sen (0mg kofeiny)</div></div>
                <div style="background:#fef8f0;padding:12px;border-radius:8px;"><div style="font-size:12px;color:#8f7a3d;font-weight:600;margin-bottom:4px;">W środku</div><div style="font-size:13px;color:#555;">Optymalna fosfatydylocholina w błonach neuronów. Pełna ochrona mitochondrialna.</div></div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div style="text-align:center;margin-top:32px;">
        <div style="display:inline-flex;gap:24px;flex-wrap:wrap;justify-content:center;">
          <div style="text-align:center;"><div style="font-size:24px;font-weight:700;color:#2e7d32;">95%+</div><div style="font-size:12px;color:#888;">biodostępność</div></div>
          <div style="text-align:center;"><div style="font-size:24px;font-weight:700;color:#2e7d32;">0 mg</div><div style="font-size:12px;color:#888;">kofeiny</div></div>
          <div style="text-align:center;"><div style="font-size:24px;font-weight:700;color:#2e7d32;">30 dni</div><div style="font-size:12px;color:#888;">gwarancji</div></div>
        </div>
      </div>
    </div>
  </section>
'''

TIMELINE_JS = '''
<script>
function toggleTP(el){
  var d=el.querySelector('.tp-details');
  var a=el.querySelector('.tp-arrow');
  if(!d)return;
  var open=d.style.display!=='none';
  document.querySelectorAll('.tp-details').forEach(function(x){x.style.display='none';});
  document.querySelectorAll('.tp-arrow').forEach(function(x){x.style.transform='';});
  if(!open){d.style.display='block';a.style.transform='rotate(180deg)';
    var p=el.closest('div[style*="padding-left"]');
    var phases=p.querySelectorAll('.timeline-phase-s');
    var total=phases.length,idx=[].indexOf.call(phases,el);
    var bar=document.getElementById('timeline-progress-s');
    if(bar)bar.style.width=((idx+1)/total*100)+'%';
  }
}
</script>'''

# Floating comparison button
FLOAT_BTN = '''
<button id="sdpMobBtn" onclick="location.href='produkt.html#porownaj-sklad'" aria-label="Porównaj skład" style="position:fixed;bottom:75px;left:16px;z-index:998;width:48px;height:48px;border-radius:50%;background:linear-gradient(135deg,#2e7d32,#388e3c);color:#fff;border:none;font-size:22px;box-shadow:0 4px 16px rgba(46,125,50,.35);cursor:pointer;display:none;align-items:center;justify-content:center;">🔬</button>
<script>(function(){if(window.innerWidth<768){var b=document.getElementById('sdpMobBtn');if(b)b.style.display='flex';window.addEventListener('resize',function(){if(window.innerWidth<768){b.style.display='flex';}else{b.style.display='none';}});}})();</script>
'''

PAGES = ['matura.html', 'sesja.html', 'lato.html']

for page in PAGES:
    with open(page, 'r') as f:
        content = f.read()
    
    # Check if timeline already exists
    if 'timeline-phase-s' in content:
        print(f"SKIP {page}: timeline already present")
        continue
    
    # Insert timeline before the satisfaction guarantee section
    # Find a good insertion point — before the first "30-dniowa gwarancja" section
    guarantee_patterns = [
        '<section style.*?30-dniowa gwarancja',
        '<!--.*?guarantee.*?-->',
        '30-dniowa gwarancja satysfakcji',
    ]
    
    # Insert BEFORE footer or BEFORE </body> if no footer marker
    insert_marker = '<!-- Footer -->'
    fallback_marker = '</body>'
    if insert_marker in content:
        new_content = content.replace(
            insert_marker,
            TIMELINE_HTML + '\n' + insert_marker
        )
        # Add JS + floating button before </body>
        new_content = new_content.replace(fallback_marker, TIMELINE_JS + FLOAT_BTN + '\n' + fallback_marker)
        with open(page, 'w') as f:
            f.write(new_content)
        print(f"OK {page}: injected timeline + floating button")
    elif fallback_marker in content:
        new_content = content.replace(
            fallback_marker,
            TIMELINE_HTML + TIMELINE_JS + FLOAT_BTN + '\n' + fallback_marker
        )
        with open(page, 'w') as f:
            f.write(new_content)
        print(f"OK {page}: injected timeline + floating button")
    else:
        print(f"SKIP {page}: no insertion marker found")
    else:
        print(f"WARN {page}: no </body> found")

print("\nDone!")
