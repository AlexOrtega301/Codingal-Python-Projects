# Get input from the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print("\nBefore swapping:")
print("a =", a)
print("b =", b)
print("c =", c)

# Swap the values
a, b, c = b, c, a

print("\nAfter swapping:")
print("a =", a)
print("b =", b)
print("c =", c)
