from tkinter import *
import mysql.connector
from tkinter import messagebox

t = Tk()
t.title("Deposit")
t.geometry('800x700')
t.configure(bg="yellow")

connection = mysql.connector.connect(host='localhost', user='root', password='6368752',
                                     port='3306', database='amanbms')

c = connection.cursor()
def insertdata():
    AccNo_val = Account.get()
    email_val = Email.get()
    mobile_val = Mobile.get()
    amount_val = Amount1.get()
    amount_words_val = Amount2.get()
    
    c.execute("INSERT INTO accounts (account_number, email, mobile, amount, amount_words) VALUES (%s, %s, %s, %s, %s)",
              (AccNo_val, email_val, mobile_val, amount_val, amount_words_val))
    connection.commit()
    
    messagebox.showinfo("Success", "Account Created Successfully")
    t.destroy()


Deposit = Label(t, text="Deposit", font=("Arial", 30), bg="Turquoise", fg="brown")
Deposit.place(relx=0.5, rely=0.2, anchor=CENTER)

AccountNumber = Label(t, text="Account Number", font=("Arial", 20), bg="Black", fg="yellow")
AccountNumber.place(relx=0.2, rely=0.35, anchor=CENTER)
Account = Entry(t, font=("Arial", 15), bg="white", fg="black")
Account.place(relx=0.7, rely=0.35, anchor=CENTER)

EmailId = Label(t, text="Email Id", font=("Arial", 20), bg="pink", fg="brown")
EmailId.place(relx=0.2, rely=0.43, anchor=CENTER)
Email = Entry(t, font=("Arial", 15), bg="white", fg="black")
Email.place(relx=0.7, rely=0.43, anchor=CENTER)

Mobileno = Label(t, text="Mobile", font=("Arial", 20), bg="Magenta", fg="white")
Mobileno.place(relx=0.2, rely=0.5, anchor=CENTER)
Mobile = Entry(t, font=("Arial", 15), bg="white", fg="black")
Mobile.place(relx=0.7, rely=0.5, anchor=CENTER)

Amountdeposit = Label(t, text="Amount in figures", font=("Arial", 20), bg="Maroon", fg="white")
Amountdeposit.place(relx=0.2, rely=0.57, anchor=CENTER)
Amount1 = Entry(t, font=("Arial", 15), bg="white", fg="black")
Amount1.place(relx=0.7, rely=0.57, anchor=CENTER)

Amountdeposit_words = Label(t, text="Amount in words", font=("Arial", 20), bg="red", fg="white")
Amountdeposit_words.place(relx=0.2, rely=0.64, anchor=CENTER)
Amount2 = Entry(t, font=("Arial", 15), bg="white", fg="black")
Amount2.place(relx=0.7, rely=0.64, anchor=CENTER)


deposit_button = Button(t, text="Deposit", font=("Arial", 20), bg="green", fg="white", command=insertdata)
deposit_button.place(relx=0.5, rely=0.8, anchor=CENTER)

t.mainloop()
