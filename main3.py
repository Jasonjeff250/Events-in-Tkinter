from tkinter import *
window = Tk()
window.title("Event Handler")
window.geometry("100x100")

#Event Handler for key press
def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)

#Bind key press event to handle_keypress()
window.bind("<Key>", handle_keypress)

#Event handler for button click
def handle_click(event):
    print("\nThe button was clicked!")

button = Button(text="Click me!")
button.pack()

button.bind("<Button-1>",handle_click)

window.mainloop()