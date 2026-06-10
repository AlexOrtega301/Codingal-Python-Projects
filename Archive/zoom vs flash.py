import random
zoom = random.randint(1,1000)
flash = random.randint(1,1000)
print(zoom)
print(flash)
if zoom > flash:
    print("NO")
if zoom < flash:
    print("SÍ")
if zoom == flash:
    print("NO SE")
a = input("Salir Y o Y")
