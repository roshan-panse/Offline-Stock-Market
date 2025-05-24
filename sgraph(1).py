# SAMPLEGRAPH WINDOW 
#importing libraries 
from tkinter import * 
from PIL import Image,ImageTk

# defining commands 
def proceed():
    sgraph_window.destroy()
    import graph

# create intro window    
sgraph_window=Tk()
sgraph_window.geometry("1535x835")
sgraph_window.title("SAMPLE GRAPH")
sgraph_window.resizable(0,0)
sgraph_window.config(bg="black")


# importing imgs
bb=ImageTk.PhotoImage(Image.open("sgraph.jpg"))
bbLabel=Label(sgraph_window,image=bb,bd=0)
bbLabel.place(x=0,y=0)
wintitle=Label(sgraph_window,text=' SAMPLE GRAPH ',font=('times',35,'bold'),bg='seagreen',fg='white',bd=8)
wintitle.place(x=550,y=0)

# proceed button
proceedButton=Button(sgraph_window,text="PROCEED⇒",command=proceed,font=("times",15,"bold"),width=10,bg="purple4",fg="white",bd=8)
proceedButton.place(x=1380,y=785 )

sgraph_window.mainloop()
