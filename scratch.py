import tkinter as tk

print("start")
win = tk.Tk()
canvas = tk.Canvas(win, bg="black", width=420, height=420)
canvas.create_oval((100,100), (200,200), fill="pink")
canvas.create_line((100,120), (330,310), fill="white")
canvas.pack()
win.mainloop()
