# Parte 3 — Colisiones, puntaje y game over

**Objetivo:** terminar el juego. Debe detectar cuando el jugador choca con un
meteorito, llevar un puntaje que aumenta mientras sobrevives, y mostrar un
mensaje de "Game Over" cuando pierdes.

**Conceptos que repasamos:** detección de colisiones con `pygame.Rect`,
texto en pantalla con `pygame.font`, control de estado del juego con variables
booleanas.

## Qué hacer

Esta vez los `TODO` son solo la consigna, sin pasos de código. Ya tienen todo lo
que necesitan de las partes anteriores — ¡confía en lo que ya sabes!

1. Variable de puntaje.
2. Variable para saber si el juego terminó.
3. El jugador deja de moverse cuando el juego termina.
4. Detectar colisión jugador-meteorito.
5. El puntaje aumenta mientras el juego sigue activo.
6. Mostrar el puntaje en pantalla.
7. Mostrar "Game Over" cuando el jugador pierde.

## Cómo saber que funcionó

- Al chocar con un meteorito, el juego se "congela" (los meteoritos y el jugador
  dejan de moverse) y aparece un mensaje en pantalla.
- El número de puntaje sube mientras juegas y deja de subir al perder.

## 🎁 Reto bonus (para la próxima clase o en casa)

Si terminaste antes de tiempo, o quieres seguir en casa, intenta agregar:

- Que la velocidad de los meteoritos aumente con el tiempo (dificultad progresiva).
- Un sistema de vidas en vez de terminar con un solo choque.
- Reiniciar el juego presionando una tecla después del Game Over.
- Un sonido cuando el jugador pierde (`pygame.mixer`).
