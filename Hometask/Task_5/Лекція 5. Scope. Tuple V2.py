# Task1
def receive_input():
    input_string = input('Please enter some data')
    return input_string


def check_input() -> int:
    while True:
        try:
            input_string = receive_input()
            input_string = int(input_string)
            print(f'The inputted value - {input_string}')
            break
        except ValueError:
            print('That was not an integer')


check_input()

# Task2
def get_user_input():
    while True:
        try:
            user_string = input('Enter a string: ')
            user_index = int(input('Enter an integer: '))
            return user_string, user_index
        except ValueError:
            print('Invalid input. Please enter a valid string and integer.')

def print_char_at_index():
    while True:
        try:
            user_string, user_index = get_user_input()
            char_at_index = user_string[user_index]
            print(f'Character at index {user_index}: {char_at_index}')
            break
        except IndexError:
            print(f'Index {user_index} is out of range for the given string.')
        except Exception:
            print('An error occurred')

print_char_at_index()

# Task3


def transaction(amount, _type):
    # Two inner functions called deposit and withdrawal for argument _type.
    def deposit(amount):
        balance =10000
        balance += amount
        print(f"Deposit of ${amount} successful. New balance: ${balance}")

    def withdrawal(amount):
        balance =10000
        if amount <= balance:
            balance -= amount
            print(f"Withdrawal of ${amount} successful. New balance: ${balance}")
        else:
            print("Insufficient funds. Withdrawal unsuccessful.")

    if _type == 'deposit':
        deposit(amount)
    elif _type == 'withdrawal':
        withdrawal(amount)
    else:
        print("Invalid transaction type. Please use 'deposit' or 'withdrawal'.")

# Usage:
transaction(200, 'deposit')
transaction(50, 'withdrawal')
transaction(1200, 'withdrawal')


# Task4

import random

def roll_dice(N:int = 6):
    # Simulate a dice roll and return the result from 1 to 6.
    return random.randint(1, N)

print("The dice rolled:", roll_dice())

# Task5

def simulate_dice_rolls(num_rolls):
    # Simulate rolls dice rolls and store the results in a list.
    rolls = []
    for i in range(num_rolls):
        rolls.append(roll_dice())
    count_1, count_2, count_3, count_4, count_5, count_6 = 0, 0, 0, 0, 0, 0
    for roll in rolls:
        if roll == 1:
            count_1 += 1
        elif roll == 2:
            count_2 += 1
        elif roll == 3:
            count_3 += 1
        elif roll == 4:
            count_4 += 1
        elif roll == 5:
            count_5 += 1
        elif roll == 6:
            count_6 += 1
    return count_1, count_2, count_3, count_4, count_5, count_6

results = simulate_dice_rolls(1000)

for i in range(len(results)):
    print(f"Number {i+1}: {count} times")
	

# Task6

import random

def receive_input():
    num_regions = int(input('Enter the number of regions: '))
    ratings = []
    for i in range(1, num_regions + 1):
        rating = int(input(f'Enter a rating for 1st candidate in {i} region: '))
        ratings.append(rating)
    return num_regions, ratings

def simulate_region_election(rating):
    total_votes = 10000
    candidate_votes = int((rating / 100) * total_votes)
    opponent_votes = total_votes - candidate_votes
    return candidate_votes, opponent_votes

def simulate_election(input_data):
    num_regions, ratings = input_data
    election_result = []
    for i in range(num_regions):
        rating = ratings[i]
        region_result = simulate_region_election(rating)
        print(f'Region {i + 1}: {region_result[0]} votes for 1st candidate, {region_result[1]} votes for 2nd candidate')
        election_result.append(region_result)
    return election_result

def calculate_result(election_result):
    total_candidate_votes = sum(result[0] for result in election_result)
    total_votes = sum(sum(result) for result in election_result)
    percentage = (total_candidate_votes / total_votes) * 100
    percentage = round(percentage, 2)
    return total_candidate_votes, percentage

def announce_result(result):
    total_votes, percentage = result
    print(f'\nResult: 1st candidate won with {total_votes} votes and {percentage}% of all votes')

input_data = receive_input()
election_result = simulate_election(input_data)
result = calculate_result(election_result)
announce_result(result)
