# Task 1
False == ( not True )
( True and  False ) == ( True and False )
not ( True and "A" == "B" )

# Task 2
wheat_weights = 0.065
grains_of_wheat_on_chessboard = (2 ** 64 - 1) * wheat_weights / 10 ** 6
print(
    f'If one wheat weights - {wheat_weights} gram, weights of all wheat on a chessboard will be '
    f'{int(grains_of_wheat_on_chessboard)} tons or {int(grains_of_wheat_on_chessboard / 10 ** 9)} billion tons ')

# Task 3
string_from_input = input('Please enter a positive, integer number to get all factors')
if string_from_input.isdigit() and string_from_input.isdecimal() and int(string_from_input) >= 0 :
    string_from_input = int(string_from_input)
    i = int(string_from_input / 2)
    factors_of_number = str(string_from_input)
    while i >= 1:
        if  string_from_input % i == 0:
            factors_of_number += ' ' + str(i)
        i -= 1
    print(f'All factors of this number is: {factors_of_number}')
else:
    print('This number isn`t positive and integer')

# Task 4 Check whether a triangle is equilateral, isosceles or scalene
all_sides = input('Please input all three sides using space').split()
side_a = all_sides[0]
side_b = all_sides[1]
side_c = all_sides[2]
if side_a == side_b == side_c:
    print('Triangle is equilateral')
elif side_a == side_b or side_a == side_c or side_b == side_c:
    print('Triangle is isosceles')
else:
     print('Triangle is scalene')

# Task 5
symbol_sequence = input('Enter symbol sequence:')
i = 0
max_number_of_symbol_repeat = 1
consecutive_symbol = ''
while i < len(symbol_sequence) - 1:
    if symbol_sequence[i] == symbol_sequence[i + 1]:
        max_number_of_symbol_repeat +=1
        consecutive_symbol += str(max_number_of_symbol_repeat)
    else:
        max_number_of_symbol_repeat = 1
        consecutive_symbol += str(max_number_of_symbol_repeat)
    i += 1
consecutive_symbol = int(consecutive_symbol.index(max(consecutive_symbol))) + 1
print( f'Longest consecutive symbol is \'{symbol_sequence[consecutive_symbol]}\'')

# Task 6
given_date = input('Please enter date in format yyyy-mm-dd').split('-')
day_of_given_date = int(given_date[2])
month_of_given_date = int(given_date[1])
year_of_given_date = int(given_date[0])
max_days_in_month = str('31 28 31 30 31 30 31 31 30 31 30 31').split()
if year_of_given_date % 4 == 0:
    max_days_in_month[1] = 29
if int(max_days_in_month[month_of_given_date - 1]) > day_of_given_date:
    print (f'**Input a year:** {year_of_given_date}\n'
           f'**Input a month [1-12]:** {month_of_given_date}\n'
           f'**Input a day [1-31]:** {day_of_given_date}\n'
           f'The next date is {year_of_given_date}-{month_of_given_date}-{day_of_given_date + 1}')
else:
    print (f'**Input a year:** {year_of_given_date}\n'
           f'**Input a month [1-12]:** {month_of_given_date}\n'
           f'**Input a day [1-31]:** {day_of_given_date}\n'
           f'The next date is {year_of_given_date}-{month_of_given_date + 1}-1')
