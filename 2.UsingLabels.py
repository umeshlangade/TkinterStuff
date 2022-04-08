from tkinter import *

root = Tk()
root.resizable(False, False)

label = Label(root,text="HELLO LABELS, WE ARE TESTING JUSTIFY PROPERTIES OF TKINTER",width=35)
#label['text']="Hello Tkinter"
label.config(font="Times 12")
label.config(fg="yellow",bg="black", justify=LEFT)
label.config(wraplength='150')
label.pack(pady=20)

root.geometry("450x400")

root.mainloop()