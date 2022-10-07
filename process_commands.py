from game import add_game, list_games
from game_stats import count_games, count_winrate


def str_to_dict(arguments_tokens):
    dictionary = {}
    for pairs in arguments_tokens:
        pair = pairs.split('=')
        dictionary[pair[0]] = pair[1]
    return dictionary


def parse_command(command):
    tokens = command.split()
    name = tokens[0]
    arguments_tokens = tokens[1:]
    arguments = str_to_dict(arguments_tokens)
    return name, arguments


def process_commands(matches):
    while True:
        try:
            command = input('Enter the command: ')
            name, arguments = parse_command(command)
            if name == 'ADD':
                add_game(matches, arguments)
            elif name == 'LIST_OF_GAMES':
                list_games(matches)
            elif name == 'STOP':
                break
            elif name == 'COUNT':
                print(count_games(matches, arguments))
            elif name == 'WIN_RATE':
                print(count_winrate(matches, arguments))
        except Exception:
            print('command failed')
