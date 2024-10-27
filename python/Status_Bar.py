from tkinter import *
import time
root = Tk()
def up():
    sv.set("busy...")
    time.sleep(2)
    sv.set("READY IT")
root.geometry("666x464")
root.title("Status_Bar")
sv = StringVar()
sv.set("READY")
ss = Label(root,textvariable=sv,relief=SUNKEN,anchor="w",borderwidth=10)
ss.pack(side=BOTTOM,fill=X)
Button(root,text="update",command=up).pack()
root.mainloop()