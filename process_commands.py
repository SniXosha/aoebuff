from game import add_game, list_games


def process_commands(matches):
    while True:
        first_command = input('Enter the command: ')
        if first_command == 'ADD':
            nickname = input('Nickname: ')
            race = input('Race: ')
            result = input('Result: ')
            add_game(matches, nickname, race, result)
        elif first_command == 'LIST_OF_GAMES':
            list_games(matches)
        elif first_command == 'STOP':
            break
