from tkinter import Button
import random
import settings 

class Cell:
    all = []
    # constructor
    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x = x
        self.y = y

        # Append the object to the Cell.all list
        Cell.all.append(self)

    # create the button object with the set parameters
    def create_btn_object(self, location):
        btn = Button(
            location,
            width=12,
            height=4,
        )
        #passes a refernce to a function on a click event (left click)
        btn.bind("<Button-1>", self.left_clicked_actions)
         #passes a refernce to a function on a click event (right click)
        btn.bind("<Button-3>", self.right_clicked_actions)
        self.cell_btn_object = btn

    def left_clicked_actions(self, event):
        if self.is_mine:
            self.show_mine()

    def show_mine(self):
        # A logic to interrupt the game with a loosing message
        self.cell_btn_object.configure(bg='red')

    def right_clicked_actions(self, event):
        print(event)
        print("I am right clicked")

    @staticmethod
    def randomize_mines():
        my_list = Cell.all
        # this method picks randomly 2 items fom the array
        picked_cells = random.sample(
            my_list, settings.MINES_COUNT
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True
        
    # changes how an object is represented fro a more understable object
    def __repr__(self):
        return f"Cell({self.x}, {self.y})"