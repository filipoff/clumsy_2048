import unittest
from grid import *


class GridSlideTest(unittest.TestCase):

    def setUp(self):
        self.test_grid = Grid(4, 4)
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
            self.test_grid.cells = self.sample_grids_before_slide[x]
            self.test_grid.slide_left()
            self.assertEqual(self.test_grid.cells, sample_grids_after_slide[x])

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
            self.test_grid.cells = self.sample_grids_before_slide[x]
            self.test_grid.slide_right()
            self.assertEqual(self.test_grid.cells, sample_grids_after_slide[x])

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
            self.test_grid.cells = self.sample_grids_before_slide[x]
            self.test_grid.slide_up()
            self.assertEqual(self.test_grid.cells, sample_grids_after_slide[x])

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
            self.test_grid.cells = self.sample_grids_before_slide[x]
            self.test_grid.slide_down()
            self.assertEqual(self.test_grid.cells, sample_grids_after_slide[x])

if __name__ == '__main__':
    unittest.main()
