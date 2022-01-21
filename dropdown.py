# Import module
from tkinter import *

# Create object
root = Tk()

#icon
root.iconbitmap(default='icon.ico')


# Adjust size
root.geometry( "400x200" )

# Change the label text
def show():
	label.config( text = clicked.get() )

# Dropdown menu options
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

# datatype of menu text
clicked = StringVar()

# initial menu text
clicked.set( "Wybierz miesiąc" )

# Create Dropdown menu
drop = OptionMenu( root , clicked , *options )
drop.pack()

# Create button, it will change label text
button = Button( root , text = "Dodaj" , command = show ).pack()

# Create Label
label = Label( root , text = " Tu wyświetli się miesiąc " )
label.pack()

# Execute tkinter
root.mainloop()
