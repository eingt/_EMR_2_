from tkinter import *
from tkinter import ttk
import os

def click():
    print("Clicked")

def gohome():
    window.destroy()

def StaffCard():
    window.destroy()
    import StaffCard

def recadd():
    command = "update Selected set cur_misc = 'add' where no = 1"
    mycursor.execute(command)
    mydb.commit()
    os.system('AddUpdateStaffCard.py')

def recupdate():
    sel_iid = tree.focus()
    sel_record = tree.item(sel_iid, 'values')
    sel_id = str(sel_record[0])
    command = "update Selected set cur_id ="+sel_id+" where no = 1"
    mycursor.execute(command)
    command = "update Selected set cur_misc = 'update' where no = 1"
    mycursor.execute(command)
    mydb.commit()
    os.system('AddUpdateStaffCard.py')

def recdelete():
    sel_iid = tree.focus()
    sel_record = tree.item(sel_iid, 'values')
    sel_id = str(sel_record[0])
    command = "delete from nonmedstaff where id = "+sel_id
    mycursor.execute(command)

def search():
    opt = clicked.get()
    if opt == 'ID':
        index = 0
    elif opt == 'Name':
        index = 1
    elif opt == 'Phone Number':
        index = 5
    elif opt == 'Email':
        index = 6

    tree.delete(*tree.get_children())
    entry = TextBox.get()
    for staff in nonmedstaff:
        if staff[4] == sel_dept_id:
            if ((str(entry).lower() in str(staff[index]).lower()) or (entry == '')):
                rec = []
                rec.append(staff[0])
                rec.append(staff[1])
                rec.append(staff[2])
                rec.append(staff[5])
                rec.append(staff[6])
                rec.append(staff[8])
                tree.insert('', END, values=rec)


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
    print(sel_dept)

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

bg = PhotoImage(file = "AdminSelNonMed BG.png", master = window)
background = canvas.create_image(
    608, 342,
    image=bg)

#Department Name
canvas.create_text(
    210, 70,
    text = sel_dept+" Staff",
    fill = "#6953d9",
    anchor = "w",
    font = ("Lato-Bold", int(40)))

#Department ID
mycursor.execute('SELECT * FROM nonmeddept')
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

AddIcon = PhotoImage(file = "Add Icon.png", master = window)
b9 = Button(window,
    image = AddIcon,
    borderwidth = 0,
    highlightthickness = 0,
    command = recadd,
    relief = "flat")

b9.place(
    x = 825, y = 624,
    width = 30,
    height = 30)

EditIcon = PhotoImage(file = "Edit Icon.png", master = window)
b10 = Button(window,
    image = EditIcon,
    borderwidth = 0,
    highlightthickness = 0,
    command = recupdate,
    relief = "flat")

b10.place(
    x = 785, y = 625,
    width = 29,
    height = 27)

DeleteIcon = PhotoImage(file = "Delete Icon.png", master = window)
b11 = Button(window,
    image = DeleteIcon,
    borderwidth = 0,
    highlightthickness = 0,
    command = recdelete,
    relief = "flat")

b11.place(
    x = 745, y = 625,
    width = 29,
    height = 27)

#SEARCHOPTIONS
options = ['ID','Name','Phone Number','Email']
clicked = StringVar()
style1 = ttk.Style()
style1.configure("TMenubutton", background = "#FFFFFF")
drop = ttk.OptionMenu(window, clicked, options[1], *options, command = search)
drop.place(x=1090,y=80)

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

mycursor.execute('SELECT * FROM NONMEDSTAFF')
nonmedstaff = mycursor.fetchall()
search()

tree.place(x=215, y=210)

def go(event):
    sel_iid = tree.focus()
    sel_record = tree.item(sel_iid, 'values')
    sel_id = str(sel_record[0])
    command = "update Selected set cur_id = '"+sel_id+"' where no = 1"
    mycursor.execute(command)
    mydb.commit()
    StaffCard()

tree.bind('<Double-1>', go)

window.resizable(False, False)
window.mainloop()
