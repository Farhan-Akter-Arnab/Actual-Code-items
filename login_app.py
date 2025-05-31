from tkinter import *
root = Tk()
root.title('Login App')
root.geometry('424x424')
frame = Frame(master=root, height=224, width=364, bg="black")
lbl1 = Label(frame, text="Full Name", bg="orange", fg="white", width=12)
lbl2 = Label(frame, text="Email ID", bg="orange", fg="white", width=12)
lbl3 = Label(frame, text="Enter Password", bg="orange", fg="white", width=12)
name_entry = Entry(frame)
email_entry = Entry(frame)
pass_entry = Entry(frame, show="π")
def display():
    name = name_entry.get()
    greet = "Hey " + name
    message = "\nCongratulations for your new account!"
    textbox.insert(END, greet)
    textbox.insert(END, message)
textbox = Text(bg="#BEBEBE", fg="black")
btn = Button(text= "Create Account", command=display, bg="forestgreen")
frame.place(x=24, y=0)
lbl1.place(x=24, y=24)
name_entry.place(x=150, y=24)
lbl2.place(x=24, y=88)
email_entry.place(x=150)