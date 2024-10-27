from tkinter import *
import tkinter.messagebox as tmsg
    
root = Tk()
 
def getnum():
    print(f"The number is : {myslider2.get()}")
    tmsg.showinfo(f"you pick {myslider2.get()}",f"you pick {myslider2.get()}")

    
root.geometry("500x300")
root.maxsize(500,300)
root.minsize(500,300)
root.title("sliders")
root.config(bg="orange")

# myslider1 = Scale(root,from_=0,to=100,bg="peachpuff")
# myslider1.pack()
Label(text="pick a number.(with this)").pack()
myslider2 = Scale(root,from_=0,to=100,bg="peachpuff",orient=HORIZONTAL,tickinterval=50)
myslider2.pack()
myslider2.set(0)
Button(text="Get Any Number",command=getnum).pack()


root.mainloop()