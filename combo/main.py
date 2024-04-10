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

# SPINBOX
spin_int = tk.IntVar(value=3)
spin = ttk.Spinbox(master=window, from_=2, to=90, increment=3, command= lambda : print("Hello message from here"))
spin.bind("<<Increment>>", lambda e: print("Increment"))
spin.bind("<<Decrement>>", lambda e: print("Decrement"))
string_letter = tk.StringVar()
spin_letters = ttk.Spinbox(master=window, values=("A","B", "C", "D", "E"), textvariable=string_letter)
spin_letters.bind("<<Decrement>>", lambda e: print(string_letter.get()))

spin_letters.pack()


# spin["values"] = (1,2,3,4,6)
spin.pack()

window.mainloop()
