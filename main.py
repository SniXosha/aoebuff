from serialize import load_obj, save_obj
from process_commands_test import process_commands_test

matches_path = 'data/matches.json'

if __name__ == '__main__':
    matches = load_obj(matches_path, [])

    process_commands_test(matches)

    save_obj(matches, matches_path)
