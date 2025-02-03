from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, 
                 width, 
                 height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__w_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__w_running = True
        while self.__w_running:
            self.redraw()
        print("Window closed...")
    
    def close(self):
        self.__w_running = False

    def draw_line(self, line_instance, fill_color="black"):
        line_instance.draw(self.__canvas, fill_color)


class Point():
    def __init__(self, horizontal_coord, vertical_coord):
        self.horizontal_coord = horizontal_coord
        self.vertical_coord = vertical_coord


class Line():
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2 

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.point1.horizontal_coord, 
            self.point1.vertical_coord, 
            self.point2.horizontal_coord, 
            self.point2.vertical_coord, 
            fill=fill_color, width=2)