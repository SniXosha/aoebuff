def count_games(matches, nickname_for_count):
    all_games_count = 0
    for game in matches:
        if nickname_for_count == game['nickname']:
            all_games_count += 1
    return all_games_count


def count_winrate(matches, nickname_for_count_wins):
    win_games_count = 0
    for game in matches:
        if nickname_for_count_wins == game['nickname']:
            if game['result'] == 'win':
                win_games_count += 1
            winrate = (win_games_count / count_games(matches, nickname_for_count_wins)) * 100
    return winrate
