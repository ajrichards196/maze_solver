from window import Window, Line, Point
from cell import Cell
import time, random

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win:Window=None,
            seed=None
            ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        if seed:
            self.seed = random.seed(seed)
        self.__cells = []
        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0,0)

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
        x = self.x1 + (self.cell_size_x * i)
        y = self.y1 + (self.cell_size_y * j)
        cell = self.__cells[i][j]
        cell.draw(x1 = x, x2 = x + self.cell_size_x, y1 = y, y2 = y + self.cell_size_y)
        self._animate()

    def _animate(self):
        if self.win:
            self.win.redraw()
            time.sleep(0.15)

    def __break_entrance_and_exit(self):
        entrance = self.__cells[0][0]
        entrance.has_top_wall = False
        self.__draw_cell(0,0)
        exit = self.__cells[-1][-1]
        exit.has_bottom_wall = False
        self.__draw_cell(self.num_cols-1, self.num_rows-1)

    def __break_walls_r(self, i, j):
        current_cell = self.__cells[i][j]
        current_cell.visited = True
        while True:
            visit = []
            if j > 0 and j <= self.num_rows -1:
                cell_above = self.__cells[i][j-1]
                if not cell_above.visited:
                    visit.append([i, j-1, 'top'])
            if j >= 0 and j < self.num_rows -1:
                cell_below = self.__cells[i][j+1]
                if not cell_below.visited:
                    visit.append([i, j+1, 'bottom'])
            if i > 0 and i <= self.num_cols -1:
                cell_left = self.__cells[i-1][j]
                if not cell_left.visited:
                    visit.append([i-1, j, 'left'])
            if i >= 0 and i < self.num_cols-1:
                cell_right = self.__cells[i+1][j]
                if not cell_right.visited:
                    visit.append([i+1, j, 'right'])
            print(i,j, visit)
            if not visit:
                self.__draw_cell(i,j)
                return
            pick_random = random.randint(0, len(visit)-1)
            next_cell = visit[pick_random]
            direction = next_cell[2]
            if direction == 'top':
                current_cell.has_top_wall = False
            if direction == 'bottom':
                current_cell.has_bottom_wall = False
            if direction == 'left':
                current_cell.has_left_wall = False
            if direction == 'right':
                current_cell.has_right_wall = False
            self.__draw_cell(i,j)
            self.__break_walls_r(next_cell[0], next_cell[1])
                

