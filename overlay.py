import tkinter as tk
from tkinter import Menu, messagebox, ttk
from pathlib import Path
import os


rect_color = "#ffcccb"
config_path = str(Path.home() / 'Documents') + r"/RMBestFriend/Configs/"

def center_window(window, min_width, min_height):
    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate the x and y coordinates for centering
    x = (screen_width - min_width) // 2
    y = (screen_height - min_height) // 2

    # Set the window's geometry to center it on the screen
    window.geometry(f"{min_width}x{min_height}+{x}+{y}")


def save_coordinates(cor_x, cor_y, e_x, e_y):
    if not os.path.exists(config_path):
        os.makedirs(config_path)

    with open(config_path + r"/coordinates.txt", "w") as file:
        file.write(f"Start X: {cor_x}\n")
        file.write(f"Start Y: {cor_y}\n")
        file.write(f"End X: {e_x}\n")
        file.write(f"End Y: {e_y}\n")


def load_coordinates():
    try:
        with open(config_path + r"/coordinates.txt", "r") as file:
            lines = file.readlines()
            cor_x = float(lines[0].split(":")[1].strip())
            cor_y = float(lines[1].split(":")[1].strip())
            e_x = float(lines[2].split(":")[1].strip())
            e_y = float(lines[3].split(":")[1].strip())

            return cor_x, cor_y, e_x, e_y
    except FileNotFoundError:
        return None, None, None, None


root = tk.Tk()
root.title("RM Best Friend")
root.attributes("-alpha", 0.75)
root.attributes("-topmost", True)
#root.iconbitmap("icon.ico")
root.state("zoomed")

frame = tk.Frame(root)
frame.pack(side=tk.LEFT, fill=tk.Y)

# Define a bold font
bold_font = ("Arial", 12, "bold")

# Create three labels
label1 = tk.Label(frame, text="HP Detection: -", width=15, font=bold_font, anchor="w")
label2 = tk.Label(frame, text="Buffer: -", width=15, font=bold_font, anchor="w")
label3 = tk.Label(frame, text="GT Buffer: -", width=15, font=bold_font, anchor="w")

# Pack the labels to display them in the window
label1.pack(side=tk.TOP)
label2.pack(side=tk.TOP)
label3.pack(side=tk.TOP)

menu_bar = Menu(root)
root.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Menu", menu=file_menu)
#file_menu.add_command(label="Keys setup", command=keys_setup_window)
canvas = tk.Canvas(root, cursor="cross")
canvas.pack(fill=tk.BOTH, expand=True)

rect = None

(start_x, start_y, end_x, end_y) = load_coordinates()

# canvas.bind("<ButtonPress-1>", on_press)
# canvas.bind("<B1-Motion>", on_drag)
# canvas.bind("<ButtonRelease-1>", on_release)

if start_x:
    rect = canvas.create_rectangle(start_x,
                                   start_y,
                                   end_x,
                                   end_y,
                                   fill=rect_color)

root.mainloop()