import tkinter as tk
from time import strftime


def update_clock():
    current_time = strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_clock)


root = tk.Tk()
root.title("Digital Clock")
root.geometry("300x120")
root.resizable(False, False)

clock_label = tk.Label(
    root,
    font=("Arial", 40),
    background="black",
    foreground="lime",
)
clock_label.pack(expand=True, fill="both")

update_clock()
root.mainloop()
