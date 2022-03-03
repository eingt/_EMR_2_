from tkinter import *
from tkinter import ttk

def click():
    print("Clicked")

def AdminDoctorsPage():
    window.destroy()
    import AdminDoctorsPage

def Admin= "tsPage():
    window.destroy()
    import Admin= "tsPage

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


    
def update():
    command = "update pharmacy set name = '" + str(name_entry.get()) + "' where id = "+ str(sel_record[0])+";"
    mycursor.execute(command)
    command = "update pharmacy set age = " + str(age_entry.get()) + " where id = "+ str(sel_record[0])
    mycursor.execute(command)
    command = "update pharmacy set phone = '" + str(phone_entry.get()) + "' where id = "+ str(sel_record[0])
    mycursor.execute(command)
    command = "update pharmacy set gender = '" + gender_entry + "' where id = "+ str(sel_record[0])
    mycursor.execute(command)
    command = "update pharmacy set email = '" + str(email_entry.get()) + "' where id = "+ str(sel_record[0])
    mycursor.execute(command)

    mycursor.execute('SELECT * FROM '+table+'DEPT')
    depts = mycursor.fetchall()
    for dept in depts:
        if str(dept_entry.get()) == dept[1]:
            command = "update pharmacy set deptid = " + str(dept[0]) + " where id = "+ str(sel_record[0])
    mycursor.execute(command)

    command = "update pharmacy set room = '" + str(room_entry.get()) + "' where id = "+ str(sel_record[0])
    mycursor.execute(command)
    command = "update pharmacy set salary = '" + str(salary_entry.get()) + "' where id = "+ str(sel_record[0])
    mycursor.execute(command)
    command = "update pharmacy set joindate = '" + str(join_entry.get()) + "' where id = "+ str(sel_record[0])
    mycursor.execute(command)
    mydb.commit()
index = 1
def search():
    global index
    opt = clicked.get()
    if opt == options[0]:
        index = 0
    elif opt == options[1]:
        index = 1
    elif opt == options[2]:
        index = 2

    tree.delete(*tree.get_children())
    entry = TextBox.get()
    for medicine in medicines:
        if ((str(entry).lower() in str(medicine[index]).lower()) or (entry == '')):
            rec = medicine
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

bg = PhotoImage(file = "AdminPharmacyPage BG.png")
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
    command = AdminHomePage,
    relief = "flat")

b8.place(
    x = 140, y = 30,
    width = 28,
    height = 24)

TextBoximg = PhotoImage(file = "TextBox2.png")
TextBox = canvas.create_image(
    700, 125,
    image = TextBoximg)

TextBox = Entry(
    bd = 0)

TextBox.place(
    x = 550, y = 106,
    width=285,
    height=38)

SearchIcon = PhotoImage(file = "Search Icon.png")
b12 = Button(
    image = SearchIcon,
    bd = 0,
    command = search,
    relief = "flat")

b12.place(
    x = 830, y = 110,
    width=28,
    height=28)

#Table
style = ttk.Style()
style.configure("Treeview", font=("Lato-semilight", 11), rowheight = 20, selectbackground = "#bdb0ff")
tree = ttk.Treeview(window, column=(1, 2, 3, 4, 5), show='', height=20,padding=6)
tree.column("# 1", anchor=CENTER, stretch=NO, width=60)
tree.column("# 2", anchor=CENTER, stretch=NO, width=170)
tree.column("# 3", anchor=CENTER, stretch=NO, width=180)
tree.column("# 4", anchor=CENTER, stretch=NO, width=150)
tree.column("# 5", anchor=CENTER, stretch=NO, width=90)
mycursor.execute('SELECT * FROM PHARMACY')
medicines = mycursor.fetchall()
tree.place(x=185, y=210)

#SEARCHOPTIONS
options = ['ID','Name','Manufacturer']
clicked = StringVar()
style1 = ttk.Style()
style1.configure("TMenubutton", background = "#FFFFFF")
drop = ttk.OptionMenu(window, clicked, options[1], *options, command = search())
drop.place(x=800,y=80)

search()

AddIcon = PhotoImage(file = "Add Icon.png")
b9 = Button(
    image = AddIcon,
    borderwidth = 0,
    highlightthickness = 0,
    command = click,
    relief = "flat")

b9.place(
    x = 825, y = 624,
    width = 30,
    height = 30)

EditIcon = PhotoImage(file = "Edit Icon.png")
b10 = Button(
    image = EditIcon,
    borderwidth = 0,
    highlightthickness = 0,
    command = click,
    relief = "flat")

b10.place(
    x = 785, y = 625,
    width = 29,
    height = 27)

DeleteIcon = PhotoImage(file = "Delete Icon.png")
b11 = Button(
    image = DeleteIcon,
    borderwidth = 0,
    highlightthickness = 0,
    command = click,
    relief = "flat")

b11.place(
    x = 745, y = 625,
    width = 29,
    height = 27)

#Alerts
mycursor.execute('SELECT * FROM PHARMACY WHERE STOCK<50')
meds = mycursor.fetchall()
AlertList = []
for med in meds:
    AlertList.append(med[1])
if len(AlertList) == 0:
    AlertList.append('No Alerts')
listbox = Listbox(
    height = 15,
    width = 15,
    bd = 0,
    activestyle = 'none',
    highlightcolor = "#8571E8",
    highlightbackground = "#8571E8",
    selectbackground = "#8571E8",
    selectmode = NONE,
    font = "Lato-Light",
    fg = "#ffffff",
    bg = "#8571E8",
    relief = "flat")
for item in AlertList:
    listbox.insert(END, item)
listbox.place(x = 940, y = 230)


window.resizable(False, False)
window.mainloop()
