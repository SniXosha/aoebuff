def count_games(matches, nickname):
    all_games_count = 0
    for match in matches:
        if nickname == match['nickname']:
            all_games_count += 1
    return all_games_count


def count_winrate(matches, nickname):
    win_games_count = 0
    for match in matches:
        if nickname == match['nickname'] and match['result'] == 'win' :
            win_games_count += 1
    winrate = (win_games_count / count_games(matches, nickname)) * 100
    return winrate
