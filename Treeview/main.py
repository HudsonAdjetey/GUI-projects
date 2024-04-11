import tkinter as tk
from tkinter import ttk
from random import  choice


window = tk.Tk()

window.geometry("600x400")
window.title("Tree View")

# data
first_names = ["bob", "Maria", "Alex", "James", "Susan", "Henry", "Lisa", "Anna", "Linda"]
last_names = ["Smith", "Brown", "Wilson", "Thomson", "Cook","Taylor", "Walker", "Clark"]


tree_view = ttk.Treeview(master=window, columns=("First", "Last", "Email"), show="headings")
tree_view.heading(column="First", text="First Name")
tree_view.heading(column="Last", text="Last Name")
tree_view.heading(column="Email", text="Email")


tree_view.insert("", index=0, values=("Hobby", "Doe", "@johnDoes@gmail.com"))
for i in range(100):
    first_name = choice(first_names)
    last_name = choice(last_names)
    email = f"{str(first_name).lower()}{str(last_name).lower()}@example.com"
    tree_view.insert("", index=i, values=(first_name, last_name, email))

tree_view.pack(expand=True, fill="both")
window.mainloop()
