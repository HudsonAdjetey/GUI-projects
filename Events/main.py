import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("600x500")
window.title("Event Binding")

text = tk.Text(master=window)
text.pack()

entry = ttk.Entry(master=window)
entry.pack()

btn = ttk.Button(master=window, text="Dum Button")
btn.pack()

window.mainloop()
