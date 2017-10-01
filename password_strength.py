import getpass
import re
import math

def get_password_strength(password, customer_name, company):
    return is_not_short(password) + is_long(password) + is_low_upper_case(password) + is_digit(password) + \
           is_special_symbols(password) + not_in_blacklist(password) + not_repeat_symbols(password) + \
           not_name_in_password(password, customer_name) + not_company_in_password(password, company) + not_date_in_password(password)

def is_not_short(password):
    return len(password) > 6

def is_long(password):
    return len(password) > 11

def is_low_upper_case(password):
    return any([pwd_letter for pwd_letter in password if pwd_letter.islower()]) and \
           any([pwd_letter for pwd_letter in password if pwd_letter.isupper()])

def is_digit(password):
    return bool(list(filter(lambda x: x.isdigit(), password)))

def is_special_symbols(password):
    special_symbols_list = '%$#@!*?;:-_+=<>/~'
    return bool(list(filter(lambda x: x in special_symbols_list, password)))

def not_in_blacklist(password):
    blacklist = ['12345', 'password', 'qwerty', 'abc123', 'dragon',
                 '1qa2ws', '1qa@WS', 'master', 'monkey', 'superman',
                 '67890', '98765', '54321', 'abcde', 'fuckyou', 'pussy']
    return not bool([b for b in blacklist if password in b])

def not_repeat_symbols(password):
    for pwd_letter in password:
        if password.count(pwd_letter) >= math.floor(len(password)/2) and password.count(pwd_letter) > 1:
            return False
    return True

def not_name_in_password(password, customer_name):
    return password not in customer_name and customer_name not in password

def not_company_in_password(password, company):
    return password not in company and company not in password

def not_date_in_password(password):
    date_in_pwd = re.match('([0-3]?\d)[/.-]([0-1]?\d)[/.-](\d{2,4})', password)
    phone_in_pwd = re.match('(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})',
                            password)
    return not bool(date_in_pwd or phone_in_pwd)



if __name__ == '__main__':
    customer_name = input('input name: ')
    company = input('input company: ')
    password = getpass.getpass('input password: ')
    password_complexy = get_password_strength(password, customer_name, company)
    print('Password complexy is {}'.format(password_complexy))
    if password_complexy <= 5:
        print('You password is very simple')
    elif password_complexy <= 8:
        print('You password is medium')
    else:
        print('You password is complexy')
