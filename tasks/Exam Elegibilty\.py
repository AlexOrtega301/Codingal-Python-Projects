# Simple CLI program to calculate attendance percentage

# Get input from the user
total_days = int(input("Enter total number of working days: "))
absent_days = int(input("Enter total number of absent days: "))

# Calculate attendance percentage
attended_days = total_days - absent_days
attendance_percentage = (attended_days / total_days) * 100

# Show the attendance percentage
print(f"\nYour attendance percentage is: {attendance_percentage:.2f}%")

# Check if student can sit in the exam
if attendance_percentage < 75:
    print("You are NOT allowed to sit in the exam. 😔")
else:
    print("You are allowed to sit in the exam! 🎉")
