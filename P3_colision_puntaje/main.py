"""
PARTE 3: Colisiones, puntaje y game over
Esta es la última parte: ¡ahora depende más de ti!
Lee los TODO con atención, pero esta vez no incluyen pistas de código.
"""
import pygame
import random
import sys


pygame.init()

pygame.mixer.init()
pygame.mixer.music.load("media/fresita.mp3")
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)

ANCHO, ALTO = 800, 400
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Esquiva los Meteoritos")
reloj = pygame.time.Clock()
FPS = 60

puntaje = 0
aumento = 67
nivel = 1


COLOR_FONDO = (20, 20, 40)
COLOR_JUGADOR = (0, 200, 255)
COLOR_METEORITO = (255, 100, 60)
COLOR_TEXTO = (255, 255, 255)



fuente = pygame.font.SysFont(None, 36)
fuente_grande = pygame.font.SysFont(None, 64)


sprite_jugador = pygame.image.load('MEDIA/kabum.png').convert_alpha()
sprite_meteorito = pygame.image.load('MEDIA/allinol.png').convert_alpha()
sprite_jugador = pygame.transform.scale(sprite_jugador, (50,50))
sprite_meteorito = pygame.transform.scale(sprite_meteorito, (50,50))

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

# TODO 2: Crea una variable booleana `juego_terminado` inicializada en False.
juego_terminado = False
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    teclas = pygame.key.get_pressed()

    # TODO 3: Haz que el jugador solo pueda moverse mientras `juego_terminado` sea False.
    if juego_terminado == False:
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
    puntaje +=1

    jugador_rect = pygame.Rect(jugador_x, jugador_y, JUGADOR_ANCHO, JUGADOR_ALTO)

    for meteorito in meteoritos:
        if jugador_rect.colliderect(meteorito):
            juego_terminado = True


    for i in range(4):
        if puntaje //10 == i*aumento:
            VELOCIDAD_METEORITO += 0.5
            print("Aumenta la velocidad del meteoro a", VELOCIDAD_METEORITO)
            nivel = i+1


    pantalla.fill(COLOR_FONDO)
    pantalla.blit(sprite_jugador, (jugador_x, jugador_y))
    for meteorito in meteoritos:
        pantalla.blit(sprite_meteorito, (meteorito.x, meteorito.y))

    texto_puntaje = fuente.render(f"Puntaje : {puntaje // 10}", True, COLOR_TEXTO)
    pantalla.blit(texto_puntaje, (10, 10))

    texto_nivel = fuente.render(f"Nivel : {nivel}",True, COLOR_TEXTO)
    pantalla.blit(texto_nivel, (200,20))


    if juego_terminado:
        print("Terminaste")
        pantalla.fill("red")
        texto_gameover = fuente_grande.render(f"Perdiste /n llegate al nivel {nivel} que fracasad@ eres", True, COLOR_TEXTO)
        rect_texto = texto_gameover.get_rect(center=(ANCHO // 2, ALTO // 2))
        pantalla.blit(texto_gameover, rect_texto)
    



    pygame.display.flip()
    reloj.tick(FPS)

pygame.quit()
sys.exit()


