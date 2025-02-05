from cell import Cell
import time
import random


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()


    def _create_cells(self):

        for _ in range(self._num_cols):
            row = []
            for _ in range(self._num_rows):
                row.append(Cell(self._win))
            self._cells.append(row)

        for col_coord in range(self._num_cols):
            for row_coord in range(self._num_rows):
                self._draw_cell(col_coord, row_coord)


    def _draw_cell(self, col, row):
           
        if self._win is None:
            return
        
        x1 = self._x1 + col * self._cell_size_x
        y1 = self._y1 + row * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[col][row].draw(x1, x2, y1, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):

        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, col, row):
        self._cells[col][row]._visited = True

        while True:
            to_visit = []

            #neighbors
            if row > 0 and not self._cells[col][row - 1]._visited: #up
                to_visit.append((col, row-1))
            if row < self._num_rows - 1 and not self._cells[col][row + 1]._visited: #down
                to_visit.append((col, row + 1))
            if col  > 0 and not self._cells[col - 1][row]._visited: #left
                to_visit.append((col - 1, row))
            if col < self._num_cols - 1 and not self._cells[col + 1][row]._visited: #right
                to_visit.append((col + 1, row))

            if len(to_visit) == 0:
                self._draw_cell(col, row)
                return
            
            random_index = random.randrange(len(to_visit))
            next_col, next_row = to_visit[random_index]
            
            if next_row < row:
                self._cells[col][row].has_top_wall = False
                self._cells[next_col][next_row].has_bottom_wall = False

            if next_row > row:
                self._cells[col][row].has_bottom_wall = False
                self._cells[next_col][next_row].has_top_wall = False

            if next_col < col:
                self._cells[col][row].has_left_wall = False
                self._cells[next_col][next_row].has_right_wall = False

            if next_col > col:
                self._cells[col][row].has_right_wall = False
                self._cells[next_col][next_row].has_left_wall = False
                
            self._break_walls_r(next_col, next_row)


    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell._visited = False

    
    def solve(self):
        return self._solve_r(0, 0)


    def _solve_r(self, col, row):    
        current = self._cells[col][row]

        self._animate()
        current._visited = True

        if current == self._cells[self._num_cols - 1][self._num_rows - 1]:
            return True

        #up
        if (
        row > 0
        and current.has_top_wall == False
        and not self._cells[col][row - 1]._visited
        ):
            current.draw_move(self._cells[col][row - 1])
            recur = self._solve_r(col, row-1)
            if recur:
                return True
            else:
                next = self._cells[col][row - 1]
                next.draw_move(current, undo=True)

        #down
        if (
        row < self._num_rows - 1 
        and current.has_bottom_wall == False 
        and not self._cells[col][row + 1]._visited
        ):
            current.draw_move(self._cells[col][row + 1])
            recur = self._solve_r(col, row + 1)
            if recur:
                return True
            else:
                next = self._cells[col][row + 1]
                next.draw_move(current, undo=True)

        #left
        if (
        col  > 0 
        and current.has_left_wall == False 
        and not self._cells[col - 1][row]._visited
        ):
            current.draw_move(self._cells[col - 1][row])
            if self._solve_r(col - 1, row):
                return True
            else:
                next = self._cells[col - 1][row]
                next.draw_move(current, undo=True)

        #right
        if (
        col < self._num_cols - 1 
        and current.has_right_wall == False 
        and not self._cells[col + 1][row]._visited
        ):
            current.draw_move(self._cells[col + 1][row])
            recur = self._solve_r(col + 1, row)
            if recur:
                return True
            else:
                next = self._cells[col + 1][row]
                next.draw_move(current, undo=True)

        return False