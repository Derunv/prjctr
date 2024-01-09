from Task3 import game_score_saver_csv as get_csv, game_challenge as stat_challenge
import csv

# Check if a file with data exists; if not, create it using the Task3 functions.
try:
    open('game_challenge_score.csv', mode='r')
except FileNotFoundError:
    get_csv(stat_challenge(100))

with open('game_challenge_score.csv', mode='r') as file, open('high_scores.csv', 'w') as high_scores:
    reader = csv.DictReader(file)
    players_score = {}
    for row in reader:
        name = row.get('Player name')
        score = row.get('Score')
        if name in players_score.keys(): # Create dict and add Player name as Key
            # (if Gamers has same Name result will be wrong), values: list of result
            players_score[name].append(score)
        else:
            players_score[name] = [score]
            # players_score[name].append(score)
    writer = csv.writer(high_scores)
    writer.writerow(['Player name', 'Highest score'])
    for player, score in players_score.items():
        writer.writerow((player, max(score)))


