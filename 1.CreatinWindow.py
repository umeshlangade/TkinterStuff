from tkinter import *
from tkinter import ttk

root = Tk()
root.resizable(False, False)


def proc_tkinterButton():
    print("You clicked on Tkinter Button..!!")


def proc_ttkButton():
    print("You Clicked on Ttk Button..!!")


button1 = Button(root, text="1.Click me", command=proc_tkinterButton)
button2 = ttk.Button(root, text="2.Click me", command=proc_ttkButton)
button1.pack(pady=30)
button2.pack()

root.geometry("150x200")
root.mainloop()
