import tkinter as tk

window = tk.Tk()
window.title("Canvas")
window.geometry("600x400")

canvas = tk.Canvas(master=window, bg="white")
canvas.pack()

# canvas.create_rectangle((100, 50, 100, 200), fill ="red", width=10, dash=(1, 1))
# canvas.create_line(10,24, 100, 150)
# canvas.create_oval((0, 100, 100, 200), fill="green")
# canvas.create_polygon((0, 0, 100, 200, 300, 50))
# canvas.create_arc((200, 0, 300, 100))
#
# canvas.create_window((100, 100), window = tk.Label(window, text="this is a canvas"))
def draw_on_canvas(event):
    x = event.x
    y = event.y
    canvas.create_oval((x- brush_size /2, y-brush_size / 2, x + brush_size / 2, y + brush_size / 2), fill='black')


def adjust_brush(event):
    global brush_size
    if event.delta > 0:
        brush_size +=4
    else:
        brush_size -=4
    brush_size = min(brush_size, 50)


brush_size = 4



canvas.bind("<Motion>", lambda  e: draw_on_canvas(e))
canvas.bind("<MouseWheel>", lambda  e: adjust_brush(e))

window.mainloop()

