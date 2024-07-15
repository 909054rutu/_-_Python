#import tkinter as +
from tkinter import *
def disp_square():
    n=t1.get()
    n=int(n)
    s=n*n
    t2.insert(0,s)
    
window=Tk()
window.geometry("500x300")
l1=Label(window,text="Enter Number")
l2=Label(window,text="Result")
t1=Entry(window,width="10")
t2=Entry(window,width="10")
b1=Button(window,text="square",command=disp_square)
l1.grid(row=0,column=0)
l2.grid(row=1,column=0)
t1.grid(row=0,column=1)
t2.grid(row=1,column=1)
b1.grid(row=5,column=1)
window.mainloop()
