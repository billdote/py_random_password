import string
import random

def generate_random_password():
    length = int(input('Enter desired length of password: '))
    
    exclude_schar = input('Enter any special characters to exclude (!@#$()%^&*): ')
    schar = '!@#$%^&*()'.replace(exclude_schar, '') if exclude_schar else '!@#$%^&*()'

    characters = list(string.ascii_letters + string.digits + schar)
    
    random.shuffle(characters)
    password = []

    for i in range(length):
        password.append(random.choice(characters))

    random.shuffle(password)
    print(f"Generated Password: {''.join(password)}")

generate_random_password()
