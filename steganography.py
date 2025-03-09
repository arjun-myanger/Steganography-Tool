from PIL import Image
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox


def text_to_binary(text):
    """Convert text to binary"""
    return "".join(format(ord(char), "08b") for char in text)


def binary_to_text(binary):
    """Convert binary to text"""
    chars = [binary[i : i + 8] for i in range(0, len(binary), 8)]
    return "".join(chr(int(char, 2)) for char in chars)


def hide_text_in_image():
    """Hide a text message inside an image chosen via file dialog"""
    root = tk.Tk()
    root.withdraw()  # Hide main Tkinter window

    image_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("PNG Images", "*.png"), ("All Files", "*.*")],
    )
    if not image_path:
        messagebox.showwarning(
            "No Image Selected", "You must select an image to proceed!"
        )
        return

    secret_text = input("Enter the text to hide: ")
    binary_secret = text_to_binary(secret_text) + "1111111111111110"  # End marker

    img = Image.open(image_path)
    img = img.convert("RGB")
    pixels = np.array(img, dtype=np.uint8)  # Explicitly set dtype to uint8

    binary_index = 0
    for row in pixels:
        for pixel in row:
            for color in range(3):  # Modify R, G, B values
                if binary_index < len(binary_secret):
                    pixel[color] = np.uint8(
                        (int(pixel[color]) & ~1) | int(binary_secret[binary_index])
                    )  # Safe conversion
                    binary_index += 1

    encoded_img = Image.fromarray(pixels)

    # Ask user where to save the encoded image
    output_path = filedialog.asksaveasfilename(
        defaultextension=".png", filetypes=[("PNG Images", "*.png")]
    )
    if output_path:
        encoded_img.save(output_path)
        messagebox.showinfo("Success", f"✅ Secret message hidden in {output_path}")

    root.destroy()  # Close Tkinter


def extract_text_from_image():
    """Extract hidden text from an image chosen via file dialog"""
    root = tk.Tk()
    root.withdraw()

    image_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("PNG Images", "*.png"), ("All Files", "*.*")],
    )
    if not image_path:
        messagebox.showwarning(
            "No Image Selected", "You must select an image to proceed!"
        )
        return

    img = Image.open(image_path)
    img = img.convert("RGB")
    pixels = np.array(img, dtype=np.uint8)  # Explicitly set dtype

    binary_data = ""
    for row in pixels:
        for pixel in row:
            for color in range(3):  # Extract from R, G, B values
                binary_data += str(pixel[color] & 1)

    end_marker = "1111111111111110"
    if end_marker in binary_data:
        binary_data = binary_data[: binary_data.index(end_marker)]
        secret_text = binary_to_text(binary_data)
        messagebox.showinfo("Hidden Message", f"🔓 Extracted Message: {secret_text}")
    else:
        messagebox.showwarning("No Hidden Text", "⚠️ No hidden message found.")

    root.destroy()  # Close Tkinter


def main():
    print("\n🖼️ Steganography Tool: Hide & Extract Text in Images")
    print("1. Hide Text\n2. Extract Text\n3. Exit")

    while True:
        choice = input("\nChoose an option (1-3): ")

        if choice == "1":
            hide_text_in_image()

        elif choice == "2":
            extract_text_from_image()

        elif choice == "3":
            print("Exiting... 🔚")
            break

        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()
