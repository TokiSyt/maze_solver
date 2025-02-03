from graphics import Line, Point

class Cell:
    def __init__(self, window_instance=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None 
        self._y1 = None 
        self._x2 = None 
        self._y2 = None 
        self._win = window_instance
        self._visited = False


    def draw(self, x1, x2, y1, y2):
        if self._win is None:
            return
        self._x1 = x1 
        self._y1 = y1 
        self._x2 = x2 
        self._y2 = y2 

        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, "white")

        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, "white")

        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, "white")

        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, "white")


    def draw_move(self, to_cell, undo=False):
        line_color = "red"
        if undo:
            line_color = "gray"

        cell1_x = abs(self._x1 + self._x2) // 2
        cell1_y = abs(self._y1 + self._y2) // 2

        cell2_x = abs(to_cell._x1 + to_cell._x2) // 2
        cell2_y = abs(to_cell._y1 + to_cell._y2) // 2

        line = Line(Point(cell1_x, cell1_y), Point(cell2_x, cell2_y))
        self._win.draw_line(line, line_color)
