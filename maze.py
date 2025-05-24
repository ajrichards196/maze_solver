from window import Window, Line, Point
from cell import Cell
import time

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win:Window=None
            ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.__cells = []
        self.__create_cells()

    def __create_cells(self):
        for i in range(0, self.num_cols):
            row = []
            for j in range(0, self.num_rows):
                row.append(Cell(self.win))
            self.__cells.append(row)
        for i in range(0, self.num_cols):
            for j in range(0, self.num_rows):
                if self.win:
                    self.__draw_cell(i,j)       


    def __draw_cell(self, i, j):
        x = self.cell_size_x * i
        y = self.cell_size_y * j
        cell = self.__cells[i][j]
        cell.draw(x1 = x, x2 = x + self.cell_size_x, y1 = y, y2 = y + self.cell_size_y)
        self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)
        