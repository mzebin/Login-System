import tkinter as tk
from tkinter import ttk

from ttkthemes import ThemedTk

from signup import Signup
from utils import check_credentials, show_message


class LoginApp(ThemedTk):
    def __init__(self):
        super().__init__(theme="equilux")

        self.title("Login System")
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

        # Show password button
        self.show_password_button = ttk.Button(
            self, text="Show Password", command=self.toggle_password_visibility
        )
        self.show_password_button.grid(row=2, column=0, columnspan=4, sticky="nsew")

        # Sign Up and Login buttons
        self.signup_button = ttk.Button(self, text="Sign Up", command=self.open_signup)
        self.signup_button.grid(row=3, column=0, columnspan=2, sticky="nsew")
        self.login_button = ttk.Button(self, text="Login", command=self.login)
        self.login_button.grid(row=3, column=2, columnspan=2, sticky="nsew")

    def open_signup(self):
        # Open the signup window
        signup_window = Signup(self)
        self.wait_window(signup_window)

    def login(self):
        # Get username and password from entry fields
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check if credentials are valid
        if check_credentials(username, password):
            # Show success message and close the login window
            show_message("Login successful")
            self.destroy()
        else:
            # Show error message for invalid credentials
            show_message("Invalid username or password. Please try again.")

    def toggle_password_visibility(self):
        # Toggle the password visibility in the entry field
        current_state = self.password_entry.cget("show")
        show = "" if current_state == "*" else "*"
        text = "Hide Password" if current_state == "*" else "Show Password"
        self.password_entry.config(show=show)
        self.show_password_button.config(text=text)


if __name__ == "__main__":
    # Create and run the login application
    app = LoginApp()
    app.mainloop()
