import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def display_contacts(self):
        if self.contacts:
            contact_info = ""
            for index, contact in enumerate(self.contacts, start=1):
                contact_info += f"{index}. Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}\n"
            return contact_info
        else:
            return "No contacts in the contact book."

    def search_contact(self, name):
        found_contacts = [contact for contact in self.contacts if contact.name.lower() == name.lower()]
        if found_contacts:
            contact_info = ""
            for index, contact in enumerate(found_contacts, start=1):
                contact_info += f"{index}. Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}\n"
            return contact_info
        else:
            return "No matching contacts found."

def add_contact_window():
    add_window = tk.Toplevel(root)
    add_window.title("Add Contact")

    # Create labels and entry fields for user input
    name_label = tk.Label(add_window, text="Name:")
    name_label.grid(row=0, column=0, padx=10, pady=5)
    name_entry = tk.Entry(add_window)
    name_entry.grid(row=0, column=1, padx=10, pady=5)

    phone_label = tk.Label(add_window, text="Phone Number:")
    phone_label.grid(row=1, column=0, padx=10, pady=5)
    phone_entry = tk.Entry(add_window)
    phone_entry.grid(row=1, column=1, padx=10, pady=5)

    email_label = tk.Label(add_window, text="Email:")
    email_label.grid(row=2, column=0, padx=10, pady=5)
    email_entry = tk.Entry(add_window)
    email_entry.grid(row=2, column=1, padx=10, pady=5)

    # Function to add contact when the button is clicked
    def add_contact():
        name = name_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()
        if name and phone and email:
            contact_book.add_contact(Contact(name, phone, email))
            messagebox.showinfo("Success", "Contact added successfully.")
            add_window.destroy()
        else:
            messagebox.showerror("Error", "Please fill in all the fields.")

    # Button to add the contact
    add_button = tk.Button(add_window, text="Add Contact", command=add_contact, bg="#5cb85c", fg="white")
    add_button.grid(row=3, columnspan=2, pady=10)

def display_contacts_window():
    display_window = tk.Toplevel(root)
    display_window.title("Display Contacts")

    # Display contacts
    contacts_text = contact_book.display_contacts()
    contacts_label = tk.Label(display_window, text=contacts_text, padx=10, pady=10)
    contacts_label.pack()

def search_contact_window():
    search_window = tk.Toplevel(root)
    search_window.title("Search Contact")

    # Create label and entry field for user input
    search_label = tk.Label(search_window, text="Enter name to search:", padx=10, pady=5)
    search_label.pack()
    search_entry = tk.Entry(search_window)
    search_entry.pack()

    # Function to search for contacts
    def search_contact():
        name = search_entry.get()
        if name:
            found_contacts = contact_book.search_contact(name)
            if found_contacts:
                messagebox.showinfo("Search Results", found_contacts)
            else:
                messagebox.showinfo("Search Results", "No matching contacts found.")
            search_window.destroy()
        else:
            messagebox.showerror("Error", "Please enter a name to search.")

    # Button to initiate search
    search_button = tk.Button(search_window, text="Search", command=search_contact, bg="#5bc0de", fg="white")
    search_button.pack()

# Create Tkinter window
root = tk.Tk()
root.title("Contact Book")
root.geometry("300x200")
root.configure(bg="#E8E8E8")

# Create contact book instance
contact_book = ContactBook()

# Create buttons for different operations
add_button = tk.Button(root, text="Add Contact", command=add_contact_window, bg="#5cb85c", fg="white", padx=10, pady=5)
add_button.pack(pady=5)

display_button = tk.Button(root, text="Display Contacts", command=display_contacts_window, bg="#5bc0de", fg="white", padx=10, pady=5)
display_button.pack(pady=5)

search_button = tk.Button(root, text="Search Contact", command=search_contact_window, bg="#f0ad4e", fg="white", padx=10, pady=5)
search_button.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
