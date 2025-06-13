from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Virus Detected...")
root.geometry("224x224")
def msg():
    messagebox.showwarning("Alert", "Stop! Virus Detected!")
button = Button(root, text="Scan for Virus", command=msg, bg="black", fg="forestgreen")
button.place(x=48, y=88)
root.mainloop()