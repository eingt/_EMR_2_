from tkinter import *
import mysql.connector


mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'maneeshj',
    port = '3306',
    database = 'EMR'
)

mycursor = mydb.cursor()

def click():
    print("Clicked")
    
def gohome():
    window.destroy()

def AdminSelDocDept():
    window.destroy()
    import AdminSelDocDept


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

bg = PhotoImage(file = "AdminDoctorsPage BG.png", master=window)
background = canvas.create_image(
    608.0, 342.0,
    image=bg)

Homebutton = PhotoImage(file = f"Home Button.png", master=window)
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

#Insights
mycursor.execute('SELECT COUNT(*) FROM DOCTORS')
doctorcount = mycursor.fetchall()[0][0]
mycursor.execute('SELECT COUNT(*) FROM PATIENTS')
patientcount = mycursor.fetchall()[0][0]
mycursor.execute('SELECT COUNT(*) FROM NONMEDSTAFF')
nonmedcount = mycursor.fetchall()[0][0]
mycursor.execute('SELECT COUNT(*) FROM APPOINTMENTS WHERE DATE = CURDATE()')
appointmentcount = mycursor.fetchall()[0][0]
mycursor.execute('SELECT COUNT(*) FROM USERACCOUNTS')
userscount = mycursor.fetchall()[0][0]

canvas.create_text(
    1098.5, 425.0,
    text = doctorcount,
    fill = "#e0e0e0",
    font = ("Lato-Regular", int(18)))

canvas.create_text(
    1098.5, 469.5,
    text = patientcount,
    fill = "#e0e0e0",
    font = ("Lato-Regular", int(18)))

canvas.create_text(
    1098.5, 514.5,
    text = nonmedcount,
    fill = "#e0e0e0",
    font = ("Lato-Regular", int(18)))

canvas.create_text(
    1098.5, 559.0,
    text = appointmentcount,
    fill = "#e0e0e0",
    font = ("Lato-Regular", int(18)))

canvas.create_text(
    1099.5, 604.0,
    text = userscount,
    fill = "#e0e0e0",
    font = ("Lato-Regular", int(18)))

#Departments
mycursor.execute('SELECT * FROM DOCTORSDEPT')

departments = mycursor.fetchall()
DeptList = []
for dept in departments:
    DeptList.append(dept[1])

listbox = Listbox(window,
    height = 14,
    width = 33,
    bd = 0,
    highlightcolor = "#ffffff",
    selectbackground = "#bdb0ff",
    selectmode = SINGLE,
    font = "Lato-Light",
    fg = "black",
    relief = "flat")
for item in DeptList:
    listbox.insert(END, item)

def go(event):
    cs = listbox.curselection()
    global dept
    dept = listbox.get(cs)
    command = "update Selected set cur_dept = '"+dept+"' where no = 1"
    mycursor.execute(command)
    mydb.commit()
    AdminSelDocDept()

#Double Click
listbox.bind('<Double-1>', go)
listbox.pack()

listbox.place(
    x = 212, y = 230
)

window.resizable(False, False)
window.mainloop()
