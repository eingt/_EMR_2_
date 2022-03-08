from tkinter import *
from tkinter import ttk

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

def UpdateCard():
    sel_iid = tree.focus()
    account = tree.item(sel_iid, 'values')
    command = "update Selected set cur_misc = '" + account[0] + "' where no = 1"
    mycursor.execute(command)
    window.destroy()
    import UpdateUserAccount

def AdminHomePage():
    window.destroy()
    import AdminHomePage

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
        index = 3

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

bg = PhotoImage(file = "AdminUsersPage BG.png", master = window)
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

TextBoximg = PhotoImage(file = "TextBox2.png", master = window)
TextBox = canvas.create_image(
    1000, 128,
    image = TextBoximg)

TextBox = Entry(window,
    bd = 0)

TextBox.place(
    x = 850, y = 109,
    width=285,
    height=38)

Homebutton = PhotoImage(file = f"Home Button.png", master = window)
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

SearchIcon = PhotoImage(file = "Search Icon.png", master = window)
bs = Button(window,
    image = SearchIcon,
    bd = 0,
    command = search,
    relief = "flat")

bs.place(
    x = 1135, y = 113,
    width=28,
    height=28)



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
drop = ttk.OptionMenu(window, clicked, options[1], *options, command = search())
drop.place(x=1100,y=80)
search()

UpdateButton = PhotoImage(file = "Update.png", master = window)
b9 = Button(window,
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
