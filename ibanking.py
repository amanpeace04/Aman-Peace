from tkinter import *
import mysql.connector
from tkinter import messagebox


def update_internet_banking_status(status):
  
    account_number_val = Account.get()
    email_val = Email.get()
    mobile_val = Mobile.get()
    address_val = Add.get()
    pincode_val = Pin.get()

    if not all([account_number_val, email_val, mobile_val, address_val, pincode_val]):
        messagebox.showwarning("Warning", "Please fill in all fields.")
        return

 
    connection = mysql.connector.connect(host='localhost', user='root', password='6368752',
                                         port='3306', database='amanbms')
    cursor = connection.cursor()

   
    cursor.execute("SELECT * FROM accounts WHERE accno = %s", (account_number_val,))
    result = cursor.fetchone()

    if result:
   
        cursor.execute("UPDATE accounts SET internet_banking = %s WHERE accno = %s", (status, account_number_val))
        connection.commit()

        messagebox.showinfo("Success", f"Internet banking has been {status.lower()}ed successfully.")
    else:
        messagebox.showerror("Error", "Account not found.")

    
    cursor.close()
    connection.close()

t = Tk()
t.title("Internet Banking")
t.geometry('800x700')
t.configure(bg="yellow")

InternetBanking = Label(t, text="Internet Banking", font=("Arial", 30), bg="Turquoise", fg="brown")
InternetBanking.place(relx=0.48, rely=0.15, anchor=CENTER)

AccountNumber = Label(t, text="Account Number", font=("Arial", 20), bg="Black", fg="yellow")
AccountNumber.place(relx=0.2, rely=0.25, anchor=CENTER)
Account = Entry(t, font=("Arial", 15), bg="white", fg="black")
Account.place(relx=0.7, rely=0.25, anchor=CENTER)

EmailId = Label(t, text="Email Id", font=("Arial", 20), bg="pink", fg="brown")
EmailId.place(relx=0.2, rely=0.32, anchor=CENTER)
Email = Entry(t, font=("Arial", 15), bg="white", fg="black")
Email.place(relx=0.7, rely=0.32, anchor=CENTER)

Mobileno = Label(t, text="Mobile", font=("Arial", 20), bg="Magenta", fg="white")
Mobileno.place(relx=0.2, rely=0.39, anchor=CENTER)
Mobile = Entry(t, font=("Arial", 15), bg="white", fg="black")
Mobile.place(relx=0.7, rely=0.39, anchor=CENTER)

Address = Label(t, text="Address", font=("Arial", 20), bg="Maroon", fg="white")
Address.place(relx=0.2, rely=0.46, anchor=CENTER)
Add = Entry(t, font=("Arial", 15), bg="white", fg="black")
Add.place(relx=0.7, rely=0.46, anchor=CENTER)

PinCode = Label(t, text="Pin Code", font=("Arial", 20), bg="red", fg="white")
PinCode.place(relx=0.2, rely=0.53, anchor=CENTER)
Pin = Entry(t, font=("Arial", 15), bg="white", fg="black")
Pin.place(relx=0.7, rely=0.53, anchor=CENTER)


activate_button = Button(t, text="Activate", font=("Arial", 20), bg="green", fg="white", command=lambda: update_internet_banking_status("Activated"))
activate_button.place(relx=0.2, rely=0.65, anchor=CENTER)


deactivate_button = Button(t, text="Deactivate", font=("Arial", 20), bg="green", fg="white", command=lambda: update_internet_banking_status("Deactivated"))
deactivate_button.place(relx=0.7, rely=0.65, anchor=CENTER)

t.mainloop()
