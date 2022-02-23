from tkinter import *
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
    sel_docid = int(d[3])

def update():
    command = "update doctors set name = '" + str(name_entry.get()) + "' where id = "+ str(sel_docid)+";"
    mycursor.execute(command)
    command = "update doctors set age = " + str(age_entry.get()) + " where id = "+ str(sel_docid)
    mycursor.execute(command)
    command = "update doctors set phone = '" + str(phone_entry.get()) + "' where id = "+ str(sel_docid)
    mycursor.execute(command)
    command = "update doctors set price = '" + str(price_entry.get()) + "' where id = "+ str(sel_docid)
    mycursor.execute(command)
    command = "update doctors set email = '" + str(email_entry.get()) + "' where id = "+ str(sel_docid)
    mycursor.execute(command)

    mycursor.execute('SELECT * FROM DOCTORSDEPT')
    depts = mycursor.fetchall()
    for dept in depts:
        if str(dept_entry.get()) == dept[1]:
            command = "update doctors set deptid = " + str(dept[0]) + " where id = "+ str(sel_docid)
    mycursor.execute(command)

    command = "update doctors set room = '" + str(room_entry.get()) + "' where id = "+ str(sel_docid)
    mycursor.execute(command)
    command = "update doctors set salary = '" + str(salary_entry.get()) + "' where id = "+ str(sel_docid)
    mycursor.execute(command)
    command = "update doctors set joindate = '" + str(join_entry.get()) + "' where id = "+ str(sel_docid)
    mycursor.execute(command)
    mydb.commit()
    root.destroy()
    import DoctorCard

def cancel():
    root.destroy()
    import DoctorCard

root = Tk()
root.title('Update Doctor Details')
root.iconbitmap("EMR Symbol.ico")

root.geometry("551x568")
root.configure(bg = "#ffffff")
canvas = Canvas(
    root,
    bg = "#ffffff",
    height = 568,
    width = 551,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"AddUpdate Pharmacy Card BG.png")
background = canvas.create_image(
    275.5, 284.0,
    image=background_img)

mycursor.execute('SELECT * FROM DOCTORS')
doctors = mycursor.fetchall()
for doctor in doctors:
    if doctor[0] == sel_docid:
        sel_doc = doctor

name_entryimg = PhotoImage(file = f"TextBox4.png")
name_entry = canvas.create_image(
    276.0, 132.5,
    image = name_entryimg)

name_entry = Entry(
    bd = 0,
    highlightthickness = 0)
name_entry.insert(0,sel_doc[1])
name_entry.place(
    x = 77.5, y = 119,
    width = 397.0,
    height = 29)

mfd_entryimg = PhotoImage(file = f"TextBox4.png")
mfd_entry = canvas.create_image(
    156.5, 212.5,
    image = mfd_entryimg)

mfd_entry = Entry(
    bd = 0,
    highlightthickness = 0)
mfd_entry.insert(0,sel_doc[2])
mfd_entry.place(
    x = 77.5, y = 199,
    width = 158.0,
    height = 29)

stock_entryimg = PhotoImage(file = f"TextBox4.png")
stock_entry = canvas.create_image(
    156.5, 292.5,
    image = stock_entryimg)

stock_entry = Entry(
    bd = 0,
    highlightthickness = 0)
stock_entry.insert(0,sel_doc[6])
stock_entry.place(
    x = 77.5, y = 279,
    width = 158.0,
    height = 29)

price_entryimg = PhotoImage(file = f"TextBox4.png")
price_entry = canvas.create_image(
    389.0, 212.5,
    image = price_entryimg)

price_entry = Entry(
    bd = 0,
    highlightthickness = 0)
price_entry.insert(0,sel_doc[3])
price_entry.place(
    x = 303.5, y = 199,
    width = 171.0,
    height = 29)







entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    276.0, 172.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#ebebeb",
    highlightthickness = 0)

entry0.place(
    x = 77.5, y = 157,
    width = 397.0,
    height = 29)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    276.0, 252.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#ebebeb",
    highlightthickness = 0)

entry1.place(
    x = 77.5, y = 237,
    width = 397.0,
    height = 29)

entry2_img = PhotoImage(file = f"img_textBox2.png")
entry2_bg = canvas.create_image(
    276.0, 332.5,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#ebebeb",
    highlightthickness = 0)

entry2.place(
    x = 77.5, y = 317,
    width = 397.0,
    height = 29)

entry3_img = PhotoImage(file = f"img_textBox3.png")
entry3_bg = canvas.create_image(
    276.0, 412.5,
    image = entry3_img)

entry3 = Entry(
    bd = 0,
    bg = "#ebebeb",
    highlightthickness = 0)

entry3.place(
    x = 77.5, y = 397,
    width = 397.0,
    height = 29)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 207, y = 462,
    width = 138,
    height = 53)

window.resizable(False, False)
window.mainloop()
