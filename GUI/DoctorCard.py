from tkinter import *
from tkinter import ttk
def UpdateCard():
    command = "update Selected set cur_id = " + str(sel_doc[0]) + " where no = 1"
    mycursor.execute(command)
    mydb.commit()
    window.destroy()
    import UpdateDoctorCard

def click():
    print("Button is Clicked")

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

def AdminDoctorsPage():
    window.destroy()
    import AdminDoctorsPage

def AdminSelDocDept():
    window.destroy()
    import AdminSelDocDept

def app_selected(event):
    opt = clicked.get()

    if opt == 'Upcoming':
        tree.delete(*tree.get_children())
        mycursor.execute('''SELECT * FROM appointments where date > date(now()) or
        (date = date(now()) and time > time(now()))
        order by date asc, time asc;''')
        upcoming_app = mycursor.fetchall()
        mycursor.execute('SELECT * FROM PATIENTS')
        patients = mycursor.fetchall()

        for appointment in upcoming_app:
            for patient in patients:
                if (patient[0] == appointment[0]):
                    patientname = patient[1]
            if (appointment[1] == sel_doc[0]):
                rec = []
                rec.append(appointment[4])
                rec.append(appointment[3])
                rec.append(patientname)
                rec.append(appointment[2])
                tree.insert('', END, values=rec)

    if opt == 'Completed':
        tree.delete(*tree.get_children())
        mycursor.execute('''SELECT * FROM appointments where date < date(now()) or
        (date = date(now()) and time < time(now()))
        order by date asc, time asc;''')
        completed_app = mycursor.fetchall()
        mycursor.execute('SELECT * FROM PATIENTS')
        patients = mycursor.fetchall()

        for appointment in completed_app:
            for patient in patients:
                if (patient[0] == appointment[0]):
                    patientname = patient[1]
            if (appointment[1] == sel_doc[0]):
                rec = []
                rec.append(appointment[4])
                rec.append(appointment[3])
                rec.append(patientname)
                rec.append(appointment[2])
                tree.insert('', END, values=rec)

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

bg = PhotoImage(file = "DoctorCardBG.png")
background = canvas.create_image(
    608, 342,
    image=bg)

ProfileIcon = PhotoImage(file = "Profile Icon.png")
b1 = Button(
    image = ProfileIcon,
    borderwidth = 0,
    command = ProfilePage,
    relief = "flat")

b1.place(
    x = 20, y = 605,
    width = 88,
    height = 70)

'''CashierIcon = PhotoImage(file = "Cashier Icon.png")
b2 = Button(
    image = CashierIcon,
    borderwidth = 0,
    command = click,
    relief = "flat")

b2.place(
    x = 20, y = 467,
    width = 90,
    height = 75)'''

PharmacyIcon = PhotoImage(file = "Pharmacy Icon.png")
b3 = Button(
    image = PharmacyIcon,
    borderwidth = 0,
    command = AdminPharmacyPage,
    relief = "flat")

b3.place(
    x = 20, y = 401,
    width = 90,
    height = 61)

UserAccountsIcon = PhotoImage(file = "User Accounts Icon.png")
b4 = Button(
    image = UserAccountsIcon,
    borderwidth = 0,
    command = AdminUsersPage,
    relief = "flat")

b4.place(
    x = 20, y = 317,
    width = 91,
    height = 77)

NonMedIcon = PhotoImage(file = "Non Med Icon.png")
b5 = Button(
    image = NonMedIcon,
    borderwidth = 0,
    command = AdminNonMedPage,
    relief = "flat")

b5.place(
    x = 20, y = 253,
    width = 91,
    height = 57)

PatientsIcon = PhotoImage(file = "Patients Icon.png")
b6 = Button(
    image = PatientsIcon,
    borderwidth = 0,
    command = AdminPatientsPage,
    relief = "flat")

b6.place(
    x = 20, y = 183,
    width = 91,
    height = 63)

DoctorsIcon = PhotoImage(file = "Doctors Icon.png")
b7 = Button(
    image = DoctorsIcon,
    borderwidth = 0,
    command = AdminDoctorsPage,
    relief = "flat")

b7.place(
    x = 20, y = 110,
    width = 91,
    height = 63)

PrevPage = PhotoImage(file = "ArrowLeft.png")
b8 = Button(
    image = PrevPage,
    borderwidth = 0,
    command = AdminSelDocDept,
    relief = "flat")

b8.place(
    x = 140, y = 30,
    width = 28,
    height = 24)

UpdateButton = PhotoImage(file = "Update.png")
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
    sel_docid = int(d[3])


mycursor.execute('SELECT * FROM DOCTORS')
doctors = mycursor.fetchall()
for doctor in doctors:
    if doctor[0] == sel_docid:
        sel_doc = doctor


#Doctor Name
canvas.create_text(
    350, 120.0,
    text = sel_doc[1],
    fill = "#000000",
    anchor = 'w',
    font = ("Lato-Bold", int(30)))

#Doctor ID
canvas.create_text(
    350, 159.0,
    text = sel_doc[0],
    fill = "#000000",
    anchor = 'w',
    font = ("Lato-Regular", int(20.0)))

#Profile Picture

if sel_doc[3] == 'Male':
    MaleIcon = PhotoImage(file = "Male Profile Pic.png")
    canvas.create_image(
        260, 130,
        image = MaleIcon)
elif sel_doc[3] == 'Female':
    FemaleIcon = PhotoImage(file=f"Female Profile Pic.png")
    canvas.create_image(
        260, 130,
        image=FemaleIcon)

#Age
canvas.create_text(
    300, 263.0,
    text = sel_doc[2],
    fill = "#000000",
    anchor = 'w',
    font = ("Lato-Light", int(14.0)))

#Gender
canvas.create_text(
    300, 353.0,
    text = sel_doc[3],
    fill = "#000000",
    anchor = 'w',
    font = ("Lato-Light", int(14.0)))

#Room
canvas.create_text(
    300, 441.0,
    text = sel_doc[5],
    fill = "#000000",
    anchor = 'w',
    font = ("Lato-Light", int(14.0)))

#Join Date
canvas.create_text(
    320, 525.0,
    text = sel_doc[8],
    fill = "#000000",
    anchor = 'w',
    font = ("Lato-Light", int(14.0)))

#Phone No.
canvas.create_text(
    540, 263.0,
    text = sel_doc[6],
    fill = "#000000",
    anchor = 'w',
    font = ("Lato-Light", int(14.0)))

#E-Mail
canvas.create_text(
    540, 353.0,
    text = sel_doc[7],
    fill = "#000000",
    anchor = 'w',
    font = ("Lato-Light", int(14.0)))

#Salary
canvas.create_text(
    540, 441.0,
    text = sel_doc[9],
    fill = "#000000",
    anchor = 'w',
    font = ("Lato-Light", int(14.0)))

#Department
mycursor.execute('SELECT * FROM DOCTORSDEPT')
depts = mycursor.fetchall()
for dept in depts:
    if sel_doc[4] == dept[0]:
        sel_deptname = dept[1]
canvas.create_text(
    570, 525,
    text = sel_deptname,
    fill = "#000000",
    anchor = 'w',
    font = ("Lato-Light", int(14.0)))

#Appointments
options = ['Upcoming','Completed']
clicked = StringVar()
style1 = ttk.Style()
style1.configure("TMenubutton", background = "#FFFFFF")
drop = ttk.OptionMenu(window, clicked, options[0], *options, command = app_selected)
drop.place(x=1090,y=40)

style2 = ttk.Style()
style2.configure("Treeview", font=(None, 10))
tree = ttk.Treeview(window, column=(1, 2, 3, 4), show='', height=24,padding=6)
tree.column("# 1", anchor=CENTER, stretch=NO, width=60)
tree.column("# 2", anchor=CENTER, stretch=NO, width=90)
tree.column("# 3", anchor=CENTER, stretch=NO, width=100)
tree.column("# 4", anchor=CENTER, stretch=NO, width=100)

tree.place(x=800, y=120)

mycursor.execute('select curdate()')
curdate = mycursor.fetchall()
mycursor.execute('SELECT * FROM APPOINTMENTS')
appointments = mycursor.fetchall()
app_selected(appointments)


window.resizable(False, False)
window.mainloop()
