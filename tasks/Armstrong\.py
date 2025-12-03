# Program to check if a number is an Armstrong number

# Get input from the user
num = int(input("Enter a positive integer: "))

# Calculate the number of digits
n = len(str(num))

# Initialize sum
sum_of_powers = 0
temp = num

# Calculate sum of digits raised to the power n
while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** n
    temp //= 10

# Check if sum of powers equals the original number
if sum_of_powers == num:
    print(f"{num} is an Armstrong number! 🎉")
else:
    print(f"{num} is NOT an Armstrong number. 😔")
