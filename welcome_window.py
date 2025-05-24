#  WELCOME WINDOW
# importing libraries

from tkinter import *
from PIL import ImageTk,Image
# defining commands

def proceed():
    welcome_window.destroy()
    import sign

#create welcome window

welcome_window = Tk()
welcome_window.title('WELCOME WINDOW')
welcome_window.geometry("1535x835")
welcome_window.resizable(0,0)
LBACK=ImageTk.PhotoImage(Image.open("Untitled.jpg"))
BACK=Label(welcome_window,image=LBACK)
BACK.place(x=0,y=0)
#bgimage
 

# proceed 

proceedButton=Button(welcome_window,text="PROCEED⇒",command=proceed,font=("Times",20,"bold"),bg="purple4",fg="white",bd=8)
proceedButton.place(x=1310,y=765)

welcome_window.mainloop()