from window import Window, Point, Line

class Cell:
    def __init__(self, window:Window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = False
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