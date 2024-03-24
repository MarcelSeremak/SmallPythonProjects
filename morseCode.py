import tkinter as tk
from tkinter import ttk

# All the letters and important characters and their versions in Morse Alphabet
morse_alphabet = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.',
    ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
    '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', " ": "  "}


# Function which changes text to morse code
def text_to_morsecode(text):
    morse_code = ""
    for char in text.upper():
        morse_code += morse_alphabet[char]
    return morse_code


def get_user_input():
    user_input = entry.get()
    morse = text_to_morsecode(user_input)
    root.destroy()
    result = tk.Tk()
    result.wm_minsize(400, 400)
    result.title("Result")
    label_widget = tk.Label(result, text="Result in Morse code", height=2, width=50)
    label_widget.pack(padx=20)
    text_widget = tk.Text(result, height=20, width=50)
    text_widget.insert("end", morse)
    text_widget.pack(padx=20, pady=20)
    result.mainloop()


# Create main window
root = tk.Tk()
root.title("Styled Input Window")

# Create a style for the window
style = ttk.Style()
style.theme_use('clam')
# Create and configure the frame
frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, sticky="nsew")
frame.columnconfigure(0, weight=1)

# Create label
label = ttk.Label(frame, text="Enter your string:", font=("Helvetica", 12))
label.grid(row=0, column=0, sticky="w", padx=(0, 10), pady=(0, 5))

# Create entry widget
entry = ttk.Entry(frame, font=("Helvetica", 12))
entry.grid(row=1, column=0, sticky="ew", padx=(0, 10), pady=(0, 10))
entry.focus()

# Create button
button = ttk.Button(frame, text="Submit", command=get_user_input)
button.grid(row=2, column=0, sticky="ew", padx=(0, 10))

# Adjust padding of widgets in the frame
for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Run the application
root.mainloop()
