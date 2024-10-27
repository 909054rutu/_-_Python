import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def cal_age():
    try:
        birthdate=entry.get()
        birthdate=datetime.strptime(birthdate,"%Y-%m-%d")
        today=datetime.today()
        age=today.year-birthdate.year-((today.month,today.day)<(birthdate.month,birthdate.day))
        messagebox.showinfo("Age",f"You are {age} years old")
    except ValueError:
        messagebox.errorinfo("Invalid Age","Please enter valid")

window=tk.Tk()
window.title("Age Calculator")

label=tk.Label(window,text="Enter Your BirthDate YYYY-MM-DD")
label.pack(pady=10)

entry=tk.Entry(window)
entry.pack(pady=10)

button=tk.Button(window,text="calculate",command=cal_age)
button.pack(pady=10)

window.mainloop()
