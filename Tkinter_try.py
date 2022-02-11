from tkinter import *

root = Tk()

x = Entry(root,width=30,bg="grey",fg="white",borderwidth=3)
x.pack()
x.insert(0, "What's your name?")

label1 = Label(root, text="Hello world", bg="pink").pack()
label2 = Label(root, text="This is an interface").pack()

def click1():
    label = Label(root, text=f"Hello {x.get()}")
    label.pack()

button1 = Button(root, text="click", padx=50, pady=5, command= click1)
button1.pack()


root.mainloop()