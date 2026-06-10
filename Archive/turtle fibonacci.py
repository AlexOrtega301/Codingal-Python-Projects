import turtle

# Configurar la ventana de dibujo
turtle.setup(800, 600)

# Crear una instancia de 'Turtle'
t = turtle.Turtle()
t.speed(0)  # Velocidad de dibujo
# Definir los primeros dos términos de la serie de Fibonacci
a, b = 0, 1
t.color("red")
# Función para dibujar un cuarto de círculo con radio 'r'
def quarter_circle(r):
    for i in range(90):
        t.forward(r)
        t.left(1)

# Dibujar la espiral de Fibonacci
for i in range(10):  # Ajusta el rango para más o menos términos
    quarter_circle(b * 3)  # Ajusta el multiplicador para cambiar el tamaño
    a, b = b, a + b  # Siguiente número de Fibonacci

# Ocultar la tortuga y mostrar el resultado
t.hideturtle()
turtle.done()   
import turtle

# Configurar la ventana de dibujo
turtle.setup(800, 600)

# Crear una instancia de 'Turtle'
t = turtle.Turtle()
t.speed('fastest')  
a, b = 0, 1


def quarter_circle(r):
    for i in range(90):
        t.forward(r)
        t.left(1)


for i in range(10):  
    quarter_circle(b * 3)  
    a, b = b, a + b
    
t.hideturtle()
turtle.done()
