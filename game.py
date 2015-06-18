from enum import Enum


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


class Game:

    def __init(self, grid):
        self.__grid = grid
        self.__score = 0
        self.__high_scores = []
        self.__history = []
        self.__state = State.running

    def slide_to(self, direction):
        if direction not in ['left', 'right', 'up', 'down']:
            return
        points_gained = {'left': self.__grid.slide_left,
                         'right': self.__grid.slide_right,
                         'up': self.__grid.slide_up,
                         'down': self.__grid.slide_down
                         }.get(direction)()
        self.__score += points_gained

    def get_value_at(self, position):
        return self.__grid[position]

    @property
    def score(self):
        return self.__score
