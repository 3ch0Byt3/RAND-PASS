import random
import string

def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    random_password = ''.join(random.choice(characters) for i in range(length))
    return random_password

# Specify the length of the password
password_length = 12
random_password = generate_random_password(password_length)

print(f"Generated random password: > {random_password}")