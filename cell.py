from window import Window, Point, Line

class Cell:
    def __init__(self, window:Window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window
        self.visited = False

    def draw(self, x1, x2, y1, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        #left wall
        point_a = Point(self.__x1, self.__y1)
        point_b = Point(self.__x1, self.__y2)
        line = Line(point_a=point_a, point_b=point_b)
        if self.has_left_wall and self.__win:
            self.__win.draw_line(line=line, fill_colour="black")
        if not self.has_left_wall and self.__win:
            self.__win.draw_line(line=line, fill_colour="white")

        #right wall
        point_a = Point(self.__x2, self.__y1)
        point_b = Point(self.__x2, self.__y2)
        line = Line(point_a=point_a, point_b=point_b)
        if self.has_right_wall and self.__win:
            self.__win.draw_line(line=line, fill_colour="black")
        if not self.has_right_wall and self.__win:
            self.__win.draw_line(line=line, fill_colour="white")

        #top wall
        point_a = Point(self.__x1, self.__y1)
        point_b = Point(self.__x2, self.__y1)
        line = Line(point_a=point_a, point_b=point_b)
        if self.has_top_wall and self.__win:
            self.__win.draw_line(line=line, fill_colour="black")
        if not self.has_top_wall and self.__win:
            self.__win.draw_line(line=line, fill_colour="white")

        #bottom wall
        point_a = Point(self.__x1, self.__y2)
        point_b = Point(self.__x2, self.__y2)
        line = Line(point_a=point_a, point_b=point_b)
        if self.has_bottom_wall and self.__win:
            self.__win.draw_line(line=line, fill_colour="black")
        if not self.has_bottom_wall and self.__win:
            self.__win.draw_line(line=line, fill_colour="white")

    def draw_move(self, to_cell:"Cell", undo=False):
        if undo:
            colour = "gray"
        else:
            colour = "red"
        if self.__win:
            centre_start = Point(
                self.__x2 - ((self.__x2 - self.__x1) / 2),
                self.__y2 - ((self.__y2 - self.__y1) / 2)
            )
            centre_end = Point(
                to_cell.__x2 - ((to_cell.__x2 - to_cell.__x1) / 2),
                to_cell.__y2 - ((to_cell.__y2 - to_cell.__y1) / 2)
            )
            line = Line(point_a=centre_start, point_b=centre_end)
            self.__win.draw_line(line=line, fill_colour=colour)


