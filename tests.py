import unittest

from maze import Maze
from window import Window

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

    def test_maze_break_entrance(self):
        num_cols = 3
        num_rows = 3
        #win = Window(800,800)
        m1 = Maze(0,0,num_rows, num_cols,10,10)
  
        self.assertFalse(
            m1._Maze__cells[0][0].has_top_wall
        )

    def test_maze_break_exit(self):
        num_cols = 3
        num_rows = 3
        #win = Window(800,800)
        m1 = Maze(0,0,num_rows, num_cols,10,10)

        self.assertFalse(
            m1._Maze__cells[-1][-1].has_bottom_wall
        )

    def test_reset_visited_status(self):
        num_cols = 3
        num_rows = 3
        m1 = Maze(0,0,num_rows, num_cols,10,10)
        for cells in m1._Maze__cells:
            for cell in cells:
                cell.visited = True
        m1._Maze__reset_cells_visited()
        for cells in m1._Maze__cells:
            for cell in cells:
                self.assertFalse(
                    cell.visited
                )



if __name__ == "__main__":
    unittest.main()