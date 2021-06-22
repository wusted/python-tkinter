import tkinter as tk
from tkinter import ttk

def main():
    # Create the entire GUI event loop
    app = CounterApp()

    # Start the GUI event loop
    app.window.mainloop()

class CounterApp:

    def __init__(self):
        self.window = tk.Tk()
        self.my_counter = None  # All attributes should be initialize in init
        self.create_widgets()

    def create_widgets(self):
        self.my_counter = ttk.Label(self.window, text="0")
        self.my_counter.grid(row=0, column=0)

        increment_button = ttk.Button(self.window, text="Add 1 to counter")
        increment_button.grid(row=1, column=0)
        increment_button["command"] = self.increment_counter

        reset_button = ttk.Button(self.window, text="Reset counter to 0")
        reset_button.grid(row=2, column=0)
        reset_button["command"] = self.reset_button

        quit_button = ttk.Button(self.window, text="Quit")
        quit_button.grid(row=3, column=0)
        quit_button["command"] = self.window.destroy

    def increment_counter(self):
        self.my_counter["text"] = str(int(self.my_counter["text"]) + 1)

    def reset_button(self):
        self.my_counter["text"] = str(int(self.my_counter["text"]) * 0)

if __name__ == "__main__":
    main()

