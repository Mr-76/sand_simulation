import tkinter as tk

# Create a Tkinter window
window = tk.Tk()
window.title("Square")

# Create a Canvas widget
canvas = tk.Canvas(window, width=400, height=400, bg="white")
canvas.pack()

# Define the coordinates of the square
x1 = 50
y1 = 50
x2 = 250
y2 = 250

# Draw a square on the canvas
square = canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="red")

# Start the Tkinter event loop
window.mainloop()
