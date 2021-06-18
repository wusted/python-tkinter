import tkinter as tk
from tkinter import simpledialog as simpdial

main_app_window = tk.Tk()

answer_1 = simpdial.askstring("Input", "What is your name?", parent=main_app_window)

if answer_1 is not None:
    print("Your first name is ", answer_1)
else:
    print("You don't have first name?")

answer_1 = simpdial.askinteger("Input", "What is your age?", parent=main_app_window, minvalue=0, maxvalue=100)

if answer_1 is not None:
    print("Your age is", answer_1)
else:
    print("You don't have an age?")

answer_1 = simpdial.askfloat("Input", "What is your monthly salary in USD $ ?", parent=main_app_window, minvalue=0.0, maxvalue=1000000.0)

if answer_1 is not None:
    print("Your monthly salary is", "$",answer_1,)
else:
    print("You don't have a salary?")




