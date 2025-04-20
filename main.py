from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.width = width
        self.height = height
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, width=self.width, height=self.height)
        self.__canvas.pack(fill=BOTH, expand=1)
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

def main():
    win = Window(800, 600)
    win.wait_for_close()

main()
