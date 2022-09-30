from tkinter import Button, Label 
import random
import settings 
import ctypes
import sys

class Cell:
    all = []
    cell_count = settings.CELL_COUNT
    cell_count_label_object = None

    # constructor
    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_opened = False
        self.is_mine_candidate = False
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

    @staticmethod
    def crete_cell_count_label(location):
        lbl = Label(
            location,
            bg="black",
            fg="white",
            text=f"Cells Left:{Cell.cell_count}",
            font=("", 30)
        )
        Cell.cell_count_label_object = lbl

    def left_clicked_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surronded_cells_mines_length == 0:
                for cell_obj in self.surronded_cell:
                    cell_obj.show_cell()
            self.show_cell()
            # If mines count is equal to the cells left count, player won
            if Cell.cell_count == settings.MINES_COUNT:
                ctypes.windll.user32.MessageBoxW(0, "Congratulations! You won the game!", 'Game Over', 0)
        # Cancel Left and Right click eventsif cell is already opened
        self.cell_btn_object.unbind("<Button-1>")
        self.cell_btn_object.unbind("<Button-3>")

    def get_cell_by_axis(self, x, y):
        # Return a cell object based on the value of x, y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell
    @property
    def surronded_cell(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x , self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1),
        ]
        # rewrites the array, but ignores the "none" values using a one line for loop
        cells = [cell for cell in cells if cell is not None]
        return cells
    
    @property
    def surronded_cells_mines_length(self):
        #count the cells around the cell when clicked
        counter = 0
        for cell in self.surronded_cell:
            if cell.is_mine:
                counter += 1
        return counter

    def show_cell(self):
        # this function update information if the clicked cell is not a mine
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_btn_object.configure(text=self.surronded_cells_mines_length)

            # Update the text of the cell count
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text=f"Cell left: {Cell.cell_count}"
            )
            # If this mine was a candidate, then for safty, we should configurate
            # the background color to SystemButtonFace
            self.cell_btn_object.configure(
                bg='SystemButtonFace'
            ) 
        # Marks the cell as open
        self.is_opened = True

    def show_mine(self):
        # A logic to interrupt the game with a loosing message
        self.cell_btn_object.configure(bg='red')
        ctypes.windll.user32.MessageBoxW(0, "You clicked on a mine", 'Game Over', 0) 
        sys.exit()  

    def right_clicked_actions(self, event):
        if not self.is_mine_candidate:
            self.cell_btn_object.configure(
                bg="orange"
            )
            self.is_mine_candidate = True
        else:
            self.cell_btn_object.configure(
                bg='SystemButtonFace'
            )
            self.is_mine_candidate = False

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