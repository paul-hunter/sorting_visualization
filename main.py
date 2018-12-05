
import tkinter as tk
import random
import time

window = tk.Tk()
window.title("Sorting")

canvas = tk.Canvas(window, width = 1200, height = 700)
canvas.pack()

top_x = 50
bot_x = 55
bot_y = 650
max_height = 650

offset = 22

arr = []

def randomize(lst):
    lst.clear()
    for x in range(50):
        lst.append(random.randint(0,100))
        
    
##########  Quicksort ##########
    
def quicksort(arr, left, right):
    if (left < right):
        part_index = partition(arr, left, right)
        quicksort(arr, left, part_index-1)  # Recurse using left of partition
        quicksort(arr, part_index+1, right) # Recurse using right of partition

def partition(arr, left, right):
    pivot = arr[right]  # Choose last element of left...right as pivot
    i = left - 1
    for j in range(left, right):  # Iterate through element before right
        if (arr[j] <= pivot):
            i += 1
            # Swap arr[i] with arr[j]
            arr[i], arr[j] = arr[j], arr[i]
        
    # Swap arr[i+1] with the pivot
    # then everything to left of pivot is <= pivot
    # and everything to right of pivot is > pivot
    arr[i+1], arr[right] = arr[right], arr[i+1]
    draw_rects()
    return i + 1

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            draw_rects()

def left_click(event):
    canvas.delete("all")

def right_click(event):
    bubble_sort(arr)
    print(arr)

def draw_rects():
    canvas.delete("all")
    for i, height in enumerate(arr):
        rect = canvas.create_rectangle(top_x + i*offset, max_height-6*height, bot_x + i*offset, bot_y, fill = "black")
    
# rectange(topleft x, topleft y, bottomright x, bottomright y)

randomize(arr)

draw_rects()

print(arr)

window.bind("<Button-1>", left_click)
window.bind("<Button-3>", right_click)
        
window.mainloop()
