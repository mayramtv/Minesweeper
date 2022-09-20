from tkinter import Button

class Cell:
    # constructor
    def __init__(self, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None

    # create the button object
    def create_btn_object(self, location):
        btn = Button(
            location,
            text="Text"
        )
        #passes a refernce to a function on a click event (left click)
        btn.bind("<Button-1>", self.left_clicked_actions)
         #passes a refernce to a function on a click event (right click)
        btn.bind("<Button-3>", self.right_clicked_actions)
        self.cell_btn_object = btn

    def left_clicked_actions(self, event):
        print(event)
        print("I am left clicked")

    def right_clicked_actions(self, event):
        print(event)
        print("I am right clicked")