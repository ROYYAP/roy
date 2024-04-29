import tkinter as tk
from tkinter import messagebox

def caesar_cipher(plain_text, key, mode):
    """
    Encrypts or decrypts plain_text using Caesar cipher with given key and mode.
    """
    result = ""
    for char in plain_text:
        if char.isalpha():
            # Shift letter by key positions
            char_code = ord(char) - 65 if char.isupper() else ord(char) - 97
            shifted_code = (char_code + key) % 26 if mode == "encrypt" else (char_code - key) % 26
            shifted_char = chr(shifted_code + 65 if char.isupper() else shifted_code + 97)
            result += shifted_char
        else:
            result += char
    return result

def encrypt():
    """
    Encrypts plain text using key and displays the result in the output text box.
    """
    plain_text = plain_text_box.get("1.0", "end-1c")
    key = key_box.get("1.0","end-1c")
    if key.isdigit():
        key = int(key)
        cipher_text = caesar_cipher(plain_text, key, "encrypt")
        output_box.delete("1.0", "end")
        output_box.insert("end", cipher_text)
    else:
        messagebox.showerror("Invalid Key", "Key must be an integer.")

def decrypt():
    """
    Decrypts cipher text using key and displays the result in the output text box.
    """
    cipher_text = plain_text_box.get("1.0", "end-1c")
    key = key_box.get("1.0","end-1c")
    if key.isdigit():
        key = int(key)
        plain_text = caesar_cipher(cipher_text, key, "decrypt")
        output_box.delete("1.0", "end")
        output_box.insert("end", plain_text)
    else:
        messagebox.showerror("Invalid Key", "Key must be an integer.")

def reset():
    """
    Clears all the text boxes.
    """
    plain_text_box.delete("1.0", "end")
    key_box.delete("1.0", "end")
    output_box.delete("1.0", "end")

def exit_program():
    """
    Prompts the user to confirm exiting the program.
    """
    response = messagebox.askyesno("Exit Program", "Are you sure you want to exit?")
    if response == 1:
        root.destroy()
        
# Create GUI
root = tk.Tk()
root.title("Playfai Cipher")
root.geometry("470x560")
root.minsize(470,560)
root.maxsize(470,560) 

# Create widgets
plain_text_label = tk.Label(root, text="MESSAGE:", font=("Arial", 14))
plain_text_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")


plain_text_box = tk.Text(root, width=50, height=8, font=("Arial", 11))
plain_text_box.grid(row=1, column=0, padx=5, pady=5)

key_label = tk.Label(root, text="Key (Only Numbers): ", font=("Arial", 14))
key_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

key_box = tk.Text(root, font=("Arial", 12), width=10, height=1,)
key_box.grid(row=3, column=0, padx=5, pady=5)

encrypt_button = tk.Button(root, text="Encrypt",font=("Arial", 14), command=encrypt, width=8, height=1)
encrypt_button.grid(row=4, column=0, padx=5, pady=5, sticky="e")

decrypt_button = tk.Button(root, text="Decrypt", font=("Arial", 14),  command=decrypt, width=8, height=1)
decrypt_button.grid(row=4, column=0, padx=5, pady=5, sticky="w")

output_label = tk.Label(root, text="RESULT:", font=("Arial", 14))
output_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")

output_box = tk.Text(root, width=50, height=8, font=("Arial", 11))
output_box.grid(row=6, column=0, padx=5, pady=5)

reset_button = tk.Button(root, text="Reset", font=("Arial", 14), command=reset, width=8, height=1)
reset_button.grid(row=4, column=0, padx=5, pady=5, sticky="s")

exit_button = tk.Button(root, text="Exit", font=("Arial", 14), command=exit_program, width=8, height=1)
exit_button.grid(row=7, column=0, padx=5, pady=5, sticky="s")

# Start GUI
root.mainloop()