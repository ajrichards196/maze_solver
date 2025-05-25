from window import Window, Point, Line
from cell import Cell
from maze import Maze

def main():
    win = Window(800,600)
    maze = Maze(30,30,10,10,30,30,win)
    maze.solve()
    win.wait_for_close()

if __name__ == "__main__":
    main()