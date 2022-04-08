from tkinter import *
from datetime import date
import time
import os
from PIL import ImageTk, Image

root = Tk()
root.title("Assignment 1 - Section A")
root.geometry("450x300")
root.resizable(False, False)

lblTitle= Label(root, text="AUTOMATION TOOL NAME Version 1.0.0",font="Verdana 12 bold").pack(pady=20)

# AGENT
frmAgent = LabelFrame(root, text=" AGENT DETAILS ", width=200, height=100, font="Verdana 8").place(x=10, y=60)
lblUserName = Label(frmAgent,text="UserName  -->  " + os.getlogin()).place(x=20, y=80)

# TIME STAMP
frmTimeStamp = LabelFrame(root, text=" TIMESTAMP DETAILS ", width=200, height=100, font="Verdana 8").place(x=240, y=60)
lblDay = Label(frmTimeStamp,text="DAY  -->  " + date.today().strftime("%A")).place(x=270,y=86)
lblDate = Label(frmTimeStamp,text="DATE -->  " + date.today().strftime("%x")).place(x=270,y=106)
lblTime = Label(frmTimeStamp,text="TIME -->  " + time.strftime("%H:%M:%S")).place(x=270,y=126)

btnStart = Button(root, text="START", width=60, height=2).place(x=10, y=200)


# IMAGE
# canvas = Canvas(root,width=195, height=140, bd=2, relief=GROOVE)
# img = ImageTk.PhotoImage(Image.open("bot_img1.jpg"))
# canvas.create_image(0, 0, anchor=NW, image=img)
# canvas.place(x=10, y=180)
root.mainloop()