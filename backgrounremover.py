import os
from tkinter import filedialog
import tkinter as tk
from rembg import remove
from PIL import Image

def remove_background_and_save(input_image_path, output_image_path):
    # Open the input image
    with open(input_image_path, "rb") as f:
        input_image = f.read()

    # Remove the background
    output_image = remove(input_image)

    # Save the output image in the downloads folder
    with open(output_image_path, "wb") as f:
        f.write(output_image)

def select_file():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Get the path to the user's downloads directory
    downloads_dir = os.path.join(os.path.expanduser('~'), 'Downloads')

    # Prompt the user to select a file
    input_image_path = filedialog.askopenfilename()
    if input_image_path:
        # If a file is selected, proceed to remove the background
        output_image_path = os.path.join(downloads_dir, "output_image.png")  # Path to save the output image
        remove_background_and_save(input_image_path, output_image_path)
        print("Background removed and saved successfully!")

# Example usage:
select_file()
