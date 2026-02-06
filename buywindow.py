#BUY WINDOW#
#importing libraries
from tkinter import *
import mysql.connector as sqltor
import pandas as pd
from PIL import ImageTk,Image
from tkinter import messagebox
from datetime import date
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# defining commands
def exit():
    buy_window.destroy()
def clear():
  qtyy.delete(0,END)


def grph():
    
    buy_window.destroy ()
    import graph


def portfolio():
 
    buy_window.destroy ()
    import portfolio


def buy():
     if menu1.get()=='RELIANCE':
         curprice=2421
     elif menu1.get()=='ADANI': 
         curprice=1925
     elif menu1.get()=='TATA MOTORS':
         curprice=485
     elif menu1.get()=='ITC':
         curprice=426
     elif menu1.get()=='SBI':
         curprice=578
     elif menu1.get()=='INFOSYS':
         curprice=1253
     elif menu1.get()=='HDFC BANK':
         curprice=1688
     qty=int(qtyy.get())
     amt=qty*curprice
     amount=int(amt)
     balance=10000-amount
     amnnt=Label(buy_window,text=amt,font=('times',20,'bold') ,width=10)
     amnnt.place(x=190,y=665)
     blnn=Label(buy_window,width=8,text=balance,font=('times',20,'bold'))
     blnn.place(x=1380,y=165)
   
         
        
     
     if balance<0:
        messagebox.showerror('ERROR!','''Insufficient Balance ! Pls Enter Valid QTY ''')
        blnn=Label(buy_window,width=8,text=10000,font=('times',20,'bold'))
        blnn.place(x=1380,y=165) 
                                  
     elif balance > 0 :
           if usernameentry.get()=='' and passwordentry.get()=='' :
               messagebox.showerror('error','enter data')
           else:
             usrnm=usernameentry.get()
             psswd=passwordentry.get()
             qunty=qtyy.get()
             ammtp=amount
             cmpny=menu1.get()
             cur=curprice
           
             mycon=sqltor.connect(host="localhost", user="root", passwd="291516", database="clg_project",auth_plugin="mysql_native_password")
             c=mycon.cursor(buffered=True)
             query="INSERT INTO buy (username,password,company,priceperunit,qty,amntpaid,date) VALUES (%s,%s,%s,%s,%s,%s,(curdate()))"
            
             c.execute(query,(usrnm,psswd,cmpny,cur,qunty,ammtp))
           
             mycon.commit()
             mycon.close()
             messagebox.showinfo('success','successful')
     else:
         print()


# taking data for the graph
mycon=sqltor.connect(host="localhost", user="root", passwd="291516", database="clg_project",auth_plugin="mysql_native_password")
mycursor = mycon.cursor()
if mycon.is_connected():
     reliance4_weekly=pd.read_sql("select * from reliance_weekly where date>'2025-03-27'",mycon)
     tata4_weekly=pd.read_sql("select * from tata_weekly where date>'2025-03-27'",mycon)
     adani4_weekly=pd.read_sql("select * from adani_weekly where date>'2025-03-27'",mycon)
     hdfc4_weekly=pd.read_sql("select * from hdfc_weekly where date>'2025-03-27'",mycon)
     infosys4_weekly=pd.read_sql("select * from infosys_weekly where date>'2025-03-27'",mycon)
     itc4_weekly=pd.read_sql("select * from itc_weekly where date>'2025-03-27'",mycon)
     sbi4_weekly=pd.read_sql("select * from sbi_weekly where date>'2025-03-27'",mycon)
     
     
#making graph from data 

def reliance4_graph_weekly():
      plt.figure(figsize=(7,5))
      plt.plot(reliance4_weekly['date'],reliance4_weekly['price'])
      #fill cekly['date'],reliance_weekly['price'], color='blue', alpha=0.3)
      
      plt.xlabel('Date(in weeks)')
      plt.ylabel('Stock Price')
      plt.title('Reliance_Weekly')
      plt.grid(True)
      canvas = FigureCanvasTkAgg(plt.gcf(), master=graphlabel)
      
      
      canvas.get_tk_widget().pack()
      canvas.get_tk_widget()
      canvas.draw()
     

def tata4_graph_weekly():
      plt.figure(figsize=(7,5))
      plt.plot(tata4_weekly['date'],tata4_weekly['price'])
      #fill colorr='red', alpha=0.3)
      
      plt.xlabel('Date(in weeks)')
      plt.ylabel('Stock Price')
      plt.grid(True)
      canvas = FigureCanvasTkAgg(plt.gcf(), master=graphlabel)
      canvas.get_tk_widget()
      canvas.get_tk_widget().pack()
      canvas.get_tk_widget()
      
      canvas.draw()
      
def adani4_graph_weekly():
      plt.figure(figsize=(7,5))
      plt.plot(adani4_weekly['date'],adani4_weekly['price'])
      #fill col
      
      plt.xlabel('Date(in weeks)')
      plt.ylabel('Stock Price')
      plt.title('Adani_Weekly')
      plt.grid(True)
      canvas = FigureCanvasTkAgg(plt.gcf(), master=graphlabel)
      canvas.get_tk_widget()
      canvas.get_tk_widget().pack()
      canvas.get_tk_widget()
      canvas.draw()

def hdfc4_graph_weekly():
      plt.figure(figsize=(7,5))
      plt.plot(hdfc4_weekly['date'],hdfc4_weekly['price'])
      #fill col
      
      plt.xlabel('Date(in weeks)')
      plt.ylabel('Stock Price')
      plt.title('Hdfc_Weekly')
      plt.grid(True)
      canvas = FigureCanvasTkAgg(plt.gcf(), master=graphlabel)
      canvas.get_tk_widget()
      canvas.get_tk_widget().pack()
      canvas.get_tk_widget()
      canvas.draw()
      
def infosys4_graph_weekly():
      plt.figure(figsize=(7,5))
      plt.plot(infosys4_weekly['date'],infosys4_weekly['price'])
      #fill colo
      
      plt.xlabel('Date(in weeks)')
      plt.ylabel('Stock Price')
      plt.title('Infosys_Weekly')
      plt.grid(True)
      canvas = FigureCanvasTkAgg(plt.gcf(), master=graphlabel)
      canvas.get_tk_widget()
      canvas.get_tk_widget().pack()
      canvas.get_tk_widget()
      canvas.draw()
      
def itc4_graph_weekly():
      plt.figure(figsize=(7,5))
      plt.plot(itc4_weekly['date'],itc4_weekly['price'])
      #fill color
      
      plt.xlabel('Date(in weeks)')
      plt.ylabel('Stock Price')
      plt.title('ITC_Weekly')
      plt.grid(True)
      canvas = FigureCanvasTkAgg(plt.gcf(), master=graphlabel)
      canvas.get_tk_widget()
      canvas.get_tk_widget().pack()
      canvas.get_tk_widget()
      
      canvas.draw()
      
def sbi4_graph_weekly():
      plt.figure(figsize=(7,5))
      plt.plot(sbi4_weekly['date'],sbi4_weekly['price'])
      #fill color
      
      plt.xlabel('Date(in weeks)')
      plt.ylabel('Stock Price')
      plt.title('SBI_Weekly')
      plt.grid(True)
      canvas = FigureCanvasTkAgg(plt.gcf(), master=graphlabel)
      canvas.get_tk_widget()

      canvas.get_tk_widget().pack()
      canvas.get_tk_widget()
      canvas.draw()



def current():
     if menu1.get()=='RELIANCE':
         curprice=2421
     elif menu1.get()=='ADANI': 
         curprice=1925
     elif menu1.get()=='TATA MOTORS':
         curprice=485
     elif menu1.get()=='ITC':
         curprice=426
     elif menu1.get()=='SBI':
         curprice=578
     elif menu1.get()=='INFOSYS':
         curprice=1253
     elif menu1.get()=='HDFC BANK':
         curprice=1688
    
     # label for price
     price=Label(buy_window,text=curprice,font=('times ',20,'bold'),width=10)
     price.place(x=190,y=465)
     
     #now for graph
     if menu1.get()=='RELIANCE':
         reliance4_graph_weekly()
     elif menu1.get()=='ADANI': 
         adani4_graph_weekly()
     elif menu1.get()=='TATA MOTORS':
         tata4_graph_weekly()
     elif menu1.get()=='ITC':
         itc4_graph_weekly()
     elif menu1.get()=='SBI':
         sbi4_graph_weekly()
     elif menu1.get()=='INFOSYS':
         infosys4_graph_weekly()
     elif menu1.get()=='HDFC BANK':
         hdfc4_graph_weekly()
     


# main window
buy_window=Tk()
buy_window.title("Buy Window")
buy_window.geometry("1535x835")
buy_window.resizable(0,0)
buy_window.configure(bg='seagreen1')


#importing image


bu=Label(buy_window,text='EXCHANGE STOCKS',font=('times',45,'bold'),bg='seagreen',fg='white',bd=8)
bu.place(x=500,y=0)

graphlabel=Label(buy_window,bg='seagreen1')
graphlabel.place(x=710,y=250)

# GUI CONTENT ⇣
#labels and entry box

username=Label(buy_window,text="USERNAME:",font=("Times",20,"bold"),bg="cyan",fg="black")
username.place(x=0,y=165)
usernameentry=Entry(buy_window,width=23,font=("Times",20,"bold"),bg="white",fg="black",bd=0)
usernameentry.place(x=190,y=165)


datee=Label(buy_window,text='      DATE :     ', font=('times',20,'bold'),bg='cyan',fg='black')
datee.place(x=0,y=100)
today=date.today()
d=Label(buy_window,text=today,font=('times',20,'bold'))
d.place(x=190,y=100)

password=Label(buy_window,text="PASSWORD:",font=("Times",20,"bold"),bg="cyan",fg="black")
password.place(x=0,y=265)
passwordentry=Entry(buy_window,width=23,font=("Times",20,"bold"),bg="white",fg="black",bd=0,show="*")
passwordentry.place(x=190,y=265)

compny=Label(buy_window,text=' COMPANY: ',font=('times',20,"bold"),bg='cyan',fg='black'  )
compny.place(x=0,y=365)

ppr=Label(buy_window,text='     PRICE:     ',font=('times',20,"bold"),bg='cyan',fg='black'  )
ppr.place(x=0,y=465)
price=Label(buy_window,text='PRICE',font=('times',20,'bold'),width=10)
price.place(x=190,y=465)


qtty=Label(buy_window,text=' QUANTITY: ',font=('times',20,'bold'),bg='cyan')
qtty.place(x=0,y=565)

qtyy=Entry(buy_window,font=('times',20,'bold'),width=23)
qtyy.place(x=190,y=565)

amount1=Label(buy_window,text='  AMOUNT :  ',font=('times',20,'bold'),bg='cyan')
amount1.place(x=0,y=665)
amount2=Label(buy_window,text='amount',font=('times',20,'bold'),width=10)
amount2.place(x=190,y=665)

bln1=Label(buy_window,width=10,text='Balance:',font=('times',20,'bold'),bg='seagreen2')
bln1.place(x=1180,y=165)
bln2=Label(buy_window,width=8,text=10000,font=('times',20,'bold'))
bln2.place(x=1380,y=165)

# drop down
menu1=StringVar()
menu1.set("Choose Here")
drop1=OptionMenu(buy_window,menu1,"RELIANCE","TATA MOTORS","ADANI","HDFC BANK","INFOSYS","ITC","SBI")
drop1.config(font=('times',20,'bold'))
drop1.place(x=190,y=365)



# buttons

check=Button(buy_window,text=' Current Price',command=lambda: current(),font=('times',14,'bold'),bg='purple4',fg='white',bd=8)
check.place(x=380,y=465)

buy1=Button(buy_window,text='       BUY       ',command=lambda: buy(),font=('times',20,'bold'),bg='purple4',fg='white',bd=8)
buy1.place(x=406,y=765)

portfolio1=Button(buy_window,text='PORTFOLIO',command=lambda: portfolio(),font=('times',20,'bold'),bg='purple4',fg='white',bd=8)
portfolio1.place(x=1330,y=765)

clr=Button(buy_window,text='CLEAR',command=clear,font=('times',20,'bold'),bd=8,bg='purple4',fg='white')
clr.place(x=0,y=765)


EXIT_button = Button(buy_window, text="EXIT", command=exit, bg='purple4',fg='white',width=17, font=('times', 18, 'bold'),bd=5)
EXIT_button.place(x=1280, y=0)
buy_window.mainloop()