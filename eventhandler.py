from tkinter import *

window = Tk()
window.title("Event Handler")
window.geometry("124x124")

# Event Handler for Keypress
def handle_keypress(event):
    """Print the character associated with the key pressed."""
    print(event.char)

# Bind keypress event to handle_keypress()
window.bind("<Key>", handle_keypress)

# Event handler for button click
def handle_click(event):
    print("\nThe button was clicked!")

button = Button(text="Click Me!")
button.pack()

# Bind click event to handle_click()
button.bind("<Button-1>", handle_click)
window.mainloop()