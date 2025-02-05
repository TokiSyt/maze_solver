from graphics import *
from maze import Maze
import sys

def main():
    num_rows = 10
    num_cols = 10
    margin = 50
    screen_x = 1920
    screen_y = 1080
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows

    sys.setrecursionlimit(10000)
    win = Window(screen_x, screen_y)
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, 10)
    print("Maze created!")
    is_solvable = maze.solve()
    if not is_solvable:
        print("Maze cannot be solved!")
    else:
        print("Maze solved!")
    win.wait_for_close()
main()