from tkinter import *
from tkinter import ttk

root = Tk()

def callback():
    print("UserID: " + entName.get())
    print("Password: " + entPass.get())
    if chvar.get()==1:
        print("Remember me is SELECTED..!!")
    else:
        print("Remember is NOT SELECTED..!!")

lblTitle = ttk.Label(root,text="PROJECT NAME HERE",font="Times 15 bold")
lblName = ttk.Label(root,text="UserID",font='Times 12 bold')
lblPass = ttk.Label(root,text="Password",font='Times 12 bold')

entName = ttk.Entry(0,width=20)
entPass = ttk.Entry(0,width=20)
entName.insert(0,'Enter your UserID')
entPass.insert(0,'Enter your password')
entPass.config(show="*")

btnSubmit = Button(root,text="Submit",font="Times 10 bold",command=callback)

# lblTitle.pack()
# lblName.pack()
# entName.pack()
# lblPass.pack()
# entPass.pack()
# btnSubmit.pack()

lblTitle.grid(row=0,column=1,columnspan=2)
lblName.grid(row=2,column=0,sticky=W)
lblPass.grid(row=3,column=0,sticky=W)
entName.grid(row=2,column=1)
entPass.grid(row=3,column=1)

chvar=IntVar()
chvar.set(0)
cbox  = Checkbutton(root,text="Remember me",variable=chvar,font="Times 10")
cbox.grid(row=6,column=1,sticky=E+W,pady=2)


btnSubmit.grid(row=7,column=1,sticky=E+W,pady=4)


root.geometry("300x350")
root.mainloop()