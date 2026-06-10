from time import sleep

while True:
    ign = int(input("put a number: 1 or 0:"))
    if ign == 1:
        sleep(3)
        print("Your car is ON")


    elif ign == 0:
        sleep(3)
        print("Your car is OFF")


    else:
        print("PUT ANOTHER NUMBER PLEASE!!!!!!")
