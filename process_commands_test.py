from game import add_game, list_games
from count_winrate import count_games, count_winrate


def str_to_dict(main_command_arguments):
    dictionary = {}
    for pairs in main_command_arguments:
        pair = pairs.split('=')
        dictionary[pair[0]] = pair[1]
    return dictionary


def process_commands_test(matches):
    while True:
        main_command_input = input('Enter the command: ')
        main_command_list = main_command_input.split()
        main_command_function = main_command_list[0]
        main_command_arguments = main_command_list[1:]
        arguments_dict = str_to_dict(main_command_arguments)
        if main_command_function == 'ADD':
            nickname = arguments_dict['nickname']
            race = arguments_dict['race']
            result = arguments_dict['result']
            add_game(matches, nickname, race, result)
        elif main_command_function == 'LIST_OF_GAMES':
            list_games(matches)
        elif main_command_function == 'STOP':
            break
        elif main_command_function == 'COUNT':
            nickname_for_count = arguments_dict['nickname']
            print(count_games(matches, nickname_for_count))
        elif main_command_function == 'WIN_RATE':
            nickname_for_count_wins = arguments_dict['nickname']
            print(count_winrate(matches, nickname_for_count_wins))
