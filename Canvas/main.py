import tkinter as tk

window = tk.Tk()
window.title("Canvas")
window.geometry("600x400")

canvas = tk.Canvas(master=window, bg="white")
canvas.pack()

canvas.create_rectangle((100, 50, 100, 200), fill ="red", width=10, dash=(1, 1))
canvas.create_line(10,24, 100, 150)
canvas.create_oval((0, 100, 100, 200), fill="green")
canvas.create_polygon((0, 0, 100, 200, 300, 50))
canvas.create_arc((200, 0, 300, 100))
window.mainloop()

