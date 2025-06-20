from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
root = Tk()
root.title("Denomiation Calculator")
root.configure(bg="dodgerblue")
root.geometry("624x424")
upload = Image.open("Mathematics Arslan Khan.JPG")
upload = upload.resize((288, 288))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg="dodgerblue")
label.place(x=188, y=24)
label1 = Label(root, text="Hey User! Welcome to Denomination Calculator Application.", bg="dodgerblue", font=("Times New Roman", 20, "bold"))
label1.place(relx=0.5, y=360, anchor=CENTER)
def msg():
    MsgBox = messagebox.askyesno("Denomination Calculator", "Do you want to calculate the denomination count?")
    if MsgBox == True:
        topwin()
button1 = Button(root, text="Let's get started!", command=msg, bg="forestgreen", fg="white", font=("Times New Roman", 8, "bold"))
button1.place(x=264, y=360)
def topwin():
    top = Toplevel()
    top.title("Denomination Calculator")
    top.configure(bg="black", fg="white")
    top.geometry("624x424+50+50")
    label = Label(top, text="Enter total amount", bg="black", fg="white", font=("Times New Roman", 8, "bold"))
    entry = Entry(top, font=("Times New Roman", 8, "bold"), bg="white", fg="black")
    lbl = Label(top, text="Here are the number of notes for each denomination", bg="black", fg="white", font=("Times New Roman", 8, "bold"))
    l1 = Label(top, text="1000", bg="black", fg="white", font=("Times New Roman", 8, "bold"))
    l1 = Label(top, text="824", bg="black", fg="orange", font=("Times New Roman", 8, "bold"))
    l1 = Label(top, text="624", bg="black", fg="forestgreen", font=("Times New Roman", 8, "bold"))
    t1 = Entry(top, font=("Times New Roman", 8, "bold"), bg="white", fg="black")
    t2 = Entry(top, font=("Times New Roman", 8, "bold"), bg="white", fg="black")
    t3 = Entry(top, font=("Times New Roman", 8, "bold"), bg="white", fg="black")
    def calculator():
        try:
            amount = int(entry.get())
            if amount < 0:
                raise ValueError("Amount cannot be negative")
            notes_2000 = amount // 2000
            amount %= 2000
            notes_500 = amount // 500
            amount %= 500
            notes_100 = amount // 100
            amount %= 100
            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)
            t1.insert(0, str(notes_2000))
            t2.insert(0, str(notes_500))
            t3.insert(0, str(notes_100))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")
    btn = Button(top, text="Calculate", command=calculator, bg="orange", fg="white", font=("Times New Roman", 15, "bold"))
    btn.place(x=264, y=360)
    
root.mainloop()