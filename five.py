import math
import random

class Five:
    @property
    def five_lang(self):
        return {'American': 'The fucking five',
                'Arabic': 'خَمْسة',
                'Aramaic': 'חַמְשָׁה',
                'Aramaic-Modern': 'hámsha',
                'Belarusian': 'пяць',
                'Bosnian': 'pet',
                'Bulgarian': 'пет',
                'Chinese': '五',
                'Czech': 'pět',
                'English': 'five',
                'Esperanto': 'kvin',
                'Finnish': 'viisi',
                'Greek': 'fhɛks',
                'Japanese': '五',
                'Japanese-old': 'いつ',
                'Korean': '다섯',
                'Latvian': 'pieci',
                'Lithuanian': 'penki',
                'Polish': 'pięć',
                'Russian': 'пять',
                'Slovak': 'päť',
                'Turkish': 'beş',
                'Ukrainian': 'п\'ять'}

    @property
    def five_digit(self):
        return {'Arabic': '٥',
                'Arabic-west': '۵',
                'Dewanagari': '५',
                'Bengalic': '৫',
                'Gurmukhi': '੫',
                'Gudharati ': '૫',
                'European': '5',
                'Orija': '୫',
                'Tamil': '௫',
                'Telugu': '౫',
                'Kannada': '೫',
                'Malajalam': '൫',
                'Laothany': '໕',
                'Tibet': '༥',
                'Birm': '၅',
                'Khmers': '៥',
                'Mongoly': '᠕',
                'Tai lue': '᧕',
                }

    @property
    def five(self):
        return 5

    @staticmethod
    def say_five():
        return "five"

    @staticmethod
    def draw_five():
        return'''
____
|
|--\\
   |
---/
        '''

    def print_five_in_digit_type(self, digit_type):
        print(self.five_digit.get(digit_type, '5'))

    def get_five_in_digit_type(self, digit_type):
        return self.five_digit.get(digit_type, '5')

    def as_sum(self):
        a = random.randint(1, 1000)
        b = self.five - a
        return str(a) + ' + ' + str(b)

    def as_fraction(self):
        a = random.randint(1, 1000)
        b = a*self.five
        return str(b) + ' / ' + str(a)

    def as_product(self):
        a = random.randint(1, 1000)
        b = self.five/a
        return str(a) + ' * ' + str(b)

    @staticmethod
    def print_actual_five_properties():
        print('''Five is prime number.
Five is natural number.
Five is integer number.
Five is rational number.
Five is real number.
Five is odd number.
Five is positive number''')

    @staticmethod
    def say_five_times(word: str):
        return str(word) * 5

    @staticmethod
    def is_prime():
        return True

    @staticmethod
    def is_composite():
        return True

    @staticmethod
    def is_natural():
        return True

    @staticmethod
    def is_interger():
        return True

    @staticmethod
    def is_rational():
        return True

    @staticmethod
    def is_irrational():
        return False

    @staticmethod
    def is_real():
        return True

    @staticmethod
    def is_complex():
        return False

    @staticmethod
    def is_odd():
        return True

    @staticmethod
    def is_even():
        return False

    @staticmethod
    def is_positive():
        return True

    @staticmethod
    def is_nonpositive():
        return False

    @staticmethod
    def is_negative():
        return False

    @staticmethod
    def is_nonegative():
        return True

    @staticmethod
    def is_zero():
        return False

    @staticmethod
    def is_divisor(num):
        return num % 5 == 0

    def say_five_in_language(self, language: str):
        return self.five_lang.get(language, 'five')

    def add_five(self, number):
        return number + self.five

    def sub_five(self, number):
        return number - self.five

    def mul_five(self, number):
        return number * self.five

    def div_five(self, number):
        return number / self.five

    def quo_five(self, number):
        return number // self.five

    def rem_five(self, number):
        return number % self.five

    def pow_five(self, number):
        return number ** self.five

    def log_five(self, number):
        return math.log(number, self.five)

    def exp_five(self):
        return math.e ** self.five

    def __add__(self, other):
        return self.add_five(other)

    def __radd__(self, other):
        return self.add_five(other)

    def __sub__(self, other):
        return self.five - other

    def __rsub__(self, other):
        return self.sub_five(other)

    def __mul__(self, other):
        return self.mul_five(other)

    def __rmul__(self, other):
        return self.mul_five(other)

    def __floordiv__(self, other):
        return self.five // other

    def __rfloordiv__(self, other):
        return self.quo_five(other)

    def __mod__(self, other):
        return self.five % other

    def __rmod__(self, other):
        return self.rem_five(other)

    def __truediv__(self, other):
        return self.five / other

    def __rtruediv__(self, other):
        return self.div_five(other)

    def __pow__(self, other):
        return self.five ** other

    def __rpow__(self, other):
        return self.pow_five(other)

    def __lshift__(self, other):
        return self.five << other

    def __ilshift__(self, other):
        return self.five << other

    def __rshift__(self, other):
        return other >> self.five

    def __irshift__(self, other):
        return other >> self.five

    def __and__(self, other):
        return self.five & other

    def __rand__(self, other):
        return other * self.five

    def __xor__(self, other):
        return self.five ^ other

    def __rxor__(self, other):
        return other ^ self.five

    def __or__(self, other):
        return self.five | other

    def __ror__(self, other):
        return other | self.five

    def __iadd__(self, other):
        return self.five + other

    def __isub__(self, other):
        return self.five - other

    def __imul__(self, other):
        return self.five * other

    def __idiv__(self, other):
        return self.five / other

    def __ifloordiv__(self, other):
        return self.five // other

    def __itruediv__(self, other):
        return self.five / other

    def __imod__(self, other):
        return self.five % other

    def __ipow__(self, other):
        return self.five ** other

    def __iand__(self, other):
        return self.five & other

    def __ixor__(self, other):
        return self.five ^ other

    def __ior__(self, other):
        return self.five | other

    def __neg__(self):
        return -self.five

    def __pos__(self):
        return +self.five

    def __abs__(self):
        return abs(self.five)

    def __invert__(self):
        return -self.five - 1

    def __complex__(self):
        return complex(self.five)

    def __int__(self):
        return int(self.five)

    def __float__(self):
        return float(self.five)

    def __oct__(self):
        return oct(self.five)

    def __hex__(self):
        return hex(self.five)

    def __str__(self):
        return str(self.five)

    def __lt__(self, other):
        return self.five < other

    def __le__(self, other):
        return self.five <= other

    def __eq__(self, other):
        return self.five == other

    def __ne__(self, other):
        return self.five != other

    def __ge__(self, other):
        return self.five >= other

    def __gt__(self, other):
        return self.five > other
