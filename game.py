from enum import Enum
from grid import Grid
from exceptions import GridIsFullException


class State(Enum):
    running = 'running'
    over = 'over'
    continued = 'continued'


class Player:

    def __init__(self, name, score):
        self.name = name
        self.score = score


class Chart:

    def __init__(self):
        self.top_players = []

    def add(self, candidate):
        for player in enumerate(self.top_players):
            if player[1].score < candidate.score:
                self.top_players.insert(player[0], candidate)
        if len(self.top_players) > 9:
            self.top_players.pop()

# TODO finish high_scores


class Game:

    def __init__(self, grid):
        self.__grid = grid
        self.__score = 0
        self.__high_scores = []
        self.__history = []
        self.__state = State.running

# TODO fix slide_to to generate number only if its necessery
    def slide_to(self, direction):
        if direction not in ['left', 'right', 'up', 'down']:
            return
        points_gained = {'left': self.__grid.slide_left,
                         'right': self.__grid.slide_right,
                         'up': self.__grid.slide_up,
                         'down': self.__grid.slide_down
                         }.get(direction)()
        try:
            self.__grid.generate_number()
        except GridIsFullException:
            if not self.__grid.can_slide():
                self.__state = 'over'
                return  # ?

        self.__score += points_gained
        self.__history.append((self.__grid, points_gained))
        if len(self.__history) > 3:
            self.__history.pop(0)

    def undo(self):
        if len(self.__history) > 0:
            grid, score = self.__history.pop()
            self.__grid = grid
            self.__score -= score

    def start(self):
        self.__grid.generate_number()
        self.__grid.generate_number()

    def get_value_at(self, position):
        return self.__grid[position]

    def score(self):
        return self.__score

    def reset_grid(self):
        self.__grid.reset()

    def grid_dimensions(self):
        return self.__grid.dimensions()

    def get_state(self):
        return self.__state

    def pr(self):
        self.__grid.draw()
