from tkinter import *
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
    sel_staffid = int(d[3])
    node = (d[4])

def add():
    rec = [name_entry.get(),age_entry.get(),phone_entry.get(),phone_entry.get(),
           gender_entry.get(),email_entry.get(),dept_entry.get(),join_entry.get,
           salary_entry.get()]
    mycursor.execute("insert into nonmedstaff values(%s)",rec)

def update():
    command = "update nonmedstaff set name = '" + str(name_entry.get()) + "' where id = "+ str(sel_staffid)+";"
    mycursor.execute(command)
    command = "update nonmedstaff set age = " + str(age_entry.get()) + " where id = "+ str(sel_staffid)
    mycursor.execute(command)
    command = "update nonmedstaff set phone = '" + str(phone_entry.get()) + "' where id = "+ str(sel_staffid)
    mycursor.execute(command)
    command = "update nonmedstaff set gender = '" + str(gender_entry.get()) + "' where id = "+ str(sel_staffid)
    mycursor.execute(command)
    command = "update nonmedstaff set email = '" + str(email_entry.get()) + "' where id = "+ str(sel_staffid)
    mycursor.execute(command)

    mycursor.execute('SELECT * FROM nonmeddept')
    depts = mycursor.fetchall()
    for dept in depts:
        if str(dept_entry.get()) == dept[1]:
            command = "update nonmedstaff set deptid = " + str(dept[0]) + " where id = "+ str(sel_staffid)
    mycursor.execute(command)

    command = "update nonmedstaff set salary = '" + str(salary_entry.get()) + "' where id = "+ str(sel_staffid)
    mycursor.execute(command)
    
    command = "update nonmedstaff set joindate = '" + str(join_entry.get()) + "' where id = "+ str(sel_staffid)
    mycursor.execute(command)
    mydb.commit()
    root.destroy()
    import StaffCard

root = Tk()
root.title('Update Doctor Details')
root.iconbitmap("EMR Symbol.ico")

root.geometry("551x568")
root.configure(bg = "#ffffff")
canvas = Canvas(
    root,
    bg = "#ffffff",
    height = 568,
    width = 551,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = "UpdateStaffCardBG.png")
background = canvas.create_image(
    275.5, 284.0,
    image=background_img)

mycursor.execute('SELECT * FROM nonmedstaff')
nonmedstaff = mycursor.fetchall()
for doctor in nonmedstaff:
    if doctor[0] == sel_staffid:
        sel_staff = doctor

name_entryimg = PhotoImage(file = "TextBox4.png")
name_entry = canvas.create_image(
    276.0, 132.5,
    image = name_entryimg)

name_entry = Entry(
    bd = 0,
    highlightthickness = 0)
name_entry.place(
    x = 77.5, y = 119,
    width = 397.0,
    height = 29)

age_entryimg = PhotoImage(file = "TextBox3.png")
age_entry = canvas.create_image(
    156.5, 212.5,
    image = age_entryimg)

age_entry = Entry(
    bd = 0,
    highlightthickness = 0)
age_entry.place(
    x = 77.5, y = 199,
    width = 158.0,
    height = 29)

phone_entryimg = PhotoImage(file = "TextBox3.png")
phone_entry = canvas.create_image(
    156.5, 292.5,
    image = phone_entryimg)

phone_entry = Entry(
    bd = 0,
    highlightthickness = 0)
phone_entry.place(
    x = 77.5, y = 279,
    width = 158.0,
    height = 29)

gender_entryimg = PhotoImage(file = "TextBox3.png")
gender_entry = canvas.create_image(
    389.0, 212.5,
    image = gender_entryimg)

gender_entry = Entry(
    bd = 0,
    highlightthickness = 0)
gender_entry.place(
    x = 303.5, y = 199,
    width = 171.0,
    height = 29)

email_entryimg = PhotoImage(file = "TextBox3.png")
email_entry = canvas.create_image(
    389.0, 292.5,
    image = email_entryimg)

email_entry = Entry(
    bd = 0,
    highlightthickness = 0)
email_entry.place(
    x = 303.5, y = 279,
    width = 171.0,
    height = 29)

mycursor.execute('SELECT * FROM nonmeddept')
depts = mycursor.fetchall()
for dept in depts:
    if sel_staff[4] == dept[0]:
        sel_deptname = dept[1]

dept_entryimg = PhotoImage(file = "TextBox3.png")
dept_entry = canvas.create_image(
    156.5, 372.5,
    image = dept_entryimg)

dept_entry = Entry(
    bd = 0,
    highlightthickness = 0)
dept_entry.place(
    x = 77.5, y = 359,
    width = 158.0,
    height = 29)

join_entryimg = PhotoImage(file = "TextBox3.png")
join_entry = canvas.create_image(
    156.5, 452.5,
    image = join_entryimg)

join_entry = Entry(
    bd = 0,
    highlightthickness = 0)
join_entry.place(
    x = 77.5, y = 439,
    width = 158.0,
    height = 29)

salary_entryimg = PhotoImage(file = "TextBox3.png")
salary_entry = canvas.create_image(
    391.5, 372.5,
    image = salary_entryimg)

salary_entry = Entry(
    bd = 0,
    highlightthickness = 0)
salary_entry.place(
    x = 308.5, y = 359,
    width = 166.0,
    height = 29)


img0 = PhotoImage(file = "UpdateButton.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = update,
    relief = "flat")

b0.place(
    x = 208, y = 489,
    width = 138,
    height = 53)
if mode == 'update':
    name_entry.insert(0, sel_staff[1])
    age_entry.insert(0, sel_staff[2])
    phone_entry.insert(0, sel_staff[5])
    gender_entry.insert(0, sel_staff[3])
    email_entry.insert(0, sel_staff[6])
    dept_entry.insert(0, sel_deptname)
    join_entry.insert(0, sel_staff[7])
    salary_entry.insert(0, sel_staff[8])

root.resizable(False, False)
root.mainloop()
