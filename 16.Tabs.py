from tkinter import *
from tkinter import ttk

root = Tk()
icon = PhotoImage(file="icons/in-love.png", width=100, height=100)
tabs = ttk.Notebook(root)
tabs.pack(fill=BOTH, expand=True, anchor=NW)
tab1 = ttk.Frame(tabs)
tab2 = ttk.Frame(tabs)

tabs.add(tab1,text="FIRST", image=icon, compound=LEFT)
tabs.add(tab2,text="SECOND")

root.geometry("650x550+650+200")
root.mainloop()