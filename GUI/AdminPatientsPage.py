from tkinter import *
from tkinter import ttk
import os

def click():
    print("Clicked")

def gohome():
    window.destroy()

def PatientCard():
    window.destroy()
    import PatientCard

def recadd():
    command = "update Selected set cur_misc = 'add' where no = 1"
    mycursor.execute(command)
    mydb.commit()
    os.system('AddUpdatePatientCard.py')

def recupdate():
    sel_iid = tree.focus()
    sel_record = tree.item(sel_iid, 'values')
    sel_id = str(sel_record[0])
    command = "update Selected set cur_id ="+sel_id+" where no = 1"
    mycursor.execute(command)
    command = "update Selected set cur_misc = 'update' where no = 1"
    mycursor.execute(command)
    mydb.commit()
    os.system('AddUpdatePatientCard.py')

def recdelete():
    sel_lid = tree.focus()
    sel_record = tree.item(sel_lid, 'values')
    sel_id = str(sel_record[0])
    command = "delete from patients where id = "+sel_id
    mycursor.execute(command)
    search()

index = 1
def search():
    global index
    opt = clicked.get()
    if opt == 'ID':
        index = 0
    elif opt == 'Name':
        index = 1
    elif opt == 'Phone Number':
        index = 6
    elif opt == 'Email':
        index = 7

    tree.delete(*tree.get_children())
    entry = TextBox.get()
    for patient in patients:
        if ((str(entry).lower() in str(patient[index]).lower()) or (entry == '')):
            rec = []
            rec.append(patient[0])
            rec.append(patient[1])
            rec.append(patient[2])
            rec.append(patient[3])
            rec.append(patient[4])
            rec.append(patient[5])
            rec.append(patient[6])
            rec.append(patient[7])
            rec.append(patient[8])
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

bg = PhotoImage(file = "AdminPatientsPage BG.png", master = window)
background = canvas.create_image(
    608, 342,
    image=bg)

#Page Name
canvas.create_text(
    210, 90,
    text = "Patients",
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

#TABLE

style = ttk.Style()
style.configure("Treeview", font=("Lato-semilight", 11), rowheight = 20, selectbackground = "#bdb0ff")
tree = ttk.Treeview(window, column=(1, 2, 3, 4, 5, 6, 7, 8, 9), show='', height=20,padding=6)
tree.column("# 1", anchor=CENTER, stretch=NO, width=40)
tree.column("# 2", anchor=CENTER, stretch=NO, width=140)
tree.column("# 3", anchor=CENTER, stretch=NO, width=120)
tree.column("# 4", anchor=CENTER, stretch=NO, width=120)
tree.column("# 5", anchor=CENTER, stretch=NO, width=100)
tree.column("# 6", anchor=CENTER, stretch=NO, width=100)
tree.column("# 7", anchor=CENTER, stretch=NO, width=130)
tree.column("# 8", anchor=CENTER, stretch=NO, width=140)
tree.column("# 9", anchor=CENTER, stretch=NO, width=110)


mycursor.execute('SELECT * FROM patients')
patients = mycursor.fetchall()

#SEARCHOPTIONS
options = ['ID','Name','Phone Number','Email']
clicked = StringVar()
style1 = ttk.Style()
style1.configure("TMenubutton", background = "#FFFFFF")
drop = ttk.OptionMenu(window, clicked, options[1], *options, command = search())
drop.place(x=1100,y=80)

search()
tree.place(x=170, y=210)

def go(event):
    sel_iid = tree.focus()
    sel_record = tree.item(sel_iid, 'values')
    sel_id = str(sel_record[0])
    command = "update Selected set cur_id = '"+sel_id+"' where no = 1"
    mycursor.execute(command)
    mydb.commit()
    PatientCard()

tree.bind('<Double-1>', go)

window.resizable(False, False)
window.mainloop()
