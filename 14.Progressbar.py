from tkinter import *
from tkinter import ttk

root = Tk()

# 1
pgBar = ttk.Progressbar(root, orient=HORIZONTAL, length=200)
pgBar.config(mode='indeterminate')
pgBar.start()
pgBar.stop()
pgBar.pack(pady=20)

# 2
pgBar.config(mode='determinate', maximum=50.0, value=5.0)
pgBar.start()
pgBar.stop()

# 3
value = DoubleVar()
scale = ttk.Scale(root, orient=HORIZONTAL, length=200, variable=value, from_ =0.0, to=50.0)
pgBar.config(var=value)
scale.pack()

root.geometry("450x450+650+200")
root.mainloop()
