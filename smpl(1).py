import tkinter as tk
from PIL import Image, ImageTk

def set_access_window():
    window = tk.Tk()

    
    window.title("Access Window")
    window.geometry("1535x835")

    
    back_image_path = 'BACK2.jpeg'
    set_background_image(window, back_image_path)

    
    front_image_path = 'stock m.jpg'
    set_front_image(window, front_image_path)

    
    label = tk.Label(window, text="Access Window", font=("Helvetica", 16), bg="green", fg="white")
    label.place(relx=0.5, rely=0.05, anchor=tk.N)

    
    button_width = 45  
    button_height = 2  

    button1 = tk.Button(window, text="NEWBIE", command=lambda: button_callback(1), bg="purple4", fg="white", width=button_width, height=button_height)
    button1.place(relx=0.04, rely=0.3, anchor=tk.W)

    button2 = tk.Button(window, text="GRAPHS", command=lambda: button_callback(2), bg="purple4", fg="white", width=button_width, height=button_height)
    button2.place(relx=0.04, rely=0.4, anchor=tk.W)

    button3 = tk.Button(window, text="BUY STOCKS", command=lambda: button_callback(3), bg="purple4", fg="white", width=button_width, height=button_height)
    button3.place(relx=0.04, rely=0.5, anchor=tk.W)

    button4 = tk.Button(window, text="MANAGE STOCKS", command=lambda: button_callback(4), bg="purple4", fg="white", width=button_width, height=button_height)
    button4.place(relx=0.04, rely=0.6, anchor=tk.W)

    
    window.mainloop()


def set_background_image(window, image_path):
    
    image = Image.open(image_path)
    
    
    image = image.resize((1535, 835), Image.ANTIALIAS)

    
    tk_image = ImageTk.PhotoImage(image)

    
    canvas = tk.Canvas(window, width=1535, height=835)
    canvas.pack()

    
    canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)

   
    canvas.image = tk_image

def set_front_image(window, image_path):
    
    image = Image.open(image_path)
    
    
    image = image.resize((1000, 660), Image.ANTIALIAS)

    
    tk_image = ImageTk.PhotoImage(image)

    
    canvas = tk.Canvas(window, width=1000, height=660)
    canvas.place(relx=0.7, rely=0.5, anchor=tk.CENTER)
    canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)

    canvas.image = tk_image

def button_callback(button_number):
    print(f"Button {button_number} clicked!")

set_access_window()