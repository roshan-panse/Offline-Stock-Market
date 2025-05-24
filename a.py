from tkinter import * 
import mysql.connector as myconn
from PIL import ImageTk,Image
from tkinter import messagebox
from datetime import date
import pandas as pd
from tkinter import ttk


def sell():
    print("Sell button clicked")
    portfolio.destroy ()
    import sellwindow
 

def cnfrm():
   if usernameentry.get()=="" or passwordentry.get()=="" :
        messagebox.showerror('ERROR','INSERT ALL DETAILS')
   else:
        mycon=myconn.connect(host="localhost",user="root",passwd="1711",database="school_project")
        c=mycon.cursor(buffered=True)
       
        uname=usernameentry.get()
        passw=passwordentry.get()
         


        query = "SELECT username ,password FROM buy  WHERE username = %s and password=%s"
        c.execute(query, [(uname),(passw)])
       
        ce=c.fetchall()
        if ce == NONE :
            messagebox.showerror('ERROR','INVALID DETAILS :<')
        elif ce:
               messagebox.showinfo('success','proceed to portfolio')
               buton.destroy()
               l1=Label(portfolio,text=usernameentry.get(),font=('times',20,'bold'),bg='snow',width=23).place(x=190,y=155)
               f1=Frame(portfolio,width=1300,height=700,bg='red')
               f1.place(x=10,y=200)
               
               
               
               table=pd.read_sql("select*from buy",mycon)
               tree = ttk.Treeview(f1, columns=list(table.columns), show='headings')
               
               for col in table.columns:
                 tree.heading(col, text=col)
                
               for i, row in table.iterrows():
                 tree.insert("", "end", values=list(row))
               
               style = ttk.Style()
               style.configure("Treeview.Heading", font=('times', 20, 'bold'))
               style.configure("Treeview", font=('times', 15))
               tree.pack()

                
        else:
            messagebox.showerror('ERROR','you dont have previous history')
       
       
        sell=Button(portfolio,text='SELL',command=lambda: sell(),font=('times',20,'bold'),bg='purple4',fg='white',bd=8)
        sell.place(x=730,y=480)

portfolio=Tk()
portfolio.geometry('1400x700')
portfolio.resizable(0,0)
portfolio.config(bg='cyan')

l1=Label(portfolio,text='PORTFOLIO',bg='red',fg='white',font=('times',50,'bold'))
l1.place(x=550,y=0)


username=Label(portfolio,text="USERNAME:",font=("Times",20,"bold"),bg="cyan",fg="black")
username.place(x=0,y=155)
usernameentry=Entry(portfolio,width=23,font=("Times",20,"bold"),bg="white",fg="black",bd=0)
usernameentry.place(x=190,y=155)

password=Label(portfolio,text="PASSWORD:",font=("Times",20,"bold"),bg="cyan",fg="black")
password.place(x=600,y=155)
passwordentry=Entry(portfolio,width=23,font=("Times",20,"bold"),bg="white",fg="black",bd=0,show="*")
passwordentry.place(x=790,y=155)


buton=Button(portfolio,text='CONFIRM ',width=16,bg='purple4',fg='white',font=('times',20,'bold'),bd=8,command=cnfrm)
buton.place(x=700,y=350)


portfolio.mainloop()