from random import randint
from random import random


class Grid:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.used_cell_positions = []
        self.cells = [[0 for x in range(width)] for y in range(height)]

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

    def __set_column(self, index, sequence):
        for x in range(self.height):
            self.cells[x][index] = sequence[x]

    def __left_merge(self, sequence):
        zeros_to_add = sequence.count(0)
        while 0 in sequence:
            sequence.remove(0)
        for x in range(len(sequence) - 1):
            if sequence[x] == sequence[x + 1]:
                sequence[x] *= 2
                sequence.pop(x + 1)
                sequence.append(0)
        sequence.extend([0] * zeros_to_add)

    def __right_merge(self, sequence):
        zeros_to_add = sequence.count(0)
        while 0 in sequence:
            sequence.remove(0)
        for x in range(len(sequence) - 1, 0, -1):
            if sequence[x] == sequence[x - 1]:
                sequence[x] *= 2
                sequence.pop(x - 1)
                sequence.insert(0, 0)
        sequence[0:0] = ([0] * zeros_to_add)

    def slide_left(self):
        for row_index in range(self.height):
            self.__left_merge(self.cells[row_index])

    def slide_right(self):
        for row_index in range(self.height):
            self.__right_merge(self.cells[row_index])

    def slide_up(self):
        for column_index in range(self.width):
            column = [self.cells[x][column_index] for x in range(self.height)]
            self.__left_merge(column)
            self.__set_column(column_index, column)

    def slide_down(self):
        for column_index in range(self.width):
            column = [self.cells[x][column_index] for x in range(self.height)]
            self.__right_merge(column)
            self.__set_column(column_index, column)
