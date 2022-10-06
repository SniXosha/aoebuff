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
        command = input('Enter the command: ')
        name, arguments = parse_command(command)
        if name == 'ADD':
            nickname = arguments['nickname']
            race = arguments['race']
            result = arguments['result']
            add_game(matches, nickname, race, result)
        elif name == 'LIST_OF_GAMES':
            list_games(matches)
        elif name == 'STOP':
            break
        elif name == 'COUNT':
            nickname = arguments['nickname']
            print(count_games(matches, nickname))
        elif name == 'WIN_RATE':
            nickname = arguments['nickname']
            print(count_winrate(matches, nickname))
