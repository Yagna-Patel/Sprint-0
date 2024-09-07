import tkinter as tk

def on_checkbox_toggle():
    if checkbox_var.get():
        label.config(text="Checkbox is checked!")
    else:
        label.config(text="Checkbox is unchecked!")

def on_radio_select():
    selected_value = radio_var.get()
    label.config(text=f"Selected radio button: {selected_value}")

# main window
root = tk.Tk()
root.title("Simple Tkinter GUI")

# label / text
label = tk.Label(root, text="Welcome to the GUI!")
label.pack(pady=10)

# checkbox
checkbox_var = tk.BooleanVar()
checkbox = tk.Checkbutton(root, text="Check me!", variable=checkbox_var, command=on_checkbox_toggle)
checkbox.pack(pady=10)

# radio buttons
radio_var = tk.StringVar(value="Option 1")
radio1 = tk.Radiobutton(root, text="Option 1", variable=radio_var, value="Option 1", command=on_radio_select)
radio2 = tk.Radiobutton(root, text="Option 2", variable=radio_var, value="Option 2", command=on_radio_select)
radio1.pack(pady=5)
radio2.pack(pady=5)

# place for tictactoe grid
canvas_size = 300
grid_size = 3
line_width = 2

line_canvas = tk.Canvas(root, width=canvas_size, height=canvas_size, bg="white")
line_canvas.pack(pady=10)

# the ttt grid
for i in range(1, grid_size):
    # straight lines
    line_canvas.create_line(i * canvas_size / grid_size, 0, i * canvas_size / grid_size, canvas_size, fill="black", width=line_width)
    # side lines
    line_canvas.create_line(0, i * canvas_size / grid_size, canvas_size, i * canvas_size / grid_size, fill="black", width=line_width)
line_canvas.pack(pady=10)

root.mainloop()