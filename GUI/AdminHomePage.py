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
cur_user = data[0][1]

mycursor.execute('SELECT * FROM USERACCOUNTS')
users = mycursor.fetchall()
for user in users:
    if user[0] == cur_user:
        user_name = user[2]

def click():
    print("Clicked")

def AdminDoctorsPage():
    home.withdraw()
    import AdminDoctorsPage
    home.deiconify()

def AdminPatientsPage():
    home.withdraw()
    import AdminPatientsPage
    home.deiconify()
def AdminNonMedPage():
    home.withdraw()
    import AdminNonMedPage
    home.deiconify()
def AdminUsersPage():
    home.withdraw()
    import AdminUsersPage
    home.deiconify()
def AdminPharmacyPage():
    home.withdraw()
    import AdminPharmacyPage
    home.deiconify()
def ProfilePage():
    home.withdraw()
    import ProfilePage
    home.deiconify()

home = Tk()
home.title('EMR')
home.iconbitmap("EMR Symbol.ico")

home.geometry("1216x684")
home.configure(bg = "#fefefe")
canvas = Canvas(
    home,
    bg = "#fefefe",
    height = 684,
    width = 1216,
    relief = "ridge")
canvas.place(x = 0, y = 0)

homebg = PhotoImage(file = "AdminHomePage BG.png", master=home)
background = canvas.create_image(
    608, 342,
    image=homebg)


ProfileIcon = PhotoImage(file = "Profile Icon.png", master=home)
menu1 = Button(home,
    image = ProfileIcon,
    borderwidth = 0,
    command = ProfilePage,
    relief = "flat")

menu1.place(
    x = 20, y = 605,
    width = 88,
    height = 70)


PharmacyIcon = PhotoImage(file = "Pharmacy Icon.png", master=home)
menu3 = Button(home,
    image = PharmacyIcon,
    borderwidth = 0,
    command = AdminPharmacyPage,
    relief = "flat")

menu3.place(
    x = 20, y = 401,
    width = 90,
    height = 61)

UserAccountsIcon = PhotoImage(file = "User Accounts Icon.png", master=home)
menu4 = Button(home,
    image = UserAccountsIcon,
    borderwidth = 0,
    command = AdminUsersPage,
    relief = "flat")

menu4.place(
    x = 20, y = 317,
    width = 91,
    height = 77)

NonMedIcon = PhotoImage(file = "Non Med Icon.png", master=home)
menu5 = Button(home,
    image = NonMedIcon,
    borderwidth = 0,
    command = AdminNonMedPage,
    relief = "flat")

menu5.place(
    x = 20, y = 253,
    width = 91,
    height = 57)

PatientsIcon = PhotoImage(file = "Patients Icon.png", master=home)
menu6 = Button(home,
    image = PatientsIcon,
    borderwidth = 0,
    command = AdminPatientsPage,
    relief = "flat")

menu6.place(
    x = 20, y = 183,
    width = 91,
    height = 63)

DoctorsIcon = PhotoImage(file = "Doctors Icon.png", master=home)
menu7 = Button(home,
    image = DoctorsIcon,
    borderwidth = 0,
    command = AdminDoctorsPage,
    relief = "flat")

menu7.place(
    x = 20, y = 110,
    width = 91,
    height = 63)

canvas.create_text(
    673, 275,
    text = "Welcome",
    fill = "#000000",
    font = ("Lato-Regular", int(24)))

canvas.create_text(
    665, 326,
    text = user_name,
    fill = "#6953d9",
    anchor = CENTER,
    font = ("Lato-Bold", int(50)))

home.resizable(False, False)
home.mainloop()
