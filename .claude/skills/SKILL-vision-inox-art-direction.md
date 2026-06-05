---
name: vision-inox-art-direction
description: >
  Direção de arte do projeto Vision Inox. Ativar SEMPRE antes de qualquer output visual —
  proposta HTML, site e-commerce, criativos, mockups, prompts de imagem IA.
  Consolida diretrizes de Impeccable, Taste, Huashu Design e UI UX Pro Max
  adaptadas ao contexto industrial-premium deste projeto.
trigger: >
  Ativar quando o usuário pedir: design, visual, layout, hero, seção, criativo,
  cor, tipografia, animação, proposta HTML, site, landing page, mockup, ou
  qualquer output que tenha aparência visual.
---

# Vision Inox — Art Direction SKILL

## 1. Filosofia Central (extraído de Huashu Design)

> "Constraina filosofia, não forma. Define POR QUE assim — não COMO parece."

Este projeto tem uma identidade específica: **INDUSTRIAL PREMIUM com CALOR DE BRASA.**
Não é luxury genérico. Não é camping outdoor barato. É a precisão técnica de uma
indústria de inox que encontra o desejo de quem ama churrasco no litoral.

**O projeto em uma frase de briefing:**
Inox industrial → Marca premium de churrasqueiras portáteis → Canal D2C → Litoral brasileiro

### O Produto (referência obrigatória antes de qualquer output visual)
- Churrasqueira portátil flat-pack em **inox 304**
- Construção: corte a laser + encaixe por abas (tab-and-slot), sem solda
- Diferenciais: grelha de altura ajustável (3 níveis), pega oval integrada, ventilação lateral, nervuras anti-empeno
- Embalagem: flat-pack (embalagem plana — não parece churrasqueira na caixa)
- Argumento central: **não enferruja na maresia, não empena no calor, acabamento premium**
- Público: 35-55 anos, ABC+, casa de praia / varanda gourmet / camping leve

---

## 2. Paleta de Cores (CODIFICADA — não improvisar)

### Fundos (backgrounds)
```
--bg-deep:    #090909   /* fundo principal — quase preto, warm */
--bg-2:       #0e0e12
--bg-3:       #131318
--surface:    #17171d
--surface-2:  #1d1d24
```

### Metais / Inox
```
--steel-1:    #edeff2   /* inox claro — face frontal com luz direta */
--steel-2:    #c2c5cc   /* inox médio */
--steel-3:    #8d9098   /* inox escuro — faces laterais em sombra */
--steel-4:    #54575f   /* inox sombra profunda */
--steel-5:    #3a3c42   /* sombra muito profunda */
```

### Brasa (acento emocional — usar cirurgicamente, máx. 2 elementos por seção)
```
--ember-1:    #ff4500   /* brasa intensa — CTAs principais */
--ember-2:    #ff7a1a   /* brasa média — acento primário da marca */
--ember-3:    #ffb02e   /* brasa suave / âmbar */
--ember-glow: rgba(255,90,20,0.5)  /* glow para filtros e sombras */
```

### Blueprint (fase técnica — ciano sobre escuro)
```
--cyan:       #00e5ff
--cyan-dim:   rgba(0,229,255,0.55)
--grid-line:  #0a2030   /* grid principal da blueprint */
--grid-sub:   #071525   /* sub-grid */
```

### Texto
```
--text:       #ececef   /* nunca #ffffff — sempre levemente warm */
--text-dim:   #9a9da5
--text-faint: #65686f
--line:       rgba(255,255,255,0.08)   /* bordas e separadores */
--line-2:     rgba(255,255,255,0.13)
```

### Gradientes pré-definidos
```css
/* Gradiente metálico — face frontal do produto */
background: linear-gradient(135deg, #edeff2 0%, #c2c5cc 35%, #8d9098 70%, #6a6d74 100%);

/* Gradiente metálico — face lateral (mais escuro) */
background: linear-gradient(135deg, #7e818a 0%, #555860 55%, #3c3f45 100%);

/* Gradiente metálico — topo/grelha */
background: linear-gradient(180deg, #d5d8de 0%, #9a9da5 100%);

/* Glow de brasa no fundo */
background: radial-gradient(ellipse 80% 55% at 50% 100%, rgba(255,69,0,0.25) 0%, transparent 65%);

/* Acento de brasa no hero */
background: radial-gradient(ellipse 50% 50% at 50% 50%, rgba(255,69,0,0.22) 0%, rgba(255,122,26,0.08) 38%, transparent 66%);
```

---

## 3. Tipografia (CODIFICADA — extraído de Impeccable + UI UX Pro Max)

### PROIBIDAS — AI Slop clássico (nunca usar)
❌ Inter | ❌ Roboto | ❌ Arial | ❌ Space Grotesk | ❌ Poppins | ❌ Lato | ❌ Open Sans

### Combinação aprovada para o projeto
```
--font-display: 'Fraunces', Georgia, serif
  /* Serif editorial de alto contraste óptico.
     Luxo com calor. Conecta com brasa e litoral.
     opsz alto (144) = mais elegante, menos quirky. */

--font-sans: 'Archivo', -apple-system, sans-serif
  /* Sans grotesca industrial-limpa.
     Ótima para números tabulares, labels, dados técnicos.
     Peso 800 uppercase para kickers: parece engenharia. */

Google Fonts import:
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;600;700;800;900&family=Fraunces:opsz,wght@9..144,300;9..144,400;9..144,500;9..144,700&family=Fraunces:ital,opsz,wght@1,9..144,400&display=swap" rel="stylesheet">
```

### Escala tipográfica
```
/* Kickers / labels */
font: 800 11px/1 'Archivo'; letter-spacing: 0.26em; text-transform: uppercase;

/* Body */
font: 400 15-18px/1.6 'Archivo';

/* Subtítulos de seção */
font: 400 20-24px/1.4 'Archivo'; font-weight: 600;

/* Títulos de seção */
font-family: 'Fraunces'; font-size: clamp(32px,5vw,62px); font-weight: 400; letter-spacing: -0.022em; line-height: 1.02;

/* Hero titles */
font-family: 'Fraunces'; font-size: clamp(46px,8vw,118px); font-weight: 300-500; letter-spacing: -0.035em; line-height: 1.0;

/* Ênfase / italic */
font-style: italic; color: --ember-2; /* brasa para ênfase emocional */
/* ou */
font-style: italic; color: --cyan;   /* ciano para ênfase técnica */
```

### Regras de uso
- **Fraunces** → títulos, headlines, citações, manifesto, ênfases grandes
- **Archivo** → corpo, labels, kickers, dados, tabelas, botões, UI
- **Itálico Fraunces** → palavra de ênfase emocional no título (nunca o título inteiro)
- Números com `font-variant-numeric: tabular-nums` em Archivo
- Kickers sempre: UPPERCASE + letter-spacing 0.24-0.28em + weight 700-800

---

## 4. Regras Visuais (extraído de Impeccable + Taste + UI UX Pro Max)

### FAZER ✅
- Fundo quase-preto com **profundidade** (radial-gradients sutis, noise overlay 3-5%)
- **Grain/noise overlay** fixo: `mix-blend-mode: overlay, opacity: 0.035` — cria textura premium
- Gradientes metálicos nas 3 faces do produto (claro na frontal, escuro na lateral)
- Acentos de brasa/âmbar usados **cirurgicamente** — no máximo 1-2 elementos por seção
- Tipografia editorial grande com espaço generoso ao redor
- Reveal animations: **fade + translateY(28-34px)** com `cubic-bezier(.2,.7,.2,1)` ~1s
- Linhas de separação sempre finas: `rgba(255,255,255,0.08)` — nunca sólidas
- Scroll progress bar: 2-3px no topo com glow de brasa
- Números grandes em Fraunces para estatísticas de impacto
- **Asymmetry intencional**: texto à esquerda ou centro, nunca tudo centralizado em proposta
- Hover states com `transition: transform .4s, border-color .4s` suave
- `border-radius` máximo de 18-20px em cards — nunca 50px+ em containers principais

### NÃO FAZER ❌ — Anti-patterns críticos
- ❌ Gradiente roxo/azul sobre branco (clichê máximo de AI)
- ❌ Fundo #000000 puro — usar sempre #090909 warm
- ❌ Texto #ffffff puro — usar sempre #ececef
- ❌ Glassmorphism sem razão visual clara
- ❌ Muitas cores simultâneas — deve parecer "one-color brand"
- ❌ Border-radius > 20px nos containers principais
- ❌ Ícones emoji como elementos de UI
- ❌ Sombras `box-shadow` genéricas e excessivas
- ❌ Animações bounce/elastic/spring desnecessárias
- ❌ Full-width sem padding lateral (min 5vw / min 22px)
- ❌ Texto em todas as seções centralizado (cria monotonia)
- ❌ Cards com apenas 1-2 linhas de texto (parece vazio)
- ❌ Bullets/listas onde prosa ou card funcionaria melhor
- ❌ Gradientes com mais de 3 stops sem razão visual
- ❌ Hover effects que mudam layout (só cor/opacidade/transform)

---

## 5. Referências Cinematográficas por Contexto

### Blueprint / Engenharia
- **Ref:** Documentários de manufatura Apple, Dyson Engineering videos, SpaceX renders técnicos
- **Cor:** Ciano frio (#00e5ff) sobre grafite profundo (#090909)
- **Estética:** Precisão, linhas finas, grid milimétrico, cotas técnicas, zero ornamento

### Materialização / Inox
- **Ref:** Campanhas Bang & Olufsen, De'Longhi Primadonna, Weber Summit
- **Cor:** Gradiente metálico neutro, luz especular controlada, sombras suaves
- **Estética:** Peso, qualidade tátil, reflexo de luz único, acabamento perfeito

### Brasa / Churrasco
- **Ref:** Campanhas Weber Grill (EUA), Traeger, Fire + Flavor
- **Cor:** Âmbar (#ffb02e), laranja (#ff7a1a), fundo quase preto
- **Estética:** Energia, desejo, sensação de calor, fumaça suave, partículas

### Litoral / Lifestyle Premium
- **Ref:** Campanhas Yeti Coolers, Patagonia, Camp Chef
- **Cor:** Azul-marinho profundo, areia quente, luz de fim de tarde, inox ao sol
- **Estética:** Aventura premium, natureza sem artificialidade, durabilidade

### Produto em Estúdio (e-commerce)
- **Ref:** Leica cameras, All-Clad cookware, Victorinox
- **Cor:** Fundo escuro fosco ou granito, key light lateral que revela textura
- **Iluminação:** 1 key light à esquerda-superior, 1 fill suave à direita, sem reflejo direto
- **Estética:** O produto fala por si, sem poluição visual, 80% de espaço negativo

---

## 6. Review de 5 Dimensões (extraído de Huashu Design)

Antes de finalizar QUALQUER output visual, avaliar:

1. **Impacto imediato (0-3s):** O primeiro frame provoca reação ou passa despercebido?
2. **Hierarquia informacional:** O olho sabe onde ir? Existe um ponto de entrada claro?
3. **Coerência com posicionamento:** Parece premium e técnico? Parece Vision Inox ou genérico?
4. **Diferenciação:** Poderia ser de outro produto/marca? Se sim, há problema.
5. **Emoção funcional:** Gera desejo? Conecta com a dor real (maresia, empena, brasa)?

---

## 7. Specs por Tipo de Output

### Proposta HTML (scroll imersivo) — atual
```
Hero: perspectiva 3/4 SVG + scroll-driven (550vh de track)
Fases: blueprint → materialização → brasa → litoral/slot
Sections: padding 90-160px vertical, max-width 1180px, wrap 32px lateral
Fonts: Fraunces + Archivo (Google Fonts)
Colors: paleta codificada acima
Animations: IntersectionObserver + reveal, count-up em números
Grain: SVG feTurbulence overlay, opacity 0.035
```

### Site E-commerce (a construir no Claude Code)
```
Stack recomendado: HTML+Tailwind / Shopify custom theme
Produto em destaque: foto sobre fundo escuro (#090909) com halo de brasa
Página de produto: 80% imagem, 20% texto — deixar o produto falar
CTA: background --ember-2 (#ff7a1a), texto escuro, peso 700
Reviews/prova social: estrelas em âmbar, nome em Archivo
Checkout: clean, minimal, fundo claro neutro (contraste com o dark da loja)
```

### Criativos Mídia Paga
```
Formatos: 9:16 (Reels/Stories) + 1:1 (feed) + 16:9 (YouTube pre-roll)
Hook visual: primeiros 0-1s devem mostrar DOR (ferrugem, empeno) ou DESEJO (brasa/praia)
Logo: canto superior esq, pequeno (máx 15% da largura)
Texto on-screen: Archivo Bold, white com sombra suave, 2-3 linhas max
CTA no final: ember-2 + texto "Garanta o seu"
```

### Assets GPT Image 2
```
Sempre usar fotos reais como referência (pixel-stability — ver SKILL gpt-image-prompt-pack)
Blueprint: ciano + grid sobre fundo grafite, perspectiva 3/4
Produto melhorado: iluminação de estúdio, fundo escuro, inox 304 escovado premium
Lifestyle praia: golden hour, litoral, família/casal, produto em uso natural
Sempre marcar outputs IA como "conceito/direção de design" — não como foto de produto final
```

---

## 8. Instalação no Claude Code

```bash
# Instalar este arquivo na skill global do Claude Code:
mkdir -p ~/.claude/skills/
cp SKILL-vision-inox-art-direction.md ~/.claude/skills/

# Ou no projeto específico:
mkdir -p .claude/skills/
cp SKILL-vision-inox-art-direction.md .claude/skills/

# Instalar as 5 skills externas analisadas:
npx skills add pbakaus/impeccable                            # Anti-slop + live iteration
npx skills add Leonxlnx/taste-skill                         # Design system codificado
npx skills add alchaincyf/huashu-design                     # 20 filosofias + animação + MP4
npx skills add nextlevelbuilder/ui-ux-pro-max-skill         # 161 paletas + 57 font pairings

# Playwright para screenshot de review:
npm install -g playwright
npx playwright screenshot file:///caminho/proposta.html review.png --viewport-size=1440,900
npx playwright screenshot file:///caminho/proposta.html review-mobile.png --viewport-size=390,844

# Review paralelo (3 viewports simultâneos como Huashu Design recomenda):
npx playwright screenshot file:///caminho/arquivo.html out-desktop.png --viewport-size=1440,900 &
npx playwright screenshot file:///caminho/arquivo.html out-tablet.png --viewport-size=768,1024 &
npx playwright screenshot file:///caminho/arquivo.html out-mobile.png --viewport-size=390,844 &
wait
```

### Ordem de prioridade das skills no Claude Code
1. `vision-inox-art-direction` — lida PRIMEIRO (contexto do projeto)
2. `impeccable` — para iteration visual e detecção de slop
3. `huashu-design` — para outputs HTML imersivos e animações
4. `ui-ux-pro-max` — para o e-commerce (paletas, font pairings, UX guidelines)
5. `taste-skill` — para o design system codificado do site

---

## 9. Anti-patterns Específicos de AI Slop para Este Projeto

Além dos gerais, evitar especificamente:

- ❌ Churrasqueira sobre fundo branco limpo (parece marketplace genérico)
- ❌ Foto de churrasco genérico do stock (carne grelhando sem identidade)
- ❌ Inox brilhante demais sem contexto (parece peça hospitalar)
- ❌ Paleta vermelha clássica de "churrasqueiro" (clichê total do segmento)
- ❌ Tipografia rústica/vintage (contradiz o posicionamento técnico-premium)
- ❌ Ícones de fogo/chama em flat design (banal demais)
- ❌ "Gourmet" escrito em qualquer headline (palavra já sem significado)
- ❌ Foto de casal sorrindo genérico de stock (desconecta da identidade industrial)

---

*Skill criada para: projeto Vision Inox | Consultoria: Everton Stedile*
*Baseada em: Impeccable (pbakaus), Taste (Leonxlnx), Huashu Design (alchaincyf), UI UX Pro Max (nextlevelbuilder), Playwright (Microsoft)*
