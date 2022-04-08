from tkinter import *
from tkinter import ttk

root = Tk()

def click_me():
    selected_item  = listBox.curselection()
    for item in selected_item:
        print(listBox.get(item))

listBox = Listbox(root, width=40, height=10, selectmode=SINGLE)
# listBox = Listbox(root, width=40, height=10, selectmode=MULTIPLE)
listBox.insert(0, "Python")
listBox.insert(1, "Java")
listBox.insert(2, "Javascript")
listBox.insert(3, "PowerApps")

listBox.pack(pady=20)

btnClick = Button(root,text="Click Me!!", command=click_me).place(x=200, y=200)

root.geometry("300x300+650+200")
root.mainloop()
