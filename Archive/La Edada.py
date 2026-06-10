#imports
from random import randint
from time import sleep
x = randint(1,18)
print("© Alex")
while True:
    my_age = (int(input("Cuantos Años tienes?????")))
    if my_age == x and my_age <= 19:
        print("somos de la misma edad :0")
        break
    elif my_age > x and my_age < 18:
        print("eres mas viejo que  yo :0")
    elif my_age < x and my_age < 18:
        print("eres mas joven que yo :0")
    else:
        print("ERROR")
        break
wc = (input("Salir Y o Y"))
