import random
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Usage
password_length = 12  # You can change the desired password length here
password = generate_password(password_length)
print("Generated Password:", password)