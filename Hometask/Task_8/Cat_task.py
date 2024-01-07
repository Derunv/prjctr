def generate_cat_circle(cats: int = 100) -> list:
    cat_circle = []
    for i in range(cats):
        cat_circle.append([i+1, 'hat_off'])
    return cat_circle


def cat_round_rolls(data: list) -> list:
    cat, hat = data
    if hat == 'hat_off':
        return [cat, 'hat_on']
    else:
        return [cat, 'hat_off']


def start_circle(rounds: int = 100, cats: int = 100) -> list:
    cat_circle = generate_cat_circle(cats)
    if rounds > cats:
        raise ValueError(f'You can`t run {rounds} rounds, you have {cats} cats! Please try again. '
                         f'Cats must be greater (or equal) than rounds. ')
    for i in range(rounds):
        for j in cat_circle[i::i+1]:
            cat_circle[j[0]-1] = cat_round_rolls(j)
    return cat_circle


print(start_circle(11, 10))
