from tkinter import *

def click():
    print("Button Clicked")

import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'maneeshj',
    port = '3306',
    database = 'EMR')
mycursor = mydb.cursor()

mycursor.execute('SELECT * FROM SELECTED')
data = mycursor.fetchall()
for d in data:
    sel_patientid = int(d[3])
    cardtype = 'update'

def update():
    command = "update patients set name = '" + str(name_entry.get()) + "' where id = "+ str(sel_patientid)+";"
    mycursor.execute(command)
    command = "update patients set DOB = " + str(dob_entry.get()) + " where id = "+ str(sel_patientid)
    mycursor.execute(command)
    command = "update patients set phone = '" + str(phone_entry.get()) + "' where id = "+ str(sel_patientid)
    mycursor.execute(command)
    command = "update patients set gender = '" + str(gender_entry.get()) + "' where id = "+ str(sel_patientid)
    mycursor.execute(command)
    command = "update patients set email = '" + str(email_entry.get()) + "' where id = "+ str(sel_patientid)
    mycursor.execute(command)
    command = "update patients set joindate = '" + str(reg_entry.get()) + "' where id = "+ str(sel_patientid)
    mycursor.execute(command)
    mydb.commit()

def cancel():
    root.destroy()
    import PatientCard

root = Tk()
root.title('Update Patient Details')
root.iconbitmap("EMR Symbol.ico")

root.geometry("535x590")
root.configure(bg = "#ffffff")
canvas = Canvas(
    root,
    bg = "#ffffff",
    height = 590,
    width = 535,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"UpdatePatientCard BG.png")
background = canvas.create_image(
    267.5, 276.0,
    image=background_img)

mycursor.execute('SELECT * FROM PATIENTS')
patients = mycursor.fetchall()
for patient in patients:
    if patient[0] == sel_patientid:
        sel_doc = patient

Updateimg = PhotoImage(file = f"UpdateButton.png")
b1 = Button(
    image = Updateimg,
    borderwidth = 0,
    highlightthickness = 0,
    command = update,
    relief = "flat")

b1.place(
    x = 208, y = 500,
    width = 138,
    height = 53)

CancelImg = PhotoImage(file = f"Cancel Button.png")
b2 = Button(
    image = CancelImg,
    borderwidth = 0,
    highlightthickness = 0,
    command = cancel,
    relief = "flat")

b2.place(
    x = 235, y = 550,
    width = 89,
    height = 17)

name_entryimg = PhotoImage(file = f"TextBox4.png")
name_entry = canvas.create_image(
    268.0, 163.5,
    image = name_entryimg)

name_entry = Entry(
    bd = 0,
    highlightthickness = 0)

name_entry.place(
    x = 69.5, y = 150,
    width = 397.0,
    height = 29)

gender_entryimg = PhotoImage(file = f"TextBox5.png")
gender_entry = canvas.create_image(
    122.0, 243.5,
    image = gender_entryimg)

gender_entry = Entry(
    bd = 0,
    highlightthickness = 0)

gender_entry.place(
    x = 69.5, y = 230,
    width = 105.0,
    height = 29)

height_entryimg = PhotoImage(file = f"TextBox5.png")
phone_entry = canvas.create_image(
    269.0, 243.5,
    image = height_entryimg)

height_entry = Entry(
    bd = 0,
    highlightthickness = 0)

height_entry.place(
    x = 216.5, y = 230,
    width = 105.0,
    height = 29)

weight_entryimg = PhotoImage(file = f"TextBox5.png")
weight_entry = canvas.create_image(
    416.0, 243.5,
    image = weight_entryimg)

weight_entry = Entry(
    bd = 0,
    highlightthickness = 0)

weight_entry.place(
    x = 363.5, y = 230,
    width = 105.0,
    height = 29)

dob_entryimg = PhotoImage(file = f"TextBox3.png")
dob_entry = canvas.create_image(
    148.5, 323.5,
    image = dob_entryimg)

dob_entry = Entry(
    bd = 0,
    highlightthickness = 0)

dob_entry.place(
    x = 69.5, y = 310,
    width = 158.0,
    height = 29)

reg_entryimg = PhotoImage(file = f"TextBox3.png")
reg_entry = canvas.create_image(
    381.0, 323.5,
    image = reg_entryimg)

reg_entry = Entry(
    bd = 0,
    highlightthickness = 0)

reg_entry.place(
    x = 295.5, y = 310,
    width = 171.0,
    height = 29)

phone_entryimg = PhotoImage(file = f"TextBox3.png")
phone_entry = canvas.create_image(
    148.5, 403.5,
    image = phone_entryimg)

phone_entry = Entry(
    bd = 0,
    highlightthickness = 0)

phone_entry.place(
    x = 69.5, y = 390,
    width = 158.0,
    height = 29)

email_entryimg = PhotoImage(file = f"TextBox3.png")
email_entry = canvas.create_image(
    383.5, 403.5,
    image = email_entryimg)

email_entry = Entry(
    bd = 0,
    highlightthickness = 0)

email_entry.place(
    x = 300.5, y = 390,
    width = 166.0,
    height = 29)

allergies_entryimg = PhotoImage(file = f"TextBox4.png")
allergies_entry = canvas.create_image(
    270, 483,
    image = allergies_entryimg)

allergies_entry = Entry(
    bd = 0,
    highlightthickness = 0)

allergies_entry.place(
    x = 69.5, y = 469,
    width=397.0,
    height=29)

if cardtype == 'update':
    name_entry.insert(0, sel_doc[1])
    dob_entry.insert(0, sel_doc[2])
    gender_entry.insert(0, sel_doc[3])
    height_entry.insert(0, sel_doc[4])
    weight_entry.insert(0, sel_doc[5])
    phone_entry.insert(0, sel_doc[6])
    email_entry.insert(0, sel_doc[7])
    reg_entry.insert(0, sel_doc[8])
    allergies_entry.insert(0, sel_doc[9])


root.resizable(False, False)
root.mainloop()
