from tkinter import *
from tkinter import colorchooser
root=Tk()
root.title("Drawing App")
root.geometry("700x500")
#default settings
current_color="black"
brush_size=3
eraser_on=False
#canvas
canvas=Canvas(root,bg="white")
canvas.pack(fill=BOTH,expand=True)
last_x,last_y=None,None
#function-start draw
def start_draw(event):
    global last_x,last_y
    last_x,last_y=event.x,event.y
#drawing function
def draw(event):
    global last_x,last_y
    color="white" if eraser_on else current_color
    if last_x is not None and last_y is not None:
        canvas.create_line(
            last_x,last_y,event.x,event.y,
            width=brush_size,
            fill=color,
            capstyle=ROUND,
            smooth=True
        )
    last_x,last_y=event.x,event.y
#stop drawing
def stop_draw(event):
    global last_x,last_y
    last_x,last_y=None,None
#tools
def choose_color():
    global current_color,eraser_on
    eraser_on=False
    color=colorchooser.askcolor()[1]
    if color:
        current_color=color
def use_eraser():
    global eraser_on
    eraser_on=True
def change_size(val):
    global brush_size
    brush_size=int(val)
def clear_canvas():
    canvas.delete("all")
#user interface
toolbar=Frame(root)
toolbar.pack()
Button(toolbar,text="Color",command=choose_color,bg='black',fg='white').pack(side=LEFT,padx=5)
Button(toolbar,text="Erase",command=use_eraser,bg='black',fg='white').pack(side=LEFT,padx=5)
Button(toolbar,text="Clear",command=clear_canvas,bg='black',fg='white').pack(side=LEFT,padx=5)
Scale(toolbar,from_=1, to=10,orient=HORIZONTAL,label="Brush Size:",command=change_size).pack(side=LEFT)
#bind the events
canvas.bind("<Button-1>",start_draw)#left click to start drawing
canvas.bind("<B1-Motion>",draw)#Movee the mouse to draw
canvas.bind("<ButtonRelease-1>",stop_draw)#release the mouse to stop
root.mainloop()