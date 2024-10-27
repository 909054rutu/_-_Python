import tkinter as tk
from tkinter import Label
import time

window=tk.Tk()
window.title("Digital Clock")

clock_label=Label(window,font=("gigi",30),bg="pink",fg="black")
clock_label.pack(pady="10")

def update_time():
    current_time=time.strftime("%H-%M-%S")
    clock_label.config(text=current_time)
    window.after(1000,update_time)

update_time()
window.mainloop()
