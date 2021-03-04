from tkinter import *
from tkinter import messagebox

root = Tk()
e = Entry(root, width=50)
e.insert(0, "Tkinter")
e.grid(row=1, column=1)

def screen():
    messagebox.showinfo("Information", "Please close this")

btn1 = Button(root, text="Click me", command=screen).grid(row=0, column=1)

root.mainloop()

