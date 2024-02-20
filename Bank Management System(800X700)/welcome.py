import tkinter as tk
import os

def registration():
    t.destroy()
    os.system("python registration.py")

def login():
    t.destroy()
    os.system("python login.py")

t = tk.Tk()
t.title("Welcome")
t.geometry('800x700')
t.configure(bg="yellow")

bms = tk.Label(t, text="Welcome to ABC Bank", font=("Arial", 30), bg="Turquoise", fg="brown")
bms.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

register_button = tk.Button(t, text="Registration", command=registration, font=("Arial", 20), bg="Turquoise", fg="brown")
register_button.place(relx=0.2, rely=0.3, anchor=tk.CENTER)

login_button = tk.Button(t, text="Login", command=login, font=("Arial", 20), bg="red", fg="white")
login_button.place(relx=0.8, rely=0.3, anchor=tk.CENTER)

services_button = tk.Button(t, text="Services", font=("Arial", 20), bg="black", fg="yellow")
services_button.place(relx=0.2, rely=0.5, anchor=tk.CENTER)

contact_button = tk.Button(t, text="Contact Us", font=("Arial", 20), bg="lightgreen", fg="brown")
contact_button.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

connect_button = tk.Button(t, text="Connect with us: ", font=("Arial", 20), bg="Maroon", fg="White")
connect_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

Fb = tk.Button(t, text="Facebook ", font=("Arial", 20), bg="lightblue", fg="white")
Fb.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

Insta = tk.Button(t, text="Instagram ", font=("Arial", 20), bg="pink", fg="white")
Insta.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

Twitter = tk.Button(t, text="Twitter ", font=("Arial", 20), bg="black", fg="white")
Twitter.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

t.mainloop()
