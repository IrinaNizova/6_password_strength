import unittest
from password_strength import get_password_strength

class QuadraticEquationTestCase(unittest.TestCase):
    name = 'ira'
    company = 'linux'

    def print_parts(self, password, name, company):
        print(password)
        print('is_not_short: ', is_not_short(password))
        print('is_long: ', is_long(password))
        print('is_low_upper_case: ', is_low_upper_case(password))
        print('is_digit', is_digit(password))
        print('is_special_symbols', is_special_symbols(password))
        print('not_in_blacklist', not_in_blacklist(password))
        print('not_repeat_symbols', not_repeat_symbols(password))
        print('not_name_in_password', not_name_in_password(password, name))
        print('not_company_in_password', not_company_in_password(password, company))
        print('not_date_in_password', not_date_in_password(password))
        print("___________________________________")

    def test_good_password(self):
        password = 'Nizova1987@_'
        self.assertEqual(get_password_strength(password, self.name, self.company), 10)

    def test_password_like_name(self):
        password = 'ira'
        self.assertEqual(get_password_strength(password, self.name, self.company), 4)

    def test_password_like_company(self):
        password = 'lin'
        self.assertEqual(get_password_strength(password, self.name, self.company), 4)

    def test_password_like_date(self):
        password = '11.11.1987'
        self.assertEqual(get_password_strength(password, self.name, self.company), 5)

    def test_digit_password(self):
        password = '12345'
        self.assertEqual(get_password_strength(password, self.name, self.company), 5)

    def test_common_password(self):
        password = '121212'
        self.assertEqual(get_password_strength(password, self.name, self.company), 5)

if __name__ == '__main__':
    unittest.main()