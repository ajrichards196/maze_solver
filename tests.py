import unittest

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells_1210(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0,0,num_rows, num_cols,10,10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows
        )

    def test_maze_create_cells_2030(self):
        num_cols = 20
        num_rows = 30
        m1 = Maze(0,0,num_rows, num_cols,10,10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows
        )

    def test_maze_create_cells_20003000(self):
        num_cols = 2000
        num_rows = 3000
        m1 = Maze(0,0,num_rows, num_cols,10,10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows
        )

if __name__ == "__main__":
    unittest.main()