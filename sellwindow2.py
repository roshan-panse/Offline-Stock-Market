#SELLWINDOW
#importing libraries 
from tkinter import *
import mysql.connector as sqltor
import pandas as pd
from PIL import ImageTk,Image
from tkinter import messagebox
from datetime import date
import matplotlib.pyplot as plt

# definig commands

def portfolio():
 
    sell_window.destroy ()
    import portfolio2
    
def exit():
    sell_window.destroy ()

def sell():
   
     
     mycon=sqltor.connect(host="localhost", user="root", passwd="291516", database="clg_project",auth_plugin='mysql_native_password')
     mycursor = mycon.cursor()
     if mycon.is_connected():
         query="update buy set qty=0 , amntpaid=0 where username=%s and company=%s"
         
         mycursor.execute(query,[(usernameentry.get()),(menu1.get())])
         mycon.commit()
         mycon.close()
         print("query done")
         messagebox.showinfo('Success','Successful')
    
        
    
# main window
sell_window=Tk()
sell_window.title("Buy Window")
sell_window.geometry("1300x750")
sell_window.resizable(0,0)
sell_window.title('MANAGE STOCKS')
sell_window.configure(bg='tomato')

# GUI CONTENT ⇣
# labels and entry box

username=Label(sell_window,text="USERNAME:",font=("Times",20,"bold"),bg="cyan",fg="black")
username.place(x=0,y=165)
usernameentry=Entry(sell_window,width=23,font=("Times",20,"bold"),bg="white",fg="black",bd=0)
usernameentry.place(x=190,y=165)

today=date.today()

date1=Label(sell_window,text='      DATE :     ', font=('times',20,'bold'),bg='cyan',fg='black')
date1.place(x=0,y=100)
date2=Label(sell_window,text=today,font=('times',20,'bold'))
date2.place(x=190,y=100)

wintitle=Label(sell_window,text='MANAGE STOCKS',font=('times',45,'bold'),bg='medium spring green',fg='white')
wintitle.place(x=380,y=0)


password=Label(sell_window,text="PASSWORD:",font=("Times",20,"bold"),bg="cyan",fg="black")
password.place(x=0,y=265)
passwordentry=Entry(sell_window,width=23,font=("Times",20,"bold"),bg="white",fg="black",bd=0,show="*")
passwordentry.place(x=190,y=265)


compny=Label(sell_window,text=' COMPANY: ',font=('times',20,"bold"),bg='cyan',fg='black'  )
compny.place(x=0,y=365)


menu1=StringVar()
menu1.set("Choose Here")
drop1=OptionMenu(sell_window,menu1,"RELIANCE","TATA MOTORS","ADANI","HDFC BANK","INFOSYS","ITC","SBI")
drop1.config(font=('times',20,'bold'))
drop1.place(x=190,y=365)




#button
bu=Button(sell_window,text='       SELL       ',command=lambda: sell(),font=('times',20,'bold'),bg='purple4',fg='white',bd=8)
bu.place(x=406,y=680)

port=Button(sell_window,text='PORTFOLIO',command=lambda: portfolio(),font=('times',20,'bold'),bg='purple4',fg='white',bd=8)
port.place(x=1030,y=680)

EXIT_button = Button(sell_window, text="EXIT", command=exit, bg='purple4',fg='white',width=17, font=('times', 18, 'bold'),bd=5)
EXIT_button.place(x=1080, y=0)

sell_window.mainloop()