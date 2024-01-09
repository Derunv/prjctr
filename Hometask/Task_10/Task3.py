import random
import csv

players = ['John', 'Lisa', 'Bob', 'Alex', 'David']


def play_game(name: str) -> tuple:
    return (name, random.randint(1, 1000))


def game_challenge(rounds: int) -> list:
    games_record = []
    for i in range(rounds):
        for player in players:
            games_record.append(play_game(player))
    return games_record

def game_score_saver_csv(games_record: list) -> None:
    with open('game_challenge_score.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Player name', 'Score'])
        for score in games_record:
            writer.writerow(score)


# game_score_saver_csv(game_challenge(100))
