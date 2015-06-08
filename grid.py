from random import randint
from random import random


class Grid:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.used_cells = 0
        self.cells = [[0 for x in range(width)] for y in range(height)]

    def __getitem__(self, index):
        return self.cells[index]

    def draw(self):
        for x in range(self.width):
            for y in range(self.height):
                print(self.cells[x][y], sep=']', end=' ')
            print()

    def generate_number(self):
        random_x = randint(0, self.width - 1)
        random_y = randint(0, self.height - 1)
        if self.used_cells != self.width * self.height:
            while self.cells[random_x][random_y] != 0:
                random_x = randint(0, self.width - 1)
                random_y = randint(0, self.height - 1)
        else:
        	raise Exception
        random_value = 2 if random() < 0.9 else 4
        self.cells[random_x][random_y] = random_value
        self.used_cells += 1

if __name__ == '__main__':
    g = Grid(4, 4)
    for x in range(4 * 4 + 1):
        g.generate_number()
    g.draw()
