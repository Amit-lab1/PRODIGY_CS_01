import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def caesar_cipher(text, shift, mode):
    """Encrypt or decrypt the given text using the Caesar cipher algorithm."""
    result = ''
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift if mode == 'encrypt' else ord(char) - shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            result += chr(shifted)
        else:
            result += char
    return result

def encrypt_decrypt():
    """Handle the encryption or decryption process based on user input."""
    text = input_text.get("1.0", "end-1c")
    try:
        shift = int(shift_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for the shift value.")
        return

    mode = mode_var.get()
    if mode not in ['encrypt', 'decrypt']:
        messagebox.showerror("Error", "Invalid mode! Please select 'encrypt' or 'decrypt'.")
        return

    result = caesar_cipher(text, shift, mode)
    output_text.delete("1.0", "end")
    output_text.insert("end", result)
    status_bar.config(text=f"Successfully {mode}ed the message.")

def clear_fields():
    """Clear the input and output fields."""
    input_text.delete("1.0", "end")
    output_text.delete("1.0", "end")
    shift_entry.delete(0, "end")
    mode_var.set("encrypt")
    status_bar.config(text="Fields cleared.")

def on_enter(event=None):
    """Change button color on mouse enter."""
    encrypt_button.configure(bg="#43a047")

def on_leave(event=None):
    """Revert button color on mouse leave."""
    encrypt_button.configure(bg="#4caf50")

def on_click(event=None):
    """Animate button click."""
    encrypt_button.configure(bg="#388e3c")
    root.after(100, lambda: encrypt_button.configure(bg="#43a047"))

def on_key_press(event):
    """Trigger encryption/decryption on Enter key press."""
    if event.keysym == 'Return':
        encrypt_decrypt()

# Main application setup
root = tk.Tk()
root.title("Caesar Cipher")
root.configure(background="#f0f0f0")

# Create main frame
main_frame = ttk.Frame(root, padding="20", style="My.TFrame")
main_frame.grid(row=0, column=0, sticky="nsew")

# Configure styles
style = ttk.Style()
style.configure("My.TFrame", background="#f0f0f0")
style.configure("My.TLabel", background="#f0f0f0", font=("Arial", 12))
style.configure("My.TButton", background="#4caf50", foreground="white", font=("Arial", 12, "bold"))

# Input fields
ttk.Label(main_frame, text="Enter the message:", style="My.TLabel").grid(row=0, column=0, sticky="w")
input_text = tk.Text(main_frame, height=5, width=40)
input_text.grid(row=1, column=0, columnspan=3, padx=(0, 10), pady=5, sticky="w")

ttk.Label(main_frame, text="Enter the shift value:", style="My.TLabel").grid(row=2, column=0, sticky="w")
shift_entry = ttk.Entry(main_frame, width=10)
shift_entry.grid(row=2, column=1, pady=5, sticky="w")

ttk.Label(main_frame, text="Select 'encrypt' or 'decrypt':", style="My.TLabel").grid(row=3, column=0, sticky="w")
mode_var = tk.StringVar(value="encrypt")
mode_combobox = ttk.Combobox(main_frame, textvariable=mode_var, values=["encrypt", "decrypt"], width=10)
mode_combobox.grid(row=3, column=1, pady=5, sticky="w")

# Encrypt/Decrypt button
encrypt_button = tk.Button(main_frame, text="Encrypt/Decrypt", command=encrypt_decrypt, bg="#4caf50", fg="white", font=("Arial", 12, "bold"))
encrypt_button.grid(row=4, column=0, columnspan=2, pady=10)
encrypt_button.bind("<Enter>", on_enter)
encrypt_button.bind("<Leave>", on_leave)
encrypt_button.bind("<Button-1>", on_click)

# Clear button
clear_button = tk.Button(main_frame, text="Clear", command=clear_fields, bg="#f44336", fg="white", font=("Arial", 12, "bold"))
clear_button.grid(row=4, column=2, pady=10)

# Output field
ttk.Label(main_frame, text="Result:", style="My.TLabel").grid(row=5, column=0, sticky="w")
output_text = tk.Text(main_frame, height=5, width=40)
output_text.grid(row=6, column=0, columnspan=3, padx=(0, 10), pady=5, sticky="w")

# Status bar
status_bar = ttk.Label(root, text="Welcome to the Caesar Cipher Tool!", relief=tk.SUNKEN, anchor="w")
status_bar.grid(row=1, column=0, sticky="ew")

# Bind Enter key to trigger encryption/decryption
root.bind("<Return>", on_key_press)

# Start the application
root.mainloop()
