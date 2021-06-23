import tkinter as tk
from tkinter import PhotoImage

def main():
    # Create the entire GUI program
    app = WhackAMole()

    # Start the GUI event loop
    app.window.mainloop()

class WhackAMole:
    STATUS_BACKGROUND = "white"
    NUM_MASHES_ACROSS = 4
    
    def __init__(self):
        self.window = tk.Tk()
        self.mash_frame, self.status_frame = self.create_frames()
        self.mash_photo = PhotoImage(file="mash.png")
        self.mash_buttons = self.create_mashes()

        self.hit_counter, self.miss_counter, self.start_button = self.create_status_widgets()

    def create_frames(self):
        mash_frame = tk.Frame(self.window, bg="red")
        mash_frame.grid(row=1, column=1)

        status_frame = tk.Frame(self.window, bg=WhackAMole.STATUS_BACKGROUND)
        status_frame.grid(row=1, column=2, sticky=tk.N + tk.S + tk.W + tk.W)

        return mash_frame, status_frame

    def create_mashes(self):
        mash_buttons = []
        for i in range(WhackAMole.NUM_MASHES_ACROSS):
            row_of_buttons = []
            for e in range(WhackAMole.NUM_MASHES_ACROSS):
                mash_button = tk.Button(self.mash_frame, image=self.mash_photo)
                mash_button.grid(row=i, column=e, padx=8, pady=8)

                row_of_buttons.append(mash_button)

            mash_buttons.append(row_of_buttons)

        return mash_buttons


    def create_status_widgets(self):
        spacer = tk.Label(self.status_frame, text="", bg=WhackAMole.STATUS_BACKGROUND)
        spacer.pack(side="top", fill=tk.Y, expand=True)

        hit_label = tk.Label(self.status_frame, text="Number of Kretas", bg=WhackAMole.STATUS_BACKGROUND)
        hit_label.pack(side="top", fill=tk.Y, expand=True)

        hit_counter = tk.Label(self.status_frame, text="0", bg=WhackAMole.STATUS_BACKGROUND)
        hit_counter.pack(side="top", fill=tk.Y, expand=True)

        spacer = tk.Label(self.status_frame, text="", bg=WhackAMole.STATUS_BACKGROUND)
        spacer.pack(side="top", fill=tk.Y, expand=True)

        miss_label = tk.Label(self.status_frame, text="Number of Kretas Missed", bg=WhackAMole.STATUS_BACKGROUND)
        miss_label.pack(side="top", fill=tk.Y, expand=True)

        miss_counter = tk.Label(self.status_frame, text="0", bg=WhackAMole.STATUS_BACKGROUND)
        miss_counter.pack(side="top", fill=tk.Y, expand=True)

        spacer = tk.Label(self.status_frame, text="", bg=WhackAMole.STATUS_BACKGROUND)
        spacer.pack(side="top", fill=tk.Y, expand=True)

        start_button = tk.Button(self.status_frame, text="Start")
        start_button.pack(side="top", fill=tk.Y, expand=True, ipadx=10)

        spacer = tk.Label(self.status_frame, text="", bg=WhackAMole.STATUS_BACKGROUND)
        spacer.pack(side="top", fill=tk.Y, expand=True)

        quit_button = tk.Button(self.status_frame, text="Quit")
        quit_button.pack(side="top", fill=tk.Y, expand=True, ipadx=10)

        spacer = tk.Label(self.status_frame, text="", bg=WhackAMole.STATUS_BACKGROUND)
        spacer.pack(side="top", fill=tk.Y, expand=True)

        return hit_counter, miss_counter, start_button


if __name__ == "__main__":
    main()


