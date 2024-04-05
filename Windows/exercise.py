import tkinter as tk
import ttkbootstrap as ttk


def print_out():
    entry_text =  entry_var.get()
    str_entry.set(entry_text)


window = ttk.Window(themename="journal")
window.title("Exercise Window")
window.geometry("320x350")
wind_frame = ttk.Frame(master=window)
wind_frame.pack()

entry_var = tk.StringVar()
entry = ttk.Entry(master=wind_frame, textvariable=entry_var)
entry.pack(pady=10)

str_entry = tk.StringVar()

output_label = ttk.Label(master=wind_frame, text="Output text", textvariable=str_entry, font="Sans-serif 20 bold")
output_label.pack(pady=5)

button = ttk.Button(master=wind_frame, text="Say it", command=print_out)
button.pack(pady=5)

window.mainloop()

