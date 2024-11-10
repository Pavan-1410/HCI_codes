import tkinter as tk
from tkinter import colorchooser

# Initialize main window
root = tk.Tk()
root.title("Whiteboard Application")
root.geometry("800x600")
root.configure(bg="white")

# Global variables for color and brush size
brush_color = "black"
brush_size = 5

# Function to update brush color
def change_color():
    global brush_color
    color = colorchooser.askcolor()[1]  # Open color chooser and get hex color
    if color:
        brush_color = color

# Function to update brush size
def change_brush_size(new_size):
    global brush_size
    brush_size = new_size

# Function to clear the canvas
def clear_canvas():
    canvas.delete("all")

# Draw function
def paint(event):
    x1, y1 = (event.x - brush_size), (event.y - brush_size)
    x2, y2 = (event.x + brush_size), (event.y + brush_size)
    canvas.create_oval(x1, y1, x2, y2, fill=brush_color, outline=brush_color)

# Create a canvas for drawing
canvas = tk.Canvas(root, bg="white", width=700, height=500)
canvas.pack(pady=20)

# Bind the canvas to the paint function
canvas.bind("<B1-Motion>", paint)

# Create a frame for controls
controls_frame = tk.Frame(root, bg="white")
controls_frame.pack()

# Color button
color_button = tk.Button(controls_frame, text="Choose Color", command=change_color)
color_button.grid(row=0, column=0, padx=10)

# Brush size buttons
brush_size_label = tk.Label(controls_frame, text="Brush Size:")
brush_size_label.grid(row=0, column=1, padx=10)

brush_sizes = [5, 10, 15, 20]
for i, size in enumerate(brush_sizes):
    size_button = tk.Button(controls_frame, text=str(size), command=lambda s=size: change_brush_size(s))
    size_button.grid(row=0, column=2+i, padx=5)

# Clear button
clear_button = tk.Button(controls_frame, text="Clear Canvas", command=clear_canvas)
clear_button.grid(row=0, column=len(brush_sizes)+2, padx=10)

# Run the application
root.mainloop()
