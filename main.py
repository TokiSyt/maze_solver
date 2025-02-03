from graphics import *
from cell import Cell

def main():
    win = Window(800, 600)
    cell_instance1 = Cell(win)
    cell_instance1.has_right_wall = False
    cell_instance1.draw(50, 100, 50, 100)

    cell_instance2 = Cell(win)
    cell_instance2.has_left_wall = False
    cell_instance2.has_bottom_wall = False
    cell_instance2.draw(100, 150, 50, 100)

    cell_instance1.draw_move(cell_instance2)

    cell_instance3 = Cell(win)
    cell_instance3.has_top_wall = False
    cell_instance3.has_right_wall = False
    cell_instance3.draw(100, 150, 100, 150)

    cell_instance2.draw_move(cell_instance3)

    cell_instance4 = Cell(win)
    cell_instance4.has_left_wall = False
    cell_instance4.draw(150, 200, 100, 150)

    cell_instance3.draw_move(cell_instance4, True)

    win.wait_for_close()

main()