from tkinter import *
import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'maneeshj',
    port = '3306',
    database = 'EMR'
)

mycursor = mydb.cursor()

def click():
    print("Clicked")

def gohome():
    window.destroy()
    import AdminHomePage

def AdminDoctorsPage():
    window.destroy()
    import AdminDoctorsPage

def AdminPatientsPage():
    window.destroy()
    import AdminPatientsPage

def AdminNonMedPage():
    window.destroy()
    import AdminNonMedPage

def AdminUsersPage():
    window.destroy()
    import AdminUsersPage

def AdminPharmacyPage():
    window.destroy()
    import AdminPharmacyPage

def ProfilePage():
    window.destroy()
    import ProfilePage

def AdminHomePage():
    window.destroy()
    import AdminHomePage

def AdminSelNonMed():
    window.destroy()
    import AdminSelNonMed


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

bg = PhotoImage(file = "AdminNonMedPage BG.png", master=window)
background = canvas.create_image(
    608.0, 342.0,
    image=bg)

Homebutton = PhotoImage(file = f"Home Button.png", master=window)
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

'''
ProfileIcon = PhotoImage(file = "Profile Icon.png", master=window)
b1 = Button(window,
    image = ProfileIcon,
    borderwidth = 0,
    command = ProfilePage,
    relief = "flat")

b1.place(
    x = 20, y = 605,
    width = 88,
    height = 70)

CashierIcon = PhotoImage(file = "Cashier Icon.png", master=window)
b2 = Button(window,
    image = CashierIcon,
    borderwidth = 0,
    command = click,
    relief = "flat")

b2.place(
    x = 20, y = 467,
    width = 90,
    height = 75)

PharmacyIcon = PhotoImage(file = "Pharmacy Icon.png", master=window)
b3 = Button(window,
    image = PharmacyIcon,
    borderwidth = 0,
    command = AdminPharmacyPage,
    relief = "flat")

b3.place(
    x = 20, y = 401,
    width = 90,
    height = 61)

UserAccountsIcon = PhotoImage(file = "User Accounts Icon.png", master=window)
b4 = Button(window,
    image = UserAccountsIcon,
    borderwidth = 0,
    command = AdminUsersPage,
    relief = "flat")

b4.place(
    x = 20, y = 317,
    width = 91,
    height = 77)

NonMedIcon = PhotoImage(file = "Non Med Icon.png", master=window)
b5 = Button(window,
    image = NonMedIcon,
    borderwidth = 0,
    command = AdminNonMedPage,
    relief = "flat")

b5.place(
    x = 20, y = 253,
    width = 91,
    height = 57)

PatientsIcon = PhotoImage(file = "Patients Icon.png", master=window)
b6 = Button(window,
    image = PatientsIcon,
    borderwidth = 0,
    command = AdminPatientsPage,
    relief = "flat")

b6.place(
    x = 20, y = 183,
    width = 91,
    height = 63)

DoctorsIcon = PhotoImage(file = "Doctors Icon.png", master=window)
b7 = Button(window,
    image = DoctorsIcon,
    borderwidth = 0,
    command = AdminDoctorsPage,
    relief = "flat")

b7.place(
    x = 20, y = 110,
    width = 91,
    height = 63)

canvas.create_text(
    210, 90,
    text = "Non-Medical Staff",
    fill = "#6953d9",
    anchor = "w",
    font = ("Lato-Bold", int(40)))

PrevPage = PhotoImage(file = "ArrowLeft.png", master=window)
b8 = Button(window,
    image = PrevPage,
    borderwidth = 0,
    command = AdminHomePage,
    relief = "flat")

b8.place(
    x = 140, y = 30,
    width = 28,
    height = 24)
'''


#Insights
mycursor.execute('SELECT COUNT(*) FROM DOCTORS')
doctorcount = mycursor.fetchall()[0][0]
mycursor.execute('SELECT COUNT(*) FROM PATIENTS')
patientcount = mycursor.fetchall()[0][0]
mycursor.execute('SELECT COUNT(*) FROM NONMEDSTAFF')
nonmedcount = mycursor.fetchall()[0][0]
mycursor.execute('SELECT COUNT(*) FROM APPOINTMENTS WHERE DATE = CURDATE()')
appointmentcount = mycursor.fetchall()[0][0]
mycursor.execute('SELECT COUNT(*) FROM USERACCOUNTS')
userscount = mycursor.fetchall()[0][0]

canvas.create_text(
    1098.5, 425.0,
    text = doctorcount,
    fill = "#e0e0e0",
    font = ("Lato-Regular", int(18)))

canvas.create_text(
    1098.5, 469.5,
    text = patientcount,
    fill = "#e0e0e0",
    font = ("Lato-Regular", int(18)))

canvas.create_text(
    1098.5, 514.5,
    text = nonmedcount,
    fill = "#e0e0e0",
    font = ("Lato-Regular", int(18)))

canvas.create_text(
    1098.5, 559.0,
    text = appointmentcount,
    fill = "#e0e0e0",
    font = ("Lato-Regular", int(18)))

canvas.create_text(
    1099.5, 604.0,
    text = userscount,
    fill = "#e0e0e0",
    font = ("Lato-Regular", int(18)))

#Departments
mycursor.execute('SELECT * FROM NONMEDDEPT')

departments = mycursor.fetchall()
DeptList = []
for dept in departments:
    DeptList.append(dept[1])

listbox = Listbox(
    height = 14,
    width = 33,
    bd = 0,
    highlightcolor = "#ffffff",
    selectbackground = "#bdb0ff",
    selectmode = SINGLE,
    font = "Lato-Light",
    fg = "black",
    relief = "flat")
for item in DeptList:
    listbox.insert(END, item)

def go(event):
    cs = listbox.curselection()
    global dept
    dept = listbox.get(cs)
    command = "update Selected set cur_dept = '"+dept+"' where no = 1"
    mycursor.execute(command)
    mydb.commit()
    AdminSelNonMed()

#Double Click
listbox.bind('<Double-1>', go)
listbox.pack()


listbox.place(
    x = 212, y = 230
)



window.resizable(False, False)
window.mainloop()
