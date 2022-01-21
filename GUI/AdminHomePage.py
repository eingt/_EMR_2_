from tkinter import *


def click():
    print("Clicked")


window = Tk()
window.title('EMR')
window.iconbitmap("EMR Symbol.ico")j

window.geometry("1216x684")
window.configure(bg = "#fefefe")
canvas = Canvas(
    window,
    bg = "#fefefe",
    height = 684,
    width = 1216,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

bg = PhotoImage(file = f"AdminHomePage BG.png")
background = canvas.create_image(
    608.0, 342.0,
    image=bg)

ProfileIcon = PhotoImage(file = f"Profile Icon.png")
b1 = Button(
    image = ProfileIcon,
    borderwidth = 0,
    highlightthickness = 0,
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
    highlightthickness = 0,
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
    highlightthickness = 0,
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
    highlightthickness = 0,
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
    highlightthickness = 0,
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
    highlightthickness = 0,
    command = click,
    relief = "flat")

b6.place(
    x = 20, y = 183,
    width = 91,
    height = 63)

DoctorsIcon = PhotoImage(file = f"Doctors Icon HL.png")
b7 = Button(
    image = DoctorsIcon,
    borderwidth = 0,
    highlightthickness = 0,
    command = click,
    relief = "flat")

b7.place(
    x = 20, y = 114,
    width = 91,
    height = 67)

canvas.create_text(
    682.5, 326.5,
    text = "Jim Brandt",
    fill = "#6953d9",
    font = ("Lato-Bold", int(64.0)))

canvas.create_text(
    683.0, 280.0,
    text = "Welcome",
    fill = "#000000",
    font = ("Lato-Regular", int(24.0)))

window.resizable(False, False)
window.mainloop()
