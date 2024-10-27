from tkinter import*

def show():
    window.config(bg="pink")

def show2():
    window.config(bg="red")

window=Tk()
menubar=Menu(window)
color=Menu(menubar)
color.add_command(label="pink",command=show)
color.add_command(label="red",command=show2)
menubar.add_cascade(label="color",menu=color)

window.config(menu=menubar)
window.mainloop()
