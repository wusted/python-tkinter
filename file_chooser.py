import tkinter as tk
from tkinter import filedialog
import os

main_app_window = tk.Tk()

# Build a list of tuples for each file type the filedialog should display

valid_filetypes = [("all files", ".*",), ("text files", ".txt")]

# Ask the user to select a folder
answer_1 = filedialog.askdirectory(parent=main_app_window, 
                                   initialdir=os.getcwd(), 
                                   title="Please select a folder:")

# Ask the user to select a single file name.
answer_1 = filedialog.askopenfilename(parent=main_app_window,
                                      initialdir=os.getcwd(),
                                      title="Please select a file:",
                                      filetypes=valid_filetypes)

# Ask the user to select a one or more file names
answer_1 = filedialog.askopenfilenames(parent=main_app_window,
                                       initialdir=os.getcwd(),
                                       title="Please select one or more files:",
                                       filetypes=valid_filetypes)

# Ask the user to select a single file name for saving
answer_1 = filedialog.asksaveasfilename(parent=main_app_window,
                                        initialdir=os.getcwd(),
                                        title="Please select a file name for saving:",
                                        filetypes=valid_filetypes)
