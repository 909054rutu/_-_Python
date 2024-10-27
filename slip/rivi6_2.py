 #Write Python GUI program to create background with changing colors

from tkinter import*

def show():
   l1.config(bg="red",font=("Arial",60))

def show1():
   l1.config(bg="pink",font=("bold",40))

def show2():
   l1.config(bg="yellow")

window=Tk()
window.geometry("400x500")
l1=Label(window,text="Welcome")
r1=Radiobutton(window,text="pink",value=1,command=show)
r2=Radiobutton(window,text="red",value=2,command=show1)
r3=Radiobutton(window,text="red",value=3,command=show2)

l1.grid(row=0,column=0)
r1.grid(row=1,column=0)
r2.grid(row=2,column=0)
r3.grid(row=3,column=0)

window.mainloop()

