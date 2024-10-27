#B) Write Python GUI program to create a digital clock with Tkinter to display the time.

from tkinter import*
from tkinter import Label
import time

window=Tk()
window.geometry("400x500")

l1=Label(window,font=("gigi",200),bg="black",fg="white")
l1.pack(pady=10)

def show():
    current=time.strftime("%H-%M-%S")
    l1.config(text=current)
    window.after(1000,show)

show()
window.mainloop()
