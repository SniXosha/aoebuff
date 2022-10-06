from game import add_game, list_games
from count_winrate import count_games, count_winrate


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
        elif first_command == 'COUNT':
            nickname_for_count = input('Enter the nickname of player: ')
            print(count_games(matches, nickname_for_count))
        elif first_command == 'WIN_RATE':
            nickname_for_count_wins = input('Enter the nickname of player: ')
            print(str(count_winrate(matches, nickname_for_count_wins)) + '%')


