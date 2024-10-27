from tkinter import*

def change1():
    l1.config(font=('Gigi',30))

def change2():
    l1.config(font=('Gigi',20,'bold'))

def change3():
    l1.config(font=('Gigi',20,'italic'))


window=Tk()
window.geometry("300x300")

l1=Label(window,text="welcome")
c1=Checkbutton(window,text='gigi',command=change1)
c2=Checkbutton(window,text='bold',command=change2)
c3=Checkbutton(window,text='italic',command=change3)

l1.grid(row=0,column=0)
c1.grid(row=1,column=0)
c2.grid(row=2,column=0)
c3.grid(row=3,column=0)

window.mainloop()

