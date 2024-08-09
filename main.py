from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# This is a Password Manager for everyone of us who find it hard to remember or create a new password for any new website.
# You can use the "Generate Password" button to create new strong password for your new login and the password will be automatically copied to your clipboard you just have to paste it in yous new password section.
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def search():
    try:
        with open("data.json","r") as data_file:
            data = json.load(data_file)
            data_dict = data[web.get()]
            messagebox.showinfo(title=web.get(), message=f"Email: {data_dict['email']}\n"
                                                         f"Password: {data_dict['password']}")
    except FileNotFoundError:
        messagebox.showinfo(title="File not found", message="The file does not exists")
    except KeyError:
        messagebox.showinfo(title="Record does not exist", message="The record does not exists")

def password_generator():
    pass_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    password_letters = [random.choice(letters) for c in range(nr_letters)]

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    password_symbols = [random.choice(symbols) for a in range(nr_symbols)]

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)
    password_numbers = [random.choice(numbers) for b in range(nr_numbers)]

    password_list = password_numbers + password_letters + password_symbols
    random.shuffle(password_list)

    password_str = "".join(password_list)
    # for char in password_list:
    #   password_str += char
    pass_input.insert(0, password_str)
    pyperclip.copy(password_str)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    if len(web.get()) <= 0 or len(pass_input.get()) <= 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=web.get(),
                                       message=f"These are the details you entered: \nEmail: {email_input.get()} "
                                               f"\nPassword: {pass_input.get()} \nIs it ok to save?")
        if is_ok:
            new_data = {
                web.get():
                    {"email": email_input.get(),
                     "password": pass_input.get(),
                     }
            }
            try:
                with open(file="data.json", mode="r") as data_file:
                    # Read the existing data
                    data = json.load(data_file)


            except FileNotFoundError:
                # Creates a new file if the file didn't exist
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # Update the existing data
                data.update(new_data)

                # Writes the updated data if the try passes
                with open(file="data.json", mode="w") as data_file:
                    json.dump(data, data_file, indent=4)

                # f.write(f"{web.get()} | {email_input.get()} | {pass_input.get()} \n")
            finally:
                web.delete(0, "end")  # END
                pass_input.delete(0, "end")  # END


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", border=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

#Label
website = Label(text="Website:", bg="white")
website.grid(column=0, row=1)
email = Label(text="Email/Username:", bg="white")
email.grid(column=0, row=2)
password = Label(text="Password:", bg="white")
password.grid(column=0, row=3)

#Entry
web = Entry(width=31)
web.grid(column=1, row=1)
web.focus()
email_input = Entry(width=48)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "tarun@gmail.com")
pass_input = Entry(width=31)
pass_input.grid(column=1, row=3)

#Button
gen_pass = Button(text="Generate Password", highlightthickness=0, bg="white", border=1, width=14,
                  command=password_generator)
gen_pass.grid(column=2, row=3)
add = Button(text="Add", width=41, highlightthickness=0, bg="white", border=1, command=save)
add.grid(column=1, row=4, columnspan=2)
search = Button(text="Search",  width=14, highlightthickness=0, bg="white", border=1, command=search)
search.grid(row=1, column=2)

window.mainloop()
