age = int(input("Enter your age: "))

if age > 0:
    if age >= 10 and age <= 20:
        print("You are eligible to enroll in the class.")
    else:
        print("You are not eligible to enroll in the class.")
else:
    print("Please enter a valid age.")
