import tkinter as tk
from tkinter import ttk

from utils import username_available, add_user, generate_password, show_message


class Signup(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("Signup")
        self.resizable(0, 0)

        # Username label and entry field
        self.username_label = ttk.Label(self, text="Username:")
        self.username_label.grid(row=0, column=0, sticky="nsew")
        self.username_entry = ttk.Entry(self)
        self.username_entry.grid(row=0, column=1, columnspan=2, sticky="nsew")

        # Password label and entry field
        self.password_label = ttk.Label(self, text="Password:")
        self.password_label.grid(row=1, column=0, sticky="nsew")
        self.password_entry = ttk.Entry(self, show="*")
        self.password_entry.grid(row=1, column=1, columnspan=2, sticky="nsew")

        # Confirm password label and entry field
        self.confirm_password_label = ttk.Label(self, text="Confirm Password:")
        self.confirm_password_label.grid(row=2, column=0, sticky="nsew")
        self.confirm_password_entry = ttk.Entry(self, show="*")
        self.confirm_password_entry.grid(row=2, column=1, columnspan=2, sticky="nsew")

        # Show password button
        self.show_password_button = ttk.Button(
            self, text="Show Password", command=self.toggle_password_visibility
        )
        self.show_password_button.grid(row=3, column=0, columnspan=4, sticky="nsew")

        # Suggest password button
        self.suggest_password_button = ttk.Button(
            self, text="Suggest Password", command=self.suggest_password
        )
        self.suggest_password_button.grid(row=4, column=0, columnspan=2, sticky="nsew")

        # Signup button
        self.signup_button = ttk.Button(self, text="Signup", command=self.signup)
        self.signup_button.grid(row=4, column=2, columnspan=2, sticky="nsew")

    def suggest_password(self):
        # Generate and suggest a password
        password = generate_password(14)
        self.password_entry.delete(0, "end")
        self.confirm_password_entry.delete(0, "end")
        self.password_entry.insert(0, password)
        self.confirm_password_entry.insert(0, password)

    def signup(self):
        # Get the entered username, password, and confirm password
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if username and password and confirm_password:
            if not username_available(username):
                # Show error message if the username is already taken
                show_message("Username already taken. Please choose another username.")
            elif password == confirm_password:
                # Add the user and show success message if passwords match
                add_user(username, password)
                show_message("Signup successful. You can now login.")
                self.destroy()
            else:
                # Show error message if passwords do not match
                show_message("Passwords do not match. Please try again.")
        else:
            # Show error message if any field is empty
            show_message("Please fill in all the fields.")

    def toggle_password_visibility(self):
        # Toggle the password visibility in the entry fields
        current_state = self.password_entry.cget("show")
        show = "" if current_state == "*" else "*"
        text = "Hide Password" if current_state == "*" else "Show Password"
        self.password_entry.config(show=show)
        self.confirm_password_entry.config(show=show)
        self.show_password_button.config(text=text)
