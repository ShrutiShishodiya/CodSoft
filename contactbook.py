# Import necessary modules
from Tkinter import *
import tkMessageBox

# Define the contacts list
contacts = []

# Function to add a new contact
def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()

    if name and phone:
        contact_list.insert(END, "{} - {}".format(name, phone))
        contacts.append("{} - {}".format(name, phone)) # Add the contact to the list
        clear_entries()
    else:
        tkMessageBox.showwarning("Warning", "Name and Phone are required.")

# Function to search for a contact
def search_contact():
    search_text = entry_search.get().lower()
    clear_contact_list()

    for contact in contacts:
        if search_text.lower() in contact.lower():
            contact_list.insert(END, contact)

# Function to update a contact
def update_contact():
    selected_contact = contact_list.get(ACTIVE)

    if not selected_contact:
        tkMessageBox.showwarning("Warning", "Select a contact to update.")
    else:
        clear_entries()
        parts = selected_contact.split(" - ")
        entry_name.insert(END, parts[0])
        entry_phone.insert(END, parts[1])

# Function to delete a contact
def delete_contact():
    selected_contact = contact_list.get(ACTIVE)

    if not selected_contact:
        tkMessageBox.showwarning("Warning", "Select a contact to delete.")
    else:
        contact_list.delete(ACTIVE)
        contacts.remove(selected_contact) # Remove the contact from the list

# Function to clear entry fields
def clear_entries():
    entry_name.delete(0, END)
    entry_phone.delete(0, END)
    entry_email.delete(0, END)
    entry_address.delete(0, END)

# Function to clear the contact list
def clear_contact_list():
    contact_list.delete(0, END)

# Main GUI setup
root = Tk()
root.title("Contact Book")

# Entry fields
entry_name = Entry(root, width=30)
entry_phone = Entry(root, width=30)
entry_email = Entry(root, width=30)
entry_address = Entry(root, width=30)
entry_search = Entry(root, width=30)

# Contact listbox
contact_list = Listbox(root, width=50, height=10)

# Buttons
btn_add = Button(root, text="Add Contact", command=add_contact)
btn_search = Button(root, text="Search Contact", command=search_contact)
btn_update = Button(root, text="Update Contact", command=update_contact)
btn_delete = Button(root, text="Delete Contact", command=delete_contact)

# Place widgets on the GUI
entry_name.grid(row=0, column=1, padx=10, pady=5)
entry_phone.grid(row=1, column=1, padx=10, pady=5)
entry_email.grid(row=2, column=1, padx=10, pady=5)
entry_address.grid(row=3, column=1, padx=10, pady=5)
entry_search.grid(row=6, column=1, padx=10, pady=5)

contact_list.grid(row=8, column=1, padx=10, pady=5, rowspan=5, columnspan=2)

btn_add.grid(row=4, column=1, pady=5)
btn_search.grid(row=7, column=1, pady=5)
btn_update.grid(row=8, column=2, pady=5)
btn_delete.grid(row=9, column=2, pady=5)

# Run the main loop
root.mainloop()
