from tkinter import *
from tkinter import ttk
# from tkcalendar import Calendar

root = Tk()


def callback():
    print("UserID: " + entName.get())
    print("Password: " + entPass.get())

    print("Gender: " + gender.get())

    if chRemMe.get() == 1:
        print("Remember me is SELECTED..!!")
    else:
        print("Remember is NOT SELECTED..!!")

    # print("DOB Selected Date: " + calDOB.get_date())
    # Close Window
    # root.quit()


lblTitle = ttk.Label(root, text="PROJECT NAME HERE", font="Times 15 bold")
lblName = ttk.Label(root, text="UserID", font='Times 12 bold')
lblPass = ttk.Label(root, text="Password", font='Times 12 bold')
lblJoinMonth = ttk.Label(root, text="Joining Month", font='Times 12 bold')
lblGender = ttk.Label(root, text="Gender", font='Times 12 bold')

entName = ttk.Entry(0, width=20)
entPass = ttk.Entry(0, width=20)
entName.insert(0, 'Enter your UserID')
entPass.insert(0, 'Enter your password')
entPass.config(show="*")

btnSubmit = Button(root, text="Submit", font="Times 10 bold", command=callback)

# lblTitle.pack()
# lblName.pack()
# entName.pack()
# lblPass.pack()
# entPass.pack()
# btnSubmit.pack()

lblTitle.grid(row=0, column=1, columnspan=2)
lblName.grid(row=2, column=0, sticky=W)
lblPass.grid(row=3, column=0, sticky=W)
lblJoinMonth.grid(row=4, column=0)
lblGender.grid(row=5, column=0, sticky=W)

entName.grid(row=2, column=1)
entPass.grid(row=3, column=1)

chRemMe = IntVar()
chRemMe.set(0)
chkBox = Checkbutton(root, text="Remember me", variable=chRemMe, font="Times 10")
chkBox.grid(row=7, column=1, sticky=E + W, pady=2)

gender = StringVar()
ttk.Radiobutton(root, text="male", value="male", var=gender).grid(row=5, column=1, sticky=W+E)
ttk.Radiobutton(root, text="female", value="female", var=gender).grid(row=6, column=1, sticky=W+E)


months = StringVar()
cmbBox = ttk.Combobox(root, textvariable=months, values=('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'), state='readonly')
cmbBox.grid(row=4, column=0, columnspan=2, sticky=E)

btnSubmit.grid(row=9, column=1, sticky=E+W, pady=4)

# calDOB = Calendar(root,selectmode='day',year=1994,month=8,day=16)
# calDOB.grid(row=10,column=1,columnspan=2)

spnYear = StringVar()
Spinbox(root, from_=1994, to=2022, state='readonly').grid(row=10, column=1)

root.geometry("400x450")
root.mainloop()
