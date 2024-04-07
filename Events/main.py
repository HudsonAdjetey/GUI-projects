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

# events
window.bind("<Alt-a>", lambda event: print("An event"))
window.bind("<Alt-KeyPress-a>", lambda e: print(e))

window.mainloop()
