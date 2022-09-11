from tkinter import *
import tkinter as tk

main = tk.Tk()
main.title('How is your GRADE ?')
main.option_add('*Font', 'sarabun 16')


Label(main, text = 'Percentage Score').grid(row = 0, column = 0, sticky = W, pady = 2)
etry = tk.Entry(main)
etry.grid(row = 0, column = 1, sticky = W, pady = 2)
Label(main, text = '/ 100').grid(row = 0, column = 2, sticky = W, pady = 2)

gradedaitawrai = 0
percentdaitawrai = 0

def CallBack():

    if etry.get() != "":
        percentdaitawrai = int(etry.get())
        if percentdaitawrai >= 80 and percentdaitawrai <= 100 :
            gradedaitawrai = 4.00
        elif percentdaitawrai >= 75 and percentdaitawrai < 80 :
            gradedaitawrai = 3.50
        elif percentdaitawrai >= 70 and percentdaitawrai < 75 :
            gradedaitawrai = 3.00
        elif percentdaitawrai >= 65 and percentdaitawrai < 70 :
            gradedaitawrai = 2.50
        elif percentdaitawrai >= 60 and percentdaitawrai < 65 :
            gradedaitawrai = 2.00
        elif percentdaitawrai >= 55 and percentdaitawrai < 60 :
            gradedaitawrai = 1.50
        elif percentdaitawrai >= 50 and percentdaitawrai < 55 :
            gradedaitawrai = 1.00
        elif percentdaitawrai >= 0 and percentdaitawrai < 50 :
            gradedaitawrai = 0
        else :
            gradedaitawrai = 'ERROR'
        Label(main, text = 'Your Grade is').grid(row = 1, column = 0, sticky = W, pady = 2)
        Label(main, text = gradedaitawrai).grid(row = 1, column = 1, sticky = W, pady = 2)

Label(main, text = 'Your Grade is').grid(row = 1, column = 0, sticky = W, pady = 2)
Label(main, text = gradedaitawrai).grid(row = 1, column = 1, sticky = W, pady = 2)

Button(main, text ="Calculate", command = CallBack).grid(row = 1, column = 2, sticky = W, pady = 2)


tk.mainloop()
