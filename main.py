from tkinter import Tk, BOTH, Canvas
from point import Point
from line import Line
from cell import Cell

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.width, self.height = width, height
        self.__root.title("Maze Solver")
        self._canvas = Canvas(self.__root, width=self.width, height=self.height)
        self._canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__root.lift()  # Lift window to the top
        self.__root.attributes('-topmost', True)  # Make it topmost temporarily
        self.__root.after_idle(self.__root.attributes, '-topmost', False)  # Then disable topmost
        self.__root.focus_force()  # Force focus

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        
    def close(self):
        self.__running = False

    def draw_line(self, line:Line, fill_color):
        line.draw(self._canvas, fill_color)

    def draw_cell(self, cell:Cell, fill_color):
        cell.set_window(self)
        cell.draw(self._canvas, fill_color)

def main():
    win = Window(800, 600)

    #test points
    point1 = Point(30, 60)
    point2 = Point(500,300)
    point3 = Point(475, 500)
    point4 = Point(345,340)
    point5 = Point(200, 260)
    point6 = Point(250,320)
    point7 = Point(256, 210)
    point8 = Point(103,360)

    #test lines
    line1 = Line(point1, point2)
    line2 = Line(point3, point4)
    line3 = Line(point5, point6)
    line4 = Line(point7, point8)

    #draw test lines
    win.draw_line(line1, "magenta")
    win.draw_line(line2, "steelblue")
    win.draw_line(line3, "orchid")
    win.draw_line(line4, "tomato")

    #test cells
    cell1 = Cell(20, 40, 40, 60, has_right_wall=False)
    cell2 = Cell(30, 100, 80, 150, has_right_wall=False) #these two are
    cell3 = Cell(100, 170, 80, 150, has_left_wall=False) #ad jacent
    cell4 = Cell(260, 150, 300, 190, has_bottom_wall=False) #testing wrong coordinate order correction
    cell5 = Cell(270, 310, 3430, 380, has_left_wall=False)
    cell6 = Cell(290, 400, 10, 420, has_left_wall=False, has_top_wall=False)

    #draw test cells
    win.draw_cell(cell1, "turquoise")
    win.draw_cell(cell2, "chocolate")
    win.draw_cell(cell3, "limegreen")
    win.draw_cell(cell4, "yellow")
    win.draw_cell(cell5, "cyan")
    win.draw_cell(cell6, "salmon")

    #draw test path
    cell2.draw_move(cell3) 

    win.wait_for_close()

main()
