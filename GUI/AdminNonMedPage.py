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

bg = PhotoImage(file = f"AdminNonMedPage BG.png")
background = canvas.create_image(
    608.0, 342.0,
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

canvas.create_text(
    210, 90,
    text = "Non-Medical Staff",
    fill = "#6953d9",
    anchor = "w",
    font = ("Lato-Bold", int(40)))

PrevPage = PhotoImage(file = f"ArrowLeft.png")
b8 = Button(
    image = PrevPage,
    borderwidth = 0,
    command = AdminHomePage,
    relief = "flat")

b8.place(
    x = 140, y = 30,
    width = 28,
    height = 24)


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
