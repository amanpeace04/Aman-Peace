from tkinter import *
import mysql.connector
from tkinter import messagebox


connection = mysql.connector.connect(host='localhost', user='root', password='6368752',
                                     port='3306', database='amanbms')
cursor = connection.cursor()


def generate_transaction_password():
  
    username = name.get()
    transaction_password = TransactionPassword.get()


    if not all([username, transaction_password]):
        messagebox.showerror("Error", "Please fill in all fields.")
        return

  
    cursor.execute("SELECT * FROM register WHERE username = %s", (username,))
    result = cursor.fetchone()
    if not result:
        messagebox.showerror("Error", "Invalid username.")
        return

    
    insert_query = "INSERT INTO transaction_passwords (username, transaction_password) VALUES (%s, %s)"
    values = (username, transaction_password)
    cursor.execute(insert_query, values)
    connection.commit()

    messagebox.showinfo("Success", "Transaction Password Generated Successfully")
    t.destroy()


t = Tk()
t.title("Generate Transaction Password")
t.geometry('800x700')
t.configure(bg="yellow")


T_Password = Label(t, text="Generate Transaction Password", font=("Arial", 30), bg="Turquoise", fg="brown")
T_Password.place(relx=0.5, rely=0.2, anchor=CENTER)

userName = Label(t, text="Username", font=("Arial", 20), bg="Maroon", fg="white")
userName.place(relx=0.2, rely=0.4, anchor=CENTER)
name = Entry(t, font=("Arial", 15), bg="white", fg="black")
name.place(relx=0.7, rely=0.4, anchor=CENTER)

TransactionPasswordLabel = Label(t, text="Transaction Password", font=("Arial", 20), bg="green", fg="white")
TransactionPasswordLabel.place(relx=0.2, rely=0.48, anchor=CENTER)
TransactionPassword = Entry(t, font=("Arial", 15), bg="white", fg="black", show="*")
TransactionPassword.place(relx=0.7, rely=0.48, anchor=CENTER)

generate_password_button = Button(t, text="Generate Transaction Password", font=("Arial", 20), bg="red", fg="white", command=generate_transaction_password)
generate_password_button.place(relx=0.5, rely=0.57, anchor=CENTER)

t.mainloop()
