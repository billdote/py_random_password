#!/usr/bin/env python3

from csv import writer
import string
import random
import re
import os
import sys


def generate_random_password():
    length = int(input('Enter password length: '))

    exclude_schar = input('Enter special characters to exclude (!@#$()%^&*): ')
    schar = '!@#$%^&*()'.replace(exclude_schar, '') if exclude_schar else '!@#$%^&*()'

    characters = list(string.ascii_letters + string.digits + schar)
    random.shuffle(characters)

    password = [random.choice(characters) for _ in range(length)]

    random.shuffle(password)
    password = ''.join(password)

    create_file = input(
        'Do you want to create or append to a password file? (Y/N) ')

    if re.match('Y|y', create_file):
        create_password_file(password)
    else:
        print(f"\nGenerated Password: {password}")


def create_password_file(password):
    # file headers
    col_names = ['USERNAME', 'PASSWORD', 'DESCRIPTION']

    username = input('\nEnter username: ')
    description = input('Enter description (what the login is for): ')

    data = [username, password, description]

    # create a password csv file or append to it
    # file will have a permissions mode of 600
    with open('passwords.csv', 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)

        if os.stat('passwords.csv').st_size == 0:
            os.chmod('passwords.csv', 0o600)
            csv_writer.writerow(col_names)
        csv_writer.writerow(data)


# ignore errors and exit
try:
    generate_random_password()
except:
    print('Exiting...')
    sys.exit(1)
