from PIL import Image, ImageTk

def render_realistic(event, tool, realistic_canvas):
    # Ensure realistic_canvas has an images list
    if not hasattr(realistic_canvas, "images"):
        realistic_canvas.images = []

    # Texture mapping for tools
    texture_map = {
        "special_land": "assets/realistic_textures/land.jpg",
        "special_water": "assets/realistic_textures/water.jpg",
    }

    # Get the texture for the current tool
    texture = texture_map.get(tool)

    if texture:
        try:
            x, y = event.x, event.y  # Coordinates of the event

            # Load and resize the image
            img = Image.open(texture).resize((50, 50))  # Adjust size dynamically if needed
            photo = ImageTk.PhotoImage(img)

            # Create image on the canvas
            realistic_canvas.create_image(x, y, image=photo, anchor="center")

            # Store reference to the PhotoImage object
            realistic_canvas.images.append(photo)
        except Exception as e:
            print(f"Error rendering image: {e}")
