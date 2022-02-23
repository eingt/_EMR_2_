from tkinter import *
import mysql.connector

def btn_clicked():
    print("Button Clicked")

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
    accountid = d[4]

root = Tk()
root.title('Update Patient Details')
root.iconbitmap("EMR Symbol.ico")

root.geometry("535x524")
root.configure(bg = "#ffffff")
canvas = Canvas(
    root,
    bg = "#ffffff",
    height = 524,
    width = 535,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = "UpdateUserAccount BG.png")
background = canvas.create_image(
    267.5, 263.0,
    image=background_img)

entry0_img = PhotoImage(file = "TextBox4.png")
entry0_bg = canvas.create_image(
    268.0, 150.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    highlightthickness = 0)

entry0.place(
    x = 69.5, y = 137,
    width = 397.0,
    height = 29)

entry1_img = PhotoImage(file = "TextBox4.png")
entry1_bg = canvas.create_image(
    268.0, 230.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    highlightthickness = 0)

entry1.place(
    x = 69.5, y = 217,
    width = 397.0,
    height = 29)

entry2_img = PhotoImage(file = "TextBox4.png")
entry2_bg = canvas.create_image(
    268.0, 310.5,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    highlightthickness = 0)

entry2.place(
    x = 69.5, y = 297,
    width = 397.0,
    height = 29)

entry3_img = PhotoImage(file = "TextBox4.png")
entry3_bg = canvas.create_image(
    268.0, 390.5,
    image = entry3_img)

entry3 = Entry(
    bd = 0,
    highlightthickness = 0)

entry3.place(
    x = 69.5, y = 377,
    width = 397.0,
    height = 29)

UpdateImg = PhotoImage(file = "UpdateButton.png")
b1 = Button(
    image = UpdateImg,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 199, y = 430,
    width = 138,
    height = 53)

CancelImg = PhotoImage(file = "Cancel Button.png")
b2 = Button(
    image = CancelImg,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = 223, y = 487,
    width = 89,
    height = 17)

root.resizable(False, False)
root.mainloop()
