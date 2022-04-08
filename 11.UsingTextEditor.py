from tkinter import *

root = Tk()
root.resizable(False, False)


def proc_result():
    print("Your Text Editor Data: " + txtEditor.get(1.0, END))


def proc_close():
    root.quit()


txtEditor = Text(root, width=25, height=8, font="Verdana 12", wrap=WORD)
txtEditor.grid(row=0, column=0, padx=15, pady=20)
txtEditor.insert(INSERT, "Hello, I'm tkinter library for GUI building..!!")
txtEditor.config(state='disabled')
txtEditor.config(state='normal')

btnSave = Button(root, text="SAVE", width=25, height=1, font="Verdana 12", command=proc_result)
btnClose = Button(root, text="CLOSE", width=25, height=1, font="Verdana 12", command=proc_close)
btnSave.grid(row=3, column=0)
btnClose.grid(row=4, column=0)

root.geometry("550x500")
root.mainloop()
