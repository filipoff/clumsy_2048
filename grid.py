from random import random, choice
from copy import deepcopy
from exceptions import GridIsFullException


class Grid:

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__cells = [[0 for x in range(width)] for y in range(height)]

    def __getitem__(self, position):
        x, y = position
        if x < self.__width and x >= 0 and y < self.__height and y >= 0:
            return self.__cells[x][y]

    @property
    def __free_cells(self):
        result = []
        for x in range(self.__height):
            for y in range(self.__width):
                if self.__cells[x][y] == 0:
                    result.append((x, y))
        return result

    def draw(self):
        for x in range(self.__height):
            for y in range(self.__width):
                print('[{}]'.format(self.__cells[x][y]), end=' ')
            print()
        print()

    def can_slide(self):
        slide_methods = ['slide_up', 'slide_left']
        for method in slide_methods:
            currently_testing_grid = deepcopy(self)
            if getattr(currently_testing_grid, method)()[1]:
                return True
        return False

    def reset(self):
        self.__cells = [
            [0 for x in range(self.__width)] for y in range(self.__height)]

    def dimensions(self):
        return self.__width, self.__height

    def generate_number(self):
        if len(self.__free_cells) == 0:
            raise GridIsFullException

        random_value = 2 if random() < 0.9 else 4
        x, y = choice(self.__free_cells)
        self.__cells[x][y] = random_value

    def slide_left(self):
        total_points_recieved = 0
        any_has_changed = False
        for row_index in range(self.__height):
            points_recieved, has_changed = self.__left_merge(
                self.__cells[row_index])
            any_has_changed = any_has_changed or has_changed
            total_points_recieved += points_recieved
        return total_points_recieved, any_has_changed

    def slide_right(self):
        total_points_recieved = 0
        any_has_changed = False
        for row_index in range(self.__height):
            points_recieved, has_changed = self.__right_merge(
                self.__cells[row_index])
            any_has_changed = any_has_changed or has_changed
            total_points_recieved += points_recieved
        return total_points_recieved, any_has_changed

    def slide_up(self):
        total_points_recieved = 0
        any_has_changed = False
        for column_index in range(self.__width):
            column = [self.__cells[x][column_index]
                      for x in range(self.__height)]
            points_recieved, has_changed = self.__left_merge(column)
            any_has_changed = any_has_changed or has_changed
            total_points_recieved += points_recieved
            self.__set_column(column_index, column)
        return total_points_recieved, any_has_changed

    def slide_down(self):
        total_points_recieved = 0
        any_has_changed = False
        for column_index in range(self.__width):
            column = [self.__cells[x][column_index]
                      for x in range(self.__height)]
            points_recieved, has_changed = self.__right_merge(column)
            any_has_changed = any_has_changed or has_changed
            total_points_recieved += points_recieved
            self.__set_column(column_index, column)
        return total_points_recieved, any_has_changed

    def __set_column(self, index, sequence):
        for x in range(self.__height):
            self.__cells[x][index] = sequence[x]

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
            return 0, False
        sequence_before_merge = list(sequence)
        has_changed = False
        zeros_to_add = self.__remove_zeros(sequence)
        points_recieved = 0
        for x in range(len(sequence) - 1):
            if sequence[x] == sequence[x + 1]:
                sequence[x] *= 2
                sequence.pop(x + 1)
                sequence.append(0)
                points_recieved += sequence[x]
        self.__add_zeros(sequence, zeros_to_add)
        if sequence_before_merge != sequence:
            has_changed = True
        return points_recieved, has_changed

    def __right_merge(self, sequence):
        if all(value == 0 for value in sequence):
            return 0, False
        sequence_before_merge = list(sequence)
        has_changed = False
        zeros_to_add = self.__remove_zeros(sequence)
        points_recieved = 0
        for x in range(len(sequence) - 1, 0, -1):
            if sequence[x] == sequence[x - 1]:
                sequence[x] *= 2
                sequence.pop(x - 1)
                sequence.insert(0, 0)
                points_recieved += sequence[x]
        self.__add_zeros(sequence, zeros_to_add, to_left=True)
        if sequence_before_merge != sequence:
            has_changed = True
        return points_recieved, has_changed
