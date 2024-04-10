import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Combo and Spin")
window.geometry("600x400")

# combo box
items = ["Ice cream", "Pizza", "Brocolli"]
combo_var = tk.StringVar(value=items[0])
combo = ttk.Combobox(master=window, textvariable=combo_var)
# combo["values"] = items
combo.configure(values=items)
combo.pack()
# event
combo.bind("<<ComboboxSelected>>", lambda e: combo_label.configure(text=f'Selected Food: {combo_var.get()}'))

combo_label = ttk.Label(master=window,  text="selected")
combo_label.pack()

window.mainloop()
