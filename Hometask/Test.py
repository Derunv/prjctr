# Task 1 - Area of a  Triangle Given its Vertices
x1 = 0
x2 = 0
x3 = 3
y1 = 0
y2 = 4
y3 = 0
triangle_area = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

# Task 2 - Count a number of words in the sentence
sentence = "Гаррі Поттер (англ. Harry Potter) — серія з семи фантастичних романів англійської письменниці..."
count_words = sentence.replace('(', '').replace('-', '').replace(')', '').strip().count(' ')
print(count_words)

# Task 3 - Count a number of words in the sentence
start_string = "snake_case_text"
end_string = start_string.replace('_', ' ').title().replace(' ', '')
print(end_string[:1].lower() + end_string[1:])

# Task 4 - FizzBuzz
given_number = int(input("Give me last number count to"))
output_string = ''
# fizz_buzz function
while given_number >= 1:
    if (given_number % 3) == 0 and (given_number % 5) == 0:
        output_string += 'zzuBzziF '
    elif (given_number % 3) == 0:
        output_string += 'zziF '
    elif (given_number % 5) == 0:
        output_string += 'zzuB '
    else:
        output_string += str(given_number) + ' '
    given_number -= 1
print(output_string[-2::-1])

# Task 5 CamelCase to snake_case convertor
start_string = "SnakeCaseText"
end_string = ''
a = 0
while len(start_string) > a:
    if start_string[a].isupper() and a == 0:
        end_string = start_string[a].lower()
    elif start_string[a].isupper():
        end_string += '_' + start_string[a].lower()
    else:
        end_string += start_string[a]
    a += 1
print(end_string)

# Task 6 Anagrams
strings_s1 = str(input('Put first strings'))
strings_s2 = str(input('Put second strings'))
is_strings_anagrams = True
if len(strings_s1) == len(strings_s2):
    a = 0
    while len(strings_s1) > a and is_strings_anagrams == True:
        if strings_s2.find(strings_s1[a]) == -1:
            is_strings_anagrams = False
        else:
            a += 1
else:
    is_strings_anagrams = False

print(is_strings_anagrams)
