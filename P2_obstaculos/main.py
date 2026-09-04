"""
PARTE 2: Meteoritos
Repasamos: pygame.time.get_ticks() como temporizador, listas, random.
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

JUGADOR_ANCHO, JUGADOR_ALTO = 50, 20
jugador_x = ANCHO // 2 - JUGADOR_ANCHO // 2
jugador_y = ALTO - 50
VELOCIDAD_JUGADOR = 6

# --- Meteoritos ---
# Cada meteorito lo representaremos como un pygame.Rect dentro de esta lista.
meteoritos = []
METEORITO_TAM = 30
VELOCIDAD_METEORITO = 4

# TODO 1: Define cada cuántos milisegundos debe aparecer un meteorito nuevo.
# Sugerencia: 800 (0.8 segundos)
INTERVALO_APARICION = 800

# Guardamos el momento (en ms) del último meteorito que apareció.
ultimo_spawn = pygame.time.get_ticks()

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
        jugador_x -= VELOCIDAD_JUGADOR
    if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
        jugador_x += VELOCIDAD_JUGADOR
    jugador_x = max(0, min(jugador_x, ANCHO - JUGADOR_ANCHO))

    # TODO 2: Cada INTERVALO_APARICION milisegundos, crea un meteorito nuevo.
    # Pasos sugeridos:
    #   a) obtén el tiempo actual con pygame.time.get_ticks()
    #   b) si (tiempo_actual - ultimo_spawn) >= INTERVALO_APARICION:
    #        - elige una posición x aleatoria con random.randint(0, ANCHO - METEORITO_TAM)
    #        - crea un pygame.Rect(x, 0, METEORITO_TAM, METEORITO_TAM)
    #        - agrégalo a la lista `meteoritos`
    #        - actualiza `ultimo_spawn` al tiempo actual

    tiempo_actual = pygame.time.get_ticks()
    # si el tiempo actual ya superó el intervalo desde el último spawn, creamos un meteorito nuevo
    if tiempo_actual - ultimo_spawn >= INTERVALO_APARICION:
        meteorito_x = random.randint(0, ANCHO - METEORITO_TAM) # lo colocamos en un lugar arndom
        meteorito = pygame.Rect(meteorito_x, 0, METEORITO_TAM, METEORITO_TAM) # creamos el rectángulo del meteorito
        meteoritos.append(meteorito) # agregamos el meteorito a la lista
        ultimo_spawn = tiempo_actual # actualizamos el último spawn al tiempo actual y comienza a contar de nuevo

    # TODO 3: Mueve cada meteorito de la lista hacia abajo
    # (incrementa su coordenada y en VELOCIDAD_METEORITO).
    # Pista: cada elemento de `meteoritos` es un pygame.Rect;
    # los Rect tienen un atributo .y que puedes modificar directamente.

    for meteorito in meteoritos:
        meteorito.y += VELOCIDAD_METEORITO # le sumamos la velocidad a la coordenada y del meteorito

    # TODO 4: Elimina de la lista los meteoritos que ya salieron de la pantalla
    # (es decir, cuando meteorito.y > ALTO).
    # Pista: puedes construir una nueva lista con los que SÍ quieres conservar,
    # por ejemplo usando una list comprehension o un bucle con una lista auxiliar.

    #meteoritos = [meteorito for meteorito in meteoritos if meteorito.y < ALTO] # list comprehension
    # crear una nueva lista con los meteoritos que aún están en pantalla
    meteoritos_en_pantalla = []
    for meteorito in meteoritos:
        if meteorito.y < ALTO:
            meteoritos_en_pantalla.append(meteorito)
    meteoritos = meteoritos_en_pantalla # sustituye la lista anterior con los meteoritos restantes
    # los meteoritos que superaron ALTO ya no estarán en la lista y no se dibujarán ni se moverán más

    pantalla.fill(COLOR_FONDO)
    pygame.draw.rect(
        pantalla, COLOR_JUGADOR, (jugador_x, jugador_y, JUGADOR_ANCHO, JUGADOR_ALTO)
    )
    for meteorito in meteoritos:
        pygame.draw.rect(pantalla, COLOR_METEORITO, meteorito)

    pygame.display.flip()
    reloj.tick(FPS)

pygame.quit()
sys.exit()
