import tkinter as tk
from tkinter import ttk


def get_pos(event):
    print(f'x{event.x}, y{event.y}')


window = tk.Tk()
window.geometry("600x500")
window.title("Event Binding")

text = tk.Text(master=window)
text.pack()

entry = ttk.Entry(master=window)
entry.pack()

btn = ttk.Button(master=window, text="Dum Button")
btn.pack()

text_label = ttk.Label(master=window, text= "text to be selected")
text_label.pack()
# events
# window.bind("<Alt-a>", lambda event: print("An event"))
# window.bind("<Alt-KeyPress-a>", lambda e: print(e))
# btn.bind('<Motion>', get_pos)
# window.bind("<KeyPress>", lambda e: print(e))

text.bind("<Shift-MouseWheel>", lambda e: print(e.state))

window.mainloop()
