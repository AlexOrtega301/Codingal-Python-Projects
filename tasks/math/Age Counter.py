def check_age():
    try:
        age = int(input("Enter your age: "))  # Try converting input to integer
        if age % 2 == 0:
            print(f"Age {age} is even.")
        else:
            print(f"Age {age} is odd.")
    except ValueError:
        print("Invalid input! Please enter a whole number (integer).")

# Run the function
check_age()
