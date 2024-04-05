import tkinter as tk
from tkinter import ttk

def some_func():
    entry_value = entry.get()
    label.config(text=entry_value)
    # label["text"] = entry_value
    entry["state"] = "disabled"
    button.configure(state="disabled")
    print(entry.configure()) # To know all the configures

def enable_entry():
    label.configure(text="Dummy Text")
    entry.configure(state="enabled")
    entry.delete(0, tk.END)

    button.configure(state="enabled")

window = tk.Tk()
window.title("Getting data")

label = ttk.Label(master=window, text="Dummy Text")
label.pack()

entry = ttk.Entry(master=window)
entry.pack()
button = ttk.Button(master=window, text="Button Click", command=some_func)
button.pack()


button_enable = ttk.Button(master=window, text="Enable Entry", command=lambda :  enable_entry())
button_enable.pack(pady=15)

window.mainloop()
