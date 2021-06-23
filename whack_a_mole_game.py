import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox
from random import randint

def main():
    # Create the entire GUI program
    app = WhackAMole()

    # Start the GUI event loop
    app.window.mainloop()

class WhackAMole:
    STATUS_BACKGROUND = "white"
    NUM_MASHES_ACROSS = 4
    MIN_TIME_DOWN = 1000
    MAX_TIME_DONW = 5000
    MIN_TIME_UP = 1000
    MAX_TIME_UP = 3000
    
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Whack-A-Mole")

        self.mash_frame, self.status_frame = self.create_frames()

        self.mash_photo = PhotoImage(file="mash.png")
        self.mole_cover_photo = PhotoImage(file="mash.png")
        self.label_timers = {}

        self.mash_buttons = self.create_mashes()

        self.hit_counter, self.miss_counter, self.start_button, self.quit_button = self.create_status_widgets()

        self.set_callbacks()
        self.game_is_running = False

    def create_frames(self):
        mash_frame = tk.Frame(self.window)
        mash_frame.grid(row=0, column=0)

        status_frame = tk.Frame(self.window, bg=WhackAMole.STATUS_BACKGROUND)
        status_frame.grid(row=0, column=1, sticky=tk.E + tk.W + tk.N + tk.S, ipadx=6)

        return mash_frame, status_frame

    def create_mashes(self):
        mash_labels = []
        for i in range(WhackAMole.NUM_MASHES_ACROSS):
            row_of_labels = []
            for e in range(WhackAMole.NUM_MASHES_ACROSS):
                mash_label = tk.Label(self.mash_frame, image=self.mash_photo)
                mash_label.grid(row=i, column=e, sticky=tk.E + tk.W + tk.N + tk.S)
                self.label_timers[id(mash_label)] = None

                row_of_labels.append(mash_label)

            mash_labels.append(row_of_labels)

        return mash_labels


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

        return hit_counter, miss_counter, start_button, quit_button

        
    def set_callbacks(self):
        # Set the same callback for each mash button
        for i in range(WhackAMole.NUM_MASHES_ACROSS):
            for e in range(WhackAMole.NUM_MASHES_ACROSS):
                self.mash_buttons[i][e].bind("<ButtonPress-1>", self.mash_hit)

        self.start_button["command"] = self.start
        self.quit_button["command"] = self.quit


    def mash_hit(self, event):
        if self.game_is_running:
            hit_label = event.widget
            if hit_label["image"] == self.mole_cover_photo.name:
                # MISSED! update the miss counter
                self.miss_counter["text"] = str(int(self.miss_counter["text"]) + 1)
            else:
                # HIT! update the hit counter
                self.hit_counter["text"] = str(int(self.hit_counter["text"]) + 1)
                # Remove the mash and don't update the miss counter
                self.put_down_mash(hit_label, False)

    def start(self):
        if self.start_button["text"] == "Start":
            # Change all the mashes images to blank image and
            # set a random time for the mashes to re-appear on each label.
            for i in range(WhackAMole.NUM_MASHES_ACROSS):
                for e in range(WhackAMole.NUM_MASHES_ACROSS):
                    the_label = self.mash_labels[i][e]
                    the_label["image"] = self.mash_cover_photo
                    time_down = randint(WhackAMole.MIN_TIME_DOWN,
                                        WhackAMole.MAX_TIME_DONW)
                    timer_object = the_label.after(time_down,
                                                   self.pop_up_mash, the_label)
                    self.label_timers[id(the_label)] = timer_object

            self.game_is_running = True
            self.start_button["text"] = "Stop"
            
            self.hit_counter["text"] = "0"
            self.miss_counter["text"] = "0"

        else: # The game is running, so stop the game and reset everything
            # Show every mash and stop all the timers
            for i in range(WhackAMole.NUM_MASHES_ACROSS):
                for e in range(WhackAMole.NUM_CRASHES_ACROSS):
                    the_label = self.mole_labels[i][e]
                    # Show the mash
                    the_label["image"] = self.mash_photo
                    # Delete any timer that is associated with the mole
                    the_label.after_cancel(self.label_timers[id(the_label)])

            self.game_is_running = False
            self.start_button["text"] = "Start"


    def put_down_mash(self, the_label, timer_expired):

        if self.game_is_running:
            if timer_expired:
                # The mole is going down before it was clicked on, so update the miss counter
                self.miss_counter["text"] = str(int(self.miss_counter["text"]) + 1)
            else:
                # The timer did not expire, so manually stop the timer
                the_label.after_cancel(self.label_timers[id(the_label)])

            # Make the mash invisible
            the_label["image"] = self.mash_cover_photo

            # Set a call to pop up the mash in the future
            time_down = randint(WhackAMole.MIN_TIME_DOWN,
                                WhackAMole.MAX_TIME_DOWN)
            timer_object = the_label.after(time_down, self.pop_up_mole, the_label)
            # Remember the timer object so it can be canceled later, if need be
            self.label_timers[id(the_label)] = timer_object

    def pop_up_mash(self, the_label):
        # Show the mash on the screen
        the_label["image"] = self.mash_photo

        if self.game_is_running:
            # Set a call to make the mash disappear in the future
            time_up = randint(WhackAMole.MIN_TIME_UP, WhackAMole.MAX_TIME_UP)
            timer_object = the_label.after(time_up, self.put_down_mash,
                                           the_label, True)
            self.label_timers[id(the_label)] = timer_object

    def quit(self):
        really_quit = messagebox.askyesno("Quitting?", "Do you really want to quit?")
        if really_quit:
            self.window.destroy()

    def quit(self):
        print("quit button hit")


if __name__ == "__main__":
    main()


