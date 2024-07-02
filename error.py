import re
import tkinter as tk

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

root = tk.Tk()

email_entry = tk.Entry(root)
email_entry.pack()

error_label = tk.Label(root, fg="red")
error_label.pack()

def validate():
    email = email_entry.get()
    if validate_email(email):
        error_label.config(text="")
        print("Valid email address")
    else:
        error_label.config(text="Invalid email address")
        print("Invalid email address")

validate_button = tk.Button(root, text="Validate", command=validate)
validate_button.pack()

root.mainloop()
