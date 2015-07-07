from game import Game, State
from grid import Grid


class UserInterface:

    def __init__(self, game):
        self.__game = game

    def print_grid(self):
        width, height = self.__game.grid_dimensions()
        for x in range(height):
            for y in range(width):
                print(
                    '[{}{}]'.format(' ' * (4 - len(
                        str(self.__game.get_value_at((x, y))))),
                        self.__game.get_value_at((x, y))), end=' ')
            print()
        print('Score: {}'.format(self.__game.score()))

    def user_input(self, key):
        commands = {'a': self.__game.slide_to,
                    's': self.__game.slide_to,
                    'd': self.__game.slide_to,
                    'w': self.__game.slide_to,
                    'u': self.__game.undo,
                    'r': self.__game.reset
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
        self.__game.start()
        while self.__game.get_state() == State.running:
            self.print_grid()
            self.user_input(input())


if __name__ == '__main__':
    game = Game(Grid(4, 4))
    tui = UserInterface(game)
    tui.main_loop()
