import tkinter as tk

def add_tooltip(widget, text):
    tooltip = tk.Label(
        widget, text=text, bg="yellow", fg="black", relief=tk.SOLID, borderwidth=1
    )
    tooltip.place_forget()  # Ensure it's hidden initially

    def on_enter(event):
        tooltip.place(x=widget.winfo_rootx() - widget.winfo_toplevel().winfo_rootx() + event.x + 10,
                      y=widget.winfo_rooty() - widget.winfo_toplevel().winfo_rooty() + event.y + 10)

    def on_leave(event):
        tooltip.place_forget()

    widget.bind("<Enter>", on_enter)
    widget.bind("<Leave>", on_leave)
