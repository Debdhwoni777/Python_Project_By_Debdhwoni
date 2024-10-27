from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    
    if text == "=":
        try:
            value = eval(screen.get())
            scvalue.set(value)
            screen.update()
        except Exception as e:
            scvalue.set("Error")
            screen.update()
    
    elif text == "C":
        scvalue.set("")
        screen.update()
    
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()
root.title("CALCULATOR BY DEBDHWONI")
root.geometry('490x570')
root.config(bg="orange")

scvalue = StringVar()
scvalue.set("")

screen = Entry(root, textvar=scvalue, font="lucida 40 bold", bg="navajowhite")
screen.pack(fill=X, ipadx=10, padx=10, pady=10)

button_texts = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "+", "="]
]

for row in button_texts:
    f = Frame(root, bg="orange")
    for text in row:
        b = Button(f, text=text, font="lucida 25 bold", padx=20, pady=20,bg="moccasin")
        b.pack(side=LEFT, padx=10, pady=10)
        b.bind("<Button-1>", click)
    f.pack()

root.mainloop()