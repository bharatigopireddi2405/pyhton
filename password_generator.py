import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password_button_click():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Error", "Please enter a positive length.")
            return
        password = generate_password(length)
        generated_password_label.config(text="Generated Password: " + password)
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid integer for the length.")

# Create Tkinter window with increased width and height and background color
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")  # Set width and height
root.configure(bg="#6A5ACD")  # Set background color (light gray)

# Create widgets
length_label = tk.Label(root, text="Desired length of the password:", bg="#f0f0f0")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password_button_click)
generate_button.pack()

generated_password_label = tk.Label(root, text="", bg="#f0f0f0")
generated_password_label.pack()

# Run the Tkinter event loop
root.mainloop()
