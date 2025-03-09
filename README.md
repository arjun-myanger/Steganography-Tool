# 🛠️ Steganography Tool

This Steganography Tool allows users to **hide secret messages** within image files and **retrieve them** when needed. Steganography is the practice of **concealing information** within another medium to prevent detection, making it useful for secure communication.

---

## ✨ Features

- 🔹 **Embed Messages:** Hide secret text within image files without noticeable changes.
- 🔹 **Extract Messages:** Retrieve hidden messages from steganographic images.
- 🔹 **User-Friendly Interface:** Simple GUI for seamless interaction.
- 🔹 **Command-Line Support:** Use the **CLI version** (`steganography.py`) for a terminal-based experience.
- 🔹 **Lightweight & Fast:** Efficiently processes images without significant performance impact.

---

## 📥 Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/arjun-myanger/Steganography-Tool.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd Steganography-Tool
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   This will install all necessary Python packages listed in `requirements.txt`.

---

## 🚀 Usage

You can use this tool in **two modes**: **GUI** or **Command-Line Interface (CLI)**.

### 🖥️ GUI Mode
To launch the **Steganography Tool GUI**, run:
```bash
python steganography_gui.py
```

### 🔲 CLI Mode
For a terminal-based experience, use:
```bash
python steganography.py
```

---

### 🔏 Hiding a Message:
1. **Select an image** as the cover.
2. **Enter your secret message** in the text input field (GUI) or via CLI prompt.
3. **Save the modified image** containing the hidden message.

### 🔎 Retrieving a Message:
1. **Open an image file** that contains a hidden message.
2. The tool will **extract and display** the secret message.

---

## 📦 Dependencies

This tool requires the following Python libraries:
- 🖼️ `Pillow` – for image processing.
- 🖥️ `tkinter` – for GUI functionality.

All dependencies are listed in `requirements.txt` and can be installed using the command above.

---

## 📜 License

This project is licensed under the **MIT License**. See the `LICENSE` file for more details.

---

## 🙌 Acknowledgements

This tool is inspired by various steganography techniques and tools in the open-source community. Special thanks to contributors who have helped advance the field of secure communication.

📢 **Disclaimer:** This tool should be used responsibly and ethically. Ensure you have the right to hide and extract information within the images you use.