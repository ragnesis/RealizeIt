from PIL import Image
import os

def save_canvas(canvas, filename):
    try:
        temp_file = "temp.ps"
        canvas.postscript(file=temp_file, colormode='color')  # Save canvas as PostScript
        img = Image.open(temp_file)
        img.save(filename)
    except Exception as e:
        print(f"Error saving canvas: {e}")
    finally:
        if os.path.exists(temp_file):
            os.remove(temp_file)

def save_all(drawing_canvas, realistic_canvas):
    save_canvas(drawing_canvas, "drawing_board.png")
    save_canvas(realistic_canvas, "realistic_output.png")
