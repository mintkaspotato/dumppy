import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

def welcomeMessage():
    name = name_Tf.get()
    return messagebox.showinfo('message',f'wartość dodana')
  
# Creating tkinter window
window = tk.Tk()
window.title('BUDGET1.0')
window.geometry('500x300')

logo = Image.open("logo.png")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

var = tk.StringVar()
titlabel = tk.Label( window, textvariable=var )
var.set("budget1.0 - your BUD for gadGET shopping!")
titlabel.grid(column=1,row=1)

# Label
ttk.Label(window, text = "Select the Month :", 
        font = ("Times New Roman", 10)).grid(column = 0, 
        row = 15, padx = 10, pady = 25)
  
n = tk.StringVar()
monthchoosen = ttk.Combobox(window, width = 27, 
                            textvariable = n)
  
# Adding combobox drop down list
monthchoosen['values'] = (' January', 
                          ' February',
                          ' March',
                          ' April',
                          ' May',
                          ' June', 
                          ' July', 
                          ' August', 
                          ' September', 
                          ' October', 
                          ' November', 
                          ' December')
  
monthchoosen.grid(column = 1, row = 15)
  
# Shows february as a default value
monthchoosen.current(0) 

name_Tf = tk.Entry(window)
name_Tf.grid(column=1, row=17)

tk.Button(window, text="Click Here", command=welcomeMessage).grid(column=2, row =17)

window.mainloop()