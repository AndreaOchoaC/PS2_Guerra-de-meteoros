# Parte 0 — Setup básico (repaso express)

**Objetivo:** que la ventana del juego abra correctamente con un color de fondo.

**Conceptos que repasamos:** `pygame.init()`, `pygame.display.set_mode()`, el loop
principal, `Clock` y `tick()`.

## Qué hacer

Abre `main.py` y completa los 3 `TODO`:

1. `TODO 1`: define `ANCHO` y `ALTO` de la ventana.
2. `TODO 2`: define `FPS` (cuadros por segundo).
3. `TODO 3`: define `COLOR_FONDO` como una tupla RGB.

## Cómo saber que funcionó

Al correr `python main.py`, debe abrirse una ventana con el color que elegiste,
y debe poder cerrarse con la ❌ sin que la terminal marque error.

<details>
<summary>💡 Pista si te atoras</summary>

Una tupla RGB es simplemente `(rojo, verde, azul)`, cada valor entre 0 y 255.
Por ejemplo `(0, 0, 0)` es negro y `(255, 255, 255)` es blanco.
</details>
