from tkinter import *
from tkinter import messagebox  # messegebox isnt a class but a mosult itself
import random
import pyperclip  # used to automatically copy into clipboard
import json
from json.decoder import JSONDecodeError


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    [password_list.append(random.choice(letters)) for char in range(nr_letters)]

    [password_list.append(random.choice(symbols)) for char in range(nr_symbols)]

    [password_list.append(random.choice(numbers)) for char in range(nr_symbols)]

    random.shuffle(password_list)
    password = "".join(password_list)
    # password = ""
    # for char in password_list:
    #     password += char
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)  # we can directly past without copying


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website:
            {
                "email": email,
                "password": password
            }

    }
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="error", message="Some fields are empty")

    else:
        is_ok = messagebox.askyesno(title="check",
                                    message=f"Website : {website}\n Email : {email}\n Password : {password}")
        if is_ok:

            try:
                with open("data.json", "r") as file:  # we shouldnt use "a" because that would b invalid format
                    data = json.load(file)  # reading old data
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            except JSONDecodeError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)

            else:
                data.update(new_data)
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)

            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
        else:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            if website in data:
                password = data[website]["password"]
                email = data[website]["email"]
                messagebox.showinfo(title="website",message=f"Email is {email}\n Password is {password}")
            else:
                messagebox.showerror(message="no data found")
    except FileNotFoundError:
        with open("data.json", "w") as file:
            messagebox.showerror(title="error",message="no data found")
    except JSONDecodeError :
        messagebox.showerror(title="error",message="no data found")







# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.config(padx=50, pady=50)

canvas = Canvas(window, width=200, height=200)
my_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=my_image)
# canvas.pack()
canvas.grid(row=0, column=1)

website_label = Label(window, text="Website:")
email_label = Label(window, text="Email/username:")
password_label = Label(window, text="password:")
website_label.grid(row=1, column=0)
email_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)

website_entry = Entry(window, width=21)
email_entry = Entry(window, width=35)
password_entry = Entry(window, width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "harisrashid4121203@gmail.com")
password_entry.grid(row=3, column=1)

generate_button = Button(window, text="Generate password", command=generate_password)
add_button = Button(window, text="Add", width=36, command=save_data)
generate_button.grid(row=3, column=2)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(window, text="Search", width=13, command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()
