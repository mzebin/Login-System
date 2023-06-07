import csv
import random
import string
from tkinter import messagebox

CHARACTERS = " " + string.ascii_letters + string.punctuation + string.digits


def add_user(username, password):
    # Add a new user to the credentials.csv file
    with open("credentials.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, password])


def username_available(username):
    # Check if the username is available in the credentials.csv file
    with open("credentials.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 2 and row[0] == username:
                return False
    return True


def check_credentials(username, password):
    # Check if the provided credentials match an entry in the credentials.csv file
    with open("credentials.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 2 and row[0] == username and row[1] == password:
                return True
    return False


def generate_password(length):
    # Generate a random password of the specified length
    password = ""
    for i in range(length):
        if i % 4 == 0 and i != 0 and i + 1 != length:
            password += "-"
        else:
            password += random.choice(CHARACTERS)
    return password


def show_message(message):
    # Show a message box with the provided message
    messagebox.showinfo("Message", message)
