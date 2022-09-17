import string
import random
import sys

def generate_random_password():
    length = int(input('Enter password length: '))
    
    exclude_schar = input('Enter special characters to exclude (!@#$()%^&*): ')
    schar = '!@#$%^&*()'.replace(exclude_schar, '') if exclude_schar else '!@#$%^&*()'

    characters = list(string.ascii_letters + string.digits + schar)
    
    random.shuffle(characters)
    password = []

    for i in range(length):
        password.append(random.choice(characters))

    random.shuffle(password)
    print(f"\nGenerated Password: {''.join(password)}")

try:
    generate_random_password()
except:
    print('Exiting...')
    sys.exit(1)
