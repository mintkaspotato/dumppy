#import tkinter as tk
#from PIL import Image, ImageTk
#
#root = tk.Tk()
#
#
#logo = Image.open("logo.png")
#logo = ImageTk.PhotoImage(logo)
#logo_label = tk.Label(image=logo)
#logo_label.image = logo
#logo_label.grid(column=1, row=0)        
    
  
#root.mainloop()

# importing Image class from PIL package
#from PIL import Image

# creating a object
#im = Image.open("logo.png")

#im.show()
import plotly.express as px
import numpy as np
  
  
# RGB Data as numpy array
img_rgb = np.array([[[255, 0, 0], [0, 255, 0], [0, 0, 255]],
                    ], dtype=np.uint8)
  
fig = px.imshow(img_rgb)
fig.show()