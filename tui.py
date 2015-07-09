from game import State
from utilities import getch
from re import match


class TextUserInterface:

    def __init__(self, game):
        self.__game = game

    def print_grid(self):
        width, height = self.__game.grid_dimensions()
        for x in range(height):
            for y in range(width):
                value = self.__game.get_value_at((x, y))
                print('[{}{}]'.format(
                    ' ' * (4 - len(str(value))), value if value != 0 else ' '), end=' ')
            print()

    def print_data(self):
        print('Score: {}'.format(self.__game.score()),
              'Undos left: {}'.format(self.__game.undos_left()))

    def clear_screen(self):
        print('\033c')

    def print_high_scores(self):
        for player in enumerate(self.__game.get_top_players()):
            if player[1][0] != '':
                print(
                    '{}. {} {}'.format(
                        player[0] + 1,
                        player[1][0],
                        player[1][1]))
        print()

    def user_input(self, key):
        key = key.lower()
        commands = {'a': self.__game.slide_to,
                    's': self.__game.slide_to,
                    'd': self.__game.slide_to,
                    'w': self.__game.slide_to,
                    'u': self.__game.undo,
                    'r': self.__game.reset,
                    }
        if key in commands:
            if key == 'a':
                commands[key]('left')
            elif key == 's':
                commands[key]('down')
            elif key == 'd':
                commands[key]('right')
            elif key == 'w':
                commands[key]('up')
            else:
                commands[key]()

    def main_loop(self):
        self.__game.load_top_scores('data.bin')
        self.__game.start()
        while self.__game.get_state() == State.running:
            self.clear_screen()
            self.print_grid()
            self.print_data()
            char = getch()
            self.user_input(char)
            if char == chr(26):
                break

            if self.__game.get_state() == State.game_over:
                print('Game Over!')
                if self.__game.check_score():
                    print('Your score is within the top 10!')
                    print('Enter your name:')
                    name = input()
                    score = self.__game.score()
                    while not match(r'[a-zA-Z0-9]', name):
                        print('\'{}\' is not a valid name.'.format(name))
                        print('Please try again.')
                        print('Enter your name:')
                        name = input()
                    self.__game.add_player_to_chart(name, score)
                    print('\nHigh Scores')
                    self.print_high_scores()
                    self.__game.save_top_scores('data.bin')
                    print('Do you want to play again? y/n')
                    if input() == 'y':
                        self.__game.change_state(State.running)
                        self.__game.reset()
                    else:
                        self.clear_screen()
