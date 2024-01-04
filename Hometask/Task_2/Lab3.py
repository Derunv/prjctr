#Task 0
10 > 5
str(42) == "42"
3 < 4

#Task 1
print("I'm writing code")

#Task 2
print('Enter world to check is it palindrome')
user_string = str(input())
reverse_user_string = user_string[::-1]
print('The string palindrome? - ', user_string.lower() == reverse_user_string.lower())

#Task 3
print('Hello, enter your name')
user_name = str(input())
user_name = user_name[:1].upper() + user_name[1:]
print('Enter your age')
user_age = str(input())

print('Your name is', user_name, 'and your', user_age, 'years old')

about_str = 'Your name is {} and your {} years old'
print(about_str.format(user_name, user_age))

about_str = f'Your name is {user_name} and your {user_age} years old'
print(about_str)

#Task 4
string_1 = "Animals  "
print(string_1.lower())

string_2 = "  Badger"
print(string_2.upper())

string_3 = "   HoneyPot   "
print('|', string_3.lstrip(), '|') # a)
print('|', string_3.rstrip(), '|') # b)
print('|', string_3.strip(), '|') # c)

string_1 = "Bear"
print(string_1.startswith('Be'))
string_2 = "bear"
print(string_2.startswith('Be'))
string_3 = "BEAR"
print(string_3.startswith('Be'))
string_4 = "bEar"
print(string_4.startswith('Be'))

string_1 = "Bear"
formated_string_1 = string_1
print(string_1.startswith('Be'))
string_2 = "bear"
formated_string_2 = string_2.capitalize()
print(formated_string_2.startswith('Be'))
string_3 = "BEAR"
formated_string_3 = string_3.title()
print(formated_string_3.startswith('Be'))
string_4 = "bEar"
formated_string_4 = string_4.title()
print(formated_string_4.startswith('Be'))

#Task 7
secret_message= "'X!xeXnxiXlX XtxeXrxcXeXsX Xax XsX`XtXIX'"
secret_message_low_case = secret_message.lower()
splited = secret_message_low_case.split('x')
join= ''.join(splited)
print(join[::-1])