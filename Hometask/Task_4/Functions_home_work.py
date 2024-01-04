# Task 1
def find_primes(a: int, b: int) -> str:
    # Takes in two integers and returns a list of all the prime numbers between
    # Please do not use a huge numbers
    num_list = ''
    for num in range(a, b + 1):
        flag = True
        if num == 1:
            flag = False
        elif num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    flag = False
                    break
            if flag == True:
                num_list += str(num) + ' '
    print(num_list)

find_primes(1, 200)

# Task 2
def unique_characters(string_s: str) -> bool:
    # Takes in a string and returns a Boolean value indicating whether or not all the characters in are unique
    string_s = sorted(string_s)
    for i in range(len(string_s) - 1):
        if string_s[i] == string_s[i+1]:
            return False
            break
    return True

unique_characters(input())

# Task 3
def fibonacci(n: int) -> int:
    # Calculates the Fibonacci series of numbers to the n index
    preceding_fibonacci_number = 0
    current_fibonacci_number = 1
    if n == 0:
        print('Error, 0 can`t be Fibonacci series of numbers')
    for i in range(n - 1):
        current_fibonacci_number = preceding_fibonacci_number + current_fibonacci_number
        preceding_fibonacci_number = current_fibonacci_number - preceding_fibonacci_number
    print( current_fibonacci_number)


fibonacci(int(input('Enter integer number')))

# Task 4
def swapcase(input_string: str) -> str:
    # Implements case swapping of leter same as swapcase()
    input_string = input_string.strip()
    swapcase_string = ''
    for i in range(len(input_string)):
        if input_string[i].isupper():
            swapcase_string += input_string[i].lower()
        else:
            swapcase_string += input_string[i].upper()
    return swapcase_string

print(swapcase('HelLo!'))

# Task 5
def simple_interest(initial_amount: int, interest_rate: float, years: int) -> float:
    # Calculates the performance of a deposit in a bank account using simple interest
    amount = int(initial_amount)
    for i in range(int(years)):
        amount = amount + amount * interest_rate
    return round(amount, 2)


print(simple_interest(10000, 0.1, 10)) 