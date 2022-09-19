import tkinter as tk
from tkinter import ttk
from tkinter import *
import math

def show_entry_fields():
    aws = "Error"
    # if e1.get() == "":
    #     print("e1")
    #     erm = "Please Enter The Number(s)"
    if e1.get() != "":
        x = int(e1.get())
    if e2.get() != "":
        y = int(e2.get())

    if Combo.current() == -1:
        print("Please Choose The Formula")
        erm = "Choose The Formula"
    if Combo.current() == 0:
        aws = x*y
        print(aws)
    if Combo.current() == 1:
        cal = x*x
        aws = cal*3.1415
        print(aws)
    if Combo.current() == 2:
        cal = 2*22*x
        aws = cal/7
        print(aws)
    if Combo.current() == 3:
        aws = x*x
        print(aws)
    if Combo.current() == 4:
        aws = math.sqrt(x)
        print(aws)

    print("X: %s\nY: %s" % (e1.get(), e2.get()))
    Label(master, text = 'Your Awnser is ').grid(row = 5, column = 0, sticky = W, pady = 2)
    Label(master, text = aws).grid(row = 5, column = 1, sticky = W, pady = 2)

    # Label(master, text = 'Error').grid(row = 6, column = 0, sticky = W, pady = 2)
    # Label(master, text = erm).grid(row = 6, column = 1, sticky = W, pady = 2)

    print("combo =",Combo.current())

master = tk.Tk()
master.geometry("400x200")
master.title("POG Calculator (Precision Output Gui)")
tk.Label(master, 
         text="X").grid(row=0)
tk.Label(master, 
         text="Y").grid(row=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

tk.Button(master, 
          text='Calculate', command=show_entry_fields).grid(row=7,
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)

n = tk.StringVar()
Combo = ttk.Combobox(master, width = 27, textvariable = n)


Combo['values'] = (' rectangle (x and y)',
                          ' Circle Area (x)',
                          ' Circle outline (x)',
                          ' Square (x)',
                          ' Root of (x)')


ttk.Label(master, text = "Select the formula :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 4, padx = 10, pady = 25)

Combo.grid(column = 1, row = 4)
Combo.current()

tk.mainloop()





#REF = https://www.w3schools.com/python/module_math.asp
