import math

def trig_values():
    try:
        angle_deg = float(input("Enter angle in degrees: "))  # Input in degrees
        angle_rad = math.radians(angle_deg)  # Convert degrees to radians

        sin_val = math.sin(angle_rad)
        cos_val = math.cos(angle_rad)
        tan_val = math.tan(angle_rad)

        print(f"sin({angle_deg}) = {sin_val:.4f}")
        print(f"cos({angle_deg}) = {cos_val:.4f}")
        print(f"tan({angle_deg}) = {tan_val:.4f}")
    except ValueError:
        print("Invalid input! Please enter a numeric value.")

# Run the function
trig_values()
