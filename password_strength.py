from string import punctuation
import getpass
import re
import math

MIN_LENGTH_MEDIUM_PASSWORD = 6
MIN_LENGTH_COMPLEX_PASSWORD = 12


def get_password_strength(pwd):
    return sum([is_not_short(pwd), is_long(pwd), is_low_upper_case(pwd), is_digit(pwd),
               is_special_symbols(pwd), not_in_blacklist(pwd), not_repeat_symbols(pwd),
               not_date_in_password(pwd), not_phone_in_password(pwd)]) + 1


def is_not_short(password):
    return len(password) >= MIN_LENGTH_MEDIUM_PASSWORD


def is_long(password):
    return len(password) >= MIN_LENGTH_COMPLEX_PASSWORD


def is_low_upper_case(password):
    return any([pwd_letter for pwd_letter in password if pwd_letter.islower()]) and \
           any([pwd_letter for pwd_letter in password if pwd_letter.isupper()])


def is_digit(password):
    return bool(list(filter(lambda x: x.isdigit(), password)))


def is_special_symbols(password):
    return bool(list(filter(lambda x: x in punctuation, password)))


def not_in_blacklist(password):
    with open("blacklist") as file:
        blacklist = [row.strip() for row in file]
    return not bool([b for b in blacklist if password in b])


def not_repeat_symbols(password):
    for pwd_letter in password:
        if password.count(pwd_letter) >= math.floor(len(password)/2):
            return False
    return True


def not_date_in_password(password):
    date_in_pwd = re.match('([0-3]?\d)[/.-]([0-1]?\d)[/.-](\d{2,4})', password)
    return not bool(date_in_pwd)

def not_phone_in_password(password):
    phone_in_pwd = re.match('(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})',
                            password)
    return not bool(phone_in_pwd)


if __name__ == '__main__':
    password = getpass.getpass('input password: ')
    password_complexy = get_password_strength(password)
    print('Password complexy is {}'.format(password_complexy))
    if password_complexy <= 5:
        print('You password is very simple')
    elif password_complexy <= 8:
        print('You password is medium')
    else:
        print('You password is complexy')
