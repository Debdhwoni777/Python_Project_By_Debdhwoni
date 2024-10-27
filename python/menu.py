from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
def mnu():
    print("ata akti baker menu")
     
def help():
    print("I am HELP you")
    a = tmsg.showinfo("Help","I am help you")
    print(a)

def rate():
    v = tmsg.askquestion("rate us","you are rate us ")

root.geometry("500x300")
root.maxsize(500,300)
root.minsize(500,300)
root.title("menu.py")
#menu
# fliemenu = Menu(root)
# fliemenu.add_command(label="Flie")
# fliemenu.add_command(label="exit")
# root.config(menu = fliemenu)

mymenu = Menu(root)
m1 = Menu(mymenu,tearoff=0)
m1.add_command(label="New Flie",command = mnu)
m1.add_command(label="New Folder",command = mnu)
m1.add_command(label="Save",command = mnu)
m1.add_separator()
m1.add_command(label="Save As",command = mnu)
m1.add_command(label="Delete",command = mnu)
mymenu.add_cascade(label="Flie",menu=m1)
m1.add_command(label="Exit",command = quit)
root.config(menu=mymenu)

#Menu2 
m2 = Menu(mymenu,tearoff=0)
m2.add_command(label="New Flie",command = mnu)
m2.add_command(label="New Folder",command = mnu)
m2.add_command(label="Save",command = mnu)
m2.add_separator()
m2.add_command(label="Save As",command = mnu)
m2.add_command(label="Delete",command = mnu)
mymenu.add_cascade(label="Edit",menu=m2)
m2.add_command(label="Exit",command = quit)
root.config(menu=mymenu)

#menu3
m3 = Menu(mymenu,tearoff=0)
m3.add_command(label="New Flie",command = mnu)
m3.add_command(label="New Folder",command = mnu)
m3.add_command(label="Save",command = mnu)
m3.add_separator()
m3.add_command(label="Save As",command = mnu)
m3.add_command(label="Delete",command = mnu)
mymenu.add_cascade(label="Run",menu=m3)
m3.add_command(label="Run",command = quit)
root.config(menu=mymenu)

#menu4
m4 = Menu(mymenu)
m4.add_command(label="Help",command = help)
m4.add_command(label="Help",command = rate)
mymenu.add_cascade(label="Help",menu=m4)
root.config(menu=mymenu)

#menu for qiut
m5 = Menu(mymenu)
m5.add_command(label='Exit',command=quit)
mymenu.add_cascade(label="Exit",menu=m5)
root.config(menu=mymenu)

root.mainloop()