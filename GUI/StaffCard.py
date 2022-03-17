from tkinter import *

def UpdateCard():
    command = "update Selected set cur_id = '" + str(sel_staff[0]) + "' where no = 1"
    mycursor.execute(command)
    window.destroy()
    import UpdateStaffCard

def gohome():
    window.destroy()
    import AdminHomePage

def click():
    print("Button is Clicked")

def AdminSelNonMed():
    window.destroy()
    import AdminSelNonMed

import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'maneeshj',
    port = '3306',
    database = 'EMR')
mycursor = mydb.cursor()

window = Tk()
window.title('EMR')
window.iconbitmap("EMR Symbol.ico")

window.geometry("1216x684")
window.configure(bg = "#fefefe")
canvas = Canvas(
    window,
    bg = "#fefefe",
    height = 684,
    width = 1216,
    relief = "ridge")
canvas.place(x = 0, y = 0)

bg = PhotoImage(file = "StaffCardBG.png", master = window)
background = canvas.create_image(
    608, 342,
    image=bg)

Homebutton = PhotoImage(file = f"Home Button.png", master = window)
b0 = Button(window,
    image = Homebutton,
    borderwidth = 0,
    highlightthickness = 0,
    command = gohome,
    relief = "flat")

b0.place(
    x = 20, y = 116,
    width = 95,
    height = 400)

UpdateButton = PhotoImage(file = "Update.png", master = window)
b9 = Button(window,
    image = UpdateButton,
    borderwidth = 0,
    command = UpdateCard,
    relief = "flat")

b9.place(
    x = 631, y = 605,
    width = 113,
    height = 39)

#Fetch data
mycursor.execute('SELECT * FROM SELECTED')
data = mycursor.fetchall()
for d in data:
    sel_staffid = int(d[3])


mycursor.execute('SELECT * FROM NONMEDSTAFF')
nonmedstaff = mycursor.fetchall()
for staff in nonmedstaff:
    if staff[0] == sel_staffid:
        sel_staff = staff

#Doctor Name
canvas.create_text(
    350, 120.0,
    text = sel_staff[1],
    fill = "#000000",
    anchor = 'w',
    font = ("Lato-Bold", int(30)))

#Doctor ID
canvas.create_text(
    350, 159.0,
    text = sel_staff[0],
    fill = "#000000",
    anchor = 'w',
    font = ("Lato-Regular", int(20.0)))

#Profile Picture

if sel_staff[3] == 'Male':
    MaleIcon = PhotoImage(file = "Male Profile Pic.png", master = window)
    canvas.create_image(
        260, 130,
        image = MaleIcon)
elif sel_staff[3] == 'Female':
    FemaleIcon = PhotoImage(file=f"Female Profile Pic.png", master = window)
    canvas.create_image(
        260, 130,
        image=FemaleIcon)

#Age
canvas.create_text(
    300, 263.0,
    text = sel_staff[2],
    fill = "#000000",
    anchor = 'w',
    font = ("Lato-Light", int(14.0)))

#Gender
canvas.create_text(
    300, 353.0,
    text = sel_staff[3],
    fill = "#000000",
    anchor = 'w',
    font = ("Lato-Light", int(14.0)))


#Join Date
canvas.create_text(
    320, 440,
    text = sel_staff[7],
    fill = "#000000",
    anchor = 'w',
    font = ("Lato-Light", int(14.0)))

#Phone No.
canvas.create_text(
    540, 263.0,
    text = sel_staff[5],
    fill = "#000000",
    anchor = 'w',
    font = ("Lato-Light", int(14.0)))

#E-Mail
canvas.create_text(
    540, 353.0,
    text = sel_staff[6],
    fill = "#000000",
    anchor = 'w',
    font = ("Lato-Light", int(14.0)))

#Salary
canvas.create_text(
    540, 441.0,
    text = sel_staff[8],
    fill = "#000000",
    anchor = 'w',
    font = ("Lato-Light", int(14.0)))

#Department
mycursor.execute('SELECT * FROM NONMEDDEPT')
depts = mycursor.fetchall()
for dept in depts:
    if sel_staff[4] == dept[0]:
        sel_deptname = dept[1]
canvas.create_text(
    570, 525,
    text = sel_deptname,
    fill = "#000000",
    anchor = 'w',
    font = ("Lato-Light", int(14.0)))

window.resizable(False, False)
window.mainloop()
