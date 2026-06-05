---
name: gpt-image-prompt-pack
description: >
  Templates de prompt para GPT Image 2 (gpt-image-2) aplicados ao projeto Vision Inox.
  Todos os prompts partem das 14 fotos reais do protótipo como referência de pixel-stability.
  Cobre: blueprint técnica, produto melhorado, detalhes de diferenciação, lifestyle litoral,
  embalagem premium e variações para mídia paga.
trigger: >
  Ativar quando o usuário pedir: gerar imagem, prompt de imagem, GPT Image, melhorar foto
  do produto, blueprint IA, cena de praia, produto melhorado, render, conceito visual.
---

# GPT Image 2 — Prompt Pack Vision Inox

## Contexto Obrigatório Antes de Qualquer Geração

### O Produto (referência de consistência)
- Churrasqueira portátil flat-pack, inox 304 escovado
- Forma: retangular, encaixe por abas laser (tab-and-slot), sem solda
- Faces: frontal (rasgos de ventilação vertical), lateral (pega oval), superior (grelha de barras)
- Pernas: 4 pernas finas em V
- Tamanho estimado: ~30cm L × 25cm A × 15cm P
- Acabamento: escovado uniforme (brushed), bordas tratadas, reflexo de luz controlado
- 14 fotos reais disponíveis como referência (tiradas em ambiente de fábrica)

### Como Usar as Fotos Reais no GPT Image 2
```
API: gpt-image-2 (ou gpt-image-2-2026-04-21)
Parâmetro: até 16 imagens como referência simultânea
Pixel-stability: o modelo mantém o produto consistente entre edições
Multi-turn: manter o contexto entre gerações para consistência
Resolução: 1536x1024 (landscape) ou 1024x1536 (portrait) ou custom até 3840x2160
Quality: "high" para entregáveis finais, "medium" para testes
```

### Estrutura de Prompt (extraído de Huashu Design)
```
[Constraint filosófico — POR QUE assim, não COMO parece]
+ [Descrição específica do conteúdo]
+ [Parâmetros técnicos — iluminação, ângulo, acabamento, cores]
```

Sempre usar características concretas, nunca palavras vagas:
- ❌ "estilo premium" → ✅ "iluminação de estúdio Leica com key light a 45° esquerda"
- ❌ "fundo moderno" → ✅ "fundo de granito preto fosco com reflexo sutil"
- ❌ "foto bonita" → ✅ "proporção 2:3, bokeh f/2.8, foco em encaixe das abas"

---

## BLOCO 1: Blueprint Técnica

### 1A — Blueprint Perspectiva 3/4 Completa
**Uso:** hero da proposta, seção de diferenciação, material técnico
```
[PROMPT]
Technical blueprint drawing of a compact portable charcoal grill, perspective 3/4 view,
inspired by engineering drafting and industrial design documentation.

Style: precise vector linework in electric cyan (#00E5FF) on deep graphite background (#090909),
ultra-thin strokes (0.8-1.4pt), grid overlay in navy blue (#0A2030) at 40px intervals,
sub-grid at 8px in near-black (#071525).

Details to show: front face with 6 rectangular ventilation slots (rounded corners r=4px),
right lateral face with integrated oval handle, top face as parallel grill bars perspective,
tab-and-slot assembly notches visible at edges, 4 angled V-shaped legs below.
Perspective: isometric-influenced 3/4 from upper-left, showing 3 faces simultaneously.

Annotations: technical callout lines pointing to key features — "INOX 304" left side,
"Anti-warp rib" top edge, "Adjustable grill — 3 heights" top face, "Laser-cut precision"
slots area, "Flat-pack logistics" below legs, dimension cota "H 240mm" left.
Text in Archivo font, 10-11px, same cyan color.

Photography: not photographic — engineering drawing aesthetic, crisp lines, no gradients
on elements, technical precision over beauty.
Resolution: 1536x1024, high quality.
```

### 1B — Blueprint Close-up Detalhe de Encaixe
**Uso:** seção de diferenciação "Encaixe precisão laser"
```
[PROMPT]
Close-up technical blueprint drawing focusing on the tab-and-slot laser-cut joint detail
of a stainless steel portable grill assembly. Two panels connecting via precise interlocking
tabs, shown in exploded view — 2mm apart, about to click into place.

Style: electric cyan (#00E5FF) linework on #090909, high zoom, isometric exploded view,
measurement callout showing 0.1mm tolerance, annotation "Precision laser cut — zero gap",
subtle glowing effect on the tab edges (feGaussianBlur filter aesthetic).
Background: deep graphite with fine grid, technical documentation feel.
Resolution: 1024x1024, high quality.
```

---

## BLOCO 2: Produto Melhorado — Versão Premium (Norte de Design)

### INSTRUÇÃO CRÍTICA ANTES DE GERAR
As imagens geradas neste bloco são **CONCEITO DE DESIGN / NORTE DE DIREÇÃO**.
Servem como briefing visual para a fábrica e referência para o vídeo LTX.
NÃO apresentar como foto do produto atual. Apresentar como "produto que será fabricado".

A Vision tem flexibilidade total de redesenho — o objetivo é mostrar O QUE FAZER,
e eles produzem com corte a laser do jeito que o design indicar.

### 2A — Produto em Estúdio, Ângulo 3/4 Principal
**Uso:** hero do e-commerce, página de produto, material de marketing principal
```
[PROMPT — com imagens reais do protótipo como referência]
Professional product photography of a compact portable stainless steel barbecue grill,
perspective 3/4 from upper-left angle, showing front face, lateral face, and top grill.

Upgrades from reference photos: uniform brushed finish (no fingerprints, no scratches),
perfectly sharp laser-cut edges with chamfered treatment, ventilation slots with
consistent rounded corners, integrated oval handle polished smooth, clean flat-pack
assembly with invisible seams, legs with precise V-shape and small rubber feet tips.

Lighting: studio product photography, single key light from upper-left at 35° angle
creating specular highlight across the top grill surface, soft fill from right,
no harsh shadows — similar to Leica or Bang & Olufsen product photography.
Background: deep matte black (#090909) with very subtle radial gradient vignette.
Surface: the grill rests on a dark matte surface, slight reflection below (not mirror).
Color: brushed stainless 304 steel — cool silver with subtle warm highlights from key light.

Mood: weight, quality, precision. The object looks like it costs R$800.
Resolution: 1536x1024, high quality.
```

### 2B — Produto Close-up Textura Inox
**Uso:** detalhe para página de produto, proof of quality, ads de conversão
```
[PROMPT — com fotos do protótipo como referência]
Extreme close-up macro photography of brushed stainless steel 304 surface of a premium
portable grill. Focus on the brushed texture pattern — parallel fine striations in the
metal catching light at micro level. One ventilation slot partially visible at edge,
showing precision laser-cut rounded corners with chamfered treatment.

Lighting: raking light from 90° angle to maximize texture visibility, near-specular
highlight across the brushed surface creating a gradient from bright silver to deep grey.
Background: out-of-focus dark graphite.
Depth of field: f/2.8 macro equivalent, sharp focus on texture center, soft edges.
Color: cool silver (#edeff2) center highlight transitioning to (#7b7f88) in shadows.
Feel: this is military-grade material used in food industry equipment. Not decorative.

Resolution: 1024x1024, high quality.
```

### 2C — Produto 3/4 Ângulo Alternativo (Lateral Esquerda)
**Uso:** variação para anúncios, carrossel de produto
```
[PROMPT — com fotos do protótipo como referência]
Professional product photography of compact stainless steel portable grill,
perspective 3/4 from upper-right angle, showing lateral face with oval integrated
handle prominently, partial front face with ventilation slots, and partial grill top.

Same studio setup as main angle: key light upper-left, matte black background,
brushed stainless finish uniform, all edges clean and chamfered, V-legs precise.
Emphasize the oval handle — it should look ergonomic and intentional, not stamped.
The handle slot should have a clean edge highlight showing wall thickness of material.

Resolution: 1024x1536, high quality. Vertical format for Stories/Reels use.
```

### 2D — Produto Vista Superior (Top-Down)
**Uso:** mostrar a grelha ajustável, diferencial técnico
```
[PROMPT — com fotos do protótipo como referência]
Top-down overhead studio photography of compact portable stainless steel grill.
Camera directly above, perfectly centered, showing grill bars in full detail.
Grill bars: parallel brushed stainless bars with consistent 8mm spacing,
slight specular highlight running along each bar from key light positioned at 30°.
The grill structure below visible through the bars — dark interior contrast.
Background: matte black surface, soft shadow circle around the grill.

Annotation concept: three arrows indicating grill height levels (low/mid/high)
in the image corner — minimal, engineering-style callout.
Resolution: 1024x1024, high quality.
```

---

## BLOCO 3: Detalhes de Diferenciação

### 3A — Comparativo Anti-empeno (Antes / Depois)
**Uso:** seção de diferenciação, ads de awareness
```
[PROMPT]
Split-frame product comparison image, divided vertically at center.

LEFT SIDE — "Problem": warped and deformed cheap portable grill, visible bending and
cupping of the thin metal panels after heat exposure, raw edges, generic look.
Cooler, slightly desaturated blue-grey tones. Label "Common portable grill" subtle.

RIGHT SIDE — "Vision Inox": premium brushed stainless steel grill, perfectly flat panels
with structural anti-warp ribs formed in the folds, identical to reference product photos,
key light highlighting the straight precise edges. Warmer silver tones, confident.
Label "Vision Inox — anti-warp engineering" subtle.

Center divider: thin cyan line (#00E5FF) 1px.
Style: product photography, both at identical camera angle (3/4 perspective),
same scale, same background (dark matte). No people, no props — just the products.
Resolution: 1536x1024, high quality.
```

### 3B — Inox 304 vs Genérico — Maresia
**Uso:** seção litoral, ads de awareness
```
[PROMPT]
Side-by-side comparison photo in coastal/salty air environment.

LEFT: visibly rusted and corroded portable grill after beach use — orange rust stains,
pitting, degraded surface. Bleak, cautionary. Label "Common steel — 6 months by the sea".

RIGHT: Vision Inox stainless 304 grill, pristine, same brushed finish as reference photos,
looking new despite coastal context, slight sea breeze atmospheric effect.
Label "Inox 304 — lifetime by the sea".

Setting: both grills on wooden surface with subtle beach sand and soft sea light in background.
Light: overcast coastal light, natural, not studio.
Resolution: 1536x1024, high quality.
```

---

## BLOCO 4: Lifestyle / Litoral

### 4A — Produto na Praia — Golden Hour
**Uso:** hero final da proposta (slot do vídeo), página inicial do e-commerce
```
[PROMPT — com fotos do produto melhorado como referência]
Premium lifestyle photography of a stainless steel portable grill in use on a beach
deck at golden hour sunset. The grill is positioned on a teak wood surface of a
beachfront deck, sea visible in background, warm amber-golden light of sunset
reflecting off the brushed stainless surface.

Charcoal burning inside (subtle ember glow visible through ventilation slots),
light smoke rising gracefully. Optional: one or two cuts of meat on the grill,
tongs resting on the side, cold glass of beer in background (out of focus).

People: one or two people partially visible in background, relaxed, beach casual.
Not cheesy stock photo — candid, editorial feel. Not posed.
Light: warm golden (3200K), strong directional from low sun, long shadows,
inox catching orange-amber specular highlights — ember-2 (#ff7a1a) tones on metal.
Color grade: warm, slightly desaturated, cinematic — similar to Yeti Coolers campaigns.
Mood: aspirational without being fake. This is real beach life, premium.

Resolution: 1536x1024, high quality.
```

### 4B — Varanda Gourmet — Noite
**Uso:** e-commerce secondary image, social media
```
[PROMPT — com fotos do produto melhorado como referência]
Lifestyle product photography of stainless steel portable grill on a premium outdoor
deck/balcony at night with city or sea lights in background. String lights overhead,
warm ambient light, grill with live charcoal embers (orange glow from vents).

Surface: dark composite deck or concrete, wine glasses nearby, minimalist outdoor setting.
The grill should be the hero of the image — centered, well-lit by its own ember glow
plus a soft key light from upper right simulating deck lighting.
Mood: dinner party, premium outdoor entertaining, not BBQ party — refined.
Color: warm amber embers (#ffb02e), cool dark background, stainless silver catching light.

Resolution: 1024x1536, high quality. Portrait format.
```

### 4C — Produto Viagem / Camping Premium
**Uso:** expansão para camping/outdoor, secondary content
```
[PROMPT — com fotos do produto melhorado como referência]
Outdoor lifestyle photo of stainless steel portable grill in a premium camping setup.
Flat packed (assembled as a flat set of panels) leaning against a premium gear bag,
surrounded by minimalist camp setup — canvas tent, enamel coffee mug, firewood stack.

Setting: forest clearing, natural light, late afternoon.
Message: this is for the person who doesn't compromise on gear. Premium outdoors.
Style: similar to Patagonia or Snow Peak campaign photography.
The flat-pack form factor visible — showing that it packs completely flat for transport.

Resolution: 1536x1024, high quality.
```

---

## BLOCO 5: Embalagem Premium

### 5A — Unboxing Concept
**Uso:** seção de experiência de produto, UGC inspiration
```
[PROMPT]
Premium product packaging photography, unboxing concept for a high-end stainless steel
portable grill. Flat, rectangular matte-black package with minimal branding.
Inside: the grill panels arranged geometrically in the box, separated by custom die-cut
cardboard inserts. Brushed metal surface visible — premium feel.

Packaging details: embossed brand mark on box exterior, matte black exterior with subtle
texture, inside panels in natural kraft with black printing, ribbon pull-tab.
Style: Apple product unboxing photography aesthetic — clean, precise, minimal.
One hand visible gently lifting a panel from the box (editorial hands — no nail polish,
clean, casual — not corporate stock).

Lighting: soft overhead studio light, white background.
Resolution: 1536x1024, high quality.
```

---

## BLOCO 6: Variações para Mídia Paga

### 6A — Hook Visual — Dor (Ferrugem)
**Uso:** primeiro frame de ad Reels/Stories, atenção negativa
```
[PROMPT]
Close-up photography of a heavily rusted portable BBQ grill, orange rust covering
ventilation holes and structural joints. The rust is dramatic — communicating
"this is what happens when you buy cheap at the coast". Slightly desaturated,
cool tones, almost documentary. No people. Just the problem.
Format: vertical 1024x1536. Resolution: high quality.
```

### 6B — Hook Visual — Transformação (Brasa)
**Uso:** segundo frame de ad após hook, desejo emocional
```
[PROMPT — com produto melhorado como referência]
Close-up dramatic product photography of the stainless steel grill ventilation slots
with intense orange-amber ember glow emanating from inside, photographed in near-dark.
The brushed inox surface surrounding the vents receives warm orange light (#ff7a1a)
from the internal embers, contrasting with the cool silver metal in shadow.
Micro smoke wisps rising. Extremely cinematic. No props, no context — just grill and fire.
Format: vertical 1024x1536. Resolution: high quality.
```

---

## Parâmetros Técnicos GPT Image 2 (Referência)

```python
# Via API OpenAI
response = client.images.generate(
    model="gpt-image-2",
    prompt="[PROMPT DO BLOCO ACIMA]",
    n=1,
    size="1536x1024",     # ou "1024x1536" (portrait) ou "1024x1024" (square)
    quality="high",        # "low" para testes, "medium" ou "high" para entregáveis
    output_format="png",   # ou "webp" (menor)
    background="opaque"    # ou "transparent" para composição
)

# Com referências (image-to-image / pixel-stability):
response = client.images.edit(
    model="gpt-image-2",
    image=open("foto_prototipo_01.jpg", "rb"),  # referência principal
    # Até 16 imagens de referência simultâneas
    prompt="[PROMPT DO BLOCO ACIMA]",
    n=1,
    size="1536x1024",
    quality="high"
)
```

### Ordem recomendada de geração para consistência máxima:
1. Primeiro: **2A** (produto melhorado, ângulo 3/4 principal) — âncora visual
2. Com 2A como referência: **2B, 2C, 2D** (variações mantendo o produto consistente)
3. Com 2A como referência: **4A, 4B, 4C** (lifestyle, produto já definido visualmente)
4. Com 2A + fotos prototipo: **1A** (blueprint referenciada ao produto real)
5. Por último: **6A, 6B** (ads, após produto visual definido)

### Verificação de consistência entre gerações:
- O produto mantém as mesmas proporções?
- O acabamento brushed tem o mesmo padrão?
- As ventilações têm o mesmo espaçamento?
- A pega oval está no mesmo lugar?
- O ângulo/perspectiva é compatível com a sequência?

Se não: usar a geração anterior como referência adicional na próxima.

---

*Skill criada para: projeto Vision Inox | Consultoria: Everton Stedile*
*Ferramenta: GPT Image 2 (gpt-image-2-2026-04-21) | Lançado: 21 abril 2026*
*Ref: pixel-stability, multi-turn editing, up to 16 reference images simultaneous*
