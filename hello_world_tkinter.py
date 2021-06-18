import tkinter as tk
from tkinter import ttk

# Create the application window
main_window = tk.Tk()

# Create the user interface
first_label = ttk.Label(main_window, text="Hello-World!")
first_label.grid(row=1, column=1)

# Start the GUI event loop
main_window.mainloop()
