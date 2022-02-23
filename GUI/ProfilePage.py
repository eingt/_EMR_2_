from tkinter import *
from tkinter import ttk
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
        sel_user = user
        sel_type = user[3]

if sel_type == 'Admin':
    table = "Admins"
elif sel_type == 'Doctor':
    table = "Doctors"
elif sel_type == 'Non Medical':
    table = "Nonmedstaff"

mycursor.execute('SELECT * FROM '+table)
records = mycursor.fetchall()
for record in records:
    if record[0] == sel_user[4]:
        sel_record = record

def click():
    print("Clicked")

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



def update():
    command = "update "+table+" set name = '" + str(name_entry.get()) + "' where id = "+ str(sel_record[0])+";"
    mycursor.execute(command)
    command = "update "+table+" set age = " + str(age_entry.get()) + " where id = "+ str(sel_record[0])
    mycursor.execute(command)
    command = "update "+table+" set phone = '" + str(phone_entry.get()) + "' where id = "+ str(sel_record[0])
    mycursor.execute(command)
    command = "update "+table+" set gender = '" + gender_entry + "' where id = "+ str(sel_record[0])
    mycursor.execute(command)
    command = "update "+table+" set email = '" + str(email_entry.get()) + "' where id = "+ str(sel_record[0])
    mycursor.execute(command)

    mycursor.execute('SELECT * FROM '+table+'DEPT')
    depts = mycursor.fetchall()
    for dept in depts:
        if str(dept_entry.get()) == dept[1]:
            command = "update "+table+" set deptid = " + str(dept[0]) + " where id = "+ str(sel_record[0])
    mycursor.execute(command)

    command = "update "+table+" set room = '" + str(room_entry.get()) + "' where id = "+ str(sel_record[0])
    mycursor.execute(command)
    command = "update "+table+" set salary = '" + str(salary_entry.get()) + "' where id = "+ str(sel_record[0])
    mycursor.execute(command)
    command = "update "+table+" set joindate = '" + str(join_entry.get()) + "' where id = "+ str(sel_record[0])
    mycursor.execute(command)
    mydb.commit()


def UpdateConfirmation():
    win1 = Toplevel()
    win1.title("Confirmation")
    win1.iconbitmap("EMR Symbol.ico")
    win1.geometry("400x200")
    win1.configure(bg="#fefefe")
    canvas = Canvas(
        win1,
        bg="#fefefe",
        height=200,
        width=400,
        relief="ridge")
    canvas.place(x=0, y=0)

    canvas.create_text(
        200, 70,
        text="Are you sure you want to make changes?",
        fill="#000000",
        anchor = "center",
        font=("Lato-Regular", int(12)))

    ConfirmImg = PhotoImage(file = "Confirm Img.png")
    b9 = Button(win1,
        image=ConfirmImg,
        borderwidth=0,
        command=update,
        relief="flat")

    b9.place(
        x=210, y=120,
        width=120,
        height=39)

    CancelImg = PhotoImage(file = "Cancel Button.png")
    b10 = Button(win1,
        image=CancelImg,
        borderwidth=0,
        command=click,
        relief="flat")

    b10.place(
        x=90, y=130,
        width=89,
        height=17)

    win1.resizable(False, False)
    win1.mainloop()



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

bg = PhotoImage(file = "ProfilePage BG.png")
background = canvas.create_image(
    608, 342,
    image=bg)

ProfileIcon = PhotoImage(file = "Profile Icon HL.png")
b1 = Button(
    image = ProfileIcon,
    borderwidth = 0,
    command = click,
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
    command = click,
    relief = "flat")

b3.place(
    x = 20, y = 401,
    width = 90,
    height = 61)

UserAccountsIcon = PhotoImage(file = "User Accounts Icon.png")
b4 = Button(
    image = UserAccountsIcon,
    borderwidth = 0,
    command = click,
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

#Details
if sel_record[3] == 'Male':
    MaleIcon = PhotoImage(file = "Male Profile Pic.png")
    canvas.create_image(
        260, 140,
        image = MaleIcon)
elif sel_record[3] == 'Female':
    FemaleIcon = PhotoImage(file=f"Female Profile Pic.png")
    canvas.create_image(
        260, 140,
        image=FemaleIcon)

canvas.create_text(
    385, 130,
    text = "Name :",
    fill = "#000000",
    font = ("Lato-Regular", int(12)))
name_entry = Entry(
    bd = 2,
    highlightthickness = 0,
    relief = "groove",
    font = "Lato 14")
name_entry.insert(0,sel_record[1])
name_entry.place(
    x = 360, y = 140,
    width = 350,
    height = 35)

canvas.create_text(
    270, 255,
    text = "Age :",
    fill = "#000000",
    anchor = "e",
    font = ("Lato-Regular", int(12)))
age_entry = Entry(
    bd = 2,
    highlightthickness = 0,
    relief = "groove",
    font = "Lato 11")
age_entry.insert(0,sel_record[2])
age_entry.place(
    x = 280, y = 240,
    width = 210,
    height = 30)

canvas.create_text(
    270, 355,
    text = "Gender :",
    fill = "#000000",
    anchor = "e",
    font = ("Lato-Regular", int(12)))

def selgender(sel_gender):
    sel_gender = clicked.get()

options = ['Female','Male','Other']
clicked = StringVar()
style1 = ttk.Style()
style1.configure("TMenubutton", background = "#FFFFFF", font = "Lato 11")
gender = ttk.OptionMenu(window, clicked, sel_record[3], *options)
gender.place(x = 280, y = 342)
gender_entry = clicked.get()



mycursor.execute('SELECT * FROM '+table+'DEPT')
depts = mycursor.fetchall()
for dept in depts:
    if sel_record[4] == dept[0]:
        sel_recdept = dept[1]

canvas.create_text(
    270, 455,
    text = "Department :",
    fill = "#000000",
    anchor = "e",
    font = ("Lato-Regular", int(12)))
dept_entry = Entry(
    bd = 2,
    highlightthickness = 0,
    relief = "groove",
    font = "Lato 11")
dept_entry.insert(0,sel_recdept)
dept_entry.place(
    x = 280, y = 440,
    width = 210,
    height = 30)
dept_entry.config(state = 'disabled')


canvas.create_text(
    590, 255,
    text = "Ph No. :",
    fill = "#000000",
    anchor = "e",
    font = ("Lato-Regular", int(12)))
phone_entry = Entry(
    bd = 2,
    highlightthickness = 0,
    relief = "groove",
    font = "Lato 11")
phone_entry.insert(0,sel_record[6])
phone_entry.place(
    x = 600, y = 240,
    width = 210,
    height = 30)

canvas.create_text(
    590, 355,
    text = "E-mail :",
    fill = "#000000",
    anchor = "e",
    font = ("Lato-Regular", int(12)))
email_entry = Entry(
    bd = 2,
    highlightthickness = 0,
    relief = "groove",
    font = "Lato 11")
email_entry.insert(0,sel_record[7])
email_entry.place(
    x = 600, y = 340,
    width = 210,
    height = 30)

if sel_type == 'Doctor':
    canvas.create_text(
        590, 455,
        text = "Room :",
        fill = "#000000",
        anchor = "e",
        font = ("Lato-Regular", int(12)))
    room_entry = Entry(
        bd = 2,
        highlightthickness = 0,
        relief = "groove",
        font = "Lato 11")
    room_entry.insert(0,sel_record[5])
    room_entry.place(
        x = 600, y = 440,
        width = 210,
        height = 30)
    room_entry.config(state = 'disabled')

    canvas.create_text(
        590, 555,
        text = "Salary :",
        fill = "#000000",
        anchor = "e",
        font = ("Lato-Regular", int(12)))
    salary_entry = Entry(
        bd = 2,
        highlightthickness = 0,
        relief = "groove",
        font = "Lato 11")
    salary_entry.insert(0,sel_record[9])
    salary_entry.place(
        x = 600, y = 540,
        width = 210,
        height = 30)
    salary_entry.config(state = 'disabled')

    canvas.create_text(
        270, 555,
        text="Join Date :",
        fill="#000000",
        anchor="e",
        font=("Lato-Regular", int(12)))
    join_entry = Entry(
        bd=2,
        highlightthickness=0,
        relief="groove",
        font="Lato 11")
    join_entry.insert(0, sel_record[8])
    join_entry.place(
        x=280, y=540,
        width=210,
        height=30)
    join_entry.config(state='disabled')
elif sel_type == 'Non Medical':
    canvas.create_text(
        590, 455,
        text="Salary :",
        fill="#000000",
        anchor="e",
        font=("Lato-Regular", int(12)))
    salary_entry = Entry(
        bd=2,
        highlightthickness=0,
        relief="groove",
        font="Lato 11")
    salary_entry.insert(0, sel_record[8])
    salary_entry.place(
        x = 600, y = 440,
        width=210,
        height=30)
    salary_entry.config(state='disabled')

    canvas.create_text(
        270, 555,
        text="Join Date :",
        fill="#000000",
        anchor="e",
        font=("Lato-Regular", int(12)))
    join_entry = Entry(
        bd=2,
        highlightthickness=0,
        relief="groove",
        font="Lato 11")
    join_entry.insert(0, sel_record[7])
    join_entry.place(
        x=280, y=540,
        width=210,
        height=30)
    join_entry.config(state='disabled')


#Log In Credentials

canvas.create_text(
    970, 320,
    text = "Username :",
    fill = "#FFFFFF",
    anchor = "e",
    font = ("Lato-Regular", int(12)))
username_entry = Entry(
    bd = 0,
    highlightthickness = 1,
    fg = "#FFFFFF",
    bg = "#6953D9",
    relief = "groove",
    font = "Lato 11",
    highlightbackground ='#FFFFFF', highlightcolor ='#FFFFFF')
username_entry.insert(0,sel_user[0])
username_entry.place(
    x = 975, y = 305,
    width = 160,
    height = 30)

canvas.create_text(
    970, 400,
    text = "Password :",
    fill = "#FFFFFF",
    anchor = "e",
    font = ("Lato-Regular", int(12)))
password_entry = Entry(
    bd = 0,
    highlightthickness = 1,
    fg = "#FFFFFF",
    bg = "#6953D9",
    relief = "groove",
    font = "Lato 11",
    show = "*",
    highlightbackground ='#FFFFFF', highlightcolor ='#FFFFFF')
password_entry.insert(0,sel_user[1])
password_entry.place(
    x = 975, y = 385,
    width = 160,
    height = 30)

toggle = True
def showpass():
    global toggle
    if toggle:
        password_entry.config(show = "")
        toggle = False
    else:
        password_entry.config(show="*")
        toggle = True

EyeButton = PhotoImage(file = "Eye Icon Purple.png")
b11 = Button(
    image = EyeButton,
    borderwidth = 0,
    command = showpass,
    relief = "flat")
b11.place(
    x = 1110, y = 392,
    width=18,
    height=17)

canvas.create_text(
    970, 480,
    text = "Type :",
    fill = "#FFFFFF",
    anchor = "e",
    font = ("Lato-Regular", int(12)))

type_entry = Entry(
    bd = 0,
    highlightthickness = 1,
    fg = "#FFFFFF",
    bg = "#6953D9",
    disabledforeground = "#FEFEFE",
    disabledbackground = "#5847bb",
    relief = "groove",
    font = "Lato 11",
    highlightbackground ='#FFFFFF', highlightcolor ='#FFFFFF')
type_entry.insert(0,sel_user[3])
type_entry.place(
    x = 975, y = 465,
    width = 160,
    height = 30)
type_entry.config(state = "disabled")

UpdateButton = PhotoImage(file = "Update.png")
b8 = Button(
    image = UpdateButton,
    borderwidth = 0,
    command = UpdateConfirmation,
    relief = "flat")
b8.place(
    x = 1050, y = 605,
    width = 113,
    height = 39)


window.resizable(False, False)
window.mainloop()
