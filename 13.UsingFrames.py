from tkinter import *

root = Tk()

root.title("Using Frames")

frmHome = Frame(root,height=200, width=200, bg='grey')
frmHome.pack(pady=40, fill=X)

btnSubmit = Button(frmHome,text="SUBMIT", width=8)
btnCancel = Button(frmHome,text="CANCEL", width=8)
btnSubmit.pack(pady=5)
btnCancel.pack(pady=5)

searchBar = LabelFrame(root, text="SearchBox", padx=20, pady=20)
lblSearch=Label(searchBar, text="search")
searchBar.pack(padx=20)

entSearch = Entry(searchBar)
entSearch.pack(side=LEFT, padx=20)
btnSearch = Button(searchBar, text="search")
btnSearch.pack()
root.geometry("650x450+200+150")
root.mainloop()