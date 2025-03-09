import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image
import numpy as np


# Function to convert text to binary
def text_to_binary(text):
    return "".join(format(ord(char), "08b") for char in text)


# Function to convert binary back to text
def binary_to_text(binary):
    chars = [binary[i : i + 8] for i in range(0, len(binary), 8)]
    return "".join(chr(int(char, 2)) for char in chars)


# Function to hide text in an image
def hide_text():
    image_path = filedialog.askopenfilename(
        title="Select an Image", filetypes=[("PNG Images", "*.png")]
    )
    if not image_path:
        return

    secret_text = text_entry.get("1.0", tk.END).strip()
    if not secret_text:
        messagebox.showwarning("Warning", "Please enter text to hide.")
        return

    binary_secret = text_to_binary(secret_text) + "1111111111111110"  # End marker

    img = Image.open(image_path).convert("RGB")
    pixels = np.array(img, dtype=np.uint8)

    binary_index = 0
    for row in pixels:
        for pixel in row:
            for color in range(3):
                if binary_index < len(binary_secret):
                    pixel[color] = np.uint8(
                        (int(pixel[color]) & ~1) | int(binary_secret[binary_index])
                    )
                    binary_index += 1

    encoded_img = Image.fromarray(pixels)

    output_path = filedialog.asksaveasfilename(
        defaultextension=".png", filetypes=[("PNG Images", "*.png")]
    )
    if output_path:
        encoded_img.save(output_path)
        messagebox.showinfo("Success", f"✅ Secret message hidden in {output_path}")


# Function to extract text from an image
def extract_text():
    image_path = filedialog.askopenfilename(
        title="Select an Image", filetypes=[("PNG Images", "*.png")]
    )
    if not image_path:
        return

    img = Image.open(image_path).convert("RGB")
    pixels = np.array(img, dtype=np.uint8)

    binary_data = ""
    for row in pixels:
        for pixel in row:
            for color in range(3):
                binary_data += str(pixel[color] & 1)

    end_marker = "1111111111111110"
    if end_marker in binary_data:
        binary_data = binary_data[: binary_data.index(end_marker)]
        secret_text = binary_to_text(binary_data)
        messagebox.showinfo("Hidden Message", f"🔓 Extracted Message: {secret_text}")
    else:
        messagebox.showwarning("No Hidden Text", "⚠️ No hidden message found.")


# Function to center the window
def center_window(win, width=400, height=300):
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    win.geometry(f"{width}x{height}+{int(x)}+{int(y)}")


# Create GUI window
root = tk.Tk()
root.title("Steganography Tool 🖼️🔐")
root.resizable(False, False)  # Disable window resizing

# Apply a modern theme
style = ttk.Style()
style.theme_use("clam")  # Try "alt", "vista", or "clam"

# Center the window
center_window(root)

# Frame for padding
frame = ttk.Frame(root, padding=15)
frame.pack(fill="both", expand=True)

# Label
label = ttk.Label(frame, text="Enter text to hide:", font=("Arial", 12))
label.pack(pady=5)

# Text entry box
text_entry = tk.Text(frame, height=4, width=40, font=("Arial", 10))
text_entry.pack(pady=5)

# Buttons
hide_button = ttk.Button(frame, text="🔒 Hide Text in Image", command=hide_text)
hide_button.pack(pady=5, fill="x")

extract_button = ttk.Button(
    frame, text="🔍 Extract Text from Image", command=extract_text
)
extract_button.pack(pady=5, fill="x")

exit_button = ttk.Button(frame, text="❌ Exit", command=root.quit)
exit_button.pack(pady=10, fill="x")

# Run the GUI event loop
root.mainloop()
