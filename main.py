from serialize import load_obj, save_obj
from game import add_game, list_games

matches_path = 'data/matches.json'

if __name__ == '__main__':
    matches = load_obj(matches_path, [])

    add_game(matches, 'Mista', 'eng', 'win')
    add_game(matches, 'Beastyqt', 'abbasid', 'loss')
    list_games(matches)

    save_obj(matches, matches_path)
