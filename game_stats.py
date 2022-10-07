def count_games(matches, args):
    all_games_count = 0
    for match in matches:
        if args['nickname'] == match['nickname']:
            all_games_count += 1
    return all_games_count


def count_winrate(matches, args):
    win_games_count = 0
    all_games = 0
    for match in matches:
        if not should_count(match, args):
            continue
        if match['result'] == 'win':
            win_games_count += 1
        all_games += 1
    winrate = (win_games_count / all_games) * 100
    return winrate


def should_count(match, args):
    if match['nickname'] != args['nickname']:
        return False
    if 'race' in args and args['race'] != match['race']:
        return False
    return True

