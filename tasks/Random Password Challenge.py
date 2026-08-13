import random
import string

def generate_password(length=12):
    # Define possible characters: lowercase, uppercase, digits
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    
    # Randomly choose characters
    password = ''.join(random.choice(characters) for _ in range(length))
    
    # Shuffle the password to make it less predictable
    password_list = list(password)
    random.shuffle(password_list)
    
    return ''.join(password_list)

# Example usage
print("Generated Password:", generate_password(12))
