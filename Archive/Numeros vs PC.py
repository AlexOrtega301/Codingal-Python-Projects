from random import randint
a = randint(1,10)
count = 0
while True:
    b = (int(input("enter a Number from 1 to 10")))
    if b == a:
        print("lo Lograste :0")
        break
    elif a > b :
        print("tu numero es menor :(")
        count = count + 1
    elif a < b and b <= 10:
        print("tu numero es mayor :(")
        count = count + 1
    elif b > 10:
        print("tu numero NO esta en la lista :(")
print("el numero era", a, ":)")
if count > 1:
    print("fueron",count, "intentos")
elif count < 1:
    print("fueron",count, "intentos")
elif count == 1:
    print("wow fueron",count,"intentos , eres un Master :0 , ;),:)")
g = input("Salir Y o Y")
