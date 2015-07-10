from grid import Grid
from game import Game
from tui import TextUserInterface


def main():
    grid = Grid(4, 4)
    game = Game(grid)
    user_interface = TextUserInterface(game)
    user_interface.main_loop()


if __name__ == '__main__':
    main()
