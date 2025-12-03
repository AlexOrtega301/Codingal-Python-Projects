# Program to print Fibonacci sequence using recursion

# Recursive function to find nth Fibonacci number
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Get input from the user
num_terms = int(input("Enter the number of terms you want in the Fibonacci sequence: "))

# Print the Fibonacci sequence
print("Fibonacci sequence:")
for i in range(num_terms):
    print(fibonacci(i), end=" ")
