import tkinter as tk
from tkinter import Label
import time

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Define the clock display label
clock_label = Label(root, font=("Arial", 50), bg="black", fg="white")
clock_label.pack(anchor='center')

# Function to update the time
def update_clock():
    current_time = time.strftime("%H:%M:%S")  # Get the current time in hours:minutes:seconds format
    clock_label.config(text=current_time)      # Update the label with the current time
    root.after(1000, update_clock)             # Refresh the time every second (1000 milliseconds)

# Start the clock update
update_clock()

# Run the application
root.mainloop()
