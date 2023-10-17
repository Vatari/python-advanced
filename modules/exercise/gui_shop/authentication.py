import json
import tkinter as tk
import tkmacosx as tkm

from canvas import app
from helpers import clean_screen
from products import render_products


def login(username, passwd):
    with open("db/user_credentials_db.txt", "r") as f:
        data = f.readlines()
        for line in data:
            name, password = line[:-1].split(", ")
            if name == username and passwd == password:
                with open("db/current_user.txt", "w") as f:
                    f.write(name)
                render_products()
                return

        render_login(error="Invalid username or password")


def register(**user):
    user.update({"products": []})
    with open("db/users.txt", "a", newline='\n') as file:
        file.write(json.dumps(user))
        file.write('\n')
    with open("db/user_credentials_db.txt", "a", newline='') as file:
        file.write(f"{user['username']}, {user['password']}\n")
    render_login()


def render_login(error=None):
    clean_screen()
    username = tk.Entry(app)
    username.grid(row=0, column=0)
    password = tk.Entry(app)
    password.grid(row=1, column=0)

    if error is not None:
        tk.Label(app, text="Invalid username or password").grid(row=3, column=0)
    tkm.Button(app, text="Enter", bg="green", command=lambda: login(username.get(), password.get())).grid(row=2,
                                                                                                          column=0)


def render_register():
    clean_screen()
    username = tk.Entry(app)
    username.grid(row=0, column=0)
    password = tk.Entry(app)
    password.grid(row=1, column=0)
    first_name = tk.Entry(app)
    first_name.grid(row=2, column=0)
    last_name = tk.Entry(app)
    last_name.grid(row=3, column=0)
    # Make validations for names length and username to be unique and with no special chars
    tkm.Button(
        app,
        text="Register", bg="green",
        command=lambda: register(username=username.get(), password=password.get(), first_name=first_name.get(),
                                 last_name=last_name.get())).grid(row=4,
                                                                  column=0)


def render_main_enter_screen():
    tkm.Button(app, text="Login", bg="green", fg="white", command=render_login).grid(row=0, column=0)
    tkm.Button(app, text="Register", bg="yellow", fg="black", command=render_register).grid(row=0, column=1, sticky="e")
