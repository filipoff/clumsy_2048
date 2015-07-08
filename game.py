from enum import Enum
from copy import deepcopy


class State(Enum):
    running = 'running'
    game_over = 'game_over'
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

# TODO must finish chart


class Game:

    def __init__(self, grid):
        self.__grid = grid
        self.__score = 0
        self.__high_scores = Chart()
        self.__history = []
        self.__state = State.running
        self.__undo_counter = 0

    def slide_to(self, direction):
        if direction not in ['left', 'right', 'up', 'down']:
            return
        grid_before_slide = deepcopy(self.__grid)
        points_gained, must_generate = {'left': self.__grid.slide_left,
                                        'right': self.__grid.slide_right,
                                        'up': self.__grid.slide_up,
                                        'down': self.__grid.slide_down
                                        }.get(direction)()
        if must_generate:
            self.__history.append((grid_before_slide, points_gained))
            if len(self.__history) > 3:
                self.__history.pop(0)
            self.__grid.generate_number()
            self.__score += points_gained
        else:
            if not self.__grid.can_slide():
                import ipdb
                ipdb.set_trace()
                self.__state = State.game_over

    def undo(self):
        if self.__undo_counter == 3:
            return
        if len(self.__history) > 0:
            grid, score = self.__history.pop()
            self.__grid = grid  # ? or copy
            self.__score -= score
            self.__undo_counter += 1

    def start(self):
        self.__grid.generate_number()
        self.__grid.generate_number()

    def get_value_at(self, position):
        return self.__grid[position]

    def score(self):
        return self.__score

    def reset(self):
        self.__grid.reset()
        self.__history = []
        self.__state = State.running
        self.__score = 0
        self.__undo_counter = 0
        self.start()

    def grid_dimensions(self):
        return self.__grid.dimensions()

    def get_state(self):
        return self.__state

    def pr(self):
        self.__grid.draw()

    def undos_left(self):
        return 3 - self.__undo_counter
