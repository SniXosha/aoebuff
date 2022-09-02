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
