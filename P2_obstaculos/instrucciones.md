# Parte 2 — Meteoritos

**Objetivo:** que aparezcan meteoritos en posiciones aleatorias cada cierto
tiempo, caigan hacia abajo, y desaparezcan al salir de la pantalla.

**Conceptos que repasamos:** temporizadores con `pygame.time.get_ticks()`,
listas de objetos, `random.randint()`, `pygame.Rect`.

## Qué hacer

Completa los 4 `TODO` en `main.py`. Esta vez hay menos pistas de código directo:
lee bien los comentarios, apóyate en lo que ya vimos en clases anteriores sobre
`time`.

1. Define el intervalo de aparición de meteoritos.
2. Genera un meteorito nuevo cada cierto intervalo de tiempo.
3. Mueve todos los meteoritos hacia abajo en cada cuadro.
4. Elimina de la lista los que ya salieron de la pantalla (si no lo haces, la lista crecerá para siempre y el juego se hará cada vez más lento).

## Cómo saber que funcionó

- Los meteoritos aparecen en posiciones horizontales distintas cada vez.
- Caen a velocidad constante.
- No se acumulan infinitamente (puedes comprobar imprimiendo
  `len(meteoritos)` para verificar que no sigue creciendo sin parar).

<details>
<summary>💡 Pista si te atoras con el temporizador</summary>

Es el mismo patrón que usamos antes con `time`, pero usando los milisegundos
del reloj interno de pygame en vez de `time.sleep()`, para no congelar el
juego mientras esperamos.
</details>
