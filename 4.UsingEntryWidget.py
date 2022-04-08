from tkinter import *
from tkinter import ttk

root = Tk()

def callback():
    val1 = entry1.get()
    val2 = entry2.get()
    print("ID: " + val1)
    print("Pass: " + val2)

entry1 = ttk.Entry(root,width=30)
entry2 = ttk.Entry(root,width=30)

#entry1.insert(0,"kindly enter the first name")
#entry1.state(['disabled'])
#entry1.state(['readonly'])
#entry1.state(['!disabled'])
entry2.config(show="*")

entry1.pack()
entry2.pack()

button = Button(root,text="ENTER",command=callback)
button.pack()

root.geometry("300x250")
root.mainloop()