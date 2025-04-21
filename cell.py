from point import Point
from tkinter import Tk, BOTH, Canvas

class Cell:
    def __init__(self, x1, x2, y1, y2, has_left_wall=True, has_right_wall=True, has_top_wall=True, has_bottom_wall=True):

        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall

        #swap each supplied coordinate
        self._x1, self._x2 = sorted([x1, x2])
        self._y1, self._y2 = sorted([y1, y2])

        self._win = None

    def set_window(self, win):
        self._win = win

    #draw the cell
    def draw(self, canvas:Canvas, fill_color):
        if self.has_left_wall:
            canvas.create_line(
            self._x1, self._y1, self._x1, self._y2, fill=fill_color, width=2
        )
        if self.has_right_wall:
            canvas.create_line(
            self._x2, self._y1, self._x2, self._y2, fill=fill_color, width=2
        )
        if self.has_top_wall:
            canvas.create_line(
            self._x1, self._y1, self._x2, self._y1, fill=fill_color, width=2
        )
        if self.has_bottom_wall:
            canvas.create_line(
            self._x1, self._y2, self._x2, self._y2, fill=fill_color, width=2
        )

    #draw path between cells     
    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return

        x1 = (self._x1 + self._x2)/2
        y1 = (self._y1 + self._y2)/2
        x2 = (to_cell._x1 + to_cell._x2)/2 
        y2 = (to_cell._y1 + to_cell._y2)/2

        color = "red"
        if undo:
            color = "gray"

        # Create a Line object to use with the Window's draw_line method
        from line import Line
        from point import Point
        point1 = Point(x1, y1)
        point2 = Point(x2, y2)
        line = Line(point1, point2)
        self._win.draw_line(line, color)