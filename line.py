from point import Point
from tkinter import Tk, BOTH, Canvas

class Line:
    def __init__(self, start, end):
        self.__start, self.__end = start, end

    def draw(self, canvas:Canvas, fill_color):
        canvas.create_line(
            self.__start.x, self.__start.y, self.__end.x, self.__end.y, fill=fill_color, width=2
        )