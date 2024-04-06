import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.title("Buttons")
window.geometry("600x400")

def button_fnc():
    print("Hello")

button = ttk.Button(master=window, text="Dum Button", command=lambda : button_fnc())
button.pack()

# check button
def check_fnc():
    print(text_str.get())
    if text_str.get() == "checked":
        print("Hello")
    else:
        print("Say no to drugs")

text_str = tk.StringVar(value="unchecked")
check = ttk.Checkbutton(window, text="Check box",onvalue="checked", offvalue="unchecked", variable=text_str,command=lambda : check_fnc())
check.pack()

check2 = ttk.Checkbutton(master=window, text="Check box 2", command= lambda : print("test"))
check2.pack()
# radio buttons
radio_var = tk.StringVar()
radio1 = ttk.Radiobutton(window,
                         text="Radio Button 1",
                         value="radio 1",
                         variable=radio_var,
                         command=lambda: print(radio_var.get())

                         )
radio1.pack()
radio2 = ttk.Radiobutton(window,
                         text="Radio Button 2", value=2,
                         variable=radio_var,
                         command= lambda : print(radio_var.get())
                         )
radio2.pack()


window.mainloop()