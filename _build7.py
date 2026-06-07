# -*- coding: utf-8 -*-
U='/mnt/user-data/uploads/'
P=open(U+'proposta-vision-inox-completa.html',encoding='utf-8').read()
EVO=open(U+'secao-evolucao-produto.html',encoding='utf-8').read()
CW=open(U+'secao-como-trabalhamos.html',encoding='utf-8').read()

def _strip(s,a,b):
    i=s.index(a); j=s.index(b,i); return s[:i]+s[j:]
P=_strip(P,'/* evolu\u00e7\u00e3o */','/* produtos */')
P=_strip(P,'/* entreg\u00e1veis */','/* fechamento */')
P=P.replace('.stats,.line-grid,.scen,.dgrid,.opt-grid{grid-template-columns:1fr}','.stats,.line-grid,.scen{grid-template-columns:1fr}')
P=P.replace('.ue-wrap,.price-grid,.engine-grid,.split-note,.diff-row,.evo-grid{grid-template-columns:1fr}','.ue-wrap,.engine-grid,.diff-row{grid-template-columns:1fr}')
P=P.replace('  .evo-arrow{display:none}\n','')
P=P.replace('  .vrow{grid-template-columns:1fr 90px}\n','')

for s in ['assets/proto_antes.jpg','assets/ref_5.png','assets/ref_4.png','assets/ref_3.png','assets/ref_6.png','assets/blueprint_2.png']:
    EVO=EVO.replace('<img src=""','<img src="%s"'%s,1)
EVO=EVO.replace('</style>',
  '.evo-gallery{display:grid;grid-template-columns:repeat(2,1fr);gap:18px;margin-top:26px}\n'
  '.evo-shot{border:1px solid var(--line);border-radius:14px;overflow:hidden;background:#0a0a0e;aspect-ratio:3/2}\n'
  '.evo-shot img{width:100%;height:100%;object-fit:cover;display:block;transition:transform .6s cubic-bezier(.2,.7,.2,1)}\n'
  '.evo-shot:hover img{transform:scale(1.045)}\n'
  '@media(max-width:860px){.evo-gallery{grid-template-columns:1fr}}\n</style>',1)
EVO=EVO.replace('<!-- grid de diferenciais -->',
  '<div class="evo-gallery rv">\n'
  '      <div class="evo-shot"><img src="assets/ref_2.png" alt="Vision Inox angulo frontal"></div>\n'
  '      <div class="evo-shot"><img src="assets/ref_1.png" alt="Vision Inox perspectiva direita"></div>\n'
  '    </div>\n\n    <!-- grid de diferenciais -->',1)

# ===== HERO v7 (14 cenas) =====
HERO_CSS = """/* \u2500\u2500 HERO (scrollytelling estendido) \u2500\u2500 */
#track{height:2400vh;position:relative;z-index:2}
#stage{position:sticky;top:0;height:100vh;height:100svh;width:100%;overflow:hidden;background:var(--bg)}
.kf{position:absolute;inset:0;opacity:0;will-change:opacity}
.kf .media{position:absolute;inset:0;width:100%;height:100%}
.kf img,.kf video{width:100%;height:100%;display:block;will-change:transform}
/* papel + esbocos: cover sobre mesa escura warm */
#kf-paper,#kf-sk1,#kf-sk2,#kf-sk3{background:radial-gradient(ellipse 118% 96% at 50% 52%,#1c140b,#080503 80%)}
#kf-paper img,#kf-sk1 img,#kf-sk2 img,#kf-sk3 img{object-fit:cover;object-position:center 44%}
/* blueprints: contain (prancha inteira) sobre azul profundo */
#kf-btec,#kf-bren{background:radial-gradient(ellipse 96% 88% at 50% 48%,#0b1622,#060a0f 74%)}
#kf-btec .media,#kf-bren .media{display:flex;align-items:center;justify-content:center;padding:4vh 4vw}
#kf-btec img,#kf-bren img{width:auto;height:auto;max-width:100%;max-height:92%;object-fit:contain}
#kf-btec img{filter:drop-shadow(0 0 46px rgba(0,150,210,.22))}
#kf-bren img{filter:drop-shadow(0 0 42px rgba(140,170,205,.2))}
/* detalhes + inox: cover sobre preto */
#kf-denc,#kf-dgre,#kf-inox{background:var(--bg)}
#kf-denc img,#kf-dgre img{object-fit:cover;object-position:center 50%}
#kf-inox img{object-fit:cover;object-position:center 46%}
/* lifestyle: cover fullscreen, transform-origin na logo p/ o zoom */
#kf-praia,#kf-praiaimg,#kf-camp,#kf-pisc,#kf-mont,#kf-cam{background:#000}
#kf-praia video,#kf-praiaimg img,#kf-camp img,#kf-pisc img,#kf-mont img,#kf-cam img{object-fit:cover}
#kf-praiaimg img{object-position:center 46%;transform-origin:41% 57%}
#kf-camp img{object-position:center 50%;transform-origin:50% 56%}
#kf-pisc img{object-position:center 48%;transform-origin:50% 60%}
#kf-mont img{object-position:center 46%;transform-origin:46% 60%}
#kf-cam img{object-position:center 46%;transform-origin:52% 55%}
.hero-scrim{position:absolute;inset:0;z-index:6;pointer-events:none;background:linear-gradient(180deg,rgba(9,9,9,.5) 0%,rgba(9,9,9,.1) 24%,transparent 46%,transparent 60%,rgba(9,9,9,.42) 82%,rgba(9,9,9,.86) 100%)}
.pt{position:absolute;z-index:8;pointer-events:none;opacity:0;left:max(5vw,28px);bottom:12vh;max-width:min(820px,90vw)}
.pt.center{left:0;right:0;text-align:center;bottom:14vh;max-width:none;padding:0 5vw}
.pt.right{left:auto;right:max(5vw,28px);text-align:right}
.kk{font-family:var(--fs);font-size:11px;font-weight:800;letter-spacing:.28em;text-transform:uppercase;display:block;margin-bottom:16px}
.kk.cy{color:var(--cyan)}.kk.em{color:var(--e2)}
.ht{font-family:var(--fd);font-weight:300;letter-spacing:-.03em;line-height:1.0;text-shadow:0 2px 44px rgba(0,0,0,.7),0 1px 10px rgba(0,0,0,.5)}
.ht.md{font-size:clamp(30px,5vw,62px)}
.ht.lg{font-size:clamp(44px,8vw,108px)}
.ht.xl{font-size:clamp(54px,11.5vw,154px);font-weight:300;letter-spacing:-.045em}
.htsub{font-size:clamp(14px,1.6vw,18.5px);color:#c6c9d0;margin-top:20px;max-width:46ch;line-height:1.55;text-shadow:0 1px 20px rgba(0,0,0,.85)}
.pt.center .htsub{margin-left:auto;margin-right:auto}
.pt.right .htsub{margin-left:auto}
em.cy{color:var(--cyan);font-style:italic}em.em{color:var(--e2);font-style:italic}
#dots{position:absolute;right:3.2vw;top:50%;transform:translateY(-50%);z-index:9;display:flex;flex-direction:column;gap:10px}
.dot{width:5px;height:5px;border-radius:50%;background:rgba(255,255,255,.16);transition:background .4s,transform .4s}
.dot.on{background:var(--e2);transform:scale(1.6)}
#scue{position:absolute;bottom:5.5vh;left:50%;transform:translateX(-50%);z-index:9;display:flex;align-items:center;gap:12px;transition:opacity .6s}
#scue.gone{opacity:0}
#scue span{font-size:10px;font-weight:700;letter-spacing:.22em;text-transform:uppercase;color:rgba(255,255,255,.3)}
.sbar{width:38px;height:1px;background:rgba(255,255,255,.12);overflow:hidden;position:relative}
.sbar::after{content:"";position:absolute;inset:0;width:45%;background:var(--e2);animation:sb 2s ease-in-out infinite}
@keyframes sb{0%{transform:translateX(-110%)}100%{transform:translateX(240%)}}
#auMusic,#auEmber{display:none}
#sndBtn{position:fixed;top:max(3vh,18px);right:max(3.2vw,18px);z-index:40;width:42px;height:42px;border-radius:50%;border:1px solid rgba(255,255,255,.18);background:rgba(9,9,9,.46);color:rgba(255,255,255,.72);cursor:pointer;display:none;align-items:center;justify-content:center;transition:border-color .4s,color .4s;-webkit-backdrop-filter:blur(8px);backdrop-filter:blur(8px)}
#sndBtn:hover{border-color:rgba(255,122,26,.5);color:#fff}
#sndBtn.on{border-color:var(--e2);color:var(--e2)}
#sndBtn svg{width:18px;height:18px}
#sndBtn .ic-on{display:none}
#sndBtn.on .ic-off{display:none}#sndBtn.on .ic-on{display:block}
#intro{position:fixed;inset:0;z-index:60;background:radial-gradient(ellipse 90% 65% at 50% 84%,rgba(255,69,0,.13),transparent 56%),#070707;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:0 7vw;transition:opacity 1s ease,transform 1.1s cubic-bezier(.2,.7,.2,1)}
#intro.gone{opacity:0;transform:scale(1.05);pointer-events:none}
#intro .grain{position:absolute;inset:0;opacity:.04;pointer-events:none;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='2'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")}
.intro-kk{font-family:var(--fs);font-size:11px;font-weight:800;letter-spacing:.34em;text-transform:uppercase;color:var(--e2);opacity:0;animation:introIn .9s ease .15s forwards}
.intro-h{font-family:var(--fd);font-weight:300;font-size:clamp(42px,7.5vw,88px);letter-spacing:-.03em;line-height:1.02;color:var(--text);margin:18px 0 0;opacity:0;animation:introIn .9s ease .3s forwards}
.intro-h em{font-style:italic;color:var(--e2)}
.intro-sub{font-family:var(--fs);font-size:clamp(14px,1.7vw,17px);color:var(--dim);line-height:1.6;margin:22px auto 0;max-width:40ch;opacity:0;animation:introIn .9s ease .45s forwards}
.intro-sub em{font-style:italic;color:var(--text)}
.intro-btn{margin-top:50px;width:106px;height:106px;border-radius:50%;border:1px solid rgba(255,122,26,.55);background:rgba(255,69,0,.06);color:var(--e2);cursor:pointer;display:flex;align-items:center;justify-content:center;position:relative;opacity:0;animation:introIn .9s ease .6s forwards;transition:transform .4s,background .4s}
.intro-btn:hover{background:rgba(255,69,0,.16);transform:scale(1.05)}
.intro-btn svg{width:34px;height:34px;position:relative;z-index:2}
.intro-btn .ring{position:absolute;inset:-1px;border-radius:50%;border:1px solid rgba(255,122,26,.45);animation:introPulse 2.8s ease-out infinite}
.intro-btn .ring.r2{animation-delay:1.4s}
@keyframes introPulse{0%{transform:scale(1);opacity:.7}100%{transform:scale(1.8);opacity:0}}
.intro-cue{margin-top:24px;font-family:var(--fs);font-size:12px;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:var(--text);opacity:0;animation:introIn .9s ease .75s forwards}
.intro-skip{margin-top:13px;font-family:var(--fs);font-size:12.5px;color:var(--faint);letter-spacing:.03em;cursor:pointer;background:none;border:none;text-decoration:underline;text-underline-offset:3px;opacity:0;animation:introIn .9s ease .9s forwards;transition:color .3s}
.intro-skip:hover{color:var(--dim)}
@keyframes introIn{to{opacity:1}}
@media(max-width:760px){
  #kf-btec .media,#kf-bren .media{padding:2.5vh 3vw}
  #kf-inox img{object-fit:contain;object-position:center}
  #kf-praiaimg img{object-position:26% 50%;transform-origin:26% 58%}
  #kf-camp img{transform-origin:50% 58%}
  #kf-pisc img{object-position:64% 48%;transform-origin:50% 58%}
  #kf-mont img{object-position:62% 46%;transform-origin:50% 58%}
  #kf-cam img{transform-origin:50% 56%}
  .ht.md{font-size:clamp(26px,8vw,40px)}
  .ht.lg{font-size:clamp(38px,11vw,58px)}
  .ht.xl{font-size:clamp(44px,13.5vw,72px)}
  .pt{bottom:13vh}.pt.center{bottom:15vh}
  #sndBtn{width:38px;height:38px;top:max(2.4vh,14px);right:max(4vw,14px)}
  #dots{right:2.6vw}
  .intro-btn{width:92px;height:92px}.intro-btn svg{width:30px;height:30px}
}
"""

HERO_HTML = """<!-- HERO scrollytelling -->
<div id="intro">
  <div class="grain"></div>
  <span class="intro-kk">Vision Inox</span>
  <h2 class="intro-h">Aumenta o <em>som.</em></h2>
  <p class="intro-sub">O que vem a seguir foi feito pra ser <em>sentido</em>, n\u00e3o lido.</p>
  <button class="intro-btn" id="introBtn" aria-label="Come\u00e7ar com som"><span class="ring"></span><span class="ring r2"></span><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M11 5 6 9H2v6h4l5 4V5z"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14"/></svg></button>
  <div class="intro-cue">Toque para come\u00e7ar</div>
  <button class="intro-skip" id="introSkip">continuar sem som</button>
</div>
<button id="sndBtn" aria-label="Som"><svg class="ic-off" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 5 6 9H2v6h4l5 4V5z"/><line x1="23" y1="9" x2="17" y2="15"/><line x1="17" y1="9" x2="23" y2="15"/></svg><svg class="ic-on" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 5 6 9H2v6h4l5 4V5z"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14"/></svg></button>
<div id="track">
<div id="stage">
  <div class="kf" id="kf-paper"><div class="media"><img src="assets/paper.png" alt="Folha em branco"></div></div>
  <div class="kf" id="kf-sk1"><div class="media"><img src="assets/sketch1.png" alt="Primeiro esbo\u00e7o"></div></div>
  <div class="kf" id="kf-sk2"><div class="media"><img src="assets/sketch2.png" alt="Esbo\u00e7o em evolu\u00e7\u00e3o"></div></div>
  <div class="kf" id="kf-sk3"><div class="media"><img src="assets/sketch3.png" alt="Esbo\u00e7o refinado com a marca"></div></div>
  <div class="kf" id="kf-btec"><div class="media"><img src="assets/blueprint_tec.png" alt="Blueprint t\u00e9cnica"></div></div>
  <div class="kf" id="kf-bren"><div class="media"><img src="assets/blueprint_render.png" alt="Blueprint em render"></div></div>
  <div class="kf" id="kf-denc"><div class="media"><img src="assets/det_encaixe.png" alt="Encaixe a laser"></div></div>
  <div class="kf" id="kf-dgre"><div class="media"><img src="assets/det_grelha.png" alt="Grelha em inox 304"></div></div>
  <div class="kf" id="kf-inox"><div class="media"><img src="assets/inox_hero.png" alt="Vision Inox \u2014 produto em inox 304"></div></div>
  <div class="kf" id="kf-praia"><div class="media"><video id="heroVid" muted playsinline preload="auto" poster="assets/hero-poster.jpg"><source src="assets/hero-wan.webm" type="video/webm"><source src="assets/hero-wan-web.mp4" type="video/mp4"></video></div></div>
  <div class="kf" id="kf-praiaimg"><div class="media"><img id="praiaImg" src="assets/praia_final.png" alt="Vision Inox no litoral \u2014 4K"></div></div>
  <div class="kf" id="kf-camp"><div class="media"><img src="assets/amb_camping.png" alt="Vision Inox no camping"></div></div>
  <div class="kf" id="kf-pisc"><div class="media"><img src="assets/amb_piscina.png" alt="Vision Inox na beira da piscina"></div></div>
  <div class="kf" id="kf-mont"><div class="media"><img src="assets/amb_montanha.png" alt="Vision Inox na montanha"></div></div>
  <div class="kf" id="kf-cam"><div class="media"><img src="assets/amb_caminhonete.png" alt="Vision Inox na caminhonete"></div></div>
  <div class="hero-scrim"></div>
  <audio id="auMusic" loop preload="auto"><source src="assets/hero-music.mp3" type="audio/mpeg"></audio>
  <audio id="auEmber" loop preload="auto"><source src="assets/hero-embers.mp3" type="audio/mpeg"></audio>
  <div class="pt" id="t1"><span class="kk cy">O ponto de partida</span><h2 class="ht md">Toda churrasqueira come\u00e7a <em class="cy">no papel.</em></h2></div>
  <div class="pt" id="t2"><span class="kk cy">A ideia, \u00e0 m\u00e3o</span><h2 class="ht lg">Come\u00e7a \u00e0 <em class="cy">m\u00e3o.</em></h2><p class="htsub">L\u00e1pis, r\u00e9gua e as primeiras medidas.</p></div>
  <div class="pt" id="t3"><span class="kk cy">Engenharia \u00b7 Inox 304</span><h2 class="ht md">Vira <em class="cy">projeto.</em></h2><p class="htsub">Cada dobra, cada cota \u2014 antes do primeiro corte a laser.</p></div>
  <div class="pt center" id="t4"><span class="kk cy">Corte a laser \u00b7 toler\u00e2ncia m\u00ednima</span><h2 class="ht xl">O <em class="cy">detalhe</em><br>\u00e9 o produto.</h2></div>
  <div class="pt right" id="t5"><span class="kk em">Do projeto ao produto</span><h2 class="ht xl">Vira <em class="em">inox.</em></h2><p class="htsub">Acabamento escovado, logo vazada que ventila, pernas em X.</p></div>
  <div class="pt center" id="t6"><span class="kk em">A brasa encontra o litoral</span><h2 class="ht lg">Feita para <em class="em">o litoral.</em></h2></div>
  <div class="pt center" id="t7"><span class="kk em">Litoral, mato, montanha, estrada</span><h2 class="ht lg">Boa para o <em class="em">Brasil inteiro.</em></h2></div>
  <div class="pt center" id="t8"><span class="kk em">Vision Inox \u00d7 Everton Stedile</span><h2 class="ht lg">A marca<br>come\u00e7a aqui.</h2></div>
  <div id="dots"><div class="dot"></div><div class="dot"></div><div class="dot"></div><div class="dot"></div></div>
  <div id="scue"><div class="sbar"></div><span>Role para explorar</span></div>
</div>
</div>"""

HERO_JS = """// \u2500\u2500 HERO (scrollytelling \u2014 sistema de cenas) \u2500\u2500
const track=C('track'),pbar=C('pbar');
const kfPraia=C('kf-praia'),kfPraiaImg=C('kf-praiaimg'),heroVid=C('heroVid'),praiaImg=C('praiaImg');
const t1=C('t1'),t2=C('t2'),t3=C('t3'),t4=C('t4'),t5=C('t5'),t6=C('t6'),t7=C('t7'),t8=C('t8');
const scue=C('scue'),dots=[...document.querySelectorAll('#dots .dot')];
const auMusic=C('auMusic'),auEmber=C('auEmber'),sndBtn=C('sndBtn');
const intro=C('intro'),introBtn=C('introBtn'),introSkip=C('introSkip');
let vdur=0,curPh=-1,lastPr=0,sndOn=false;
const MS=114; // musica inicia em 1:54
const seg=(p,a,b)=>ez(cl((p-a)/(b-a),0,1));
const W=.020; // meia-largura do crossfade alinhado
// cenas genericas: [id, inicio, fim, fadeIn, fadeOut, zoom]
const SC=[
 ['kf-paper',.000,.050,0,1,'s'],
 ['kf-sk1',  .050,.097,1,1,'s'],
 ['kf-sk2',  .097,.143,1,1,'s'],
 ['kf-sk3',  .143,.200,1,1,'s'],
 ['kf-btec', .200,.268,1,1,'s'],
 ['kf-bren', .268,.328,1,1,'s'],
 ['kf-denc', .328,.380,1,1,'s'],
 ['kf-dgre', .380,.432,1,1,'s'],
 ['kf-inox', .432,.500,1,1,'s'],
 ['kf-camp', .651,.733,1,1,'out'],
 ['kf-pisc', .733,.814,1,1,'in'],
 ['kf-mont', .814,.895,1,1,'out'],
 ['kf-cam',  .895,1.00,1,0,'in']
];
const SCE=SC.map(function(s){var el=C(s[0]);return {el:el,img:el?el.querySelector('img'):null,a:s[1],b:s[2],fin:s[3],fout:s[4],z:s[5]};});
function update(p){
  pbar.style.width=(cl(p,0,1)*100)+'%';
  if(p>.02)scue.classList.add('gone');else scue.classList.remove('gone');
  for(var i=0;i<SCE.length;i++){
    var s=SCE[i],o=1;
    if(s.fin)o*=seg(p,s.a-W,s.a+W);
    if(s.fout)o*=(1-seg(p,s.b-W,s.b+W));
    op(s.el,o);
    var sc,ZA=(window.innerWidth<760?0.45:1.12);
    if(s.z==='in')sc=1+seg(p,s.a,s.b)*ZA;
    else if(s.z==='out')sc=(1+ZA)-seg(p,s.a,s.b)*ZA;
    else sc=1.045-seg(p,s.a,s.b)*0.045;
    if(s.img)s.img.style.transform='scale('+sc.toFixed(3)+')';
  }
  // PRAIA: video forward(.515-.575) + reverse(.575-.610) -> img4K(.600-.625) -> zoom-in logo(.620-.651)
  op(kfPraia, seg(p,.480,.520)*(1-seg(p,.600,.625)));
  if(heroVid&&vdur){var vt; if(p<.575){vt=mp(p,.515,.575,0,vdur);}else{vt=mp(p,.575,.610,vdur,0);} vt=cl(vt,0,vdur); if(Math.abs((heroVid.currentTime||0)-vt)>.04){try{heroVid.currentTime=vt}catch(e){}}}
  op(kfPraiaImg, seg(p,.600,.625)*(1-seg(p,.631,.671)));
  if(praiaImg)praiaImg.style.transform='scale('+(1+seg(p,.620,.651)*(window.innerWidth<760?0.45:1.12)).toFixed(3)+')';
  // TEXTOS (escala e posicao variam por cena)
  op(t1, seg(p,.012,.04)*(1-seg(p,.072,.10)));
  op(t2, seg(p,.105,.14)*(1-seg(p,.178,.20)));
  op(t3, seg(p,.215,.25)*(1-seg(p,.308,.328)));
  op(t4, seg(p,.335,.36)*(1-seg(p,.41,.432)));
  op(t5, seg(p,.443,.47)*(1-seg(p,.495,.50)));
  op(t6, seg(p,.515,.55)*(1-seg(p,.585,.61)));
  op(t7, seg(p,.745,.78)*(1-seg(p,.875,.90)));
  op(t8, seg(p,.905,.94)*(1-seg(p,.985,1.0)));
  var ph=p<.20?0:p<.432?1:p<.651?2:3;
  if(ph!==curPh){dots.forEach((d,i)=>d.classList.toggle('on',i===ph));curPh=ph}
}
function applyAudio(pr){
  if(!sndOn)return;
  // musica forte no build-up (atos 1-4), sai na lifestyle (.47-.57), volta baixa nas secoes (pr>1)
  auMusic.volume=cl(0.78*cl(1-seg(pr,.47,.57),0,1)+0.34*seg(pr,1.0,1.12),0,1);
  // brasa entra na praia (.50-.60), fica na lifestyle, some nas secoes (pr>1)
  auEmber.volume=cl(0.85*seg(pr,.50,.60)*(1-seg(pr,1.0,1.08)),0,1);
}
let tick=false;
function onScroll(){if(!tick){requestAnimationFrame(function(){if(track){var r=track.getBoundingClientRect();var rng=r.height-window.innerHeight;var pr=(rng>0?-r.top/rng:0);lastPr=pr;update(cl(pr,0,1));applyAudio(pr);}tick=false});tick=true}}
function initHeroVideo(){
  if(!heroVid)return;
  heroVid.addEventListener('loadedmetadata',function(){vdur=heroVid.duration||5;onScroll();});
  heroVid.addEventListener('loadeddata',function(){var pr=heroVid.play();if(pr&&pr.then){pr.then(function(){heroVid.pause();heroVid.currentTime=0;onScroll();}).catch(function(){try{heroVid.currentTime=0}catch(e){}onScroll();});}else{try{heroVid.pause();heroVid.currentTime=0}catch(e){}onScroll();}});
}
function setSound(on){
  sndOn=on; if(sndBtn){sndBtn.classList.toggle('on',on);}
  if(on){try{auMusic.currentTime=MS}catch(e){} auMusic.volume=0;auEmber.volume=0; var a=auMusic.play(),e2=auEmber.play(); if(a&&a.catch)a.catch(function(){}); if(e2&&e2.catch)e2.catch(function(){}); applyAudio(lastPr);}
  else{auMusic.pause();auEmber.pause();}
}
if(sndBtn){sndBtn.addEventListener('click',function(){setSound(!sndOn);});}
function lockScroll(){document.documentElement.style.overflow='hidden';document.body.style.overflow='hidden';}
function unlockScroll(){document.documentElement.style.overflow='';document.body.style.overflow='';}
function enterExperience(withSound){
  if(withSound)setSound(true);
  if(sndBtn)sndBtn.style.display='flex';
  if(intro)intro.classList.add('gone');
  unlockScroll();
  setTimeout(function(){if(intro)intro.style.display='none';},1200);
}
if(introBtn)introBtn.addEventListener('click',function(){enterExperience(true);});
if(introSkip)introSkip.addEventListener('click',function(){enterExperience(false);});
if(intro){lockScroll();}
// acende o retrato do fecho quando entra na viewport
var _pcl=C('pclose');
if(_pcl&&'IntersectionObserver' in window){new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){_pcl.classList.add('lit');}})},{threshold:.32}).observe(_pcl);}
"""

P = P[:P.index('/* \u2500\u2500 HERO \u2500\u2500 */')] + HERO_CSS + P[P.index('/* \u2500\u2500 PROPOSTA \u2500\u2500 */'):]
hs=P.index('<!-- \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 HERO'); he=P.index('<!-- \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 SE\u00c7\u00c3O 01')
P = P[:hs] + HERO_HTML + '\n\n' + P[he:]
js=P.index('// \u2500\u2500 HERO ELEMENTS \u2500\u2500'); je=P.index('// \u2500\u2500 PROPOSTA: REVEAL')
P = P[:js] + HERO_JS + '\n' + P[je:]
P = P.replace("initL();update(0);resizeP();","update(0);initHeroVideo();")
P = P.replace("window.addEventListener('resize',resizeP,{passive:true});","window.addEventListener('resize',onScroll,{passive:true});")

# CSS extra: pos-shot + retrato do fecho
P=P.replace('</style>',
   '\n/* lifestyle no posicionamento */\n'
   '.pos-shot{margin-top:50px;border-radius:18px;overflow:hidden;position:relative;border:1px solid var(--line)}\n'
   '.pos-shot img{width:100%;height:auto;max-height:520px;object-fit:cover;display:block}\n'
   '.pos-shot .pos-cap{position:absolute;left:22px;bottom:16px;font:700 11px/1 var(--fs);letter-spacing:.18em;text-transform:uppercase;color:#fff;text-shadow:0 1px 14px rgba(0,0,0,.85)}\n'
   '/* retrato do fecho */\n'
   '.pclose{position:relative;padding:clamp(80px,12vh,150px) 0;background:linear-gradient(180deg,var(--bg),#0c0a08 52%,var(--bg));overflow:hidden}\n'
   '.pclose .pcwrap{max-width:1080px;margin:0 auto;padding:0 max(5vw,22px);display:grid;grid-template-columns:.82fr 1fr;gap:clamp(28px,5vw,64px);align-items:center}\n'
   '.pc-photo{position:relative;border-radius:18px;overflow:hidden;aspect-ratio:1/1;border:1px solid var(--line)}\n'
   '.pc-photo img{width:100%;height:100%;object-fit:cover;display:block;filter:grayscale(1) contrast(1.04) brightness(.9);transition:filter 1.6s ease;transform:scale(1.02)}\n'
   '.pc-photo::after{content:"";position:absolute;inset:0;background:radial-gradient(ellipse 75% 65% at 62% 42%,rgba(255,90,20,.6),transparent 72%);mix-blend-mode:color-dodge;opacity:0;transition:opacity 1.8s ease;pointer-events:none}\n'
   '.pclose.lit .pc-photo img{filter:grayscale(.32) contrast(1.05) brightness(1.02) sepia(.18)}\n'
   '.pclose.lit .pc-photo::after{opacity:.62}\n'
   '.pc-kk{font-family:var(--fs);font-weight:800;font-size:11px;letter-spacing:.28em;text-transform:uppercase;color:var(--e2);display:block;margin-bottom:18px}\n'
   '.pc-text h2{font-family:var(--fd);font-weight:300;font-size:clamp(30px,4.5vw,60px);line-height:1.04;letter-spacing:-.022em;color:var(--text)}\n'
   '.pc-text h2 em{font-style:italic;color:var(--e2)}\n'
   '.pc-text p{color:var(--dim);font-size:16px;line-height:1.66;margin-top:22px;max-width:44ch}\n'
   '@media(max-width:820px){.pclose .pcwrap{grid-template-columns:1fr;gap:28px}.pc-photo{max-width:360px;margin:0 auto;width:100%}}\n'
   '</style>',1)
P=P.replace('marca especialista, premium e confi\u00e1vel.</b></p>',
   'marca especialista, premium e confi\u00e1vel.</b></p>\n'
   '    <div class="pos-shot rv d2"><img src="assets/praia_final.png" alt="Vision Inox no litoral ao p\u00f4r do sol"><span class="pos-cap">Conceito de dire\u00e7\u00e3o \u00b7 o produto no seu territ\u00f3rio</span></div>',1)

def cstart(s,m):
    i=s.index(m); return s.rfind('<!--',0,i)
a=cstart(P,'SE\u00c7\u00c3O 04B'); b=cstart(P,'SE\u00c7\u00c3O 05')
P=P[:a]+'<!-- PRODUTO (evolucao) -->\n'+EVO+'\n\n'+P[b:]

# retrato do fecho (antes do contato)
portrait='''<!-- RETRATO / FECHO HUMANO -->
<section class="pclose" id="pclose">
  <div class="pcwrap">
    <div class="pc-photo rv"><img src="assets/retrato.jpg" alt="Everton Stedile"></div>
    <div class="pc-text">
      <span class="pc-kk rv">Quem assina isso</span>
      <h2 class="rv d1">Estrat\u00e9gia n\u00e3o se <em>terceiriza.</em><br>Se <em>assina.</em></h2>
      <p class="rv d2">Da marca ao \u00faltimo pixel desta p\u00e1gina, tudo passou por uma s\u00f3 cabe\u00e7a. Sem repasse, sem telefone sem fio. Voc\u00ea fala comigo \u2014 e \u00e9 comigo que sai.</p>
    </div>
  </div>
</section>'''

c=cstart(P,'SE\u00c7\u00c3O 09'); d=P.index('<footer>')
contato='''<!-- CONTATO / FECHO -->
<section class="close" id="contato">
  <div class="wrap">
    <h2 class="rv">A Vision j\u00e1 fabrica o melhor inox.<br><em>Vamos fazer o Brasil saber disso.</em></h2>
    <p class="rv d1" style="color:var(--dim);font-size:16px;line-height:1.65;max-width:52ch;margin:26px auto 0">O pr\u00f3ximo passo n\u00e3o \u00e9 assinar nada \u2014 \u00e9 uma conversa para alinhar escopo, metas e o formato da parceria.</p>
    <div class="rv d2" style="margin-top:40px;display:flex;gap:14px;justify-content:center;flex-wrap:wrap">
      <a class="cw-btn" href="https://wa.me/5548991578012">Falar no WhatsApp<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
      <a class="cw-btn" href="mailto:evertonstedile@gmail.com" style="background:transparent;color:var(--e2);border:1px solid rgba(255,122,26,.4)">Enviar e-mail</a>
    </div>
    <div class="sig rv d3"><span class="nm">Everton Stedile</span><span class="ti">Estrat\u00e9gia &amp; Execu\u00e7\u00e3o \u00b7 Marca, Produto e E-commerce</span></div>
  </div>
</section>'''
P=P[:c]+CW+'\n\n'+portrait+'\n\n'+contato+'\n\n'+P[d:]

P=P.replace(
 'Proposta estrat\u00e9gica confidencial \u00b7 Vision Inox \u00b7 Everton Stedile \u00b7 valores e proje\u00e7\u00f5es sujeitos a valida\u00e7\u00e3o em diagn\u00f3stico',
 'Proposta estrat\u00e9gica confidencial \u00b7 Everton Stedile \u00b7 \u201cVision Inox\u201d \u00e9 nome ilustrativo de trabalho \u2014 a identidade definitiva \u00e9 entreg\u00e1vel do projeto \u00b7 proje\u00e7\u00f5es sujeitas a valida\u00e7\u00e3o em diagn\u00f3stico')

open('/home/claude/vision/build/index.html','w',encoding='utf-8').write(P)
print('index.html len:',len(P),'chars')
