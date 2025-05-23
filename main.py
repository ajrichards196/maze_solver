from window import Window, Point, Line

lines = [
    {"point_a": [80, 60], "point_b": [180, 160], "colour": "blue"},
    {"point_a": [800, 600], "point_b": [0, 0], "colour": "red"},
    {"point_a": [400, 300], "point_b": [800, 0], "colour": "green"},
]

def main():
    win = Window(800,600)
    for line in lines:
        point_a = Point(line["point_a"][0], line["point_a"][1])
        point_b = Point(line["point_b"][0], line["point_b"][1])
        line_to_draw = Line(point_a=point_a, point_b=point_b)
        win.draw_line(line=line_to_draw, fill_colour=line["colour"])


    win.wait_for_close()

if __name__ == "__main__":
    main()