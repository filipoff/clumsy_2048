from grid import Grid
from game import Game
from tui import TextUserInterface


def main():
    grid = Grid(4, 4)
    game = Game(grid)
    grid._Grid__cells = [[1024, 4, 0, 0],
                         [1024, 4, 0, 0],
                         [4, 4, 0, 0],
                         [4, 2, 4, 0]]
    user_interface = TextUserInterface(game)
    user_interface.main_loop()


if __name__ == '__main__':
    main()
