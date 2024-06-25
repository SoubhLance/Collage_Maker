import tkinter as tk
from tkinter import filedialog
from PIL import Image

# Function to open file dialog and return selected file path
def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    return file_path

# Initialize tkinter
root = tk.Tk()
root.withdraw()  # Hide the main tkinter window

# List to store images
images = []

# Open file dialog for each image and resize them
for _ in range(5):
    file_path = open_image()
    if file_path:
        image = Image.open(file_path)
        image = image.resize((500, 500))
        images.append(image)
    else:
        break

# Create a new collage image
collage = Image.new("RGBA", (1500, 1500), color="black")

# Paste images onto the collage
positions = [(0, 0), (500, 500), (1000, 0), (0, 1000), (1000, 1000)]
for img, pos in zip(images, positions):
    collage.paste(img, pos)

# Save the collage image
collage.save("Photo_Collage.png")

# Inform user that collage has been saved
print("Photo collage saved as Photo_Collage.png")

# Close tkinter GUI
root.destroy()
