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
                print('[{}]'.format(self.cells[x][y]), end=' ')
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
        def merge(sequence, to_right=False):
            zeros_to_add = 0
            while 0 in sequence:
                sequence.remove(0)
                zeros_to_add += 1
            for x in range(len(sequence) - 1):
                if sequence[x] == sequence[x + 1]:
                    sequence[x] *= 2
                    sequence.pop(x + 1)
                    sequence.append(0)
            sequence.extend([0] * zeros_to_add)
        for row_index in range(self.height):
            merge(self.cells[row_index])

    def slide_right(self):
        pass

    def slide_up(self):
        pass

    def slide_down(self):
        pass
