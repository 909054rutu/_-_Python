#B) Write Python GUI program to take accept your birthdate and output your age when a
#button is pressed.

from tkinter import*
from tkinter import messagebox
from datetime import datetime
def show():
    try:
        birthdate=t1.get()
        birthdate=datetime.strptime(birthdate,'%Y-%m-%d')
        today=datetime.today()
        age=today.year-birthdate.year-((today.month,today.day)<(birthdate.month,birthdate.day))
        messagebox.showinfo("Age",f"You are {age} years old")
    except ValueError:
        messagebox.showinfo("Age","Invalid age")

window=Tk()
window.geometry("300x400")
l1=Label(window,text="Enter Birthdate yyyy-mm-dd")
l1.pack(pady=10)
t1=Entry(window)
t1.pack(pady=10)
b1=Button(window,text="show",command=show)
b1.pack(pady=10)

window.mainloop()
        
    
