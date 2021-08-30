import tkinter
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()

    try:
        with open("data.json", "r") as data_file:
            # Read in existing data
            existing_data = json.load(data_file)
    except FileNotFoundError:
        # Give warning data.json is not found
        messagebox.showinfo(title="Error", message="File data.json Not Found")
    else:
        if website in existing_data:
            # Retrieve username and password from existing_data and display in messagebox
            account_username = existing_data[website]["Email"]
            account_password = existing_data[website]["Password"]
            messagebox.showinfo(title=website, message=f"Username: {account_username}\n"
                                                       f"Password: {account_password}")
        else:
            messagebox.showerror(title="Account not found", message=f"No details for '{website}' exists.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    # Add letters to new password_list
    [password_list.append(choice(letters)) for _ in range(randint(8, 10))]

    # Add symbols to new password_list
    [password_list.append(choice(symbols)) for _ in range(randint(2, 4))]

    # Add numbers to new password_list
    [password_list.append(choice(numbers)) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)

    # Clear then insert new password into Password Entry
    password_entry.delete(0, tkinter.END)
    password_entry.insert(0, password)

    # Copy password to clipboard
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    # Store data from the Entries
    website_data = website_entry.get()
    username_data = username_entry.get()
    password_data = password_entry.get()
    new_data = {
        website_data: {
            "Email": username_data,
            "Password": password_data,
        }}

    if len(website_data) == 0 or len(password_data) == 0:
        messagebox.showinfo(title="Field(s) Missing", message="Please fill in any blank fields")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Read in existing data
                existing_data = json.load(data_file)
        except FileNotFoundError:
            # Create a blank JSON file and write new_data to it
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Update existing data with new_data
            existing_data.update(new_data)

            # Reopen data.json in write mode and save updated data
            with open("data.json", "w") as data_file:
                json.dump(existing_data, data_file, indent=4)
        finally:
            # Clear the website_entry and password_entry fields
            website_entry.delete(0, tkinter.END)
            password_entry.delete(0, tkinter.END)


# ---------------------------- UI SETUP ------------------------------- #
# Create Tkinter window and configure
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Create Canvas and add image
canvas = tkinter.Canvas(width=200, height=200)
logo = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Create field labels and set positions
website_label = tkinter.Label(text="Website:")
website_label.grid(column=0, row=1)

username_label = tkinter.Label(text="Email/Username:")
username_label.grid(column=0, row=2)

password_label = tkinter.Label(text="Password:")
password_label.grid(column=0, row=3)

# Create Entries and set positions/sizes
website_entry = tkinter.Entry(width=33)
website_entry.grid(column=1, row=1, sticky="w")
website_entry.focus()

username_entry = tkinter.Entry(width=52)
username_entry.grid(column=1, row=2, columnspan=2, sticky="w")
username_entry.insert(0, "pat@patrick.com")

password_entry = tkinter.Entry(width=33)
password_entry.grid(column=1, row=3, sticky="w")

# Create Entries and set positions/sizes
search_button = tkinter.Button(text="Search", width=15, command=find_password)
search_button.grid(column=2, row=1, sticky="w")

pass_gen_button = tkinter.Button(text="Generate Password", command=generate_password)
pass_gen_button.grid(column=2, row=3, sticky="w")

add_button = tkinter.Button(text="Add", width=44, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="w")
window.mainloop()
