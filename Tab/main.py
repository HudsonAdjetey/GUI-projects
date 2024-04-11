import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Tab Widget")
window.geometry("600x400")


# NOTEBOOK WIDGET
notebook = ttk.Notebook(master=window)

# Tab
tab1 = ttk.Frame(master=notebook)
label1 = ttk.Label(master=tab1, text="Text in tab 1")
label1.pack()
tab2 = ttk.Frame(master=notebook)
label2 = ttk.Label(master=tab2, text="Text in tab 2")
label2.pack()

button1 = ttk.Button(master=tab1, text="Button 1")
button1.pack()

button2 = ttk.Button(master=tab2, text="Button 2")
button2.pack()

entry1 = ttk.Entry(master=tab1)
entry1.pack()

entry2 = ttk.Entry(master=tab2)
entry2.pack()

notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")
notebook.pack()

window.mainloop()