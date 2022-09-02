match_history = []


def add_game(nickname, race, result):
    global match_history
    game = {
        'nickname': nickname,
        'race': race,
        'result': result
    }
    match_history.append(game)


def list_games():
    for game in match_history:
        print(game.get('nickname') + '(' + game.get('race') + ')' + ' - ' + game.get('result'))


if __name__ == '__main__':
    add_game('Mista', 'eng', 'win')
    add_game('Beastyqt', 'abbasid', 'loss')
    list_games()
