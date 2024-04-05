import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.title("Text variable")



str_var = tk.StringVar()

label = ttk.Label(master=window, text="Dummy", textvariable=str_var)
label.pack(pady=10)
entry = ttk.Entry(master=window, textvariable=str_var)
entry.pack()

window.mainloop()