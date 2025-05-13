from tkinter import *
import random
import time
import tkinter as tk
win= Tk()
win.geometry("400x400")



class SandCanvas(tk.Canvas):
    """Class to be abble to keep track of the touching 
    of the elements of the canvas
    this is using canvas itself and creating a dict to associate
    the data with the created object, since the shapes created by 
    canvas are not realy objects"""
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.object_data = {}

    def create_rectangle_with_data(self, x1, y1, x2, y2, data=None, **kwargs):
        obj_id = self.create_rectangle(x1, y1, x2, y2, **kwargs)
        self.object_data[obj_id] = data
        return obj_id

    def get_data(self, obj_id):
        return self.object_data.get(obj_id, None)

    def set_data(self, obj_id,value):
        self.object_data[obj_id] = value  


canvas = SandCanvas(win, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)
squares = []  

def click_handler(e):
    """
    This creates a square with size 1 and in a random place.... not tooo far
    """
    size = 1
    random_number = random.randint(1, 5)
    x1 =( e.x - size // 2) + random_number 
    y1 =( e.y - size // 2) + random_number
    x2 =( e.x + size // 2) + random_number
    y2 =( e.y + size // 2) + random_number
    square_id = canvas.create_rectangle_with_data(x1, y1, x2, y2, outline="black", fill="red",data={"Touch":"0"})
    squares.append(square_id)


def is_touch(element1):
    """
    Necessary function to verify if the element that is in collision
    is a element that either touched the bottom or touched a element that
    did that.
    """
    touch = canvas.get_data(element1)
    if touch == "1":
        return True

    else:
        return False


def decay(list_of_squares):
    """
    Function to decay de squares so they go down
    receives a list of the current created squares,also the active ones
    a square keeps falling if and only if it does not mach the maximum
    lower bound, and after collission with another block that block is 
    a block that reached the bottom or a block that touched a block
    that reached the bottom.

    """
    for element in squares:
        coords = canvas.coords(element) #coords of the current element in use
        coll = canvas.find_overlapping(coords[0], coords[1], coords[2], coords[3]+1) #verifiy collision and take ou the element itself from the list
        coll = [item for item in coll if item != element]  # Remove self
        
        if coords[-1] == 400:#if reached bottom 
            canvas.set_data(element,"1")
            squares.remove(element)
        elif (coll and is_touch(coll[0])): #if collided.
            canvas.set_data(element,"1")
            squares.remove(element)
        else:#otherwise go down
            canvas.move(element, 0, 1)
    

    #func to keep the tkinter running
    win.after(10, lambda: decay(list_of_squares))



decay(squares)
win.bind('<Motion>',click_handler)#every move of the mouse in the canvas to spawn the function to create a square....
win.mainloop()
