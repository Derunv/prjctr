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


def random_country() -> str:
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

