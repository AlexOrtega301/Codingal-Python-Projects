import turtle

# ——————————————————————————————————————————————————————————————
# Configuración de la pantalla
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("Diseño")
screen.bgcolor("blue")

# ——————————————————————————————————————————————————————————————
# Configuración de la tortuga
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()

# Tamaño de cada "pixel"
PIXEL_SIZE = 20

def draw_pixel(x, y, color):
    """Dibuja un cuadrado de lado PIXEL_SIZE en la posición (x,y)."""
    t.goto(x, y)
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(PIXEL_SIZE)
        t.right(90)
    t.end_fill()
    t.penup()

# ——————————————————————————————————————————————————————————————
# 1) CARA NEGRA CON OJOS MORADOS

# Punto de partida (arriba a la izquierda) de la rejilla de 14×14
HEAD_ORIGIN_X = -300
HEAD_ORIGIN_Y =  200

# Dibuja el fondo negro (filas 5–10, columnas 4–11)
for row in range(5, 11):        # filas de la rejilla (1 = abajo, 14 = arriba)
    for col in range(4, 12):    # columnas de la rejilla (1 = izq., 14 = der.)
        x = HEAD_ORIGIN_X + (col-1)*PIXEL_SIZE
        y = HEAD_ORIGIN_Y - (row-1)*PIXEL_SIZE
        draw_pixel(x, y, "black")

# Ojos: 2 tonos de morado
eyes = [
    # fila, col, color
    (6,  5, "#D47FFF"), (6,  6, "#800080"),
    (7,  5, "#D47FFF"), (7,  6, "#800080"),
    (6, 10, "#D47FFF"), (6,  9, "#800080"),
    (7, 10, "#D47FFF"), (7,  9, "#800080"),
]
for r, c, col in eyes:
    x = HEAD_ORIGIN_X + (c-1)*PIXEL_SIZE
    y = HEAD_ORIGIN_Y - (r-1)*PIXEL_SIZE
    draw_pixel(x, y, col)

# ——————————————————————————————————————————————————————————————
# 2) CUPCAKE

# Punto de partida (abajo a la izquierda) de la rejilla aproximada de 10×10
CAKE_ORIGIN_X =  100
CAKE_ORIGIN_Y =  150  # este Y se usa como tope superior de la base marrón

# Base marrón (trapezoide invertido)
# fila 1: col 6       → 1 píxel
# fila 2: cols 5–7    → 3 píxeles
# fila 3: cols 4–8    → 5 píxeles
# fila 4: cols 4–8    → 5 píxeles
base_coords = [
    (1, [6]),
    (2, [5,6,7]),
    (3, [4,5,6,7,8]),
    (4, [4,5,6,7,8]),
]
for r, cols in base_coords:
    for c in cols:
        x = CAKE_ORIGIN_X + (c-1)*PIXEL_SIZE
        y = CAKE_ORIGIN_Y - (r-1)*PIXEL_SIZE
        draw_pixel(x, y, "#5C4033")  # marrón

# Glaseado rosa (forma de pirámide)
# fila 5: cols 3–8   → 6 píxeles
# fila 6: cols 4–7   → 4 píxeles
# fila 7: cols 5–6   → 2 píxeles
frost_coords = [
    (5, [3,4,5,6,7,8]),
    (6, [4,5,6,7]),
    (7, [5,6]),
]
for r, cols in frost_coords:
    for c in cols:
        x = CAKE_ORIGIN_X + (c-1)*PIXEL_SIZE
        y = CAKE_ORIGIN_Y - (r-1)*PIXEL_SIZE
        draw_pixel(x, y, "pink")

# Cereza roja encima (fila 8, col 6)
x = CAKE_ORIGIN_X + (6-1)*PIXEL_SIZE
y = CAKE_ORIGIN_Y - (8-1)*PIXEL_SIZE
draw_pixel(x, y, "red")

# ——————————————————————————————————————————————————————————————
turtle.done()
