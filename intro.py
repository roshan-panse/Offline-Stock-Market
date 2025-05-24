# INTRO WINDOW
#importing libraries 
from tkinter import * 
from PIL import Image,ImageTk

# defining commands 
def proceed():
    intro_window.destroy()
    import sgraph

# create intro window    
intro_window=Tk()
intro_window.geometry("1535x835")
intro_window.title("INTRODUCTION")
intro_window.resizable(0,0)
intro_window.config(bg="black")

# importing imgs
bb=ImageTk.PhotoImage(Image.open("intro.jpg"))
bbLabel=Label(intro_window,image=bb,bd=0)
bbLabel.place(x=0,y=0)


# proceed button
proceedButton=Button(intro_window,text="PROCEED⇒",command=proceed,font=("times",15,"bold"),width=10,bg="purple4",fg="white",bd=8)
proceedButton.place(x=1380,y=785 )

intro_window.mainloop()
