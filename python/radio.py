from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
def order ():
    tmsg.showinfo("your order",f"You order {ver.get()}")
    
root.geometry("600x400")
root.maxsize(600,400)
root.minsize(600,400)
root.title("Radio Buttom")
# root.config(bg="orange")

# ver = IntVar()
ver = StringVar()

Label(root,text="What would you like sir ?",font=("lucida 22"),justify="left",padx=20,pady=20).pack()

r = Radiobutton(root,text="Rice",padx=20,variable=ver,value="Rice").pack(anchor="w")
r = Radiobutton(root,text="Dosa",padx=20,variable=ver,value="Dosa").pack(anchor="w")
r = Radiobutton(root,text="Samosa",padx=20,variable=ver,value="Samosa").pack(anchor="w")
r = Radiobutton(root,text="Roti",padx=20,variable=ver,value="Roti").pack(anchor="w")

Button(root,text="Order",command=order).pack()

root.mainloop()