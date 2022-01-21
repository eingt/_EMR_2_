from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

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

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    608.0, 342.0,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 19, y = 605,
    width = 88,
    height = 70)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 19, y = 467,
    width = 90,
    height = 75)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = 19, y = 401,
    width = 90,
    height = 61)

img3 = PhotoImage(file = f"img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b3.place(
    x = 19, y = 317,
    width = 91,
    height = 77)

img4 = PhotoImage(file = f"img4.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b4.place(
    x = 19, y = 253,
    width = 91,
    height = 57)

img5 = PhotoImage(file = f"img5.png")
b5 = Button(
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b5.place(
    x = 19, y = 183,
    width = 91,
    height = 63)

img6 = PhotoImage(file = f"img6.png")
b6 = Button(
    image = img6,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b6.place(
    x = 19, y = 114,
    width = 91,
    height = 67)

img7 = PhotoImage(file = f"img7.png")
b7 = Button(
    image = img7,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b7.place(
    x = 178, y = 43,
    width = 91,
    height = 92)

img8 = PhotoImage(file = f"img8.png")
b8 = Button(
    image = img8,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b8.place(
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

img9 = PhotoImage(file = f"img9.png")
b9 = Button(
    image = img9,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b9.place(
    x = 1125, y = 255,
    width = 17,
    height = 16)

img10 = PhotoImage(file = f"img10.png")
b10 = Button(
    image = img10,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b10.place(
    x = 1124, y = 289,
    width = 19,
    height = 20)

window.resizable(False, False)
window.mainloop()
