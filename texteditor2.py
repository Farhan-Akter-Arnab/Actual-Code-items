from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
window = Tk()
window.title("Mathematics Text Editor")
window.geometry("624x524")
window.rowconfigure(0, minsize=824, weight=1)
window.columnconfigure(1, minsize=824, weight=1)
def open_file():
    filepath = askopenfilename(
        filetypes=[("Text files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(END, text)
    window.title(f"Mathematics Text Editor - {filepath}")
def save_file():
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, END)
        output_file.write(text)
    window.title(f"Mathematics Text Editor - {filepath}")
def clear_text():
    response = messagebox.askyesno(
        "Clear Text",
        "Are you sure you want to clear the text? This action is irreversible.",
        icon="warning",
    )
    if response:
        txt_edit.delete(1.0, END)
        messagebox.showinfo("Clear Text", "Text is successfully cleared!")
    else:
        return
txt_edit = Text(window, bg="black", fg="white")
fr_buttons = Frame(window, relief=RAISED, bd=2)
btn_open = Button(fr_buttons, text="Open", command=open_file)
btn_save = Button(fr_buttons, text="Save As...", command=save_file)
btn_clear = Button(fr_buttons, text="Clear Text", command=clear_text, bg="red", fg="white")
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
btn_clear.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")
window.mainloop()