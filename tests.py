import unittest
from grid import Grid
from chart import Chart
from game import Game, State
from exceptions import *
from copy import deepcopy


class GridTests(unittest.TestCase):

    def setUp(self):
        self.sample_grids_before_slide = [[[2, 2, 2, 2],
                                           [0, 2, 4, 0],
                                           [4, 0, 2, 2],
                                           [4, 2, 0, 4]],

                                          [[4, 0, 2, 4],
                                           [0, 0, 0, 0],
                                           [4, 2, 2, 2],
                                           [4, 0, 0, 2]],

                                          [[2, 0, 0, 2],
                                           [0, 2, 4, 4],
                                           [4, 2, 0, 2],
                                           [4, 8, 2, 4]]]
        self.height = 4
        self.width = 4
        self.test_grid = Grid(self.width, self.height)
        self.total_cells = self.width * self.height

    def test_slide_left(self):
        sample_grids_after_slide = [[[4, 4, 0, 0],
                                     [2, 4, 0, 0],
                                     [4, 4, 0, 0],
                                     [4, 2, 4, 0]],

                                    [[4, 2, 4, 0],
                                     [0, 0, 0, 0],
                                     [4, 4, 2, 0],
                                     [4, 2, 0, 0]],

                                    [[4, 0, 0, 0],
                                     [2, 8, 0, 0],
                                     [4, 4, 0, 0],
                                     [4, 8, 2, 4]]]
        for x in range(len(self.sample_grids_before_slide)):
            self.test_grid._Grid__cells = self.sample_grids_before_slide[x]
            self.test_grid.slide_left()
            self.assertEqual(
                self.test_grid._Grid__cells, sample_grids_after_slide[x])

    def test_slide_right(self):
        sample_grids_after_slide = [[[0, 0, 4, 4],
                                     [0, 0, 2, 4],
                                     [0, 0, 4, 4],
                                     [0, 4, 2, 4]],

                                    [[0, 4, 2, 4],
                                     [0, 0, 0, 0],
                                     [0, 4, 2, 4],
                                     [0, 0, 4, 2]],

                                    [[0, 0, 0, 4],
                                     [0, 0, 2, 8],
                                     [0, 0, 4, 4],
                                     [4, 8, 2, 4]]]

        for x in range(len(self.sample_grids_before_slide)):
            self.test_grid._Grid__cells = self.sample_grids_before_slide[x]
            self.test_grid.slide_right()
            self.assertEqual(
                self.test_grid._Grid__cells, sample_grids_after_slide[x])

    def test_slide_up(self):
        sample_grids_after_slide = [[[2, 4, 2, 4],
                                     [8, 2, 4, 4],
                                     [0, 0, 2, 0],
                                     [0, 0, 0, 0]],

                                    [[8, 2, 4, 4],
                                     [4, 0, 0, 4],
                                     [0, 0, 0, 0],
                                     [0, 0, 0, 0]],

                                    [[2, 4, 4, 2],
                                     [8, 8, 2, 4],
                                     [0, 0, 0, 2],
                                     [0, 0, 0, 4]]]

        for x in range(len(self.sample_grids_before_slide)):
            self.test_grid._Grid__cells = self.sample_grids_before_slide[x]
            self.test_grid.slide_up()
            self.assertEqual(
                self.test_grid._Grid__cells, sample_grids_after_slide[x])

    def test_slide_down(self):
        sample_grids_after_slide = [[[0, 0, 0, 0],
                                     [0, 0, 2, 0],
                                     [2, 2, 4, 4],
                                     [8, 4, 2, 4]],

                                    [[0, 0, 0, 0],
                                     [0, 0, 0, 0],
                                     [4, 0, 0, 4],
                                     [8, 2, 4, 4]],

                                    [[0, 0, 0, 2],
                                     [0, 0, 0, 4],
                                     [2, 4, 4, 2],
                                     [8, 8, 2, 4]]]
        for x in range(len(self.sample_grids_before_slide)):
            self.test_grid._Grid__cells = self.sample_grids_before_slide[x]
            self.test_grid.slide_down()
            self.assertEqual(
                self.test_grid._Grid__cells, sample_grids_after_slide[x])

    def test_can_slide_grid(self):
        self.test_grid = Grid(4, 4)
        cant_slide_grid = [[2, 4, 8, 2],
                           [8, 2, 4, 16],
                           [2, 16, 8, 2],
                           [4, 8, 2, 4]]
        can_slide_grid = [[2, 0, 0, 2],
                          [0, 2, 4, 4],
                          [4, 2, 0, 2],
                          [4, 8, 2, 4]]
        self.test_grid._Grid__cells = cant_slide_grid
        self.assertFalse(self.test_grid.can_slide())
        self.test_grid._Grid__cells = can_slide_grid
        self.assertTrue(self.test_grid.can_slide())

    def test_slide_left_points_recieved(self):
        sample_grids_scores = [12, 4, 16]
        for x in range(len(self.sample_grids_before_slide)):
            self.test_grid._Grid__cells = self.sample_grids_before_slide[x]
            self.assertEqual(
                self.test_grid.slide_left()[0], sample_grids_scores[x])

    def test_slide_right_points_recieved(self):
        sample_grids_scores = [12, 4, 16]
        for x in range(len(self.sample_grids_before_slide)):
            self.test_grid._Grid__cells = self.sample_grids_before_slide[x]
            self.assertEqual(
                self.test_grid.slide_right()[0], sample_grids_scores[x])

    def test_slide_up_points_recieved(self):
        sample_grids_scores = [16, 16, 12]
        for x in range(len(self.sample_grids_before_slide)):
            self.test_grid._Grid__cells = self.sample_grids_before_slide[x]
            self.assertEqual(
                self.test_grid.slide_up()[0], sample_grids_scores[x])

    def test_slide_down_points_recieved(self):
        sample_grids_scores = [16, 16, 12]
        for x in range(len(self.sample_grids_before_slide)):
            self.test_grid._Grid__cells = self.sample_grids_before_slide[x]
            self.assertEqual(
                self.test_grid.slide_down()[0], sample_grids_scores[x])

    def test_free_cells_decrease(self):
        for count in range(self.total_cells):
            self.assertEqual(
                len(self.test_grid._Grid__free_cells),
                self.total_cells - count)
            self.test_grid.generate_number()

    def test_generated_number(self):
        flag = False
        self.test_grid.generate_number()
        for x in range(self.height):
            for y in range(self.width):
                if self.test_grid[(x, y)] == 2 or self.test_grid[(x, y)] == 4:
                    flag = True
        self.assertTrue(flag)

    def test_generate_number_on_full_grid(self):
        for count in range(self.total_cells):
            self.test_grid.generate_number()
        self.assertEqual(self.test_grid.generate_number(), None)

    def test_reset(self):
        self.test_grid.reset()
        for x in range(self.height):
            for y in range(self.width):
                self.assertEqual(self.test_grid[(x, y)], 0)

    def test_dimensions(self):
        self.assertEqual(
            self.test_grid.dimensions(), (self.width, self.height))

    def test_win_score_reached_exception(self):
        sample_grid = [[1024, 1024, 2, 2],
                       [1024, 2, 4, 0],
                       [4, 0, 2, 2],
                       [4, 2, 0, 4]]
        self.test_grid._Grid__cells = deepcopy(sample_grid)
        with self.assertRaises(GridWinScoreReachedException):
            self.test_grid.slide_left()
        self.test_grid._Grid__cells = deepcopy(sample_grid)
        with self.assertRaises(GridWinScoreReachedException):
            self.test_grid.slide_right()
        self.test_grid._Grid__cells = deepcopy(sample_grid)
        with self.assertRaises(GridWinScoreReachedException):
            self.test_grid.slide_up()
        self.test_grid._Grid__cells = deepcopy(sample_grid)
        with self.assertRaises(GridWinScoreReachedException):
            self.test_grid.slide_down()


class ChartTests(unittest.TestCase):

    def setUp(self):
        self.test_chart = Chart()

    def test_empty_chart(self):
        for top_player in self.test_chart:
            self.assertEqual(top_player[0], '')
            self.assertEqual(top_player[1], 0)

    def test_chart_add(self):
        self.test_chart.add('User1', 100)
        self.test_chart.add('User2', 200)
        self.test_chart.add('User3', 300)
        self.test_chart.add('User4', 400)
        self.test_chart.add('User5', 500)
        self.test_chart.add('User6', 600)
        self.test_chart.add('User7', 700)
        self.test_chart.add('User8', 800)
        self.test_chart.add('User9', 900)
        self.test_chart.add('User10', 1000)
        self.test_chart.add('User11', 50)
        for index in range(10):
            self.assertEqual(
                self.test_chart.top_players[index][0],
                ('User' + str(10 - index)))
            self.assertEqual(
                self.test_chart.top_players[index][1], (1000 - index * 100))
        for top_player in self.test_chart.top_players:
            self.assertNotEqual(top_player[0], 'User11')

    def test_chart_is_top_score(self):
        self.test_chart.add('User1', 100)
        self.test_chart.add('User2', 200)
        self.test_chart.add('User3', 300)
        self.test_chart.add('User4', 400)
        self.test_chart.add('User5', 500)
        self.test_chart.add('User6', 600)
        self.test_chart.add('User7', 700)
        self.test_chart.add('User8', 800)
        self.test_chart.add('User9', 900)
        self.test_chart.add('User10', 1000)
        self.assertTrue(self.test_chart.is_top_score(1500))
        self.assertTrue(self.test_chart.is_top_score(500))
        self.assertTrue(self.test_chart.is_top_score(100))
        self.assertFalse(self.test_chart.is_top_score(50))

    def test_chart_reset(self):
        self.test_chart.add('User1', 100)
        self.test_chart.add('User2', 200)
        self.test_chart.add('User3', 300)
        self.test_chart.add('User4', 400)
        self.test_chart.add('User5', 500)
        self.test_chart.add('User6', 600)
        self.test_chart.add('User7', 700)
        self.test_chart.add('User8', 800)
        self.test_chart.add('User9', 900)
        self.test_chart.add('User10', 1000)
        self.test_chart.reset()
        for top_player in self.test_chart:
            self.assertEqual(top_player[0], '')
            self.assertEqual(top_player[1], 0)

    def test_chart_save(self):
        self.test_chart.add('User10', 100)
        self.test_chart.add('User9', 200)
        self.test_chart.add('User8', 300)
        self.test_chart.add('User7', 400)
        self.test_chart.add('User6', 500)
        self.test_chart.add('User5', 600)
        self.test_chart.add('User4', 700)
        self.test_chart.add('User3', 800)
        self.test_chart.add('User2', 900)
        self.test_chart.add('User1', 1000)
        self.test_chart.save('save_test.dat')
        import os
        self.assertTrue(os.path.isfile('save_test.dat'))

    def test_chart_load(self):
        self.test_chart.load('save_test.dat')
        for index in range(10):
            self.assertEqual(
                self.test_chart.top_players[index][0],
                ('User' + str(index + 1)))
            self.assertEqual(
                self.test_chart.top_players[index][1], (1000 - index * 100))


class GameTests(unittest.TestCase):

    def setUp(self):
        self.height = 4
        self.width = 4
        grid = Grid(self.width, self.height)
        self.test_game = Game(grid)

    def test_start(self):
        self.test_game.start()
        counter = 0
        for x in range(self.height):
            for y in range(self.width):
                if self.test_game.get_value_at((x, y)) != 0:
                    counter += 1
        self.assertEqual(counter, 2)

    def test_grid_dimensions(self):
        self.assertEqual(
            self.test_game.grid_dimensions(), (self.width, self.height))

    def test_reset(self):
        self.test_game.reset()
        self.assertEqual(self.test_game._Game__history, [])
        self.assertEqual(self.test_game._Game__state, State.running)
        self.assertEqual(self.test_game._Game__score, 0)
        self.assertEqual(self.test_game._Game__undo_counter, 0)

    def test_undo(self):
        self.test_game.start()
        self.test_game.slide_to('left')
        saved_state = deepcopy(self.test_game._Game__grid._Grid__cells)
        self.test_game.slide_to('right')
        self.test_game.slide_to('up')
        self.test_game.slide_to('down')
        self.test_game.undo()
        self.test_game.undo()
        self.test_game.undo()
        self.test_game.undo()
        self.assertEqual(saved_state, self.test_game._Game__grid._Grid__cells)
        self.assertEqual(self.test_game.undos_left(), 0)

    def test_game_won(self):
        self.test_game.start()
        self.test_game.slide_to('invalid')
        self.test_game._Game__grid._Grid__cells = [[1024, 1024, 2, 2],
                                                   [1024, 2, 4, 0],
                                                   [4, 0, 2, 2],
                                                   [4, 2, 0, 4]]
        self.test_game.slide_to('left')
        self.assertEqual(self.test_game.get_state(), State.game_won)

    def test_game_over(self):
        self.test_game._Game__grid._Grid__cells = [[2, 4, 8, 2],
                                                   [8, 2, 4, 16],
                                                   [2, 16, 8, 2],
                                                   [4, 8, 2, 4]]
        self.test_game.slide_to('left')
        self.assertEqual(self.test_game.get_state(), State.game_over)

    def test_change_state(self):
        self.test_game.change_state(State.game_won)
        self.assertEqual(self.test_game.get_state(), State.game_won)

    def test_check_score(self):
        self.test_game.load_top_scores('save_test.dat')
        self.test_game._Game__score = 500
        self.assertTrue(self.test_game.check_score())
        self.assertTrue(self.test_game.score() == 500)


if __name__ == '__main__':
    unittest.main()
