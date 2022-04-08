from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Paned Window Widget")
root.geometry("450x300")
root.resizable(False, False)


def proc_quit():
    root.quit()


pwPane = ttk.Panedwindow(root, orient=HORIZONTAL)
pwPane.pack(pady=20)
frmFrame1 = ttk.Frame(pwPane, width=100, height=200, relief=SUNKEN)
frmFrame2 = ttk.Frame(pwPane, width=200, height=200, relief=SUNKEN)
frmFrame3 = ttk.Frame(pwPane, width=75, height=200, relief=SUNKEN)
pwPane.add(frmFrame1, weight=1)
pwPane.add(frmFrame2, weight=3)
pwPane.insert(1, frmFrame3)

lblLabel = Label(frmFrame3, text="Hello").grid(row=0, column=0, pady=20)
btnButton = Button(frmFrame3, text="Click me", command=proc_quit).grid(row=1, column=0, pady=20)
root.mainloop()
