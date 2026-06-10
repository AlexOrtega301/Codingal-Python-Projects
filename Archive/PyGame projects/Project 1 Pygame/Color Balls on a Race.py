import pygame
import random
import linecache as cahe_bad

pygame.init()
FPS = 60
WIDTH = 900
HEIGHT = 700
alex = 0
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)  # Definimos el color naranja
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
run = True
direction = "right"
x = WIDTH - 70
y = HEIGHT // 2

# Definimos la posición y dimensiones de la línea de meta
meta_x = 10
meta_y = 0
meta_width = 10
meta_height = HEIGHT

# Definimos la posición de la bola en la parte inferior
x2 = WIDTH - 70
y2 = HEIGHT - 50

# Definimos la posición de la bola azul
x3 = WIDTH - 70
y3 = HEIGHT // 6

# Definimos la posición de la bola naranja
x4 = WIDTH - 70
y4 = HEIGHT - 240
ii = input("Que pelota crees que ganara")
# Definimos la velocidad de la bola verde, la bola roja, la bola azul y la bola naranja
velocidad_bola_verde = random.randint(1, 15)
velocidad_bola_roja = random.randint(1, 15)
velocidad_bola_azul = random.randint(1, 15)
velocidad_bola_naranja = random.randint(1, 15)  # Definimos la velocidad de la bola naranja

while run:
    window.fill((0, 0, 0))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
    red_circle = pygame.draw.circle(window, RED, (x, y), 40)
    if direction == "right" and x > meta_x:
        x = x - velocidad_bola_roja
        if x <= meta_x:
            print("La pelota roja ganó")
            run = False

    # Dibujamos la línea de meta
    meta = pygame.draw.rect(window, BLUE, (meta_x, meta_y, meta_width, meta_height))

    # Dibujamos la bola en la parte inferior y la movemos con la velocidad aleatoria
    green_circle = pygame.draw.circle(window, GREEN, (x2, y2), 40)
    if x2 > 0:
        x2 = x2 - velocidad_bola_verde
        if x2 <= meta_x:
            print("La pelota verde ganó")
            run = False

    # Dibujamos la bola azul y la movemos con la velocidad aleatoria
    blue_circle = pygame.draw.circle(window, BLUE, (x3, y3), 40)
    if x3 > 0:
        x3 = x3 - velocidad_bola_azul
        if x3 <= meta_x:
            print("La pelota azul ganó")
            alex = alex + 26
            run = False

    # Dibujamos la bola naranja y la movemos con la velocidad aleatoria
    orange_circle = pygame.draw.circle(window, ORANGE, (x4, y4), 40)
    if x4 > 0:
        x4 = x4 - velocidad_bola_naranja
        if x4 <= meta_x:
            print("La pelota naranja ganó")
            run = False

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
