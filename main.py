
import tkinter as tk
import random

window = tk.Tk()
window.title("Sorting")

canvas = tk.Canvas(window, width = 1200, height = 700)
canvas.pack()

top_x = 50
top_y = 400
bot_x = 55
bot_y = 650

offset = 22

arr = []

for x in range(50):
    arr.append(random.randint(0,100))
               
# rectange(topleft x, topleft y, bottomright x, bottomright y)

for i, x in enumerate(arr):
    rect = canvas.create_rectangle(top_x + offset, top_y, bot_x + offset, bot_y, fill = "black")


window.mainloop()





def main():
    pass
