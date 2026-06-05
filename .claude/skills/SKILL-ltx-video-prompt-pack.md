---
name: ltx-video-prompt-pack
description: >
  Templates de prompt para LTX 2.3 (open-source, 22B params, 4K nativo, áudio sincronizado)
  aplicados ao projeto Vision Inox. Cobre cada segmento do vídeo hero scroll-driven:
  blueprint, materialização, brasa e litoral. Inclui parâmetros técnicos, direção de câmera,
  workflow de segmentação e instrução de integração no hero HTML.
trigger: >
  Ativar quando o usuário pedir: gerar vídeo, prompt LTX, animação de produto,
  segmento de vídeo, image-to-video, keyframe, cena de brasa, cena de praia,
  vídeo do hero, montar vídeo, scrubbing.
---

# LTX 2.3 — Video Prompt Pack Vision Inox

## Princípio Fundamental — Leia Antes de Gerar

### NÃO tente fazer o vídeo inteiro em um prompt
A transformação "blueprint → produto → praia" em uma tomada única = alucinação garantida.
Nenhum modelo de vídeo atual faz transformação morfológica longa de forma controlada.

### A abordagem correta: SEGMENTAR por keyframes
```
Cada segmento = 5-10 segundos | Cada um parte de um keyframe fixo (imagem GPT Image 2)
Os keyframes garantem consistência do produto entre cenas
Na edição: costura os segmentos com cross-fade ou corte seco
No hero HTML: o scroll-scrubbing toca o vídeo costurado frame a frame
```

### Mapa de segmentos do hero
```
SEG-1: Blueprint   (5-7s) — text-to-video OU image-to-video com referência técnica
SEG-2: Montagem    (5-7s) — image-to-video: flat-pack se encaixando
SEG-3: Materialização (7-8s) — image-to-video: inox ganha brilho, reflexo de luz
SEG-4: Brasa       (6-8s) — image-to-video: brasa acende, partículas sobem
SEG-5: Litoral     (8-10s) — image-to-video: produto na praia, golden hour
TOTAL: ~35-45 segundos costurados → controlados por scroll no hero
```

---

## Parâmetros Técnicos LTX 2.3

### Specs do modelo
```
Modelo: LTX-2.3 (Lightricks, lançado 5 março 2026)
Parâmetros: 22 bilhões (vídeo) + 5B (áudio)
Resolução nativa: 4K (3840x2160) a 50fps
Para web: usar 1920x1080 a 24fps — mais leve, look cinematográfico
Audio: sincronizado em single pass (gerar com/sem áudio conforme necessidade)
```

### Via fal.ai (cloud — mais simples para começar)
```python
import fal_client

# Image-to-video (recomendado — usa keyframe GPT Image como âncora)
handler = fal_client.submit(
    "fal-ai/ltx-video/image-to-video",
    arguments={
        "image_url": "URL_DA_IMAGEM_KEYFRAME",  # output do GPT Image 2
        "prompt": "[PROMPT DO SEGMENTO ABAIXO]",
        "negative_prompt": "blurry, low quality, watermark, text overlay, generic, stock footage",
        "num_frames": 121,    # ~5s a 24fps
        "fps": 24,
        "width": 1920,
        "height": 1080,
        "guidance_scale": 3.5,   # 3.0-4.5: mais baixo = mais criativo, mais alto = mais fiel
        "num_inference_steps": 50,
        "seed": 42              # fixar seed para reproducibilidade
    }
)

# Text-to-video (quando não há keyframe ainda)
handler = fal_client.submit(
    "fal-ai/ltx-video",
    arguments={
        "prompt": "[PROMPT]",
        "negative_prompt": "blurry, shaky, low quality, watermark, ugly, deformed",
        "num_frames": 121,
        "fps": 24,
        "width": 1920,
        "height": 1080,
        "guidance_scale": 3.5,
        "num_inference_steps": 50,
        "seed": 42
    }
)
```

### Via ComfyUI (local — custo zero, mais controle)
```
Modelo: download em huggingface.co/Lightricks/LTX-Video
ComfyUI node: LightricksLTXVideo (integrado ao ComfyUI core)
VRAM recomendada: 16GB+ (NVFP8 quantizado: ~12GB)
Workflow: image_url → LTX Video node → output MP4
```

### Negative prompt padrão (usar em TODOS os segmentos)
```
blurry, low quality, motion blur, shaky camera, watermark, logo, text overlay,
generic stock footage, overexposed, underexposed, grain, noise, artifacts,
deformed product, inconsistent proportions, wrong material (not stainless steel),
ugly, distorted, cheap looking, plastic appearance
```

---

## SEGMENTO 1 — Blueprint Técnica

**Keyframe de entrada:** Nenhum (text-to-video) OU imagem de blueprint gerada no GPT Image 2 (Bloco 1A)
**Duração:** 5-7 segundos
**FPS:** 24
**Movimento de câmera:** Lento zoom-in frontal, ou câmera estática com elementos que aparecem

```
[PROMPT SEG-1]
Technical engineering animation. A precise stainless steel portable barbecue grill
technical blueprint being drawn in real-time on deep graphite background.

Visual style: cyan (#00E5FF) linework on #090909 dark background, engineering grid
visible. The grill outline in 3/4 isometric perspective draws itself progressively
from top-to-bottom — first the top face outline, then the front face, then the lateral.
After the outline is complete, technical annotation lines appear: "INOX 304",
"Anti-warp rib", "Adjustable grill", dimension callouts.

Camera: static. The drawing happens within the frame — no camera movement.
End frame: complete blueprint fully drawn with all annotations visible.
Atmosphere: precise, technical, quiet. Like watching an engineer sketch their masterpiece.
No fire, no heat, no food — pure engineering.

Lighting: only the cyan linework emits light against the dark background.
Motion: smooth and controlled, each line appears at deliberate pace.
```

**Dica de refinamento:** Se o LTX alucinar o produto, usar o keyframe 1A do GPT Image 2
como `image_url` com guidance_scale 4.0-4.5 para maior fidelidade à referência.

---

## SEGMENTO 2 — Montagem Flat-Pack

**Keyframe de entrada:** Imagem do produto desmontado (flat-pack) — GPT Image 2 Bloco 2A com produto parcialmente montado
**Duração:** 5-7 segundos
**FPS:** 24
**Movimento de câmera:** Leve rotação em arco, 15° máximo

```
[PROMPT SEG-2]
Product assembly animation of a premium stainless steel 304 brushed portable grill.
The flat panels slide together and click into place with laser-precise interlocking tabs.

The animation shows: two side panels rotating upright from flat position, front panel
sliding into notches with satisfying precision, lateral panel clicking into tabs,
legs unfolding outward at 45°, finally the grill grate placed on top completing the assembly.

Each connection makes a subtle visual pulse — a brief edge highlight showing the
laser-cut precision of the joint. The stainless steel panels have consistent brushed finish.

Camera: slow arc movement from 3/4 view rotating 15° to the right as the assembly completes.
Lighting: cool studio key light from upper-left, specular highlights revealing metal texture.
End frame: assembled grill, perfectly formed, standing on dark matte surface. Same angle as hero shot.
Speed: smooth and deliberate — not rushed. Premium product deserves premium assembly reveal.
Background: deep matte black (#090909), subtle radial gradient.
```

---

## SEGMENTO 3 — Materialização Inox

**Keyframe de entrada:** GPT Image 2 Bloco 2A (produto 3/4 principal) — USE COMO IMAGE_URL
**Duração:** 7-8 segundos
**FPS:** 24
**Movimento de câmera:** Lento zoom-out de close para shot completo

```
[PROMPT SEG-3]
Cinematic reveal of a premium brushed stainless steel 304 portable barbecue grill.
A single dramatic studio light slowly sweeps across the metal surface — from left to right —
progressively revealing the uniform brushed finish texture in exquisite detail.

The specular highlight travels across the top grill bars first (each bar catches the light
sequentially), then sweeps across the front ventilation slots (each slot edge lights up
showing precision chamfering), finally illuminates the integrated oval handle on the lateral face.

Camera: starts tight on the brushed texture (macro), slowly pulls back to reveal the
complete grill in 3/4 perspective. Final frame: full product, centered, perfectly lit.
Lighting: dramatic single key light sweep (from 90° to 30°), dark background, no fill.
Feel: this is how you reveal a fine camera or watch — precision, weight, quality.
Audio (if generating): subtle metal resonance, low-frequency room tone. No music yet.
Background: matte black. Subtle reflection on surface below.
Duration: the light sweep takes the full 7-8 seconds — slow, deliberate, cinematic.
```

**Dica crítica:** Este é o segmento mais difícil de acertar. Guidance_scale 4.0+ e usar
obrigatoriamente o keyframe do GPT Image 2 como âncora. Seed fixo para manter consistência
se precisar renegerar. Testar múltiplos seeds (42, 123, 777) e escolher o melhor.

---

## SEGMENTO 4 — Brasa Acende

**Keyframe de entrada:** GPT Image 2 Bloco 2A (produto montado) OU foto de brasa no interior
**Duração:** 6-8 segundos
**FPS:** 24
**Movimento de câmera:** Câmera levemente desce, focando nas ventilações com glow

```
[PROMPT SEG-4]
Cinematic moment of charcoal embers igniting inside a premium stainless steel 304
portable grill. The camera starts at eye-level with the front ventilation slots and
slowly tilts down slightly as orange ember glow intensifies through the slots.

Visual progression: first slot barely glowing amber → all 6 slots emanating warm orange
light (#ff7a1a) → wisps of smoke begin rising from the top grill bars → the ember glow
pulsates gently, alive. The brushed stainless steel surface surrounding the vents
catches the warm orange light in specular highlights, contrasting with the cool silver
of the metal in shadow.

Particles: very fine ash particles float upward slowly from the top grill.
Camera: static with gentle handheld breathing effect (barely perceptible, 0.5px movement).
Tilt: starts at ventilation slot level, tilts slightly down over 3 seconds, then holds.
Background: near-black, the grill occupies center-right of frame.
Lighting: the only light source IS the ember glow — no studio key light.
Atmosphere: intimate, primal, desire. The anticipation of a great meal about to begin.
Audio (if generating): charcoal crackling, ember pops, subtle ambient warmth.
End frame: steady ember glow through all vents, smoke rising, anticipation peak.
```

---

## SEGMENTO 5 — Litoral / Golden Hour

**Keyframe de entrada:** GPT Image 2 Bloco 4A (produto na praia, golden hour) — USE COMO IMAGE_URL
**Duração:** 8-10 segundos
**FPS:** 24
**Movimento de câmera:** Lento zoom-out + leve push forward no início

```
[PROMPT SEG-5]
Cinematic lifestyle footage of a premium stainless steel portable grill on a beachfront
deck at golden hour sunset. Charcoal burning, light smoke rising against the warm sky.

The shot starts tight on the grill — brushed stainless catching amber-golden sunset light
(#ff7a1a specular highlights across brushed surface), embers glowing through ventilation slots.
Camera slowly pulls back over 5 seconds to reveal the coastal setting: teak wood deck,
sea visible in background, warm golden light, a hand reaching in from frame right
to place a piece of meat on the grill without looking at camera.

Background: sea or coastal landscape, slightly out of focus (f/2.8 DOE equivalent),
golden hour light painting everything in warm amber and deep blue shadow contrast.
People: minimal, partial — a hand, a silhouette. Not stock photo posing.
Atmosphere: aspirational without being fake. Real beach life, real fire, real food.
Color grade: warm, cinematic — Yeti Coolers / Patagonia campaign aesthetic.
Tones: ember amber (#ffb02e), deep sea blue (#0d2030) in shadows, inox silver warm.
Camera movement: combined slow push-in + pull-back creates subtle parallax effect.
Wind: very subtle — smoke direction consistent, no strong wind.
Audio: sea waves faintly, crackling embers, optional distant conversation.
End frame: grill in golden light, sea in background, smoke rising — this is the brand image.
```

---

## BLOCO DE ÁUDIO (LTX 2.3 Audio Sincronizado)

LTX 2.3 gera áudio sincronizado em single pass. Para o vídeo hero web, o áudio fica MUTED
por padrão (autoplay policy dos browsers). O áudio tem valor em:
- Versão para Instagram/Reels (usuário clica para ouvir)
- Versão para YouTube pre-roll
- Versão para apresentações

### Direção de áudio por segmento
```
SEG-1 (Blueprint): Silêncio quase total, apenas hum suave de sala — foco visual
SEG-2 (Montagem): Cliques metálicos de encaixe, som satisfatório de precisão
SEG-3 (Materialização): Silêncio dramático com leve reverb metálico
SEG-4 (Brasa): Carvão crepitando, estalos de brasa, calor sonoro
SEG-5 (Litoral): Ondas do mar, brasa suave, vento leve, ambient warm
```

### Prompt de áudio (adicionar ao final dos prompts de vídeo se querer áudio)
```
[ADICIONAR AO FINAL DE CADA PROMPT]
Audio: [descrição específica do segmento acima]. No music, no voiceover.
Pure ambient sound — diegetic only. Professional sound design, not generic stock audio.
```

---

## Workflow Completo de Produção

### Fase 1: Gerar keyframes no GPT Image 2
```
1. Produto 3/4 principal (Bloco 2A) → keyframe para SEG-3, SEG-2
2. Produto em brasa/golden hour (Bloco 4A) → keyframe para SEG-5
3. Blueprint (Bloco 1A) → referência para SEG-1 (opcional)
4. Close-up ventilação com glow (Bloco 6B) → referência para SEG-4
```

### Fase 2: Gerar segmentos no LTX 2.3
```
Ordem recomendada (do mais simples ao mais difícil):
1. SEG-1 (blueprint) — text-to-video, mais tolerante
2. SEG-5 (litoral) — image-to-video com 4A como âncora, mais estético
3. SEG-4 (brasa) — image-to-video, resultado tende a ser bonito
4. SEG-2 (montagem) — image-to-video, resultado variável
5. SEG-3 (materialização) — o mais difícil, requer mais tentativas
```

### Fase 3: Review por segmento
Avaliar cada segmento com:
- [ ] O produto mantém as proporções corretas?
- [ ] O acabamento inox está consistente com o keyframe?
- [ ] O movimento de câmera está suave e intencional?
- [ ] A iluminação é coerente com a direção de arte?
- [ ] A duração está entre 5-10s?
- [ ] O início e fim são bons para cross-fade com o segmento adjacente?

### Fase 4: Edição e costura
```
Software: CapCut, DaVinci Resolve (grátis), Final Cut Pro, ou Premiere
Método de costura: cross-fade de 12-18 frames (0.5-0.75s) entre segmentos
Cor: aplicar grade cinematográfica unificada nos 5 segmentos
  - Sombras: leve azul-grafite (#0a1020)
  - Meios-tons: neutro/warm
  - Altas luzes: leve âmbar warm (#fff8f0)
  - Saturação: -8 a -12 (levemente dessaturado = mais premium)
Exportar: MP4 H.264 ou H.265, 1920x1080, 24fps, ~40-60 Mbps para master
Para web: converter para WebM VP9 ou H.264 otimizado (FFmpeg)
```

### Fase 5: Integração no hero HTML (scroll-scrubbing)
```javascript
// Substituir o slot de vídeo no hero-vision-inox.html:
// Trocar o div.slot-box dentro de #bg3 por:

<video id="heroVideo" muted playsinline preload="auto"
  style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0;">
  <source src="hero-vision-inox.webm" type="video/webm">
  <source src="hero-vision-inox.mp4" type="video/mp4">
</video>

// No JS, adicionar ao update(p) para controle por scroll:
const heroVideo = document.getElementById('heroVideo');
if(heroVideo && heroVideo.duration) {
  const videoProgress = clamp(mp(p, 0, 1, 0, 1), 0, 1);
  heroVideo.currentTime = videoProgress * heroVideo.duration;
  heroVideo.style.opacity = 1;  // ou controlar conforme fase
}

// Pré-carregar todos os frames:
heroVideo.addEventListener('loadedmetadata', () => {
  heroVideo.currentTime = 0;  // força load do primeiro frame
});
```

---

## Fallbacks e Alternativas

### Se o LTX 2.3 não der o resultado esperado:
```
Alternativas proprietárias para testar (por tipo de cena):
- SEG-3 e SEG-5 (realismo máximo): Kling 3.0 ou Veo 3.1
- SEG-4 (brasa/fogo): Kling 3.0 (melhor com fogo/partículas)
- SEG-1 (blueprint): pode ser feito sem IA — o SVG animado do hero já cobre
- SEG-2 (montagem): Sora 2 ou Runway Gen-4 Turbo para movimento de câmera suave

Plataformas cloud:
- fal.ai (LTX 2.3 + outros modelos)
- Cliprise (Seedance 2.0, Kling 3.0, Veo 3.1, Sora 2, Runway Gen-4 Turbo)
- Runway (Gen-4 Turbo — bom para lifestyle)
- Kling (API disponível — melhor para movimento de produto)
```

### Se não tiver GPT Image 2 ainda:
```
Usar as 14 fotos reais do protótipo diretamente como image_url no LTX.
Guidance_scale mais alto (4.0-4.5) para manter fidelidade ao produto real.
Qualidade será menor na materialização premium, mas funciona para validação.
```

### Versão mínima viável (MVP do vídeo):
```
Se quiser lançar antes de ter o vídeo completo:
- O hero SVG animado (blueprint + materialização + brasa em SVG) já está pronto e funcional
- Adicionar APENAS o SEG-5 (litoral, 8-10s) no slot de praia
- O SVG faz os segmentos 1-4, o vídeo real faz apenas o 5 (a cena de desejo)
- Impacto: 85% do resultado final com 20% do esforço de produção
```

---

## Instruções Claude Code (Playwright + integração)

```bash
# Screenshot do hero com vídeo integrado para review:
npx playwright screenshot file:///caminho/hero-vision-inox.html \
  hero-review-desktop.png --viewport-size=1440,900

# Tirar screenshot do frame específico (simular scroll no meio):
npx playwright eval "
  const page = await browser.newPage();
  await page.goto('file:///caminho/hero.html');
  await page.evaluate(() => window.scrollTo(0, document.body.scrollHeight * 0.6));
  await page.screenshot({path: 'hero-brasa-frame.png'});
"

# Converter vídeo para web-otimizado (FFmpeg):
ffmpeg -i hero-vision-inox-master.mp4 \
  -c:v libvpx-vp9 -b:v 2M -an \
  hero-vision-inox.webm

ffmpeg -i hero-vision-inox-master.mp4 \
  -c:v libx264 -preset slow -crf 22 -an \
  -movflags +faststart hero-vision-inox-web.mp4
```

---

*Skill criada para: projeto Vision Inox | Consultoria: Everton Stedile*
*Ferramenta: LTX 2.3 (Lightricks, 5 março 2026) | 22B params | 4K nativo | Open-weight*
*Integração via: fal.ai API ou ComfyUI local | Hero HTML: scroll-scrubbing currentTime*
