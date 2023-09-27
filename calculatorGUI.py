# create a GUI calculator using tkinter
#Author - Sachin Jain
#Date - 14 th May, 2023
#File - calculatorGUI.py
#Description- Graphix version of calculator,using tkinter module!
from tkinter import *
from calculator import calculate

def calculator(gui):
    # name the gui window
    gui.title("Calculator")
    # make a entry text box
    entrybox = Entry(gui, width=36, borderwidth=5)
    # position the entry text box in the gui window using the grid manager
    entrybox.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


    b0 = addButton(gui, entrybox, '0')
    b1 = addButton(gui, entrybox, '1')
    b2 = addButton(gui, entrybox, '2')
    b3 = addButton(gui, entrybox, '3')
    b4 = addButton(gui, entrybox, '4')
    b5 = addButton(gui, entrybox, '5')
    b6 = addButton(gui, entrybox, '6')
    b7 = addButton(gui, entrybox, '7')
    b8 = addButton(gui, entrybox, '8')
    b9 = addButton(gui, entrybox, '9')
    b_add = addButton(gui, entrybox, '+')
    b_sub = addButton(gui, entrybox, '-')
    b_mult = addButton(gui, entrybox, '*')
    b_div = addButton(gui, entrybox, '/')
    b_clr = addButton(gui, entrybox, 'c')
    b_eq = addButton(gui, entrybox, '=')
    b_decimal = addButton(gui, entrybox, '.')
    b_lefty = addButton(gui, entrybox, '(')
    b_righty = addButton(gui, entrybox, ')')
    b_expy = addButton(gui, entrybox, '^')

    buttons = [b7, b8, b9, b_clr,
               b4, b5, b6, b_sub,
               b1, b2, b3, b_add,
               b_mult, b0, b_div, b_eq,
               b_decimal, b_lefty, b_righty, b_expy]
    k = 4
    for i in range(k):
        for j in range(k):
            buttons[i * k + j].grid(row=i + 1, column=j, columnspan=1)

    b_decimal.grid(row=k+1, column=0, columnspan=1)
    b_lefty.grid(row=k + 1, column=1, columnspan=1)
    b_righty.grid(row=k + 1, column=2, columnspan=1)
    b_expy.grid(row=k + 1, column=3, columnspan=1)


def addButton(gui, entrybox, value):
    return Button(gui, text=value, height=4, width=9, command=lambda: clickButton(entrybox, value))


def clickButton(entrybox, value):
    if value == "=":
        equ = entrybox.get()
        end = calculate(equ)
        entrybox.delete(0, END)
        entrybox.insert(0, end)

    elif value == "c":
        entrybox.delete(0, END)

    else:
        current = entrybox.get()
        entrybox.delete(0, END)
        entrybox.insert(0, str(current) + str(value))


# main program
# create the main window
gui = Tk()
# create the calculator layout
calculator(gui)
# update the window
gui.mainloop()
