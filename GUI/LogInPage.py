from tkinter import *

User = 'jb23'
Pass = 'jb23'

def ErrorMessage():
    TextBox1.delete(0, END)
    TextBox2.delete(0, END)
    canvas.create_text(
        650, 460,
        text="Username or Password is incorrect. Please try again.",
        fill="#e10808",
        anchor = "center",
        font=("Lato-Light", int(10.0)))

def LogIn():
    TB1 = (TextBox1.get())
    TB2 = (TextBox2.get())

    if TB1 == User:
        if TB2 == Pass:
            window.destroy()
            import AdminHomePage
        else:
            ErrorMessage()
    else:
        ErrorMessage()

window = Tk()
window.title("EMR Log In")
window.iconbitmap("EMR Symbol.ico")

window.geometry("830x570")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 569,
    width = 829,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

bg = PhotoImage(file = f"LogInPage BG.png")
background = canvas.create_image(
    400.0, 297.5,
    image=bg)

TextBoximg = PhotoImage(file = f"Text Box Img.png")
TextBox1 = canvas.create_image(
    643.5, 284.0,
    image = TextBoximg)

TextBox1 = Entry(
    bd = 0)

TextBox1.place(
    x = 530.0, y = 269,
    width = 227.0,
    height = 30)

TextBox2 = canvas.create_image(
    643.5, 353.0,
    image = TextBoximg)

TextBox2 = Entry(
    bd = 0,
    show = "*")

TextBox2.place(
    x = 530.0, y = 338,
    width = 227.0,
    height = 30)

LogInBtn = PhotoImage(file = f"Log In Button.png")
b1 = Button(
    image = LogInBtn,
    command = LogIn,
    relief = "flat")

b1.place(
    x = 575, y = 380,
    width = 138,
    height = 59)

window.resizable(False, False)
window.mainloop()