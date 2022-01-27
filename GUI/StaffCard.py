from tkinter import *

def UpdateCard():
    command = "update Selected set id = '" + str(sel_staff[0]) + "' where no = 1"
    mycursor.execute(command)
    window.destroy()
    import UpdateDoctorCard

def click():
    print("Button is Clicked")

def AdminNonMedPage():
    window.destroy()
    import AdminNonMedPage

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

bg = PhotoImage(file = f"DoctorCardBG.png")
background = canvas.create_image(
    608, 342,
    image=bg)

ProfileIcon = PhotoImage(file = f"Profile Icon.png")
b1 = Button(
    image = ProfileIcon,
    borderwidth = 0,
    command = click,
    relief = "flat")

b1.place(
    x = 20, y = 605,
    width = 88,
    height = 70)

CashierIcon = PhotoImage(file = f"Cashier Icon.png")
b2 = Button(
    image = CashierIcon,
    borderwidth = 0,
    command = click,
    relief = "flat")

b2.place(
    x = 20, y = 467,
    width = 90,
    height = 75)

PharmacyIcon = PhotoImage(file = f"Pharmacy Icon.png")
b3 = Button(
    image = PharmacyIcon,
    borderwidth = 0,
    command = click,
    relief = "flat")

b3.place(
    x = 20, y = 401,
    width = 90,
    height = 61)

UserAccountsIcon = PhotoImage(file = f"User Accounts Icon.png")
b4 = Button(
    image = UserAccountsIcon,
    borderwidth = 0,
    command = click,
    relief = "flat")

b4.place(
    x = 20, y = 317,
    width = 91,
    height = 77)

NonMedIcon = PhotoImage(file = f"Non Med Icon.png")
b5 = Button(
    image = NonMedIcon,
    borderwidth = 0,
    command = click,
    relief = "flat")

b5.place(
    x = 20, y = 253,
    width = 91,
    height = 57)

PatientsIcon = PhotoImage(file = f"Patients Icon.png")
b6 = Button(
    image = PatientsIcon,
    borderwidth = 0,
    command = click,
    relief = "flat")

b6.place(
    x = 20, y = 183,
    width = 91,
    height = 63)

DoctorsIcon = PhotoImage(file = f"Doctors Icon HL.png")
b7 = Button(
    image = DoctorsIcon,
    borderwidth = 0,
    command = click,
    relief = "flat")

b7.place(
    x = 20, y = 114,
    width = 91,
    height = 67)

PrevPage = PhotoImage(file = f"ArrowLeft.png")
b8 = Button(
    image = PrevPage,
    borderwidth = 0,
    command = AdminSelNonMed,
    relief = "flat")

b8.place(
    x = 140, y = 30,
    width = 28,
    height = 24)

UpdateButton = PhotoImage(file = f"Update.png")
b9 = Button(
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
    sel_staffid = int(d[2])


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
    MaleIcon = PhotoImage(file = f"Male Profile Pic.png")
    canvas.create_image(
        260, 130,
        image = MaleIcon)
elif sel_staff[3] == 'Female':
    FemaleIcon = PhotoImage(file=f"Female Profile Pic.png")
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

#Room
canvas.create_text(
    300, 441.0,
    text = "4B",
    fill = "#000000",
    anchor = 'w',
    font = ("Lato-Light", int(14.0)))

#Join Date
canvas.create_text(
    320, 525.0,
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
    if sel_staff[4] == dept[1]:
        sel_deptname = dept[1]
canvas.create_text(
    570, 525,
    text = sel_deptname,
    fill = "#000000",
    anchor = 'w',
    font = ("Lato-Light", int(14.0)))

canvas.create_text(
    901.0, 249.0,
    text = "Lisa Jenkins",
    fill = "#000000",
    font = ("Lato-Light", int(20.0)))

canvas.create_text(
    901.0, 208.0,
    text = "Clay Rigby",
    fill = "#000000",
    font = ("Lato-Light", int(20.0)))

TextBoximg = PhotoImage(file = f"TextBox2.png")
TextBox = canvas.create_image(
    986.5, 120.0,
    image = TextBoximg)

TextBox = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

TextBox.place(
    x = 834.0, y = 101,
    width = 305.0,
    height = 38)


SearchIcon = PhotoImage(file = f"Search Icon.png")
b0 = Button(
    image = SearchIcon,
    bd = 0,
    command = click,
    relief = "flat")

b0.place(
    x = 1120, y = 105,
    width=28,
    height=28)

def search():
    name_search = TextBox.get()
    print(name_search)


window.resizable(False, False)
window.mainloop()
