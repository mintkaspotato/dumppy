import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

#do not use pack and grid together



root = Tk()
root.iconbitmap(default='icon.ico')

def show():
	label.config( text = clicked.get() )

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3)

logo = Image.open("logo.png")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

clicked = StringVar()
options = [
	"Styczeń",
	"Luty",
	"Marzec",
	"Kwiecień",
	"Maj",
	"Czerwiec",
	"Lipiec",
    "Sierpień",
	"Wrzesień",
	"Październik",
	"Listopad",
	"Grudzień"
]
drop1 = OptionMenu( root , clicked , *options )
clicked.set( "Wybierz miesiąc" )
button = Button( root , text = "Dodaj" , command = show )

label = Label( root , text = " " )






root.mainloop()

