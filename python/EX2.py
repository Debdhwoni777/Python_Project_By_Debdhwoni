from tkinter import *
root = Tk()
# root.geometry("200x300")
def up():
    root.geometry(f"{v1.get()}x{v2.get()}")
root.title("EX2.py")
v1 = StringVar()
v2 = StringVar()
Entry(root,textvariable=v1).pack()
Entry(root,textvariable=v2).pack()
Button(root,text="Click",command=up).pack()
root.mainloop()