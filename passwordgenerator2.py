import random
import string
from Tkinter import *

def generate_password(length, complexity):
    # Choose characters based on complexity level
    if complexity == "easy":
        characters = string.ascii_letters # Only letters
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits # Letters and numbers
    elif complexity == "hard":
        characters = string.ascii_letters + string.digits + string.punctuation # Letters, numbers, and symbols
    else:
        return "Invalid complexity level"

    # Generate password using random characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")

        Label(master, text="Password Length:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.length_entry = Entry(master, width=5)
        self.length_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        Label(master, text="Password Complexity:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.complexity_var = StringVar(master)
        self.complexity_var.set("easy") # Default value
        self.complexity_menu = OptionMenu(master, self.complexity_var, "easy", "medium", "hard")
        self.complexity_menu.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        generate_button = Button(master, text="Generate Password", command=self.generate_password_and_display)
        generate_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.result_var = StringVar(master)
        self.result_label = Label(master, textvariable=self.result_var)
        self.result_label.grid(row=3, column=0, columnspan=2, pady=5)

    def generate_password_and_display(self):
        password_length = int(self.length_entry.get())
        password_complexity = self.complexity_var.get()
        password = generate_password(password_length, password_complexity)
        self.result_var.set("Generated Password: " + password)

def main():
    root = Tk()

    password_generator_app = PasswordGeneratorApp(root)

    root.mainloop()

if __name__ == "__main__":
    main()
