from tkinter import*



def show():
    window.config(bg="pink")

def show1():
    window.config(bg="red")

    
window=Tk()
window.geometry("300x400")
menubar=Menu(window)
color=Menu(menubar)
color.add_command(label="pink",command=show)
color.add_command(label="red",command=show1)
menubar.add_cascade(label="color",menu=color)

window.config(menu=menubar)
window.mainloop()

