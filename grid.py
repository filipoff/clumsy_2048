from random import randint
from random import random


class Grid:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.used_cell_positions = []
        self.cells = [[0 for x in range(width)] for y in range(height)]

    def __getitem__(self, index):
        return self.cells[index]

    def draw(self):
        for x in range(self.height):
            for y in range(self.width):
                print(self.cells[x][y], end=' ')
            print()
        print()

    def generate_number(self):
        if len(self.used_cell_positions) == self.width * self.height:
            raise Exception
        random_x = randint(0, self.height - 1)
        random_y = randint(0, self.width - 1)
        while (random_x, random_y) in self.used_cell_positions:
            random_x = randint(0, self.height - 1)
            random_y = randint(0, self.width - 1)

        random_value = 2 if random() < 0.9 else 4
        self.cells[random_x][random_y] = random_value
        self.used_cell_positions.append((random_x, random_y))

    def slide_left(self):

        def merge(sequence):
            result = []
            for x in range(len(sequence) - 1):
                for y in range(x + 1, len(sequence)):
                    if sequence[x] == sequence[y] and sequence[x] != 0:
                        result.append(sequence[x] * 2)
                        sequence[y] = 0
                        sequence[x] *= 2
            zeroes_count = self.width - len(result)
            for _ in range(zeroes_count):
                result.append(0)
            return result

        for row in range(self.height):
            self.cells[row] = merge(self.cells[row])

    def slide_right(self):
        pass

    def slide_up(self):
        pass

    def slide_down(self):
        pass


if __name__ == '__main__':
    width = 4
    height = 4
    g = Grid(width, height)
    g.cells[0][0] = 2
    g.cells[0][1] = 2
    g.cells[0][2] = 2
    #g.cells[0][3] = 2
    g.draw()
    g.slide_left()
    g.draw()
