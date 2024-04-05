import tkinter as tk
from tkinter import ttk

def btn_func():
    print("hello")
# create a window
window = tk.Tk()
window.title("Window and widgets")
window.geometry("800x500")

# create widgets - ttk label
label = ttk.Label(master=window, text="This is a test")
label.pack()

text_container = tk.Text(master=window)
text_container.pack()

entry = ttk.Entry(master=window)
entry.pack(pady=5 )

# wanting to call the fn directly specially when the func receives some params
button = ttk.Button(master=window, text="Add Caution", command=lambda : btn_func())
# button = ttk.Button(master=window, text="Add Caution", command=btn_func)
button.pack()

# run
window.mainloop()