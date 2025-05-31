from tkinter import *
# Create window
root = Tk()
root.title('Number pad')
root.geometry('272x324')
# Create the number grid
nums = [[7,8,9],[4,5,6],[1,2,3],['#',0,'*']]
# Configure rows and columns to resize window
for i in range(4):
    root.columnconfigure(i, weight=1, minsize=75)
    root.rowconfigure(i, weight=1, minsize=50)
# Create and place labels in the grid
for i in range(4):
    for j in range(3):
        frame = Frame(
            master = root,
            relief = SUNKEN,
            borderwidth = 1,
            bg = "black"
        )
        frame.grid(row=i, column=j, sticky='nsew')
        label = Label(master = frame, text = nums[i][j], bg="black", font = ('Arial, 24'), fg="orange")
        label.pack(expand = True, fill = 'both', padx=5, pady=5)
root.mainloop()