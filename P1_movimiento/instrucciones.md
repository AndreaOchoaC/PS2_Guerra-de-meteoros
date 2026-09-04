# Parte 1 — Movimiento del jugador

**Objetivo:** mover la nave (rectángulo) hacia la izquierda y derecha con el
teclado, sin que se salga de la pantalla.

**Conceptos que repasamos:** `pygame.key.get_pressed()`, condicionales,
coordenadas en la pantalla.

## Qué hacer

Completa los 4 `TODO` en `main.py`:

1. Obtener el estado de las teclas presionadas.
2. Mover el jugador a la izquierda si se presiona ⬅️ o A.
3. Mover el jugador a la derecha si se presiona ➡️ o D.
4. Evitar que el jugador salga de los bordes de la ventana.

## Cómo saber que funcionó

- La nave se mueve suavemente al mantener presionada una tecla.
- La nave se detiene exactamente en el borde de la ventana (no se sale ni se
  queda "flotando" fuera de la pantalla).

<details>
<summary>💡 Pista si te atoras con los límites</summary>

El borde izquierdo de la nave no puede ser menor que 0.
El borde derecho de la nave (`jugador_x + JUGADOR_ANCHO`) no puede ser mayor
que `ANCHO`. Así que el límite derecho para `jugador_x` es `ANCHO - JUGADOR_ANCHO`.
</details>
