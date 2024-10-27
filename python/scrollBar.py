from tkinter import *
root = Tk()
root.geometry("500x300")
root.title("NotPad")
# listbox = Listbox(root)
 

scrollber = Scrollbar(root)
scrollber.pack(side = RIGHT,fill=Y)
# listbox = Listbox(root,yscrollcommand=scrollber.set)
# for i in range(101):
#     listbox.insert(END,f"Item {i}")
# listbox.pack()
text = Text(root,yscrollcommand=scrollber.set)
text.pack(fill=BOTH)
scrollber.config(command=text.yview)



root.mainloop()