import pygame
from random import randint

pygame.init()

# Dimensiones de la ventana y configuración general
WIDTH = 1920
HEIGHT = 1080
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FPS = 60

# Velocidades iniciales
SPEED = randint(5, 10)
OBSTACLE_SPEED = 5

# Cargar imágenes y sonidos
bk = pygame.image.load("images/fondo.png")
bkover = pygame.image.load("images/gameoverbk.jpg")
car_red = pygame.image.load("images/car_red.png")
car_blue = pygame.image.load("images/car_blue.png")
car_green = pygame.image.load("images/car_green.png")
car_yellow = pygame.image.load("images/car_yellow.png")
obstaculo_img = pygame.image.load("images/obstaculo.png")
play_button = pygame.image.load("images/play_button.png")
fondo = pygame.mixer.Sound("music/fondo.mp3")

# Rectángulos de los objetos
car1 = car_red.get_rect(topleft=(WIDTH - 100, HEIGHT // 2 + 200))
car2 = car_blue.get_rect(topleft=(WIDTH - 100, HEIGHT // 2 + 70))
car3 = car_green.get_rect(topleft=(WIDTH - 100, HEIGHT // 2 + 450))
car4 = car_yellow.get_rect(topleft=(WIDTH - 100, HEIGHT // 2 + 330))
obstaculo = obstaculo_img.get_rect(center=(WIDTH // 2, HEIGHT // 2))
obstaculo2 = obstaculo_img.get_rect(center=(WIDTH // 7, HEIGHT // 2))
obstaculo3 = obstaculo_img.get_rect(center=(WIDTH // 5, HEIGHT // 3))
obstaculo4 = obstaculo_img.get_rect(center=(WIDTH // 3, HEIGHT // 1.5))

# Nombres de los coches
car1_name = input("Nombre para el coche 1 (rojo): ")
car2_name = input("Nombre para el coche 2 (azul): ")
car3_name = input("Nombre para el coche 3 (verde): ")
car4_name = input("Nombre para el coche 4 (amarillo): ")

# Estado de los coches (activo/inactivo)
active_cars = {
    "car1": True,
    "car2": True,
    "car3": True,
    "car4": True
}

# Contador de vueltas
vuelta_actual = {
    "car1": 0,
    "car2": 0,
    "car3": 0,
    "car4": 0
}

# Crear superficies de texto para el menú
font = pygame.font.Font(None, 65)
text_surface = font.render("Instrucciones: Llega a la meta lo más", True, (0, 0, 0))
text2_surface = font.render("rápido posible sin chocar con el obstáculo", True, (0, 0, 0))
controls_surface = font.render("Controles: Coche 1 (A/D), Coche 2 (flechas izquierda y derecha),", True, (0, 0, 0))
controls2_surface = font.render("Coche 3 (F/H), Coche 4 (J/L)", True, (0, 0, 0))

# Modo de juego inicial
game_mode = "menu"
running = True

# Bucle principal del juego
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and game_mode == "menu":
            if play_button.get_rect(center=(WIDTH // 2, HEIGHT // 2)).collidepoint(event.pos):
                game_mode = "playing"

    if game_mode == "menu":
        fondo.stop()
        window.fill((0, 255, 0))
        window.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, 0))
        window.blit(text2_surface, (WIDTH // 2 - text2_surface.get_width() // 2, text_surface.get_height()))
        window.blit(controls_surface, (WIDTH // 2 - controls_surface.get_width() // 2, text_surface.get_height() + text2_surface.get_height()))
        window.blit(controls2_surface, (WIDTH // 2 - controls2_surface.get_width() // 2, text_surface.get_height() + text2_surface.get_height() + controls_surface.get_height()))
        window.blit(play_button, (WIDTH // 2 - play_button.get_width() // 2, HEIGHT // 2 - play_button.get_height() // 2))
    elif game_mode == "game_over":
        fondo.stop()
        window.blit(bkover, (0, 0))
        y_offset = 100
        for car_name in vuelta_actual:
            for car_name in vuelta_actual:
                vuelta_text = font.render(f"{locals()[car_name + '_name']}: {vuelta_actual[car_name]} vueltas", True, (0, 225, 0))
                window.blit(vuelta_text, (WIDTH // 2 - vuelta_text.get_width() // 2, HEIGHT // -2 + y_offset))
                y_offset += 50
    elif game_mode == "playing":
        fondo.play(-1)  # Reproduce el fondo continuamente
        window.fill((0, 0, 0))
        window.blit(bk, (0, 0))
        # Dibujar los coches activos
        if active_cars["car1"]:
            window.blit(car_red, car1)
        if active_cars["car2"]:
            window.blit(car_blue, car2)
        if active_cars["car3"]:
            window.blit(car_green, car3)
        if active_cars["car4"]:
            window.blit(car_yellow, car4)

        window.blit(obstaculo_img, obstaculo)
        window.blit(obstaculo_img, obstaculo2)
        window.blit(obstaculo_img, obstaculo3)
        window.blit(obstaculo_img, obstaculo4)

        # Obtener el framerate actual
        fps = clock.get_fps()
        # Crear un objeto Surface con el texto del contador de FPS
        fps_text = font.render(f"FPS: {fps:.2f}", True, (255, 255, 255))
        # Dibujar el texto en la pantalla
        window.blit(fps_text, (10, 10))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        # Manejar movimiento solo para coches activos
        if active_cars["car1"]:
            if keys[pygame.K_a] and car1.left > 0:
                car1.x -= SPEED
            if keys[pygame.K_d] and car1.right < WIDTH:
                car1.x += SPEED
            if car1.left <= 0:
                vuelta_actual["car1"] += 1
                car1.x = WIDTH - 100  # Reiniciar posición
                print(f"El coche {car1_name} ha completado la vuelta {vuelta_actual['car1']}")
        if active_cars["car2"]:
            if keys[pygame.K_LEFT] and car2.left > 0:
                car2.x -= SPEED
            if keys[pygame.K_RIGHT] and car2.right < WIDTH:
                car2.x += SPEED
            if car2.left <= 0:
                vuelta_actual["car2"] += 1
                car2.x = WIDTH - 100  # Reiniciar posición
                print(f"El coche {car2_name} ha completado la vuelta {vuelta_actual['car2']}")
        if active_cars["car3"]:
            if keys[pygame.K_f] and car3.left > 0:
                car3.x -= SPEED
            if keys[pygame.K_h] and car3.right < WIDTH:
                car3.x += SPEED
            if car3.left <= 0:
                vuelta_actual["car3"] += 1
                car3.x = WIDTH - 100  # Reiniciar posición
                print(f"El coche {car3_name} ha completado la vuelta {vuelta_actual['car3']}")
        if active_cars["car4"]:
            if keys[pygame.K_j] and car4.left > 0:
                car4.x -= SPEED
            if keys[pygame.K_l] and car4.right < WIDTH:
                car4.x += SPEED
            if car4.left <= 0:
                vuelta_actual["car4"] += 1
                car4.x = WIDTH - 100  # Reiniciar posición
                print(f"El coche {car4_name} ha completado la vuelta {vuelta_actual['car4']}")

        # Mover los obstáculos y verificar límites
        obstaculo.y += OBSTACLE_SPEED
        if obstaculo.top < 0 or obstaculo.bottom > HEIGHT:
            OBSTACLE_SPEED = -OBSTACLE_SPEED

        obstaculo2.y += OBSTACLE_SPEED
        if obstaculo2.top < 0 or obstaculo2.bottom > HEIGHT:
            OBSTACLE_SPEED = -OBSTACLE_SPEED

        obstaculo3.y += OBSTACLE_SPEED
        if obstaculo3.top < 0 or obstaculo3.bottom > HEIGHT:
            OBSTACLE_SPEED = -OBSTACLE_SPEED

        obstaculo4.y += OBSTACLE_SPEED
        if obstaculo4.top < 0 or obstaculo4.bottom > HEIGHT:
            OBSTACLE_SPEED = -OBSTACLE_SPEED

        # Verificar colisiones y llegada a la meta
        for car_name, car_rect in [("car1", car1), ("car2", car2), ("car3", car3), ("car4", car4)]:
            if active_cars[car_name] and car_rect.colliderect(obstaculo):
                print(f"El coche {locals()[car_name + '_name']} ha chocado con el obstáculo y ha perdido!")
                active_cars[car_name] = False

            if active_cars[car_name] and car_rect.colliderect(obstaculo2):
                print(f"El coche {locals()[car_name + '_name']} ha chocado con el obstáculo y ha perdido!")
                active_cars[car_name] = False

            if active_cars[car_name] and car_rect.colliderect(obstaculo3):
                print(f"El coche {locals()[car_name + '_name']} ha chocado con el obstáculo y ha perdido!")
                active_cars[car_name] = False

            if active_cars[car_name] and car_rect.colliderect(obstaculo4):
                print(f"El coche {locals()[car_name + '_name']} ha chocado con el obstáculo y ha perdido!")
                active_cars[car_name] = False

        # Verificar si todos los coches están inactivos
        if not any(active_cars.values()):
            game_mode = "game_over"

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
