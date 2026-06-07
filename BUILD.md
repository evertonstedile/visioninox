# Build — ordem obrigatoria
1. python3 _build7.py                                          # builder canonico: gera build/index.html
2. cp audio/hero-music.mp3 audio/hero-embers.mp3 build/assets/ # re-copiar os 2 MP3 apos CADA build7
3. python3 _build8.py                                          # camada FASE B (assert anti-duplo; so apos build7)
# Caminho B (entrega rapida): editar index.html direto, sem rebuild.
# PESADOS via LFS (subir separado): hero-music.mp3, hero-wan.webm, hero-wan-web.mp4, praia_final.png
