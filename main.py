from graphics import Window
from maze import Maze
import sys

def main():
    num_rows = 18
    num_cols = 24
    margin = 50
    screen_x = 1000
    screen_y = 750
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows

    sys.setrecursionlimit(10000)
    win = Window(screen_x, screen_y)
    
    # This function will create a new maze and solve it
    def create_and_solve_maze():
        # Clear the canvas first if this is a reset
        win._Window__canvas.delete("all")
        
        maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
        print("maze created")
        is_solvable = maze.solve()
        if not is_solvable:
            print("maze can not be solved!")
        else:
            print("maze solved!")
            print("Press spacebar to generate a new maze")
    
    # Create the first maze
    create_and_solve_maze()
    
    # Bind the spacebar to reset
    def reset_maze(event):
        print("Resetting maze...")
        create_and_solve_maze()
    
    win.bind_key("<space>", reset_maze)
    
    # Wait for window close
    win.wait_for_close()

main()