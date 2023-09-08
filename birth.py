from tkinter import *
from PIL import ImageTk, Image
import sqlite3
from tkinter import ttk  # Import the ttk module for Treeview

root = Tk()
root.title("Birth.LSGD")
root.iconbitmap(r'd:\Internship@IKM\gov.ico')
root.geometry("500x600")

# creating database
con = sqlite3.connect('birth_reg.db')

my_img = ImageTk.PhotoImage(Image.open("logo.png"))
my_label = Label(image=my_img)
my_label.grid(row=0, column=0, columnspan=3)

myLabel2 = Label(root, text="Application for Registration of Birth")
myLabel2.grid(row=5, column=0, columnspan=3)

myLabel3 = Label(root, text="   ")
myLabel3.grid(row=6, column=1)

# cursor
c = con.cursor()

# create table if it doesn't exist
c.execute("""CREATE TABLE IF NOT EXISTS data (
        name_of_child text,
        dob text,
        name_of_mother text,
        name_of_father text,
        place_of_birth text,
        address text
        )""")
con.commit()

# submit fun
def submit():
    # creating database
    con = sqlite3.connect('birth_reg.db')
    # cursor
    c = con.cursor()

    # store into table
    c.execute("INSERT INTO data VALUES (:name_of_child, :dob, :name_of_mother, :name_of_father, :place_of_birth, :address)",
              {
                  'name_of_child': name_of_child.get(),
                  'dob': dob.get(),
                  'name_of_mother': name_of_mother.get(),
                  'name_of_father': name_of_father.get(),
                  'place_of_birth': place_of_birth.get(),
                  'address': address.get()
              }
              )

    # commit changes
    con.commit()

    # close connection
    con.close()

    # clear text box
    name_of_child.delete(0, END)
    dob.delete(0, END)
    name_of_mother.delete(0, END)
    name_of_father.delete(0, END)
    place_of_birth.delete(0, END)
    address.delete(0, END)

# query function
def query():
    # connect db
    conn = sqlite3.connect('birth_reg.db')

    # cursor
    c = conn.cursor()

    # query
    c.execute("SELECT * FROM data")
    records = c.fetchall()

    # Create a table (Treeview widget) to display the records
    record_table = ttk.Treeview(root, columns=("Name", "DOB", "Mother's Name", "Father's Name", "Place of Birth", "Address"))
    
    # Define column headings
    record_table.heading("#1", text="Name")
    record_table.heading("#2", text="DOB")
    record_table.heading("#3", text="Mother's Name")
    record_table.heading("#4", text="Father's Name")
    record_table.heading("#5", text="Place of Birth")
    record_table.heading("#6", text="Address")

    # Insert data into the table
    for record in records:
        record_table.insert("", "end", values=record)

    record_table.grid(row=16, column=0, columnspan=2)

    # close connection
    conn.close()

# text boxes
name_of_child = Entry(root, width=30)
name_of_child.grid(row=7, column=1, padx=20)
dob = Entry(root, width=30)
dob.grid(row=8, column=1)
name_of_mother = Entry(root, width=30)
name_of_mother.grid(row=9, column=1)
name_of_father = Entry(root, width=30)
name_of_father.grid(row=10, column=1)
place_of_birth = Entry(root, width=30)
place_of_birth.grid(row=11, column=1)
address = Entry(root, width=30)
address.grid(row=12, column=1)

# text box labels
name_of_child_label = Label(root, text="Enter Child's name: ")
name_of_child_label.grid(row=7, column=0)
dob_label = Label(root, text="DOB (DDMMYYYY): ")
dob_label.grid(row=8, column=0)
name_of_mother_label = Label(root, text="Enter Mother's name: ")
name_of_mother_label.grid(row=9, column=0)
name_of_father_label = Label(root, text="Enter Father's name: ")
name_of_father_label.grid(row=10, column=0)
place_of_birth_label = Label(root, text="Enter Place of Birth: ")
place_of_birth_label.grid(row=11, column=0)
address_label = Label(root, text="Enter Address: ")
address_label.grid(row=12, column=0)

# submit button
myButton = Button(root, text="SUBMIT", command=submit)
myButton.grid(row=13, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# query button
query_btn = Button(root, text="Show records", command=query)
query_btn.grid(row=15, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

root.mainloop()