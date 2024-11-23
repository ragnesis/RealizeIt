import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from utils.rendering import render_realistic
from utils.save_utils import save_canvas

# Initialize the main app window
root = tk.Tk()
root.title("Creative Drawing App")
root.geometry("1200x700")

# Global variables for tools and canvas
pen_color = "black"
pen_size = 5
selected_tool = "pen"

# Create frames for toolbox, drawing board, and realistic rendering
toolbox_frame = tk.Frame(root, width=200, bg="lightgray")
toolbox_frame.pack(side=tk.LEFT, fill=tk.Y)

drawing_board_frame = tk.Frame(root, bg="white", width=500, height=700)
drawing_board_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

realistic_canvas_frame = tk.Frame(root, bg="black", width=500)
realistic_canvas_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Drawing board canvas
drawing_canvas = tk.Canvas(drawing_board_frame, bg="white", width=500, height=700)
drawing_canvas.pack(fill=tk.BOTH, expand=True)

# Realistic rendering canvas
realistic_canvas = tk.Canvas(realistic_canvas_frame, bg="white", width=500, height=700)
realistic_canvas.pack(fill=tk.BOTH, expand=True)

# Function to handle pen drawing
def start_drawing(event):
    drawing_canvas.old_x, drawing_canvas.old_y = event.x, event.y

def draw(event):
    global selected_tool, pen_color, pen_size
    x, y = event.x, event.y
    if selected_tool == "pen" or selected_tool.startswith("special"):
        drawing_canvas.create_line(
            drawing_canvas.old_x, drawing_canvas.old_y, x, y,
            width=pen_size, fill=pen_color, capstyle=tk.ROUND
        )
        drawing_canvas.old_x, drawing_canvas.old_y = x, y
        render_realistic(event, selected_tool, realistic_canvas)

def clear_canvas():
    drawing_canvas.delete("all")
    realistic_canvas.delete("all")

# Bind drawing events
drawing_canvas.bind("<Button-1>", start_drawing)
drawing_canvas.bind("<B1-Motion>", draw)

# Quit app function
def quit_app():
    if messagebox.askyesno("Exit", "Are you sure you want to quit?"):
        root.destroy()

# Add buttons to toolbox
def create_tool_button(name, color, tool_type):
    btn = tk.Button(
        toolbox_frame, text=name, bg=color, command=lambda: set_tool(tool_type)
    )
    btn.pack(pady=5, padx=5, fill=tk.X)

def set_tool(tool):
    global selected_tool, pen_color
    selected_tool = tool
    if tool == "pen":
        pen_color = "black"
    elif tool == "eraser":
        pen_color = "white"
    else:
        pen_color = "blue"  # Default for special tools

create_tool_button("Black Pen", "black", "pen")
create_tool_button("Eraser", "white", "eraser")
create_tool_button("Land Brush", "green", "special_land")
create_tool_button("Water Brush", "blue", "special_water")
tk.Button(toolbox_frame, text="Clear All", bg="red", command=clear_canvas).pack(pady=10)
tk.Button(toolbox_frame, text="Quit", bg="gray", command=quit_app).pack(pady=10)

# Run the application
root.mainloop()
