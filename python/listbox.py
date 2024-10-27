from tkinter import *
root = Tk()
def add():
    global i
    lb.insert(ACTIVE,f"{i}")
    i += 1
i = 0
root.title("Listbox")
root.geometry("500x300")
lb = Listbox(root)
lb.pack()
lb.insert(END,"Frist Item of this listbox")

Button(root,text="Add Item",command=add).pack()

root.mainloop()