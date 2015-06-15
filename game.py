from grid import Grid


class Game:

    def __init(self, grid):
        self.__grid = grid
        self.__score = 0

    def slide_left(self):
        self.__score += self.grid.slide_left()
        self.__grid.generate_number()

    def slide_right(self):
        self.__score += self.grid.slide_right()
        self.__grid.generate_number()

    def slide_up(self):
        self.__score += self.grid.slide_up()
        self.__grid.generate_number()

    def slide_down(self):
        self.__score += self.grid.slide_down()
        self.__grid.generate_number()
