from tkinter import *
import time
import tkinter as tk
win= Tk()
win.geometry("750x250")
def callback(e):
   x= e.x
   y= e.y
   print("Pointer is currently at %d, %d" %(x,y))


canvas = tk.Canvas(win, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)
squares = []  

def click_handler(e):
    """
    A todo click cria um quadrado de tamanho 1
    as cordenas sao os pontos de um quadrado....
    """
    size = 1
    x1 = e.x - size // 2
    y1 = e.y - size // 2
    x2 = e.x + size // 2
    y2 = e.y + size // 2
    square_id = canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="red")
    squares.append(square_id)

def decay(list_of_squares):
    """
    Funcao de decair o bloco de areia apos 20 ms cai bloco de areia que foi colocado
    recebe uma lista dos graos ja criados, e apos isso decrementa 1 pixel da sua 
    posicao, deve tratar casos de nao passar da tela e ficar no topo de outros graos

    """
    for element in squares:
        coords = canvas.coords(element)
        print("Square coords:", coords)
        if coords[-1] < 240:
            canvas.move(element, 0, 1)
    

    win.after(20, lambda: decay(list_of_squares))


decay(squares)

win.bind("<Button-1>", click_handler)
win.bind('<Motion>',click_handler)
win.mainloop()

#win.bind("<Button-1>", lambda x: click_handler(e))
