import tkinter as tk

window = tk.Tk()
window.title("Canvas")
window.geometry("600x400")

canvas = tk.Canvas(master=window, bg="white")
canvas.pack()

canvas.create_rectangle((0, 0, ))

window.mainloop()

