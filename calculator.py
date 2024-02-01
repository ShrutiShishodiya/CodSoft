from Tkinter import *

# Variable to track dot button usage
dot_pressed = False

def on_click(button_value):
    global dot_pressed
    current_text = entry.get()

    if button_value == '(':
        # Add an open bracket only if the last character is not a digit or a close bracket
        if not current_text or not current_text[-1].isdigit() and current_text[-1] != ')':
            current_text += str(button_value)
            dot_pressed = False
    elif button_value == ')':
        # Add a close bracket only if the last character is a digit or an open bracket
        if current_text and (current_text[-1].isdigit() or current_text[-1] == '('):
            current_text += str(button_value)
            dot_pressed = False
    elif button_value == '.':
        # Allow only one dot in a number
        if not dot_pressed:
            current_text += str(button_value)
            dot_pressed = True
    else:
        # Add the clicked button value
        current_text += str(button_value)
        dot_pressed = False

    entry.delete(0, END)
    entry.insert(END, current_text)

def clear_entry():
    global dot_pressed
    # Clear the entry widget and reset dot_pressed
    entry.delete(0, END)
    dot_pressed = False

def calculate():
    global dot_pressed
    try:
        expression = entry.get()

        if expression.endswith('.='):
            # Remove the additional equal sign after the dot
            expression = expression.replace('.=', '=')

        if '=' in expression:
            expression = expression.split('=')[-1].strip()

        # Check if the expression contains an operator or an equal sign
        if any(op in expression for op in ['+', '-', '*', '/']):
            # Add brackets around the entire expression
            expression_with_brackets = '(' + expression + ')'
        else:
            expression_with_brackets = expression

        # Evaluate the expression and display the result
        result = eval(expression_with_brackets)

        entry.delete(0, END)
        entry.insert(END, str(result))
        dot_pressed = False
    except Exception as e:
        # Handle errors by displaying "Error"
        entry.delete(0, END)
        entry.insert(END, "Error")
        dot_pressed = False

root = Tk()
root.title("Simple Calculator")

entry = Entry(root, width=20, font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '(', ')', '+',
    '.'
]

row_val = 1
col_val = 0

for button in buttons:
    Button(root, text=button, width=5, height=2, command=lambda b=button: on_click(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

Button(root, text="C", width=5, height=2, command=clear_entry).grid(row=row_val, column=col_val)
col_val += 1

Button(root, text="=", width=5, height=2, command=calculate).grid(row=row_val, column=col_val)

root.bind('<Return>', lambda event=None: calculate())

root.mainloop()
