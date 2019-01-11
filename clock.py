from tkinter import *
from datetime import datetime
from settings import *

clock = Settings()

# Updates the program and clock settings
def tick():
    time_string = datetime.now().strftime(clock.time_format)
    date_string = datetime.now().strftime(clock.date_format)

    root.config(bg=clock.background_color)

    container.configure(bg=clock.background_color)

    current_time.configure(text=time_string,
                           font=(clock.time_font, clock.time_size, clock.time_weight, clock.time_slant),
                           fg=clock.time_color,
                           bg=clock.background_color)

    current_date.configure(text=date_string,
                           font=(clock.date_font, clock.date_size, clock.date_weight, clock.date_slant),
                           fg=clock.date_color,
                           bg=clock.background_color)

    clock.update_settings()
    current_time.after(clock.update_ms, tick)


# TKInterface
root = Tk()
root.title(clock.window_title)

# Binds 'Esc' key to exit program
root.bind('<Escape>', exit)

# Runs program in full-screen
if clock.full_screen:
    root.attributes('-fullscreen', True)
    root.config(cursor='none')

# Creates container to hold time and date
container = Frame(root)
current_time = Label(container)
current_date = Label(container)

container.pack(expand=True)
current_time.pack()
current_date.pack()

tick()
root.mainloop()
