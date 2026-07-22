try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
except ValueError:
    print("Error: Invalid input. Please enter valid numbers.")


def add(a, b):
    try:
        print(a + b)
    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")
def subs(a, b):
    try:
        print(a - b)
    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")
def multi(a, b):
    try:
        print(a * b)
    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")
def div(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")
def floor(a, b):
    try:
        print(a // b)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")
try:
    add(a, b)
    subs(a, b)
    multi(a, b) 
    div(a, b)
    floor(a, b)
except NameError:
    print("The program will end now.")
