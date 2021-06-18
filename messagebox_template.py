import tkinter as tk
from tkinter import ttk, messagebox

# Create the application window
main_window = tk.Tk()

# Create the user interface
first_label = ttk.Label(main_window, text="Hello-World!")
first_label.grid(row=1, column=1)

# Message Boxes
messagebox.showinfo("Information","Informative message")
messagebox.showerror("Error", "Error message")
messagebox.showwarning("Warning", "Warning message")
answer = messagebox.askokcancel("Question", "Do you want to open this file?")
answer = messagebox.askretrycancel("Question", "Do you want to try that again?")
answer = messagebox.askyesno("Question", "Do you like Python?")
answer = messagebox.askyesnocancel("Question", "Continue playing?")

if answer == False:
   main_window.destroy()

# Start the GUI event loop
main_window.mainloop()
