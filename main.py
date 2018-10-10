from five import Five

# Example of using Five library

my_five = Five()

if my_five + 3 == 8 and 4 ** my_five < 10000:
    print(my_five.say_five_times('Everyone should drinks vodka!\n'))

print(my_five.say_five_in_language('Russian'))  # пять
print(my_five.say_five_in_language('Polish'))  # pięć
print(my_five.draw_five())
my_five.print_actual_five_properties()
print(my_five.is_complex() == False)
print(bin(int(my_five)))
my_five.print_five_in_digit_type('European')
my_five.print_five_in_digit_type('Arabic')
my_five.print_five_in_digit_type('Arabic-west')
print(my_five.as_sum())  # 3+2
print(my_five.as_fraction())  # 10/2
print(my_five.say_five_times(my_five.draw_five()))
