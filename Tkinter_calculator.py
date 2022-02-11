from tkinter import *

root = Tk()
root.title("Calculator")

x = Entry(root, width=30, borderwidth= 3)
x.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

def button_click(num):
    current = x.get()
    x.delete(0,END)
    x.insert(0,str(current) + str(num))

def button_clear():
    x.delete(0, END)

def button_add():
    first_num = x.get()
    global math
    global first_number
    math = "ADD"
    first_number = int(first_num)
    x.delete(0,END)

def button_subtract():
    first_num = x.get()
    global math
    global first_number
    math = "SUBTRACT"
    first_number = int(first_num)
    x.delete(0, END)

def button_multiply():
    first_num = x.get()
    global math
    global first_number
    math = "MULTI"
    first_number = int(first_num)
    x.delete(0, END)

def button_divide():
    first_num = x.get()
    global math
    global first_number
    math = "DIVI"
    first_number = int(first_num)
    x.delete(0, END)

def button_equal():
    second_num = x.get()
    x.delete(0, END)

    if math == "ADD":
        x.insert(0, first_number + int(second_num))
    elif math == "SUBTRACT":
        x.insert(0, first_number - int(second_num))
    elif math == "MULTI":
        x.insert(0, first_number * int(second_num))
    else:
        x.insert(0, first_number / int(second_num))

button_0 = Button(root, text="0", padx=30, pady=30, command=lambda: button_click(0))
button_1 = Button(root, text="1", padx=30, pady=30, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=30, pady=30, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=30, pady=30, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=30, pady=30, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=30, pady=30, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=30, pady=30, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=30, pady=30, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=30, pady=30, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=30, pady=30, command=lambda: button_click(9))

button_0.grid(row=4, column=0)
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_add = Button(root,text="+",padx=30,pady=20,command=button_add)
button_subtract = Button(root,text="-",padx=30,pady=20,command=button_subtract)
button_multiply = Button(root,text="*",padx=30,pady=20,command=button_multiply)
button_divide = Button(root,text="/",padx=30,pady=20,command=button_divide)

button_equal = Button(root, text="=",padx=30,pady=20,command=button_equal)
button_clear = Button(root, text="clear",padx=30,pady=20,command=button_clear)

button_add.grid(row=5, column=0)
button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

button_equal.grid(row=5, column=1)
button_clear.grid(row=5, column=2)


root.mainloop()