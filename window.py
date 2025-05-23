from tkinter import Tk, BOTH, Canvas

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point_a: Point, point_b: Point):
        self.point_a = point_a
        self.point_b = point_b

    def draw(self, canvas:Canvas, fill_colour:str):
        x1 = self.point_a.x
        y1 = self.point_a.y
        x2 = self.point_b.x
        y2 = self.point_b.y
        canvas.create_line(x1, y1, x2, y2, fill=fill_colour, width=2)

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title = 'title'
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(self.__root, width=width, height=height)
        self.canvas.pack()
        self.winrun = False

    def redraw(self):
        self.__root.update()
        self.__root.update_idletasks()

    def wait_for_close(self):
        self.winrun = True
        while self.winrun:
            self.redraw()

    def close(self):
        self.winrun = False

    def draw_line(self, line: Line, fill_colour):
        line.draw(canvas=self.canvas, fill_colour=fill_colour)





        


    
