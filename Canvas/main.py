import tkinter as tk

window = tk.Tk()
window.title("Canvas")
window.geometry("600x400")

canvas = tk.Canvas(master=window, bg="white")
canvas.pack()

canvas.create_rectangle((100, 50, 100, 200), fill ="red", width=10, dash=(1, 1))
canvas.create_line(start_x,start_y, end_x, end_y)
window.mainloop()

