from tkinter import *

root = Tk()
root.resizable(False, False)


def proc_submit():
    print("User ID: " + txtID.get())
    print("Pass: " + txtPass.get())
    print("You clicked SUBMIT..!!")


def proc_cancel():
    print("You clicked CANCEL..!!")
    root.quit()


def change_bgcolor_submit(e):
    btnSubmit.config(background="green")


def change_fgcolor_submit(e):
    btnSubmit.config(background="grey")


def change_bgcolor_cancel(e):
    btnCancel.config(background="green")


def change_fgcolor_cancel(e):
    btnCancel.config(background="grey")


lblTitle = Label(root, text="Place Geometry Manager", font="Verdana 14 bold")
lblID = Label(root, text="UserID: ", font="Verdana 10 bold")
lblPass = Label(root, text="Passkey: ", font="Verdana 10 bold")

txtID = Entry(root, width=25)
txtPass = Entry(root, width=25)

btnSubmit = Button(root,
                   text="SUBMIT", width=8, fg='white',
                   bg='Black', activebackground="#f00",
                   activeforeground="#fff", command=proc_submit
                   )

btnCancel = Button(root, text="CANCEL", width=8,
                   fg='white', bg='Black',
                   activebackground="#f00",
                   activeforeground="#fff",
                   command=proc_cancel
                   )

for b in [btnSubmit]:
    b.bind("<Enter>", change_bgcolor_submit)
    b.bind("<Leave>", change_fgcolor_submit)

for b in [btnCancel]:
    b.bind("<Enter>", change_bgcolor_cancel)
    b.bind("<Leave>", change_fgcolor_cancel)

lblTitle.place(x=100, y=20)
lblID.place(x=100, y=70)
lblPass.place(x=100, y=100)
txtID.place(x=200, y=70)
txtPass.place(x=200, y=100)
btnSubmit.place(x=200, y=140)
btnCancel.place(x=290, y=140)

# WINDOW SIZE(FIRST TWO VALUES) & POSITION ON SCREEN(LAST TWO VALUES)
root.geometry("450x250+350+250")
root.mainloop()
