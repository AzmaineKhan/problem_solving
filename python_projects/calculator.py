import tkinter as tk

# Function to add symbol to the expression
def on_button_click(symbol):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + symbol)

# # Function to evaluate the expression
def evaluate_expression():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to clear the expression
def clear_entry():
    entry.delete(0, tk.END)
# Create main window
window = tk.Tk()
window.title("Simple Calculator")

# Entry widget for displaying the expression and result
entry = tk.Entry(window, width=16, font=('Arial', 24), borderwidth=2, relief='solid', justify='right')
entry.grid(row=0, column=0, columnspan=4)

# List of buttons to display on the calculator
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Add buttons to the window
for text, row, col in buttons:
    if text == 'C':
        button = tk.Button(window, text=text, width=5, height=2, font=('Arial', 18), command=clear_entry)
    elif text == '=':
        button = tk.Button(window, text=text, width=5, height=2, font=('Arial', 18), command=evaluate_expression)
    else:
        button = tk.Button(window, text=text, width=5, height=2, font=('Arial', 18), command=lambda t=text: on_button_click(t))
    button.grid(row=row, column=col, padx=5, pady=5)

# Start the Tkinter event loop
window.mainloop()
