import tkinter as tk
from tkinter import ttk

# Function to update the display when a button is clicked
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

# Function to clear the display
def clear():
    entry.delete(0, tk.END)

# Function to perform calculations
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create a style for ttk buttons
style = ttk.Style()
style.configure("TButton", padding=10, font=('Helvetica', 16))

# Create an entry widget for displaying the input and output
entry = tk.Entry(window, width=20, borderwidth=5, font=('Helvetica', 16))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define the buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '+',
]

# Create and place the buttons on the grid
row_num = 1
col_num = 0
for button_text in buttons:
    button = ttk.Button(window, text=button_text, command=lambda text=button_text: button_click(text))
    button.grid(row=row_num, column=col_num, padx=5, pady=5, sticky="nsew")
    col_num += 1
    if col_num > 3:
        col_num = 0
        row_num += 1

# Create a clear button
clear_button = ttk.Button(window, text="Clear", command=clear)
clear_button.grid(row=row_num, column=col_num + 1, padx=5, pady=5, sticky="nsew")

# Create an equals button
equals_button = ttk.Button(window, text="=", command=calculate)
equals_button.grid(row=row_num, column=col_num, padx=5, pady=5, sticky="nsew")

# Configure row and column weights to make the buttons expand
for i in range(4):
    window.grid_columnconfigure(i, weight=1)
for i in range(1, 6):
    window.grid_rowconfigure(i, weight=1)

# Run the GUI
window.mainloop()