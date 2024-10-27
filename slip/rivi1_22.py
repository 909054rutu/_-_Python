import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def cal_age():
    try:
        birthdate=t1.get()
        birthdate=datetime.strptime(birthdate,"%Y-%m-%d")
        today=datetime.today()
        age=today.year-birthdate.year-((today.month,today.day)<(birthdate.month,birthdate.day))
        messagebox.showinfo("Age",f"you are {age} years old")
    except ValueError:
        messagebox.showerror("Invalid","Enter valid")

window=tk.Tk()
window.geometry("400x500")

l1=tk.Label(window,text="Enter Date YYYY-MM-DD")
t1=tk.Entry(window)
b1=tk.Button(window,text="cal",command=cal_age)

l1.grid(row=0,column=0)
t1.grid(row=0,column=1)
b1.grid(row=1,column=1)

window.mainloop()
