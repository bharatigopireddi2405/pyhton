# Projects
import tkinter as tk
import tkinter.messagebox

# Function to handle button clicks
def button_click(number):
    entry.insert(tk.END, number)

# Function to evaluate the expression
def evaluate_expression():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        tkinter.messagebox.showinfo("Error", "Syntax Error")

# Function to clear the entry field
def clear_entry():
    entry.delete(0, tk.END)

# Create main window
window = tk.Tk()
window.title('Calculator')

# Create and configure entry field
entry = tk.Entry(window, relief=tk.SUNKEN, borderwidth=3, width=30)
entry.grid(row=0, column=0, columnspan=4, ipady=2, pady=2)

# Define button labels and their positions
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Create buttons using a loop
for (text, row, col) in buttons:
    if text == 'C':
        button = tk.Button(window, text=text, padx=15, pady=5, width=3, command=clear_entry)
    elif text == '=':
        button = tk.Button(window, text=text, padx=15, pady=5, width=9, command=evaluate_expression)
    else:
        button = tk.Button(window, text=text, padx=15, pady=5, width=3, command=lambda t=text: button_click(t))
    button.grid(row=row, column=col, pady=2)

window.mainloop()
