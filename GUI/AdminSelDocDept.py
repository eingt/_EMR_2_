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


def DoctorCard():
    window.destroy()
    import DoctorCard

index = 1
def search():
    global index
    opt = clicked.get()
    if opt == 'ID':
        index = 0
    elif opt == 'Name':
        index = 1
    elif opt == 'Room':
        index = 2
    elif opt == 'Email':
        index = 3

    tree.delete(*tree.get_children())
    entry = TextBox.get()
    for doctor in doctors:
        if doctor[4] == sel_dept_id:
            if ((str(entry).lower() in str(doctor[index]).lower()) or (entry == '')):
                doc = []
                doc.append(doctor[0])
                doc.append(doctor[1])
                doc.append(doctor[5])
                doc.append(doctor[6])
                doc.append(doctor[7])
                doc.append(doctor[9])
                tree.insert('', END, values=doc)


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
for d in data:
    sel_dept = d[2]

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

bg = PhotoImage(file = "AdminSelDocDept BG.png")
background = canvas.create_image(
    608, 342,
    image=bg)

#Department Name
canvas.create_text(
    210, 70,
    text = sel_dept+" Department",
    fill = "#6953d9",
    anchor = "w",
    font = ("Lato-Bold", int(40)))

#Department ID
mycursor.execute('SELECT * FROM DOCTORSDEPT')
depts = mycursor.fetchall()

for dept in depts:
    if dept[1] == sel_dept:
        sel_dept_id = dept[0]

canvas.create_text(
    210, 110,
    text = sel_dept_id,
    fill = "#000000",
    anchor = "w",
    font = ("Lato-Regular", int(18)))

TextBoximg = PhotoImage(file = "TextBox2.png")
TextBox = canvas.create_image(
    1000, 128,
    image = TextBoximg)

TextBox = Entry(
    bd = 0)

TextBox.place(
    x = 850, y = 109,
    width=285,
    height=38)

SearchIcon = PhotoImage(file = "Search Icon.png")
b0 = Button(
    image = SearchIcon,
    bd = 0,
    command = search,
    relief = "flat")

b0.place(
    x = 1135, y = 113,
    width=28,
    height=28)

ProfileIcon = PhotoImage(file = "Profile Icon.png")
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
    command = click,
    relief = "flat")

b5.place(
    x = 20, y = 253,
    width = 91,
    height = 57)


= "tsIcon = PhotoImage(file = "= "ts Icon.png")
b6 = Button(
    image = = "tsIcon,
    borderwidth = 0,
    command = click,
    relief = "flat")

b6.place(
    x = 20, y = 183,
    width = 91,
    height = 63)

DoctorsIcon = PhotoImage(file = "Doctors Icon HL.png")
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
    command = AdminDoctorsPage,
    relief = "flat")

b8.place(
    x = 140, y = 30,
    width = 28,
    height = 24)


#TABLE
style = ttk.Style()
style.configure("Treeview", font=(None, 10))
tree = ttk.Treeview(window, column=(1, 2, 3, 4, 5, 6), show='', height=20,padding=6)
tree.column("# 1", anchor=CENTER, stretch=NO, width=45)
tree.column("# 2", anchor=CENTER, stretch=NO, width=220)
tree.column("# 3", anchor=CENTER, stretch=NO, width=100)
tree.column("# 4", anchor=CENTER, stretch=NO, width=220)
tree.column("# 5", anchor=CENTER, stretch=NO, width=200)
tree.column("# 6", anchor=CENTER, stretch=NO, width=100)
mycursor.execute('SELECT * FROM DOCTORS')
doctors = mycursor.fetchall()

#SEARCHOPTIONS
options = ['ID','Name','Room','Email']
clicked = StringVar()
style1 = ttk.Style()
style1.configure("TMenubutton", background = "#FFFFFF")
drop = ttk.OptionMenu(window, clicked, options[1], *options, command = search())
drop.place(x=1090,y=80)


search()

tree.place(x=215, y=210)



def go(event):
    sel_iid = tree.focus()
    sel_record = tree.item(sel_iid, 'values')
    sel_id = str(sel_record[0])
    command = "update Selected set cur_id = '"+sel_id+"' where no = 1"
    mycursor.execute(command)
    mydb.commit()
    DoctorCard()

tree.bind('<Double-1>', go)

window.resizable(False, False)
window.mainloop()
