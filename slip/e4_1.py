#A) Write Python GUI program to create background with changing colors

from tkinter import*

def show():
    l1.config(font=("gigi",200),bg="red")

def show2():
    l1.config(font=("gigi",200,'bold'),bg="pink")

def show3():
    l1.config(font=("italic",200),bg="yellow")

window=Tk()
window.geometry("400x500")

l1=Label(window,text="Shree Swami Samarth")
l1.pack(pady=10)

r1=Checkbutton(window,text="red",command=show)
r1.pack(pady=10)

r2=Checkbutton(window,text="green",command=show2)
r2.pack(pady=10)

r3=Checkbutton(window,text="yellow",command=show3)
r3.pack(pady=10)

window.mainloop()
