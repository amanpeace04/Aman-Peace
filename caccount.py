from tkinter import *
from tkinter import messagebox
import mysql.connector

t = Tk()
t.title("Create Account")
t.geometry('800x700')
t.configure(bg="yellow")

connection = mysql.connector.connect(host='localhost', user='root', password='6368752',
                                     port='3306', database='amanbms')
c = connection.cursor()

def insertdata():
    name_val = name.get()
    accno_val = accno_entry.get()  
    mobile_val = Mobile.get()
    address_val = Address.get()
    pincode_val = PinCode.get()
    acctype_val = acctype.get()
    transaction_password_val = transaction_password_entry.get()  # Getting transaction password

    if not all([name_val, accno_val, mobile_val, address_val, pincode_val, acctype_val, transaction_password_val]):
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    
    c.execute("SELECT * FROM register WHERE accno = %s", (accno_val,))
    result = c.fetchone()
    if not result:
       
        messagebox.showerror("Error", "Invalid Account Number. Please check and try again.")
        return

 
    if acctype_val == "Saving":
        bal = 1000
    else:
        bal = 5000

    c.execute("INSERT INTO accounts (accno, name, mobile, address, pincode, acctype, balance, transaction_password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
              (accno_val, name_val, mobile_val, address_val, pincode_val, acctype_val, bal, transaction_password_val))
    connection.commit()
    messagebox.showinfo("Success", "Account Created Successfully. Your initial balance is: {}".format(bal))
    t.destroy()

CreateAccount = Label(t, text="Create Account", font=("Arial", 30), bg="Turquoise", fg="brown")
CreateAccount.place(relx=0.5, rely=0.2, anchor=CENTER)

namelabel = Label(t, text="Name", font=("Arial", 20), bg="Black", fg="yellow")
namelabel.place(relx=0.2, rely=0.3, anchor=CENTER)
name = Entry(t, font=("Arial", 15), bg="white", fg="black")
name.place(relx=0.7, rely=0.3, anchor=CENTER)

accno_label = Label(t, text="Account Number", font=("Arial", 20), bg="blue", fg="white")
accno_label.place(relx=0.2, rely=0.38, anchor=CENTER)
accno_entry = Entry(t, font=("Arial", 15), bg="white", fg="black")
accno_entry.place(relx=0.7, rely=0.38, anchor=CENTER)

Mobileno = Label(t, text="Mobile", font=("Arial", 20), bg="green", fg="white")
Mobileno.place(relx=0.2, rely=0.46, anchor=CENTER)
Mobile = Entry(t, font=("Arial", 15), bg="white", fg="black")
Mobile.place(relx=0.7, rely=0.46, anchor=CENTER)

Add = Label(t, text="Address", font=("Arial", 20), bg="Maroon", fg="white")
Add.place(relx=0.2, rely=0.54, anchor=CENTER)
Address = Entry(t, font=("Arial", 15), bg="white", fg="black")
Address.place(relx=0.7, rely=0.54, anchor=CENTER)

Pin = Label(t, text="Pin Code", font=("Arial", 20), bg="Magenta", fg="white")
Pin.place(relx=0.2, rely=0.62, anchor=CENTER)
PinCode = Entry(t, font=("Arial", 15), bg="white", fg="black")
PinCode.place(relx=0.7, rely=0.62, anchor=CENTER)

transaction_password_label = Label(t, text="Transaction Password", font=("Arial", 20), bg="orange", fg="red")
transaction_password_label.place(relx=0.2, rely=0.7, anchor=CENTER)
transaction_password_entry = Entry(t, font=("Arial", 15), bg="white", fg="black", show="*")
transaction_password_entry.place(relx=0.7, rely=0.7, anchor=CENTER)

atype = Label(t, text="Acc Type", font=("Arial", 20), bg="maroon", fg="white")
atype.place(relx=0.2, rely=0.78, anchor=CENTER)
acctype = StringVar(t)
acctype.set("Saving") 
acctype_menu = OptionMenu(t, acctype, "Saving", "Current")
acctype_menu.config(font=("Arial", 15), bg="black", fg="yellow")
acctype_menu.place(relx=0.7, rely=0.78, anchor=CENTER)

CreateAccount = Button(t, text="Create Account", font=("Arial", 20), bg="red", fg="white", command=insertdata)
CreateAccount.place(relx=0.45, rely=0.88, anchor=CENTER)

t.mainloop()

