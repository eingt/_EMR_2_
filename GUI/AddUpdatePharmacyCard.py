from tkinter import *
import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'maneeshj',
    port = '3306',
    database = 'EMR')
mycursor = mydb.cursor()

def add():
    rec = (name_entry.get(),mfd_entry.get(),int(stock_entry.get()),float(price_entry.get()))
    mycursor.execute("insert into pharmacy(MedName,MfdCompany,Stock,Price) values(%s,%s,%s,%s)",rec)


def update():
    command = "update doctors set name = '" + str(name_entry.get()) + "' where id = "+ str(sel_medid)+";"
    mycursor.execute(command)
    command = "update doctors set age = " + str(mfd_entryimg.get()) + " where id = "+ str(sel_medid)
    mycursor.execute(command)
    command = "update doctors set phone = '" + str(stock_entry.get()) + "' where id = "+ str(sel_medid)
    mycursor.execute(command)
    command = "update doctors set price = '" + str(price_entry.get()) + "' where id = "+ str(sel_medid)
    mycursor.execute(command)

    mycursor.execute(command)
    mydb.commit()
    root.destroy()
    import AdminPharmacyPage

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

background_img = PhotoImage(file = "AddUpdatePharmacyCard BG.png")
background = canvas.create_image(
    275.5, 284.0,
    image=background_img)


name_entryimg = PhotoImage(file = "TextBox4.png")
name_entry = canvas.create_image(
    276.0, 171,
    image = name_entryimg)

name_entry = Entry(
    bd = 0,
    highlightthickness = 0)
name_entry.insert(0,sel_doc[1])
name_entry.place(
    x=77.5, y=157,
    width=397.0,
    height=29)

mfd_entryimg = PhotoImage(file = "TextBox4.png")
mfd_entry = canvas.create_image(
    276.0, 251,
    image = mfd_entryimg)

mfd_entry = Entry(
    bd = 0,
    highlightthickness = 0)
mfd_entry.insert(0,sel_doc[2])
mfd_entry.place(
    x=77.5, y=237,
    width=397.0,
    height=29)

stock_entryimg = PhotoImage(file = "TextBox4.png")
stock_entry = canvas.create_image(
    276.0, 331,
    image = stock_entryimg)

stock_entry = Entry(
    bd = 0,
    highlightthickness = 0)
stock_entry.insert(0,sel_doc[6])
stock_entry.place(
    x=77.5, y=317,
    width=397.0,
    height=29)

price_entryimg = PhotoImage(file = "TextBox4.png")
price_entry = canvas.create_image(
    276.0, 411,
    image = price_entryimg)

price_entry = Entry(
    bd = 0,
    highlightthickness = 0)
price_entry.insert(0,sel_doc[3])
price_entry.place(
    x=77.5, y=397,
    width=397.0,
    height=29)

Updateimg = PhotoImage(file = "UpdateButton.png")
b1 = Button(
    image = Updateimg,
    borderwidth = 0,
    highlightthickness = 0,
    command = add,
    relief = "flat")

b1.place(
    x = 208, y = 480,
    width = 138,
    height = 53)

CancelImg = PhotoImage(file = "Cancel Button.png")
b2 = Button(
    image = CancelImg,
    borderwidth = 0,
    highlightthickness = 0,
    command = cancel,
    relief = "flat")

b2.place(
    x = 235, y = 530,
    width = 89,
    height = 17)


root.resizable(False, False)
root.mainloop()
