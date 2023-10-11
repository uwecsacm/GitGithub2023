import tkinter as tk

from tkinter import messagebox

def click(event):
    if object_id is not None:
        coord = can.coords(object_id)
        width = coord[2] - coord[0]
        height = coord[3] - coord[1]

        can.coords(object_id, event.x, event.y, event.x+width, event.y+height)

def delete():
    msg = messagebox.askyesnocancel('Info', 'Delete canvas ?')
    if msg == True:
        can.delete(tk.ALL)

def create_rectangle():
    global object_id

    object_id = can.create_polygon(10, 10, 70, 70, fill='black', outline='red', width=3)

def create_circle():
    global object_id
    
    object_id = can.create_oval(175, 100, 100, 175, fill='orange', outline='orange', width = 120);

def create_line():
    global object_id

    object_id = can.create_line(200, 200, 100, 100, fill='blue', width=5)

# --- main ---

object_id = None

window = tk.Tk()
window.title('Get Github objets')
window.resizable(width=True, height=True)
window.geometry('400x200+100+50')
window.configure(bg='light green')

can = tk.Canvas(window, bg='white', height=500, width=500)
can.pack(side=tk.RIGHT)
can.bind("<Button-1>", click)

btn_line = tk.Button(window, text='Line', width=30, command=create_line)
btn_line.pack()

btn_rectangle = tk.Button(window, text='Rectangle', width=30, command=create_rectangle)
btn_rectangle.pack()

btn_circle = tk.Button(window, text='Circle', width=30, command=create_circle)
btn_circle.pack()

btn_delete = tk.Button(window, text='Delete', width=30, command=delete)
btn_delete.pack()

window.mainloop()
