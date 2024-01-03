# Task 1
import random

capitals = {
        'Ukraine': 'Kyiv', 'France': 'Paris', 'Germany': 'Berlin',
        'Italy': 'Rome', 'USA': 'Washington', 'Canada': 'Ottawa',
        'Switzerland': 'Bern', 'Austria': 'Vienna',
        'Belgium': 'Brussels', 'Sweden': 'Stockholm',
        'Norway': 'Oslo', 'Denmark': 'Copenhagen',
        'Finland': 'Helsinki', 'Poland': 'Warsaw',
        'Romania': 'Bucharest', 'Bulgaria': 'Sofia', 'Greece': 'Athens'
}


def random_country() -> tuple[str, str]:
        country, capital = random.choice(list(capitals.items()))
        return country, capital


def game(country: str, capital: str) -> str:
        print(f'Please enter capital for {country}')
        user_input = input('The capital is:')
        if user_input.lower() == 'exit':
                return 'exit'
        elif user_input.lower() == capital.lower():
                return 1
        else:
                return -1


def start(lives=3):
        score = 0
        while lives > 0:
                country, capital = random_country()
                status = game(country, capital)
                if status == 'exit':
                        print(f'Your`s score is {score}')
                        lives = 0
                elif status == 1:
                        score += 1
                        print(f"You are right! Your`s score is {score}")

                else:
                        lives -= 1
                        print(f"Sorry you are wrong! Your score is {score}")



start()

# Task 2
def roman_to_int(s: str) -> int:
    roman_symbol_value = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M':1000 }
    converted_value = []
    for i in range(len(s)):
        converted_value.append(roman_symbol_value[s[i]])
        if i != 0:
            if converted_value[i - 1] < converted_value[i]:
                converted_value[i - 1] = - converted_value[i - 1]
    return sum(converted_value)

def test_roman_to_int():
     result1 = roman_to_int("III")
     assert result1 == 3
     result1 = roman_to_int("LVIII")
     assert result1 == 58
     result1 = roman_to_int("MCMXCIV")
     assert result1 == 1994

test_roman_to_int()

# Task 3
def int_to_roman(s: int) -> str:
    roman_symbol_value = {
        1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC",
        50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"
    }
    result = ""

    for value, numeral in roman_symbol_value.items():
        while s >= value:
            result += numeral
            s -= value
    return result


def test_int_to_roman():
    result1 = int_to_roman(3)
    assert result1 == "III"

    result1 = int_to_roman(58)
    assert result1 == "LVIII"

    result1 = int_to_roman(1994)
    assert result1 == "MCMXCIV"


# print(int_to_roman(58))
test_int_to_roman()

# Task 4
def majority_element(nums: list) -> int:
    nums_lib = {}
    for num in nums:
        if num in nums_lib:
            nums_lib[num] += 1
        else:
            nums_lib[num] = 1
    max_value = 0
    key = None
    for num, value in nums_lib.items():
        if value > max_value:
            max_value = value
            key = num
    #max_num = (max(nums_lib.values()), nums_lib.keys())
    return key


def test_majority_element():
    result1 = majority_element([3, 2, 3])
    assert result1 == 3

    result1 = majority_element([2, 2, 1, 1, 1, 2, 2])
    assert result1 == 2

test_majority_element()


# Task 5
def get_subjects_not_passed_by_all_students(student_exams):
    subject_scores = {}
    subject_not_passed_by_all_students = set()
    # Populate the dictionary with subjects and corresponding scores
    for name, score, subject in student_exams:
        if subject in subject_scores:
            subject_scores[subject].append(score)
        else:
            subject_scores[subject] = [score]
    for subject in subject_scores:
        #print(max(subject_scores.get(subject)))
        if max(subject_scores.get(subject)) < 60:
            subject_not_passed_by_all_students.add(subject)
    return subject_not_passed_by_all_students


def test_get_subjects_not_passed_by_all_students():
    exams = [
        ("Alice", 55, "Math"),
        ("Bob", 40, "Math"),
        ("Charlie", 30, "Math"),
        ("Alice", 50, "Science"),
        ("Bob", 45, "Science"),
        ("Charlie", 40, "Science"),
        ("Alice", 95, "History"),
        ("Bob", 85, "History"),
        ("Charlie", 90, "History"),
        ("Charli", 90, "History")
    ]
    assert get_subjects_not_passed_by_all_students(exams) == {"Science", "Math"}

test_get_subjects_not_passed_by_all_students()