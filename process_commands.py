from game import add_game, list_games
from game_stats import count_games, count_winrate


def str_to_dict(main_command_arguments):
    dictionary = {}
    for pairs in main_command_arguments:
        pair = pairs.split('=')
        dictionary[pair[0]] = pair[1]
    return dictionary


def process_commands(matches):
    while True:
        command_name = input('Enter the command: ')
        command_tokens = command_name.split()
        command_token_function = command_tokens[0]
        command_tokens_arguments = command_tokens[1:]
        arguments_dict = str_to_dict(command_tokens_arguments)
        if command_token_function == 'ADD':
            nickname = arguments_dict['nickname']
            race = arguments_dict['race']
            result = arguments_dict['result']
            add_game(matches, nickname, race, result)
        elif command_token_function == 'LIST_OF_GAMES':
            list_games(matches)
        elif command_token_function == 'STOP':
            break
        elif command_token_function == 'COUNT':
            nickname_for_count = arguments_dict['nickname']
            print(count_games(matches, nickname_for_count))
        elif command_token_function == 'WIN_RATE':
            nickname_for_count_wins = arguments_dict['nickname']
            print(count_winrate(matches, nickname_for_count_wins))
