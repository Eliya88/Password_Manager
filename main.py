from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    """give the user a random powerful password"""
    letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
    numbers = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    symbols = ('!', '#', '$', '%', '&', '(', ')', '*', '+')

    # create a list of random letters, numbers and symbols
    password_list_1 = [choice(letters) for _ in range(randint(8, 10))]

    password_list_2 = [choice(symbols) for _ in range(randint(2, 4))]

    password_list_3 = [choice(numbers) for _ in range(randint(2, 4))]

    # combine the lists
    password_list_combined = password_list_1 + password_list_2 + password_list_3

    # shuffle the list
    shuffle(password_list_combined)

    # turn the list to a string
    password = "".join(password_list_combined)
    pass_input.delete(0, END)
    pass_input.insert(0, password)
    
    # copy the password to the user clipboard that he can paste in the web.
    pyperclip.copy(text=password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    """create a json file and saves the data the user inserts"""
    website = web_input.get()
    email = email_input.get()
    password = pass_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    # check if the user left some fields empty
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="You left some fields empty!")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                # Reading the data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", mode="w") as new_file:
                json.dump(new_data, new_file, indent=4)

        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", mode="w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)

        finally:
            web_input.delete(0, END)
            pass_input.delete(0, END)


# ------------------------------- WEB SEARCHING --------------------------------- #
def search_web():
    web = web_input.get()
    try:
        with open("data.json", mode="r") as data_file:
            # Reading the data
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title='Error', message="You didn't have any save data")

    else:
        if web in data:
            messagebox.showinfo(title=web, message=f"Email:  {data[web]['email']}\n"
                                                   f"Password:  {data[web]['password']}")
        else:
            messagebox.showinfo(title='Error', message=f"There is no website called {web} in your stored data")
    finally:
        web_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=50)

# create an image on the screen.
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# create labels.
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)

email_label = Label(text="Email/UserName:")
email_label.grid(column=0, row=2)

pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

# create user input box.
web_input = Entry(width=34)
web_input.grid(column=1, row=1)
web_input.focus()

email_input = Entry(width=53)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "eliyaz1998@gmail.com")

pass_input = Entry(width=34)
pass_input.grid(column=1, row=3, columnspan=1)

# create buttons.
pass_button = Button(text="Generate Password", command=generate_password)
pass_button.grid(column=2, row=3)

add_button = Button(width=44, text="Add", command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=14, command=search_web)
search_button.grid(column=2, row=1, columnspan=2)

window.mainloop()
