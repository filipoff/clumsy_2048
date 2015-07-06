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
                    '[ {} ]'.format(self.__game.get_value_at((x, y))), end=' ')
            print()
        print()

    def user_input(self, key):
        if key == 'a':
            self.__game.slide_to('left')
        elif key == 'd':
            self.__game.slide_to('right')
        elif key == 'w':
            self.__game.slide_to('up')
        elif key == 's':
            self.__game.slide_to('down')

    def main_loop(self):
        self.__game.start()
        while self.__game.get_state() == State.running:
            self.print_grid()
            self.user_input(input())


if __name__ == '__main__':
    game = Game(Grid(4, 4))
    tui = UserInterface(game)
    tui.main_loop()
