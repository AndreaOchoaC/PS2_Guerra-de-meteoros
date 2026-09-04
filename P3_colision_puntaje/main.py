"""
PARTE 3: Colisiones, puntaje y game over
Lee los TODO con atención, pero esta vez no incluyen pistas de código.
"""
import pygame
import random
import sys

pygame.init()

ANCHO, ALTO = 800, 400
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Esquiva los Meteoritos")
reloj = pygame.time.Clock()
FPS = 60

COLOR_FONDO = (20, 20, 40)
COLOR_JUGADOR = (0, 200, 255)
COLOR_METEORITO = (255, 100, 60)
COLOR_TEXTO = (255, 255, 255)

fuente = pygame.font.SysFont(None, 36)
fuente_grande = pygame.font.SysFont(None, 64)

JUGADOR_ANCHO, JUGADOR_ALTO = 50, 20
jugador_x = ANCHO // 2 - JUGADOR_ANCHO // 2
jugador_y = ALTO - 50
VELOCIDAD_JUGADOR = 6

meteoritos = []
METEORITO_TAM = 30
VELOCIDAD_METEORITO = 4
INTERVALO_APARICION = 800
ultimo_spawn = pygame.time.get_ticks()

# TODO 1: Crea una variable para llevar el puntaje del jugador, inicializada en 0.
puntos = 0

# TODO 2: Crea una variable booleana `juego_terminado` inicializada en False.
juego_terminado = False

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    teclas = pygame.key.get_pressed()

    # TODO 3: Haz que el jugador solo pueda moverse mientras `juego_terminado` sea False.
    
    if not juego_terminado:
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            jugador_x -= VELOCIDAD_JUGADOR
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            jugador_x += VELOCIDAD_JUGADOR
    jugador_x = max(0, min(jugador_x, ANCHO - JUGADOR_ANCHO))

    tiempo_actual = pygame.time.get_ticks()
    if tiempo_actual - ultimo_spawn >= INTERVALO_APARICION:
        x = random.randint(0, ANCHO - METEORITO_TAM)
        meteoritos.append(pygame.Rect(x, 0, METEORITO_TAM, METEORITO_TAM))
        ultimo_spawn = tiempo_actual

    for meteorito in meteoritos:
        meteorito.y += VELOCIDAD_METEORITO
    meteoritos = [m for m in meteoritos if m.y < ALTO]

    jugador_rect = pygame.Rect(jugador_x, jugador_y, JUGADOR_ANCHO, JUGADOR_ALTO)

    # TODO 4: Detecta si el jugador choca con algún meteorito.
    # Si choca, marca `juego_terminado = True`.
    # Pista de concepto (sin código): pygame.Rect tiene un método para saber si
    # colisiona con otro Rect. Revisa la documentación de pygame.Rect si no lo recuerdas.

    for meteorito in meteoritos:
        if jugador_rect.colliderect(meteorito):
            juego_terminado = True

        # TODO 5: Mientras el juego NO haya terminado, aumenta el puntaje con el paso
        # del tiempo (por ejemplo, sumando 1 cada cuadro, o usando el tiempo transcurrido).
  
    if not juego_terminado:
        puntos += 1 # dentro del ciclo!

    pantalla.fill(COLOR_FONDO)
    pygame.draw.rect(pantalla, COLOR_JUGADOR, jugador_rect)
    for meteorito in meteoritos:
        pygame.draw.rect(pantalla, COLOR_METEORITO, meteorito)

    # TODO 6: Dibuja el puntaje en pantalla usando la fuente ya creada (`fuente`).
    # Pista de concepto: fuente.render(texto, True, color) crea una "superficie"
    # de texto que luego se dibuja con pantalla.blit(superficie, (x, y)).
    texto_puntaje = fuente.render(f"Puntaje: {puntos // 10}", True, COLOR_TEXTO)
    pantalla.blit(texto_puntaje, (10, 10)) # dibuja el texto en coordenadas 10,10

    # TODO 7: Si `juego_terminado` es True, muestra un mensaje de "Game Over"
    # en el centro de la pantalla y termina el juego.

    if juego_terminado:
        texto_gameover = fuente_grande.render("GAME OVER", True, COLOR_TEXTO)
        rect_texto = texto_gameover.get_rect(center=(ANCHO // 2, ALTO // 2))
        pantalla.blit(texto_gameover, rect_texto)

    pygame.display.flip()
    reloj.tick(FPS)

pygame.quit()
sys.exit()
