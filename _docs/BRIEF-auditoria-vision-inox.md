# BRIEF COMPLETO — Auditoria Premium Imersiva · Vision Inox
*Documento autossuficiente. Cole-o **inteiro** no Claude Code, na pasta do projeto. Não depende de nenhuma conversa anterior. O agente deve tratar tudo abaixo como sua instrução.*

---

## 0. Missão

Auditar a proposta web (single-file `index.html`) da **Vision Inox** contra a régua premium do projeto e produzir **`AUDITORIA-vision-inox.md`** — um relatório de achados acionáveis. **É diagnóstico, não cirurgia: não altere nenhum arquivo.** A meta da peça é provocar "como ele fez isso" num cliente exigente; a auditoria existe pra fechar a distância entre "muito bom" e "inquestionável".

---

## 1. Contexto do projeto

- **Marca:** Vision Inox (nome de trabalho) — D2C de **churrasqueiras portáteis flat-pack em inox 304**, corte a laser + encaixe por abas (sem solda). Diferenciais: não enferruja na maresia, não empena no calor, logo 100% vazada que ventila, grelha de altura ajustável, pega oval, flat-pack.
- **Cliente:** fabricante industrial de inox entrando no digital pela primeira vez. Olhar técnico apurado — repara em precisão.
- **A peça:** proposta de conversão em **scrollytelling premium**. Hero scroll-driven de **14 cenas (~2400vh)**: nascimento (papel→esboços→logo) → engenharia (blueprint→render) → detalhe (macros) → produto (inox) → território (praia c/ vídeo+zoom → camping → piscina → montanha → caminhonete → fecho), seguido das seções de proposta. **Fase B** já aplicada: showroom de produtos 3D, vocabulário de gestos nas seções, magnetismo de scroll.
- **Hospedagem:** GitHub Pages (URL grátis). WebGL/Three.js liberado; **não otimizar para WhatsApp WebView nem adicionar fallback** — irrelevante aqui.
- **Fora de escopo:** preço/contrato (vão em documento separado) e a **copy** (aprovada esta semana — não re-discutir palavras, só tipografia/quebra/enquadramento).

---

## 2. Sistema travado (a régua — não improvisar)

**Cores** (a paleta completa está na skill `vision-inox-art-direction`; âncoras-chave):
- Fundo: `#090909` (nunca `#000` puro) · grafites `#0e0e12` `#131318` `#17171d`
- Inox/steel: `#edeff2` `#c2c5cc` `#8d9098` `#54575f` `#3a3c42`
- Brasa: `#ff4500` (--e1, CTA) · `#ff7a1a` (--e2, acento da marca) · `#ffb02e` (âmbar)
- Ciano: `#00e5ff` (--cy, fase técnica)
- Texto: `#ececef` (**nunca `#ffffff` puro**) · `#9a9da5` · `#65686f` · linhas `rgba(255,255,255,.08)`

**Tipografia:** `Fraunces` (display/serif, --fd — títulos, ênfases) + `Archivo` (sans, --fs — corpo, kickers, dados). **Proibidas (AI slop):** Inter, Roboto, Arial, Space Grotesk, Poppins, Lato, Open Sans. *(Atenção: "inter" dentro de "pointer" é falso positivo.)*

**Física do movimento (a alma do imersivo):** easing único `cubic-bezier(.2,.7,.2,1)`, ~1s, **zero bounce/elastic/spring**. Reveal = fade + `translateY(28–34px)`. Grain overlay `opacity ~.035`. `border-radius` ≤ 20px em containers principais.

**Logo:** 100% vazada (dobra como ventilação real), nas duas faces longas — frente legível, traseira espelhada (a espelhada na praia é correta por design).

---

## 3. Arquitetura técnica (pra navegar o `index.html`)

- `#track` (~2400vh) com `#stage` sticky. Progresso: `pr = -track.getBoundingClientRect().top / (track.offsetHeight - innerHeight)`. **Pra posicionar o hero em `p`:** `scrollTo(0, topoAbsDoTrack + p*(offsetHeight-innerHeight))`.
- Cenas no array **`SC`** = `[id, início, fim, fadeIn, fadeOut, zoom]`; crossfade alinhado `W=.020`. Ranges reais das cenas de ambiente: camping `.651–.733`, piscina `.733–.814`, montanha `.814–.895`, caminhonete `.895–1.0`.
- **Textos** `#t1`–`#t8` + `#t6b`/`#t7b`/`#t7c` (cenas lifestyle). Sincronia: `op(el, seg(p,in0,in1)*(1-seg(p,out0,out1)))`.
- **Praia** (à parte): vídeo fwd `.515–.575` → reverse via `currentTime` `.575–.61` → crossfade p/ `praia_final.png` (4K) → zoom-in na logo `.62–.651`. "Portais pela logo": praia→camp `.640`, pisc→mont `.814`.
- **Mobile:** zoom condicional por viewport (`innerWidth<760` usa zoom menor). Princípio: produto inteiro → `contain`; imersão → `cover` + object-position recalibrado. **No mobile o risco nunca é nitidez — é enquadramento/corte.**
- **Áudio:** música build-up (sai na lifestyle, volta a `0.34` nas seções com `pr>1`) + `hero-embers.mp3` (entra na praia `.50–.60`, some nas seções). Overlay **`#intro`** libera áudio via **`#introBtn`** — faz fade de 1s e vira `display:none` aos 1200ms.
- **Fase B:** gestos `data-rv` (`depth`/`mask`/`slide`/`rise`) revelados pelo IntersectionObserver `io`; showroom `.line-grid.showroom`; magnetismo `scroll-snap-type:y proximity` com **hero livre** (`#track`/`#stage`/`.kf` = `scroll-snap-align:none`).
- **Assets pesados** (pra eixo de performance): `hero-music.mp3` ~7,85MB · `hero-wan.webm` ~4,48MB · `hero-wan-web.mp4` ~3,57MB · `praia_final.png` ~2,48MB (4K) · 6× `ref_*.png` ~2MB cada.

---

## 4. Setup

- **Working dir:** pasta com `index.html` (+ `_build7.py`/`_build8.py` + `assets/`).
- **Modelo:** **Sonnet** — varredura + relatório é execução. (A priorização estratégica dos achados volta pro chat com Opus.)
- **Skills — ativar nesta ordem:**
  1. `vision-inox-art-direction` (régua-mãe: 5 dimensões, paleta/fontes, anti-slop). *Se não estiver em `.claude/skills/`, copie o `SKILL-vision-inox-art-direction.md` do projeto pra lá.*
  2. `impeccable` — detecção de slop *(se instalada: `npx skills add pbakaus/impeccable`)*
  3. `huashu-design` — imersivo/animação *(se instalada)*
  4. `ui-ux-pro-max` — UX/contraste/acessibilidade *(se instalada)*
- **Playwright:** browsers em `/opt/pw-browsers`; launch com `--use-gl=swiftshader --autoplay-policy=no-user-gesture-required`; **sempre** `document.documentElement.style.scrollBehavior='auto'` antes de `scrollTo`; clicar `#introBtn` e **esperar ~1,5s** (senão o intro em fade-out aparece como texto-fantasma na screenshot — é artefato de medição, não bug).

---

## 5. Regras de ouro (invioláveis)

1. **Diagnóstico, não cirurgia.** Não altere nenhum arquivo. Só gere `AUDITORIA-vision-inox.md`.
2. **Não toque no scrubbing do hero** nem proponha mudar a altura do `#track`.
3. **Copy aprovada** — só audite tipografia/quebra/enquadramento, nunca a escolha de palavras.
4. "Frame preto" / "texto-fantasma" em screenshot = artefato de medição (smooth-scroll ou intro em fade). Não reporte como bug do site.
5. Preço/contrato não existem na peça — não é achado.

---

## 6. Eixos da auditoria (o trabalho)

Para **cada achado**: `[SEVERIDADE] eixo — o quê — onde (linha/seletor) — recomendação — esforço (trivial/médio/alto)`.
**Severidades:** `CRÍTICO` (quebra de layout, ilegível, fere posicionamento, erro JS) · `IMPORTANTE` (destoa do premium, inconsistência perceptível a olho) · `POLISH` (rigor fino).

**Método:** (1) ler `index.html` inteiro; (2) Playwright em **6 viewports** — 320, 390, 768, 1024, 1440, 1920 — capturando o hero em `p = .05 .20 .35 .50 .62 .70 .82 .95`, cada seção pós-hero, e **todos os erros/warnings de console**; salvar screenshots `audit_<viewport>_<ponto>.png`; (3) avaliar contra os eixos:

**Eixo 1 — Fidelidade ao sistema travado (código).** Hex fora da paleta da §2 (classifique `#fff`/`#000` sólidos como TEXTO editorial = fere regra, vs ícone/sombra/background = tolerável). Fonte fora de Fraunces/Archivo. Texto editorial em `#ffffff` puro. `border-radius > 20px` em container principal.

**Eixo 2 — Impacto e hierarquia (visual, 0–3s).** O primeiro frame (intro/hero) provoca reação? Cada seção tem ponto de entrada claro pro olho? Há assimetria intencional ou tudo centralizado vira monotonia? Cards com 1–2 linhas parecem vazios?

**Eixo 3 — Física / movimento imersivo (a alma).** Easing único `cubic-bezier(.2,.7,.2,1)` ~1s, zero bounce/elastic. Reveals consistentes (fade + translateY ~28–34px). Gestos Fase B (depth/mask/slide) coerentes entre seções. Crossfades do hero suaves — sem flash/salto/duplo-texto entre cenas. Hover muda só cor/opacidade/transform, nunca layout.

**Eixo 4 — Diferenciação e emoção (posicionamento).** "Poderia ser de qualquer outra marca?" Se sim, é problema. Conecta com a dor real (maresia/empeno/brasa)? Anti-slop específico: nada de vermelho-churrasqueiro, foto de churrasco stock genérico, inox tipo peça hospitalar, ícone de chama flat, palavra "gourmet", tipografia rústica/vintage.

**Eixo 5 — Performance e robustez (premium = rápido e sólido).** Peso total e por asset (sinalize `praia_final.png` 4K e qualquer asset > 1,5MB); estime LCP. **Zero erro de console** em todos os viewports. Layout não quebra em 320px; sem scroll horizontal em nenhum. Áudio com estados/volumes corretos por fase, sem clip. Vídeo: poster aparece, sem flash preto no 1º frame.

**Eixo 6 — Tipografia fina e acessibilidade (o acabamento).** Viúvas/órfãs e quebras ruins em headlines (nos 6 viewports). Kickers consistentes (uppercase + letter-spacing 0.24–0.28em). Números com `font-variant-numeric: tabular-nums`. `alt` em todas as imagens. Contraste de texto sobre imagem (scrim suficiente?). Foco visível nos botões. `@media (prefers-reduced-motion)` respeitado?

**OUTPUT — `AUDITORIA-vision-inox.md`:**
- Resumo executivo: veredito geral (1 parágrafo) + contagem por severidade.
- Achados agrupados por eixo, ordenados por severidade, no formato acima.
- **"Top 5 que mais elevam a percepção do cliente"** (sua leitura de maior ROI estético).
- Lista dos screenshots gerados.

*Não aplique nenhuma mudança. Não toque no scrubbing nem na altura do `#track`.*

---

## 7. Depois de rodar

Traga o `AUDITORIA-vision-inox.md` (e 3–4 screenshots que mais incomodaram) de volta pro chat. Lá, em registro Opus, separo **o que muda a percepção do cliente** do **que é polish**, fechamos a lista, e aplico tudo em **leva única** (achados + os 4 flags já mapeados: 2× `#fff` em CTA, 1 texto branco a conferir, `#000` no `kf-cam`) — pra reempacotar uma vez só.
