from tkinter import *
import mysql.connector
from tkinter import messagebox
import os

t = Tk()
t.title("Login")
t.geometry('800x700')
t.configure(bg="yellow")

connection = mysql.connector.connect(host='localhost', user='root', password='6368752',
                                     port='3306', database='amanbms')
c = connection.cursor()

def login():
   
    username = name.get()
    password = LoginPassword.get()


    if not all([username, password]):
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    c.execute("SELECT * FROM register WHERE username = %s AND password = %s", (username, password))
    result = c.fetchone()
    if result:
        messagebox.showinfo("Success", "Login Successful")
        t.destroy()
        os.system("Transactions.py")
    else:
        messagebox.showerror("Error", "Invalid username or password")

Login = Label(t, text="Login", font=("Arial", 30), bg="Turquoise", fg="brown")
Login.place(relx=0.5, rely=0.2, anchor=CENTER)

userName = Label(t, text="Username", font=("Arial", 20), bg="Maroon", fg="white")
userName.place(relx=0.2, rely=0.4, anchor=CENTER)
name = Entry(t, font=("Arial", 15), bg="white", fg="black")
name.place(relx=0.7, rely=0.4, anchor=CENTER)

Password = Label(t, text="Login Password", font=("Arial", 20), bg="green", fg="white")
Password.place(relx=0.2, rely=0.48, anchor=CENTER)
LoginPassword = Entry(t, font=("Arial", 15), bg="white", fg="black", show="*")
LoginPassword.place(relx=0.7, rely=0.48, anchor=CENTER)

login = Button(t, text="Login", font=("Arial", 20), bg="red", fg="white", command=login)
login.place(relx=0.43, rely=0.57, anchor=CENTER)

t.mainloop()

