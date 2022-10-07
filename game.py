

def add_game(matches, arguments):
    game = {
        'nickname': arguments['nickname'],
        'race': arguments['race'],
        'result': arguments['result']
    }
    matches.append(game)


def list_games(matches):
    for game in matches:
        print(game.get('nickname') + '(' + game.get('race') + ')' + ' - ' + game.get('result'))

