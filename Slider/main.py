import tkinter as tk
from tkinter import  ttk
from tkinter import  scrolledtext


window = tk.Tk()
window.title("Sliders")

# slider
scale_int = tk.DoubleVar(value=15)
scale = ttk.Scale(master=window,
                  command= lambda e: print(scale_int.get()),
                  from_= 0, to=30,
                  length=300,
                  orient="vertical",
                  variable=scale_int
                  )

scale.pack()

# progress bar
progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(master=window, length=300, variable=scale_int, maximum=30, mode="indeterminate")
progress_bar.pack()

# progress_bar.start(100)


# scrolled text
scrolled_text = scrolledtext.ScrolledText(master=window, height=5)
scrolled_text.pack()

aut_var = tk.IntVar()
auto_start = ttk.Progressbar(window, length=300, variable=aut_var, maximum=30, orient="vertical")
auto_start.pack()

aut_slider = ttk.Scale(window, from_=0, to=30, length=300, variable=aut_var, command= lambda e: auto_start.stop())
aut_slider.pack()
label_progress = ttk.Label(window, text="0", textvariable=aut_var )
label_progress.pack()

auto_start.start()

if aut_var == 30:
    auto_start.stop()

window.mainloop()
