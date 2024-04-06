# Create another check button and 2 radio buttons
# radio Button:
#  Values for the buttons are A and B
#   ticking either prints the value of the check button
#   Ticking the radio button unlocks the checkbutton
#
# Check button
#   ticking the checkbutton prints the value of the radio button value
# use tkinter var for booleans

import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Exercise")
window.geometry("300x200")

radio_var = tk.StringVar()
check_var = tk.BooleanVar(value=False)
check_button = ttk.Checkbutton(master=window, text="check", variable=check_var, onvalue=True, offvalue=False, command = lambda : print(radio_var.get()))
check_button.pack()

radio1 = ttk.Radiobutton(master=window, text="Radio 1", variable=radio_var, value=1, command=lambda : print(check_var.get()))
radio1.pack()

radio2 = ttk.Radiobutton(master=window,text="Radio 2", variable=radio_var, value=2, command = lambda : print(check_var.get()))
radio2.pack()

window.mainloop()