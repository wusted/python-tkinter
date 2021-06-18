import tkinter as tk
from tkinter import colorchooser

main_app_window = tk.Tk()
hex_color, web_color = colorchooser.askcolor(parent=main_app_window,
                                             initialcolor=(255, 0, 0))

