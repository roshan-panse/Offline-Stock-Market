# ACCESS WINDOW 
#importing libraries 

from tkinter import *
from PIL import Image,ImageTk

# definig commands 

def new():
  access_window.destroy()
  import intro

def graphwin():
  access_window.destroy()
  import graph

def buywin():
  access_window.destroy()
  import buywindow

def port():
  access_window.destroy()
  import portfolio
 
# creating window 

access_window=Tk()
access_window.geometry('1535x835')
access_window.resizable(0,0)
access_window.config(bg='sea green')
access_window.title('ACCESS WINDOW')

# inserting imgs

logimage=ImageTk.PhotoImage(Image.open("BACK2.jpeg"))
logLabel=Label(access_window,image=logimage).place(x=0,y=0)

graphimg=ImageTk.PhotoImage(Image.open("stock m.jpg"))
graphh=Label(access_window,image=graphimg,bd=0).place(x=450,y=100)


# GUI CONTENT ⇣
#labels 

wintitle=Label(access_window,text=' ACCESS WINDOW ',font=('times',35,'bold'),bg='seagreen',fg='white',bd=8)
wintitle.place(x=550,y=0)

# buttons

newbie=Button(access_window,text='NEWBIE',width=25,bg='purple4',fg='white',font=('times',20,'bold'),bd=8,command= new)
newbie.place(x=0,y=150)

graph=Button(access_window,text='GRAPHS ',bg='purple4',width=25,fg='white',font=('times',20,'bold'),bd=8,command=graphwin)
graph.place(x=0,y=250)

buystock=Button(access_window,text='BUY STOCKS',bg='purple4',width=25,fg='white',font=('times',20,'bold'),bd=8,command=buywin)
buystock.place(x=0,y=350)

mngstock=Button(access_window,text='MANAGE STOCKS ',width=25,bg='purple4',fg='white',font=('times',20,'bold'),bd=8,command=port)
mngstock.place(x=0,y=450)


access_window.mainloop()