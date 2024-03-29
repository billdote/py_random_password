#!/usr/bin/env python3

import os
import random
import string
from re import match
from sys import exit
from csv import writer


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
        'Do you want to create or append to a password file (Y/N)? ')

    if match('Y|y', create_file):
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
    exit(1)
