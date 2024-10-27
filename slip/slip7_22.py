from tkinter import*
from random import*
from string import*

def show():
    pas=""
    for i in range(0,8):
        pas+=choice(ascii_letters)
        t1.insert(0,pas)

window=Tk()
window.geometry("300x300")

l1=Label(window,text="Random Password")
t1=Entry(window)
b1=Button(window,text="click",command=show)

t1.grid(row=0,column=1)
l1.grid(row=0,column=0)
b1.grid(row=2,column=1)

        
