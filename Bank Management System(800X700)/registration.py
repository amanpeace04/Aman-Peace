import random
from tkinter import *
import mysql.connector
from tkinter import messagebox

t = Tk()
t.title("Registration")
t.geometry('800x700')
t.configure(bg="yellow")

connection = mysql.connector.connect(host='localhost', user='root', password='6368752',
                                     port='3306', database='amanbms')
c = connection.cursor()

def generate_account_number():
    return random.randint(100000, 999999)

def insertdata():
    accno = generate_account_number()
    n = name.get()
    uname = username_entry.get()
    pwd = password_entry.get()
    e = Email.get()
    m = Mobile.get()
    
    if not all([n, uname, pwd, e, m]):
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    insert_query = "INSERT INTO register(accno, name, username, password,emailid,mobile) VALUES (%s,%s,%s,%s,%s,%s)"
    vals = (accno, n, uname, pwd, e, m)
    c.execute(insert_query, vals)
    connection.commit()
    messagebox.showinfo("Success", "Registration Successful")
    t.destroy()

reg = Label(t, text="Registration", font=("Arial", 30), bg="Turquoise", fg="brown")
reg.place(relx=0.5, rely=0.2, anchor=CENTER)

namelabel = Label(t, text="Name", font=("Arial", 20), bg="black", fg="yellow")
namelabel.place(relx=0.2, rely=0.35, anchor=CENTER)
name = Entry(t, font=("Arial", 15), bg="white", fg="black")
name.place(relx=0.7, rely=0.35, anchor=CENTER)

userName = Label(t, text="Username", font=("Arial", 20), bg="green", fg="white")
userName.place(relx=0.2, rely=0.45, anchor=CENTER)
username_entry = Entry(t, font=("Arial", 15), bg="white", fg="black")
username_entry.place(relx=0.7, rely=0.45, anchor=CENTER)

password_label = Label(t, text="Login Password", font=("Arial", 20), bg="blue", fg="white")
password_label.place(relx=0.2, rely=0.55, anchor=CENTER)
password_entry = Entry(t, font=("Arial", 15), bg="white", fg="black", show="*")
password_entry.place(relx=0.7, rely=0.55, anchor=CENTER)

EmailId = Label(t, text="Email Id", font=("Arial", 20), bg="pink", fg="brown")
EmailId.place(relx=0.2, rely=0.65, anchor=CENTER)
Email = Entry(t, font=("Arial", 15), bg="white", fg="black")
Email.place(relx=0.7, rely=0.65, anchor=CENTER)

Mobileno = Label(t, text="Mobile", font=("Arial", 20), bg="maroon", fg="white")
Mobileno.place(relx=0.2, rely=0.75, anchor=CENTER)
Mobile = Entry(t, font=("Arial", 15), bg="white", fg="black")
Mobile.place(relx=0.7, rely=0.75, anchor=CENTER)

register = Button(t, text="Register", command=insertdata, font=("Arial", 20), bg="red", fg="white")
register.place(relx=0.43, rely=0.85, anchor=CENTER)

t.mainloop()
