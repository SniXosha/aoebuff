import json
import os.path

data_path = 'data/matches.json'


def add_game(matches, nickname, race, result):
    game = {
        'nickname': nickname,
        'race': race,
        'result': result
    }
    matches.append(game)


def list_games(matches):
    for game in matches:
        print(game.get('nickname') + '(' + game.get('race') + ')' + ' - ' + game.get('result'))


def load_history(path):
    if not os.path.exists(path):
        return []

    with open(path, 'r') as file:
        return json.load(file)


def save_history(history, path):
    with open(path, 'w') as file:
        return json.dump(history, file)


if __name__ == '__main__':
    match_history = load_history(data_path)

    add_game(match_history, 'Mista', 'eng', 'win')
    add_game(match_history, 'Beastyqt', 'abbasid', 'loss')
    list_games(match_history)

    save_history(match_history, data_path)
