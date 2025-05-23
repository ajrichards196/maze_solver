from window import Window, Point, Line
from cell import Cell

x1 = 80
x2 = 160
y1 = 80
y2 = 160
lines = [    
    #left wall
    {"point_a": [x1, y1], "point_b": [x1, y2], "colour": "blue"},
    #right wall
    {"point_a": [x2, y1], "point_b": [x2, y2], "colour": "red"},
    #top wall
    {"point_a": [x1, y1], "point_b": [x2, y1], "colour": "green"},
    #bottom wall
    {"point_a": [x1, y2], "point_b": [x2, y2], "colour": "black"},
]

def main():
    win = Window(800,600)
    # for line in lines:
    #     point_a = Point(line["point_a"][0], line["point_a"][1])
    #     point_b = Point(line["point_b"][0], line["point_b"][1])
    #     line_to_draw = Line(point_a=point_a, point_b=point_b)
    #     win.draw_line(line=line_to_draw, fill_colour=line["colour"])

    cell_a = Cell(win)
    cell_a.draw(80,160, 80, 160)
    cell_b = Cell(win)
    cell_b.draw(160, 240, 160, 240)
    cell_c = Cell(win)
    cell_c.draw(240,320, 80, 160)
    cell_a.draw_move(to_cell=cell_b)
    cell_b.draw_move(cell_c)
    win.wait_for_close()

if __name__ == "__main__":
    main()