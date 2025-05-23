from window import Window, Point, Line

class Cell:
    def __init__(self, window:Window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window

    def draw(self, x1, x2, y1, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        if self.has_left_wall:
            point_a = Point(self.__x1, self.__y1)
            point_b = Point(self.__x1, self.__y2)
            line = Line(point_a=point_a, point_b=point_b)
            self.__win.draw_line(line=line, fill_colour="black")

        if self.has_right_wall:
            point_a = Point(self.__x2, self.__y1)
            point_b = Point(self.__x2, self.__y2)
            line = Line(point_a=point_a, point_b=point_b)
            self.__win.draw_line(line=line, fill_colour="black")

        if self.has_top_wall:
            point_a = Point(self.__x1, self.__y1)
            point_b = Point(self.__x2, self.__y1)
            line = Line(point_a=point_a, point_b=point_b)
            self.__win.draw_line(line=line, fill_colour="black")

        if self.has_bottom_wall:
            point_a = Point(self.__x1, self.__y2)
            point_b = Point(self.__x2, self.__y2)
            line = Line(point_a=point_a, point_b=point_b)
            self.__win.draw_line(line=line, fill_colour="black")

    def draw_move(self, to_cell:"Cell", undo=False):
        if undo:
            colour = "gray"
        else:
            colour = "red"
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
        print(centre_start.x, centre_start.y, centre_end.x, centre_end.y)