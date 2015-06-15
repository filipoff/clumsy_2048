from random import randint, choice, random


class Grid:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [[0 for x in range(width)] for y in range(height)]

    def draw(self):
        for x in range(self.height):
            for y in range(self.width):
                print('[{}]'.format(self.cells[x][y]), end=' ')
            print()
        print()

    @property
    def free_cells(self):
        result = []
        for x in range(self.height):
            for y in range(self.width):
                if self.cells[x][y] == 0:
                    result.append((x, y))
        return result

    def generate_number(self):
        if len(self.free_cells) == 0:
            raise Exception

        random_value = 2 if random() < 0.9 else 4
        x, y = choice(self.free_cells)
        self.cells[x][y] = random_value

    def __set_column(self, index, sequence):
        for x in range(self.height):
            self.cells[x][index] = sequence[x]

    def __remove_zeros(self, sequence):
        zeros_removed = sequence.count(0)
        while 0 in sequence:
            sequence.remove(0)
        return zeros_removed

    def __add_zeros(self, sequence, count, to_left=False):
        if to_left:
            sequence[0:0] = ([0] * count)
        else:
            sequence.extend([0] * count)

    def __left_merge(self, sequence):
        if all(value == 0 for value in sequence):
            return
        zeros_to_add = self.__remove_zeros(sequence)
        for x in range(len(sequence) - 1):
            if sequence[x] == sequence[x + 1]:
                sequence[x] *= 2
                sequence.pop(x + 1)
                sequence.append(0)
        self.__add_zeros(sequence, zeros_to_add)

    def __right_merge(self, sequence):
        if all(value == 0 for value in sequence):
            return
        zeros_to_add = self.__remove_zeros(sequence)
        for x in range(len(sequence) - 1, 0, -1):
            if sequence[x] == sequence[x - 1]:
                sequence[x] *= 2
                sequence.pop(x - 1)
                sequence.insert(0, 0)
        self.__add_zeros(sequence, zeros_to_add, to_left=True)

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
