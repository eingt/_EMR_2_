from tkinter import *
from tkinter import ttk

def click():
    print("Clicked")

def UpdateCard():
    sel_iid = tree.focus()
    account = tree.item(sel_iid, 'values')
    print(account[0])
    command = "update Selected set cur_misc = '" + account[0] + "' where no = 1"
    mycursor.execute(command)
    window.destroy()
    import UpdateUserAccount

def AdminDoctorsPage():
    window.destroy()
    import AdminDoctorsPage

def AdminHomePage():
    window.destroy()
    import AdminHomePage

def AdminNonMedPage():
    window.destroy()
    import AdminNonMedPage

def PatientCard():
    window.destroy()
    import PatientCard

index = 1
def search():
    global index
    opt = clicked.get()
    if opt == 'UserName':
        index = 0
    elif opt == 'Name':
        index = 2
    elif opt == 'AccountType':
        index = 2

    tree.delete(*tree.get_children())
    entry = TextBox.get()
    for account in accounts:
        if ((entry.lower() in account[index].lower()) or (entry == '')):
            rec = []
            rec.append(account[0])
            rec.append(account[1])
            rec.append(account[2])
            rec.append(account[3])
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

bg = PhotoImage(file = f"AdminUsersPage BG.png")
background = canvas.create_image(
    608, 342,
    image=bg)

#Page Name
canvas.create_text(
    210, 90,
    text = "User Accounts",
    fill = "#6953d9",
    anchor = "w",
    font = ("Lato-Bold", int(40)))


mycursor.execute('SELECT * FROM PATIENTS')
depts = mycursor.fetchall()

TextBoximg = PhotoImage(file = f"TextBox2.png")
TextBox = canvas.create_image(
    1000, 128,
    image = TextBoximg)

TextBox = Entry(
    bd = 0)

TextBox.place(
    x = 850, y = 109,
    width=285,
    height=38)

SearchIcon = PhotoImage(file = f"Search Icon.png")
b0 = Button(
    image = SearchIcon,
    bd = 0,
    command = search,
    relief = "flat")

b0.place(
    x = 1135, y = 113,
    width=28,
    height=28)

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
    command = AdminHomePage,
    relief = "flat")

b8.place(
    x = 140, y = 30,
    width = 28,
    height = 24)

#TABLE

style = ttk.Style()
style.configure("Treeview", font=("Lato-light", 15), rowheight=30)
tree = ttk.Treeview(window, column=(1, 2, 3, 4), show='', height=13, padding=6)
tree.column("# 1", anchor=CENTER, stretch=NO, width=220)
tree.column("# 2", anchor=CENTER, stretch=NO, width=220)
tree.column("# 3", anchor=CENTER, stretch=NO, width=260)
tree.column("# 4", anchor=CENTER, stretch=NO, width=230)


mycursor.execute('SELECT * FROM USERACCOUNTS')
accounts = mycursor.fetchall()
for account in accounts:
    rec = []
    rec.append(account[0])
    rec.append(account[1])
    rec.append(account[2])
    rec.append(account[3])
    tree.insert('', END, values=rec)

tree.place(x=200, y=210)

#SEARCHOPTIONS
options = ['UserName','Name','AccountType']
clicked = StringVar()
style1 = ttk.Style()
style1.configure("TMenubutton", background = "#FFFFFF")
drop = ttk.OptionMenu(window, clicked, options[1], *options, command = search)
drop.place(x=1090,y=290)
search()

UpdateButton = PhotoImage(file = f"Update.png")
b9 = Button(
    image = UpdateButton,
    borderwidth = 0,
    command = UpdateCard,
    relief = "flat")

b9.place(
    x = 1050, y = 615,
    width = 105,
    height = 39)

def go(event):
    sel_iid = tree.focus()
    sel_record = tree.item(sel_iid, 'values')
    sel_id = str(sel_record[0])


tree.bind('<Double-1>', go)

window.resizable(False, False)
window.mainloop()
