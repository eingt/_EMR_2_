from tkinter import *


#-----------------------------------------------------------------------------------
def click():
    print("Clicked")

def AdminDoctorsPage():
    window.destroy()
    import AdminDoctorsPage

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

bg = PhotoImage(file = f"DoctorCard BG.png")
background = canvas.create_image(
    608, 342,
    image=bg)

ProfileIcon = PhotoImage(file = f"Profile Icon.png")
b1 = Button(
    image = ProfileIcon,
    borderwidth = 0,
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
    command = click,
    relief = "flat")

b7.place(
    x = 20, y = 114,
    width = 91,
    height = 67)
'''
MaleIcon = PhotoImage(file = f"Male Profile Icon.png")
b8 = Button(
    image = MaleIcon,
    borderwidth = 0,
    highlightthickness = 0,
    command = click,
    relief = "flat")

b8.place(
    x = 178, y = 43,
    width = 91,
    height = 92)
'''
UpdateButton = PhotoImage(file = f"Update Button.png")
b9 = Button(
    image = UpdateButton,
    borderwidth = 0,
    command = click,
    relief = "flat")

b9.place(
    x = 1100, y = 115,
    width = 67,
    height = 22)

canvas.create_text(
    368.0, 66.5,
    text = "John Peter",
    fill = "#000000",
    font = ("Lato-Bold", int(24.0)))

canvas.create_text(
    357.5, 90.0,
    text = "101",
    fill = "#000000",
    font = ("Lato-Regular", int(18.0)))

canvas.create_text(
    628.5, 69.5,
    text = "36",
    fill = "#000000",
    font = ("Lato-Light", int(14.0)))

AppCard = PhotoImage(file = f"AppointmentsCard.png")
canvas.create_image(
    930, 290,
    image = AppCard)

canvas.create_text(
    798.0, 262.0,
    text = "Clay Rigby",
    fill = "#000000",
    font = ("Lato-Regular", int(24.0)))

canvas.create_text(
    1031.5, 263.0,
    text = "15:30",
    fill = "#6953d9",
    font = ("Lato-Regular", int(36.0)))

canvas.create_text(
    798.5, 295.5,
    text = "8659423575",
    fill = "#000000",
    font = ("Lato-Light", int(18.0)))
'''
img9 = PhotoImage(file = f"img9.png")
b9 = Button(
    image = img9,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b9.place(
    x = 726, y = 229,
    width = 424,
    height = 106)
'''

EditButton = PhotoImage(file = f"Edit Icon.png")
b10 = Button(
    image = EditButton,
    borderwidth = 0,
    command = click,
    relief = "flat")

b10.place(
    x = 1125, y = 255,
    width = 17,
    height = 16)

DeleteButton = PhotoImage(file = f"Delete Icon.png")
b11 = Button(
    image = DeleteButton,
    borderwidth = 0,
    command = click,
    relief = "flat")

b11.place(
    x = 1124, y = 289,
    width = 19,
    height = 20)




window.resizable(False, False)
window.mainloop()
