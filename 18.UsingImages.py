from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("using Images")
root.geometry("350x350")

lblText = Label(root, text="Using Images", font="verdana 12")
lblText.pack()
myPic = Image.open("C:/Users/umesh/PycharmProjects/PythonTkinterMasterClass/icons/laughing.png")
resizePic = myPic.resize((300,225),Image.ANTIALIAS)
newPic = ImageTk.PhotoImage(resizePic)
lbl_img = Label(root, image=newPic)
lbl_img.pack()

root.mainloop()
