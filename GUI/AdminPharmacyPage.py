from tkinter import *
from tkinter import ttk

def click():
    print("Clicked")

def gohome():
    window.destroy()


def recaddupdate():
    sel_iid = tree.focus()
    sel_record = tree.item(sel_iid, 'values')
    sel_id = str(sel_record[0])
    command = "update Selected set cur_id ="+sel_id+" where no = 1"
    mycursor.execute(command)
    mydb.commit()
    window.withdraw()
    import AddUpdatePharmacyCard
    window.deiconify()

def recdelete():
    sel_iid = tree.focus()
    sel_record = tree.item(sel_iid, 'values')
    sel_id = str(sel_record[0])
    command = "delete from doctors where id = "+sel_id
    mycursor.execute(command)
    search()

    
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

bg = PhotoImage(file = "AdminPharmacyPage BG.png", master = window)
background = canvas.create_image(
    608, 342,
    image=bg)

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


TextBoximg = PhotoImage(file = "TextBox2.png", master = window)
TextBox = canvas.create_image(
    700, 125,
    image = TextBoximg)

TextBox = Entry(window,
    bd = 0)

TextBox.place(
    x = 550, y = 106,
    width=285,
    height=38)

SearchIcon = PhotoImage(file = "Search Icon.png", master = window)
b12 = Button(window,
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

AddIcon = PhotoImage(file = "Add Icon.png", master = window)
b9 = Button(window,
    image = AddIcon,
    borderwidth = 0,
    highlightthickness = 0,
    command = recaddupdate,
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
    command = recaddupdate,
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

#Alerts
mycursor.execute('SELECT * FROM PHARMACY WHERE STOCK<50')
meds = mycursor.fetchall()
AlertList = []
for med in meds:
    AlertList.append(med[1])
if len(AlertList) == 0:
    AlertList.append('No Alerts')
listbox = Listbox(window,
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
