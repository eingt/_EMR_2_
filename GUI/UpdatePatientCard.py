from tkinter import *

def btn_clicked():
    print("Button is Clicked")

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

def update():
    command = "update patients set name = '" + str(name_entry.get()) + "' where id = "+ str(sel_paientid)+";"
    mycursor.execute(command)
    command = "update patients set DOB = " + str(dob_entry.get()) + " where id = "+ str(sel_paientid)
    mycursor.execute(command)
    command = "update patients set phone = '" + str(phone_entry.get()) + "' where id = "+ str(sel_paientid)
    mycursor.execute(command)
    command = "update patients set gender = '" + str(gender_entry.get()) + "' where id = "+ str(sel_paientid)
    mycursor.execute(command)
    command = "update patients set email = '" + str(email_entry.get()) + "' where id = "+ str(sel_paientid)
    mycursor.execute(command)


    command = "update patients set joindate = '" + str(join_entry.get()) + "' where id = "+ str(sel_paientid)
    mycursor.execute(command)
    mydb.commit()

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

updateimg = PhotoImage(file = f"UpdateButton.png")
b1 = Button(
    image = updateimg,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 199, y = 520,
    width = 138,
    height = 53)

entry0_img = PhotoImage(file = f"TextBox4.png")
entry0_bg = canvas.create_image(
    268.0, 163.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    highlightthickness = 0)

entry0.place(
    x = 69.5, y = 150,
    width = 397.0,
    height = 29)

entry1_img = PhotoImage(file = f"TextBox5.png")
entry1_bg = canvas.create_image(
    122.0, 243.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    highlightthickness = 0)

entry1.place(
    x = 69.5, y = 230,
    width = 105.0,
    height = 29)

entry2_img = PhotoImage(file = f"TextBox5.png")
entry2_bg = canvas.create_image(
    269.0, 243.5,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    highlightthickness = 0)

entry2.place(
    x = 216.5, y = 230,
    width = 105.0,
    height = 29)

entry3_img = PhotoImage(file = f"TextBox5.png")
entry3_bg = canvas.create_image(
    416.0, 243.5,
    image = entry3_img)

entry3 = Entry(
    bd = 0,
    highlightthickness = 0)

entry3.place(
    x = 363.5, y = 230,
    width = 105.0,
    height = 29)

entry4_img = PhotoImage(file = f"TextBox3.png")
entry4_bg = canvas.create_image(
    148.5, 323.5,
    image = entry4_img)

entry4 = Entry(
    bd = 0,
    highlightthickness = 0)

entry4.place(
    x = 69.5, y = 310,
    width = 158.0,
    height = 29)

entry5_img = PhotoImage(file = f"TextBox3.png")
entry5_bg = canvas.create_image(
    381.0, 323.5,
    image = entry5_img)

entry5 = Entry(
    bd = 0,
    highlightthickness = 0)

entry5.place(
    x = 295.5, y = 310,
    width = 171.0,
    height = 29)

entry6_img = PhotoImage(file = f"TextBox3.png")
entry6_bg = canvas.create_image(
    148.5, 403.5,
    image = entry6_img)

entry6 = Entry(
    bd = 0,
    highlightthickness = 0)

entry6.place(
    x = 69.5, y = 390,
    width = 158.0,
    height = 29)

entry7_img = PhotoImage(file = f"TextBox3.png")
entry7_bg = canvas.create_image(
    383.5, 403.5,
    image = entry7_img)

entry7 = Entry(
    bd = 0,
    highlightthickness = 0)

entry7.place(
    x = 300.5, y = 390,
    width = 166.0,
    height = 29)

entry8_img = PhotoImage(file = f"TextBox4.png")
entry8_bg = canvas.create_image(
    270, 483,
    image = entry8_img)

entry8 = Entry(
    bd = 0,
    highlightthickness = 0)

entry8.place(
    x = 69.5, y = 469,
    width=397.0,
    height=29)

root.resizable(False, False)
root.mainloop()
