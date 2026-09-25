# PROPUESTA EXTRA # ¿Cómo personalizamos el juego?
# Agreguemos máscaras/sprites para el jugador y los meteoritos, y un fondo con estrellas.

"""
SOLUCIÓN COMPLETA: Esquiva los Meteoritos
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

# crear sprites de los meteoritos y del jugador
# usar las imágenes de MEDIA/meteorito.png y MEDIA/jugador.png
# resize para que tengan el tamaño adecuado
sprite_jugador = pygame.image.load("MEDIA/ship3.png").convert_alpha()
sprite_meteorito = pygame.image.load("MEDIA/asteroid50x50.png").convert_alpha()

sprite_jugador = pygame.transform.scale(sprite_jugador, (50, 50))
sprite_meteorito = pygame.transform.scale(sprite_meteorito, (50, 50))

JUGADOR_ANCHO, JUGADOR_ALTO = 50, 50
jugador_x = ANCHO // 2 - JUGADOR_ANCHO // 2
jugador_y = ALTO - 50
VELOCIDAD_JUGADOR = 6

meteoritos = []
METEORITO_TAM = 30
VELOCIDAD_METEORITO = 4
INTERVALO_APARICION = 800
ultimo_spawn = pygame.time.get_ticks()

puntaje = 0
juego_terminado = False

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    teclas = pygame.key.get_pressed()

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

        puntaje += 1

    jugador_rect = pygame.Rect(jugador_x, jugador_y, JUGADOR_ANCHO, JUGADOR_ALTO)

    for meteorito in meteoritos:
        if jugador_rect.colliderect(meteorito):
            juego_terminado = True

    # usar la imagen de fondo para llenar la pantalla, en lugar de un color sólido
    fondo = pygame.image.load("MEDIA/sky2.jpg").convert()
    pantalla.blit(fondo, (0, 0))
    # usar los sprites para dibujar al jugador y a los meteoritos
    
    pantalla.blit(sprite_jugador, (jugador_x, jugador_y))
    for meteorito in meteoritos:
        pantalla.blit(sprite_meteorito, (meteorito.x, meteorito.y))

    texto_puntaje = fuente.render(f"Puntaje: {puntaje // 10}", True, COLOR_TEXTO)
    pantalla.blit(texto_puntaje, (10, 10))

    if juego_terminado:
        texto_gameover = fuente_grande.render("GAME OVER", True, COLOR_TEXTO)
        rect_texto = texto_gameover.get_rect(center=(ANCHO // 2, ALTO // 2))
        pantalla.blit(texto_gameover, rect_texto)

    pygame.display.flip()
    reloj.tick(FPS)

pygame.quit()
sys.exit()
