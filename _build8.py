# -*- coding: utf-8 -*-
# Fase B / B1 — camada showroom sobre o output do _build7.
# Pipeline: python3 _build7.py && python3 _build8.py
F='/home/claude/vision/build/index.html'
P=open(F,encoding='utf-8').read()

# ---------- 1) MOTOR: vocabulário de gestos + showroom (CSS) ----------
FASE_B_CSS = """
/* ===== FASE B — Stage-Reveal System ===== */
/* vocabulário de gestos (usam o .in que o observer ja adiciona) */
.rv[data-rv="depth"]{transform:translateY(22px) scale(.955);filter:blur(7px);transition:opacity 1.1s cubic-bezier(.2,.7,.2,1),transform 1.1s cubic-bezier(.2,.7,.2,1),filter 1.1s cubic-bezier(.2,.7,.2,1)}
.rv[data-rv="depth"].in{transform:none;filter:none}
.rv[data-rv="mask"]{clip-path:inset(0 0 100% 0);transition:opacity 1s cubic-bezier(.2,.7,.2,1),clip-path 1.2s cubic-bezier(.2,.7,.2,1)}
.rv[data-rv="mask"].in{clip-path:inset(0 0 0 0)}
.rv[data-rv="slide-l"]{transform:translateX(-46px)}
.rv[data-rv="slide-l"].in{transform:none}
.rv[data-rv="slide-r"]{transform:translateX(46px)}
.rv[data-rv="slide-r"].in{transform:none}

/* ===== SHOWROOM DE PRODUTOS — palco com profundidade ===== */
.line-grid.showroom{position:relative;align-items:center}
.line-grid.showroom>.stage-floor{position:absolute;left:50%;bottom:-42px;transform:translateX(-50%);width:78%;height:150px;background:radial-gradient(ellipse 55% 100% at 50% 0,rgba(255,69,0,.2),transparent 72%);filter:blur(24px);pointer-events:none;z-index:0}
.line-grid.showroom .pcard{position:relative;z-index:1;transition:transform .55s cubic-bezier(.2,.7,.2,1),opacity .55s ease,filter .55s ease,box-shadow .55s ease,border-color .55s ease}
/* estados de repouso: herói à frente, laterais recuados ao fundo */
.line-grid.showroom .pcard:not(.hero-card){transform:scale(.92);opacity:.6;filter:saturate(.72) brightness(.8)}
.line-grid.showroom .hero-card{transform:scale(1.05) translateY(-6px);z-index:3;box-shadow:0 28px 72px -22px rgba(255,69,0,.4),0 0 0 1px rgba(255,122,26,.55)}
/* foco rotativo no hover (desktop) */
@media(hover:hover) and (min-width:861px){
  .line-grid.showroom:hover .hero-card{transform:scale(.93);opacity:.6;filter:saturate(.72) brightness(.8);box-shadow:none;border-color:var(--line)}
  .line-grid.showroom .pcard:hover{transform:scale(1.06) translateY(-6px)!important;opacity:1!important;filter:none!important;z-index:4;box-shadow:0 28px 72px -22px rgba(255,69,0,.4),0 0 0 1px rgba(255,122,26,.55)!important}
}
/* reveal cinematografico (emerge do fundo; herói chega por último) */
.line-grid.showroom .pcard.rv{opacity:0}
.line-grid.showroom .pcard:not(.hero-card).rv{transform:scale(.88) translateY(32px)}
.line-grid.showroom .pcard:not(.hero-card).rv.in{transform:scale(.92);opacity:.6}
.line-grid.showroom .hero-card.rv{transform:scale(1.0) translateY(38px)}
.line-grid.showroom .hero-card.rv.in{transform:scale(1.05) translateY(-6px);opacity:1}
/* mobile: empilha sem 3D, herói só com destaque de borda/glow */
@media(max-width:860px){
  .line-grid.showroom>.stage-floor{display:none}
  .line-grid.showroom .pcard:not(.hero-card){transform:none;opacity:1;filter:none}
  .line-grid.showroom .pcard:not(.hero-card).rv{transform:translateY(28px)}
  .line-grid.showroom .pcard:not(.hero-card).rv.in{transform:none;opacity:1}
  .line-grid.showroom .hero-card{transform:none}
  .line-grid.showroom .hero-card.rv{transform:translateY(34px)}
  .line-grid.showroom .hero-card.rv.in{transform:none}
}

/* ===== FASE B3 — magnetismo de scroll (proximity; hero/track fica LIVRE) ===== */
html{scroll-snap-type:y proximity}
#track,#stage,.kf{scroll-snap-align:none}
section.sec,section.manifesto,section.pos,section.evo,section.cw,section.pclose,section.close{scroll-snap-align:start;scroll-snap-stop:normal}
"""
assert '/* ===== FASE B' not in P, "Fase B ja aplicada — rode _build7 antes"
P=P.replace('</style>', FASE_B_CSS+'\n</style>',1)

# ---------- 2) HTML da seção de produtos: vira palco ----------
# 2a) line-grid -> showroom + piso
P=P.replace('<div class="line-grid">',
            '<div class="line-grid showroom"><div class="stage-floor"></div>',1)
# 2b) reordenar delays: herói (Premium) chega por último; Parrilla antecipa
P=P.replace('<div class="pcard hero-card rv d2">','<div class="pcard hero-card rv d3">',1)
P=P.replace('<div class="pcard rv d3"><div class="ring">Topo','<div class="pcard rv d2"><div class="ring">Topo',1)
# 2c) título e lead da seção de produtos com gesto depth (protagonista emerge)
P=P.replace('<h2 class="rv d1">Uma linha de tr\u00eas.','<h2 class="rv d1" data-rv="depth">Uma linha de tr\u00eas.',1)
P=P.replace('<p class="lead rv d2">Desenhamos a linha','<p class="lead rv d2" data-rv="depth">Desenhamos a linha',1)

# ---------- 3) B2: propagar gestos pras 8 seções (JS programático) ----------
APPLY_FN = (
"function applyScenes(){"
"document.querySelectorAll('section h2.rv').forEach(function(h){if(!h.hasAttribute('data-rv'))h.setAttribute('data-rv','depth');});"
"document.querySelectorAll('.big.rv').forEach(function(e){e.setAttribute('data-rv','mask');});"
"document.querySelectorAll('.pos-shot.rv, .evo-compare.rv').forEach(function(e){e.setAttribute('data-rv','mask');});"
"document.querySelectorAll('.tagline.rv').forEach(function(e){e.setAttribute('data-rv','depth');});"
"var SEL='.diff-row,.stat,.ecard,.scen-card,.cw-front,.cw-phase,.evo-card,.ue';"
"document.querySelectorAll(SEL).forEach(function(el){var sibs=[].slice.call(el.parentElement.children).filter(function(x){return x.matches&&x.matches(SEL);});var i=Math.max(0,sibs.indexOf(el));el.style.transitionDelay=(0.05+i*0.07)+'s';});"
"}\n"
)
assert 'function applyScenes' not in P
P=P.replace('// \u2500\u2500 PROPOSTA: REVEAL + COUNT + BARS \u2500\u2500',
            APPLY_FN+'// \u2500\u2500 PROPOSTA: REVEAL + COUNT + BARS \u2500\u2500',1)
P=P.replace("  document.querySelectorAll('.rv').forEach(el=>io.observe(el));",
            "  applyScenes();\n  document.querySelectorAll('.rv').forEach(el=>io.observe(el));",1)

open(F,'w',encoding='utf-8').write(P)
print('Fase B (B1+B2) aplicada. index.html agora:',len(P),'chars')
