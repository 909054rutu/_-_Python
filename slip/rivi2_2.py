#B) Write Python GUI program to create a digital clock with Tkinter to display the time.

import tkinter as tk
from tkinter import Label
import time

window=tk.Tk()
window.geometry("300x400")

l1=Label(window,font=("Arial","20"),bg="black",fg="white")
l1.grid(row=5,column=1)

def cal_time():
    current_time=time.strftime("%H-%M-%S")
    l1.config(text=current_time)
    window.after(1000,cal_time)

cal_time()
window.mainloop()


