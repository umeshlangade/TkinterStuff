from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()


def proc_info():
    msg_info = messagebox.askquestion("2BHK", "Are you sure, you want to buy..!!")
    if msg_info == 'yes':
        print("Customer will buy 2BHK flat")
    else:
        print("Customer won't buy 2BHK flat")


def proc_del():
    messagebox.showinfo("Success..!!","This is just an information messagebox..!!")


btnInfo = ttk.Button(root, text="Information", command=proc_info).grid(row=0, column=0, pady=25, padx=50)
btnDel = ttk.Button(root, text="Delete", command=proc_del).grid(row=0, column=1)

root.geometry("400x350")
root.mainloop()
