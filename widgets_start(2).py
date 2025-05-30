from tkinter import *
from datetime import date
root = Tk()
root.title("Getting Started with Widgets")
root.geometry('824x624')
lbl = Label(text="Hey There!", fg="white", bg="dodgerblue", height=2, width=300)
lbl.pack(pady=(10,5))
name_lbl = Label(text="Enter your full name", bg="#3895D3")
name_lbl.pack(pady=(5,9))
name_entry = Entry()
name_entry.pack(pady=(8,10))
age_lbl = Label(text="Enter your age", bg="#3895D3")
age_lbl.pack(pady=(5,9))
age_entry = Entry()
age_entry.pack(pady=(8,10))
def display():
    name = name_entry.get().strip()
    text_box.delete("1.0", END)
    if not name:
        text_box.insert(END, "Please enter your name!\n")
        return
    greet = f"Assalamu Alaikum {name}!\n"
    message = "Welcome to the Application!\nToday's date is: "
    today = date.today()
    age_reply = ""
    age = int(age_entry.get())
    if age < 18:
        age_reply = "You are only ", age , " years old. You are too little to be eligible for voting!\n"
    elif age >= 18:
        age_reply = "You are ", age , " years old. You are eligible for voting!\n"
    elif not age_entry.get():
        age_reply = "Please enter your age!\n"   
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, str(today))
    text_box.insert(END, age_reply)
text_box = Text(height=4)
text_box.pack(pady=(5,10))
btn = Button(text="Begin", command=display, height=4, bg="#1261AB", fg="white")
btn.pack(pady=(5,20))
root.mainloop()