from window import Window, Point, Line
from cell import Cell
from maze import Maze

def main():
    win = Window(800,600)
    maze = Maze(0,0,20,30,30,15,win)
    win.wait_for_close()

if __name__ == "__main__":
    main()