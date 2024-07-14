import tkinter
window =tkinter.Tk()
window.geometry("500x300")
l1=tkinter.Label(window,text="Enter Number1")
l1.grid(row=0,column=0)
t1=tkinter.Entry(window)
t1.grid(row=0,column=1)
l2=tkinter.Label(window,text="Enter Number2")
l2.grid(row=1,column=0)
t2=tkinter.Entry(window)
t2.grid(row=1,column=1)

b1=tkinter.Button(window,text="ok")#,bg="pink")
b1.grid(row=2,column=0)
b2=tkinter.Button(window,text="Exit")#,bg="purple")
b2.grid(row=2,column=1)


c1=tkinter.Checkbutton(window,text="java")
c1.grid(row=3,column=0)
c2=tkinter.Checkbutton(window,text="php")
c2.grid(row=3,column=1)

r1=tkinter.Radiobutton(window,text="male")
r1.grid(row=4,column=0)
r2=tkinter.Radiobutton(window,text="female")
r2.grid(row=4,column=1)
window.mainloop()
