# PATCH — headlines lifestyle no hero (aplicar no `_build7.py`)

Editei o `index.html` direto (caminho B). Para a fonte não defasar, aplique estes 3 trechos no `_build7.py`, no ponto onde ele gera o hero. Se o HTML estiver em f-string, cuidado só com escapes de `{}` — os textos abaixo não têm chaves nem aspas problemáticas, colam direto.

---

## 1. Declaração das vars JS — adicionar t6b, t7b, t7c

**Localizar:**
```js
const t1=C('t1'),t2=C('t2'),t3=C('t3'),t4=C('t4'),t5=C('t5'),t6=C('t6'),t7=C('t7'),t8=C('t8');
```
**Trocar por:**
```js
const t1=C('t1'),t2=C('t2'),t3=C('t3'),t4=C('t4'),t5=C('t5'),t6=C('t6'),t6b=C('t6b'),t7=C('t7'),t7b=C('t7b'),t7c=C('t7c'),t8=C('t8');
```

---

## 2. Blocos HTML dos textos — substituir t6/t7/t8 (3 linhas) por 6

**Localizar (os 3 divs antigos):**
```html
  <div class="pt center" id="t6"><span class="kk em">A brasa encontra o litoral</span><h2 class="ht lg">Feita para <em class="em">o litoral.</em></h2></div>
  <div class="pt center" id="t7"><span class="kk em">Litoral, mato, montanha, estrada</span><h2 class="ht lg">Boa para o <em class="em">Brasil inteiro.</em></h2></div>
  <div class="pt center" id="t8"><span class="kk em">Vision Inox × Everton Stedile</span><h2 class="ht lg">A marca<br>começa aqui.</h2></div>
```
**Trocar por:**
```html
  <div class="pt center" id="t6"><span class="kk em">A brasa encontra o litoral</span><h2 class="ht lg">Feita para <em class="em">o litoral.</em></h2><p class="htsub">Inox 304: a maresia não enferruja, o sol não empena.</p></div>
  <div class="pt center" id="t6b"><span class="kk em">Mato fechado, fogo aceso</span><h2 class="ht lg">Vai onde o <em class="em">asfalto acaba.</em></h2><p class="htsub">Desmonta plana, cabe na mochila, monta sem ferramenta.</p></div>
  <div class="pt center" id="t7"><span class="kk em">Varanda, quintal, beira d'água</span><h2 class="ht lg">Estica o <em class="em">domingo.</em></h2><p class="htsub">Do mergulho à brasa sem trocar de cenário.</p></div>
  <div class="pt center" id="t7b"><span class="kk em">Serra, sereno, altitude</span><h2 class="ht lg">Frio lá fora, <em class="em">brasa aqui.</em></h2><p class="htsub">O sereno vem e vai. O inox fica.</p></div>
  <div class="pt center" id="t7c"><span class="kk em">Estrada afora</span><h2 class="ht lg">Boa para o <em class="em">Brasil inteiro.</em></h2><p class="htsub">Do litoral ao interior, a mesma brasa.</p></div>
  <div class="pt center" id="t8"><span class="kk em">Vision Inox × Everton Stedile</span><h2 class="ht lg">A marca<br>começa aqui.</h2></div>
```

---

## 3. Sincronia de opacidade — substituir op(t6/t7/t8) (3 linhas) por 6

**Localizar:**
```js
  op(t6, seg(p,.515,.55)*(1-seg(p,.585,.61)));
  op(t7, seg(p,.745,.78)*(1-seg(p,.875,.90)));
  op(t8, seg(p,.905,.94)*(1-seg(p,.985,1.0)));
```
**Trocar por:**
```js
  op(t6, seg(p,.515,.55)*(1-seg(p,.585,.61)));
  op(t6b, seg(p,.668,.690)*(1-seg(p,.715,.728)));
  op(t7, seg(p,.748,.770)*(1-seg(p,.793,.806)));
  op(t7b, seg(p,.830,.852)*(1-seg(p,.875,.888)));
  op(t7c, seg(p,.905,.920)*(1-seg(p,.938,.950)));
  op(t8, seg(p,.956,.966)*(1-seg(p,.990,1.0)));
```

---

## Mapa de sincronia (referência)

| Bloco | Cena | range cena (SC) | in | out |
|-------|------|-----------------|----|----|
| t6 | praia | .515–.61 (à parte) | .515–.55 | .585–.61 |
| t6b | camping | .651–.733 | .668–.690 | .715–.728 |
| t7 | piscina | .733–.814 | .748–.770 | .793–.806 |
| t7b | montanha | .814–.895 | .830–.852 | .875–.888 |
| t7c | caminhonete | .895–1.0 | .905–.920 | .938–.950 |
| t8 | fecho (sobre cam) | — | .956–.966 | .990–1.0 |

Nada além disso mudou. Scrubbing, áudio, zoom e Fase B intactos.
