number = int(input("Enter the number: "))
power = int(input("Enter the power: "))

result = 1

for i in range(power):
    result *= number

print(f"{number} raised to the power {power} is: {result}")
