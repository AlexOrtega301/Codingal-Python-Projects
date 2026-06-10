import random
import pygame

pygame.init()

FPS = 60
WIDTH = 800
HEIGHT = 600
RED = (255, 0, 0)

window = pygame.display.set_mode((WIDTH, HEIGHT))
window.fill(RED)
run = True
crazy_mode = False
clock = pygame.time.Clock()  # Windows se define 'clock'

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                window.fill(random_color)
            elif event.key == pygame.K_TAB:
                random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                window.fill(random_color)
            elif event.key == pygame.K_c:
                crazy_mode = not crazy_mode
    if crazy_mode:
        random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        window.fill(random_color)
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
