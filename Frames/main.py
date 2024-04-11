import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Frame and parenting")
window.geometry("600x400")

# frame
frame = ttk.Frame(master=window, width=400, height=90, borderwidth=20, relief=tk.RIDGE)
frame.pack_propagate(False)
frame.pack(side=tk.LEFT)



# PARENTING
label = ttk.Label(master=frame, text="Label in frame")
label.pack()

button = ttk.Button(master=frame, text="Label in Frame")
button.pack()

label_outside = ttk.Label(master=window, text="Label outside the frame")
label_outside.pack()

window.mainloop()