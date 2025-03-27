import random, string


def generate_salt_key(length=10):
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def password_verify(password):
    if len(password) > 8 and len(password) < 16 and any(char.isdigit() for char in password) and any(char.isupper() for char in password):
        return True
    return False