from tkinter import *
from tkinter import messagebox

def submit_message():
   
    name_val = name.get()
    email_val = Email.get()
    message_val = message_entry.get("1.0", "end-1c")  

   
    if not all([name_val, email_val, message_val]):
        messagebox.showwarning("Warning", "Please fill in all fields.")
        return

    messagebox.showinfo("Success", "Your message has been submitted successfully. We will contact you as soon as possible.")

t = Tk()
t.title("Contact Us")
t.geometry('800x700')
t.configure(bg="yellow")

Contact = Label(t, text="Contact Us", font=("Arial", 30), bg="Turquoise", fg="brown")
Contact.place(relx=0.5, rely=0.2, anchor=CENTER)

namelabel = Label(t, text="Name", font=("Arial", 20), bg="black", fg="yellow")
namelabel.place(relx=0.2, rely=0.35, anchor=CENTER)
name = Entry(t, font=("Arial", 15), bg="white", fg="black")
name.place(relx=0.7, rely=0.35, anchor=CENTER)

EmailId = Label(t, text="Email Id", font=("Arial", 20), bg="pink", fg="brown")
EmailId.place(relx=0.2, rely=0.43, anchor=CENTER)
Email = Entry(t, font=("Arial", 15), bg="white", fg="black")
Email.place(relx=0.7, rely=0.43, anchor=CENTER)

message_label = Label(t, text="Message:", font=("Arial", 20), bg="maroon", fg="white")
message_label.place(relx=0.2, rely=0.51, anchor=CENTER)
message_entry = Text(t, font=("Arial", 15), height=2, width=20)
message_entry.place(relx=0.7, rely=0.51, anchor=CENTER)

submit = Button(t, text="Submit", font=("Arial", 20), bg="red", fg="white", command=submit_message)
submit.place(relx=0.43, rely=0.65, anchor=CENTER)


t.mainloop()
