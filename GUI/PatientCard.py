from tkinter import *
from tkinter import ttk

def UpdateCard():
    command = "update Selected set cur_id = '" + str(sel_patient[0]) + "' where no = 1"
    mycursor.execute(command)
    window.destroy()
    import UpdatePatientCard

def AdminDoctorsPage():
    window.destroy()
    import AdminDoctorsPage

def click():
    print("Button is Clicked")

def AdminNonMedPage():
    window.destroy()
    import AdminNonMedPage

def AdminSelNonMed():
    window.destroy()
    import AdminSelNonMed
    
def app_selected(event):
    opt = clicked.get()

    if opt == 'Upcoming':
        tree.delete(*tree.get_children())
        mycursor.execute('''SELECT * FROM appointments where date > date(now()) or
                                (date = date(now()) and time > time(now()))
                                order by date asc, time asc;''')
        upcoming_app = mycursor.fetchall()
        mycursor.execute('SELECT * FROM DOCTORS')
        doctors = mycursor.fetchall()

        for appointment in upcoming_app:
            for doctor in doctors:
                if (doctor[0] == appointment[1]):
                    docname = doctor[1]
            if (appointment[0] == sel_patient[0]):
                rec = []
                rec.append(appointment[4])
                rec.append(appointment[3])
                rec.append(docname)
                rec.append(appointment[2])
                tree.insert('', END, values=rec)

    if opt == 'Completed':
        tree.delete(*tree.get_children())
        mycursor.execute('''SELECT * FROM appointments where date < date(now()) or
                                (date = date(now()) and time < time(now()))
                                order by date asc, time asc;''')
        completed_app = mycursor.fetchall()
        mycursor.execute('SELECT * FROM DOCTORS')
        doctors = mycursor.fetchall()

        for appointment in completed_app:
            for doctor in doctors:
                if (doctor[0] == appointment[1]):
                    docname = doctor[1]
            if (appointment[0] == sel_patient[0]):
                rec = []
                rec.append(appointment[4])
                rec.append(appointment[3])
                rec.append(docname)
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

bg = PhotoImage(file = f"PatientCardBG.png")
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

DoctorsIcon = PhotoImage(file = f"Doctors Icon.png")
b7 = Button(
    image = DoctorsIcon,
    borderwidth = 0,
    command = AdminDoctorsPage,
    relief = "flat")

b7.place(
    x = 20, y = 110,
    width = 91,
    height = 63)

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
    sel_patientid = int(d[3])


mycursor.execute('SELECT * FROM PATIENTS')
patients = mycursor.fetchall()
for patient in patients:
    if patient[0] == sel_patientid:
        sel_patient = patient

#Name
canvas.create_text(
    350, 120.0,
    text = sel_patient[1],
    fill = "#000000",
    anchor = 'w',
    font = ("Lato-Bold", int(30)))

#ID
canvas.create_text(
    350, 159.0,
    text = sel_patient[0],
    fill = "#000000",
    anchor = 'w',
    font = ("Lato-Regular", int(20.0)))

#Profile Picture

if sel_patient[3] == 'Male':
    MaleIcon = PhotoImage(file = f"Male Profile Pic.png")
    canvas.create_image(
        260, 130,
        image = MaleIcon)
elif sel_patient[3] == 'Female':
    FemaleIcon = PhotoImage(file=f"Female Profile Pic.png")
    canvas.create_image(
        260, 130,
        image=FemaleIcon)

#DOB
canvas.create_text(
    325, 268,
    text = sel_patient[2],
    fill = "#000000",
    anchor = 'w',
    font = ("Lato-Light", int(13)))

#Gender
canvas.create_text(
    530, 268,
    #900, 141,
    text = sel_patient[3],
    fill = "#000000",
    anchor = 'w',
    font = ("Lato-Light", int(13)))

#Phone No.
canvas.create_text(
    290, 353.0,
    text = sel_patient[6],
    fill = "#000000",
    anchor = 'w',
    font = ("Lato-Light", int(13)))

#Email
canvas.create_text(
    530, 353,
    text = sel_patient[7],
    fill = "#000000",
    anchor = 'w',
    font = ("Lato-Light", int(13)))

#Reg Date
canvas.create_text(
    310, 443,
    text = sel_patient[8],
    fill = "#000000",
    anchor = 'w',
    font = ("Lato-Light", int(13)))

#Height
canvas.create_text(
    900, 142,
    text = sel_patient[4]+" cm",
    fill = "#FFFFFF",
    anchor = 'w',
    font = ("Lato-Light", int(13)))

#Weight
canvas.create_text(
    1060, 142,
    text = sel_patient[5]+" kg",
    fill = "#FFFFFF",
    anchor = 'w',
    font = ("Lato-Light", int(13)))

#BMI
bmi = float(int(sel_patient[5])/((int(sel_patient[4])/100)**2))
canvas.create_text(
    1040, 198,
    text = round(bmi, 1),
    fill = "#FFFFFF",
    anchor = 'w',
    font = ("Lato-Light", int(13)))

allergylist = sel_patient[9].split(',')
allergyheight = len(allergylist)

allergies = Label(window,
                  text = sel_patient[9],
                  bg = "#8572E4",
                  fg = "#FFFFFF",
                  height = allergyheight,
                  wraplengt = 60,
                  font = ("Lato-Light", int(13)))

allergies.place(x = 900, y = 185)


#Appointments
options = ['Upcoming','Completed']
clicked = StringVar()
style1 = ttk.Style()
style1.configure("TMenubutton", background = "#FFFFFF")
drop = ttk.OptionMenu(window, clicked, options[0], *options, command = app_selected)
#drop.config(bg = "#FFFFFF")
drop.place(x=1090,y=290)

style2 = ttk.Style()
style2.configure("Treeview", font=(None, 10))
tree = ttk.Treeview(window, column=(1, 2, 3, 4), show='', height=12,padding=6)
tree.column("# 1", anchor=CENTER, stretch=NO, width=60)
tree.column("# 2", anchor=CENTER, stretch=NO, width=90)
tree.column("# 3", anchor=CENTER, stretch=NO, width=100)
tree.column("# 4", anchor=CENTER, stretch=NO, width=100)

tree.place(x=800, y=370)

mycursor.execute('select curdate()')
curdate = mycursor.fetchall()
mycursor.execute('SELECT * FROM APPOINTMENTS')
appointments = mycursor.fetchall()
app_selected(appointments)


window.resizable(False, False)
window.mainloop()
