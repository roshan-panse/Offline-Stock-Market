#GRAPH_WINDOW
# importing libraries
from tkinter import *
import matplotlib.pyplot as plt
import mysql.connector as sqltor
import pandas as pd
from PIL import ImageTk,Image


# definig commands

def BUY():
    graph_window.destroy()
    import buywindow 

#connecting mysql and python

mycon=sqltor.connect(host="localhost", user="root", passwd="291516", database="clg_project",auth_plugin="mysql_native_password")
if mycon.is_connected():
      reliance_monthly=pd.read_sql("select*from reliance_monthly",mycon)
      tata_monthly=pd.read_sql("select*from tata_monthly",mycon)
      adani_monthly=pd.read_sql("select*from adani_monthly",mycon)
      hdfc_monthly=pd.read_sql("select*from hdfc_monthly",mycon)
      infosys_monthly=pd.read_sql("select*from infosys_monthly",mycon)
      itc_monthly=pd.read_sql("select*from itc_monthly",mycon)
      sbi_monthly=pd.read_sql("select*from sbi_monthly",mycon)
      # now weekly
      reliance_weekly=pd.read_sql("select*from reliance_weekly",mycon)
      tata_weekly=pd.read_sql("select*from tata_weekly",mycon)
      adani_weekly=pd.read_sql("select*from adani_weekly",mycon)
      hdfc_weekly=pd.read_sql("select*from hdfc_weekly",mycon)
      infosys_weekly=pd.read_sql("select*from infosys_weekly",mycon)
      itc_weekly=pd.read_sql("select*from itc_weekly",mycon)
      sbi_weekly=pd.read_sql("select*from sbi_weekly",mycon)
    
# code for graphs

# for reliance
def reliance_graph_monthly():
      plt.plot(reliance_monthly['date'],reliance_monthly['price'])
      #fi(reliance_monthly['date'],reliance_monthly['price'], color='blue', alpha=0.3)
      plt.xlabel('Date(in months)')
      manager = plt.get_current_fig_manager()
      manager.full_screen_toggle()
      plt.ylabel('Stock Price')
      plt.title('Reliance_Monthly')
      plt.show()

def reliance_graph_weekly():
      plt.plot(reliance_weekly['date'],reliance_weekly['price'])
      #fill cekly['date'],reliance_weekly['price'], color='blue', alpha=0.3)
      plt.xlabel('Date(in weeks)')
      manager = plt.get_current_fig_manager()
      manager.full_screen_toggle()
      plt.ylabel('Stock Price')
      plt.title('Reliance_Weekly')
      plt.show()
      
#for Tata
def tata_graph_monthly():
      plt.plot(tata_monthly['date'],tata_monthly['price'])
      #fill color
      
      plt.xlabel('Date(in months)')
      manager = plt.get_current_fig_manager()
      manager.full_screen_toggle()
      plt.ylabel('Stock Price')
      plt.title('Tata_Monthly')
      plt.show()
      
def tata_graph_weekly():
      plt.plot(tata_weekly['date'],tata_weekly['price'])
      #fill colorr='red', alpha=0.3)
      plt.xlabel('Date(in weeks)')
      manager = plt.get_current_fig_manager()
      manager.full_screen_toggle()
      plt.ylabel('Stock Price')
      plt.title('Tata_Weekly')
      plt.show()
     
# for Adani 
def adani_graph_monthly():
      plt.plot(adani_monthly['date'],adani_monthly['price'])
      #fill color
      
      plt.xlabel('Date(in months)')
      plt.ylabel('Stock Price')
      plt.title('Adani_Monthly')
      manager = plt.get_current_fig_manager()
      manager.full_screen_toggle()
      plt.show()

def adani_graph_weekly():
      plt.plot(adani_weekly['date'],adani_weekly['price'])
      #fill color

      plt.xlabel('Date(in weeks)')
      manager = plt.get_current_fig_manager()
      manager.full_screen_toggle()
      plt.ylabel('Stock Price')
      plt.title('Adani_Weekly')
      plt.show()

# for hdfc 

def hdfc_graph_monthly():
      plt.plot(hdfc_monthly['date'],hdfc_monthly['price'])
      
      plt.xlabel('Date(in months)')
      plt.ylabel('Stock Price')
      plt.title('Hdfc_Monthly')
      manager = plt.get_current_fig_manager()
      manager.full_screen_toggle()
      plt.show()
    
def hdfc_graph_weekly():
      plt.plot(hdfc_weekly['date'],hdfc_weekly['price'])
      #fill col
      plt.xlabel('Date(in weeks)')
      manager = plt.get_current_fig_manager()
      manager.full_screen_toggle()
      plt.ylabel('Stock Price')
      plt.title('Hdfc_Weekly')
      plt.show()
      
# for infosys
def infosys_graph_monthly():
      plt.plot(infosys_monthly['date'],infosys_monthly['price'])
      #fill color
    
      plt.xlabel('Date(in months)')
      plt.ylabel('Stock Price')
      plt.title('Infosys_Monthly')
      manager = plt.get_current_fig_manager()
      manager.full_screen_toggle()
      plt.show()
      
def infosys_graph_weekly():
      plt.plot(infosys_weekly['date'],infosys_weekly['price'])
      #fill colo
      plt.xlabel('Date(in weeks)')
      manager = plt.get_current_fig_manager()
      manager.full_screen_toggle()
      plt.ylabel('Stock Price')
      plt.title('Infosys_Weekly')
      plt.show()

#for itc

def itc_graph_monthly():
      plt.plot(itc_monthly['date'],itc_monthly['price'])
      #fill color

      plt.xlabel('Date(in months)')
      plt.ylabel('ITC_Monthly')
      plt.title('')
      manager = plt.get_current_fig_manager()
      manager.full_screen_toggle()
      plt.show()
      
def itc_graph_weekly():
      plt.plot(itc_weekly['date'],itc_weekly['price'])
      #fill color
    
      plt.xlabel('Date(in weeks)')
      manager = plt.get_current_fig_manager()
      manager.full_screen_toggle()
      plt.ylabel('Stock Price')
      plt.title('ITC_Weekly')
      plt.show()
      
#for sbi
def sbi_graph_monthly():
      plt.plot(sbi_monthly['date'],sbi_monthly['price'])
      #fill color
      
      plt.xlabel('Date(in months)')
      plt.ylabel('Stock Price')
      plt.title('SBI_Monthly')
      manager = plt.get_current_fig_manager()
      manager.full_screen_toggle()
      plt.show()
          
def sbi_graph_weekly():
      plt.plot(sbi_weekly['date'],sbi_weekly['price'])
      #fill color
      
      plt.xlabel('Date(in weeks)')
      manager = plt.get_current_fig_manager()
      manager.full_screen_toggle()
      plt.ylabel('Stock Price')
      plt.title('SBI_Weekly')
      plt.show()
      
         
# working of menu3 (duration)
def brand1():
     selected_time1=menu3.get() 
     if selected_time1=="MONTHLY":    
         selected_company1=menu1.get()
         if selected_company1=="RELIANCE":
             reliance_graph_monthly()
         elif selected_company1=="TATA MOTORS":
             tata_graph_monthly()
         elif selected_company1=="ADANI":
             adani_graph_monthly()
         elif selected_company1=="HDFC BANK":
             hdfc_graph_monthly()
         elif selected_company1=="INFOSYS":
             infosys_graph_monthly()
         elif selected_company1=="ITC":
             itc_graph_monthly()
         elif selected_company1=="SBI":
             sbi_graph_monthly()
     # weekly
     elif selected_time1=="WEEKLY":
         selected_company1=menu1.get()
         if selected_company1=="RELIANCE":
             reliance_graph_weekly()
         elif selected_company1=="TATA MOTORS":
             tata_graph_weekly()
         elif selected_company1=="ADANI":
             adani_graph_weekly()
         elif selected_company1=="HDFC BANK":
             hdfc_graph_weekly()
         elif selected_company1=="INFOSYS":
             infosys_graph_weekly()
         elif selected_company1=="ITC":
             itc_graph_weekly()
         elif selected_company1=="SBI":
             sbi_graph_weekly()
         

# working of  menu 4 (duration)
def brand2():
     selected_time2=menu4.get() 
     if selected_time2=="MONTHLY":    
         selected_company2=menu2.get()
         if selected_company2=="RELIANCE":
             reliance_graph_monthly()
         elif selected_company2=="TATA MOTORS":
             tata_graph_monthly()
         elif selected_company2=="ADANI":
             adani_graph_monthly()
         elif selected_company2=="HDFC BANK":
             hdfc_graph_monthly()
         elif selected_company2=="INFOSYS":
             infosys_graph_monthly()
         elif selected_company2=="ITC":
             itc_graph_monthly()
         elif selected_company2=="SBI":
             sbi_graph_monthly()
     # weekly
     elif selected_time2=="WEEKLY":
         selected_company2=menu2.get()
         if selected_company2=="RELIANCE":
             reliance_graph_weekly()
         elif selected_company2=="TATA MOTORS":
             tata_graph_weekly()
         elif selected_company2=="ADANI":
             adani_graph_weekly()
         elif selected_company2=="HDFC BANK":
             hdfc_graph_weekly()
         elif selected_company2=="INFOSYS":
             infosys_graph_weekly()
         elif selected_company2=="ITC":
             itc_graph_weekly()
         elif selected_company2=="SBI":
             sbi_graph_weekly()



# working of compare (displays combine graph of selected companies)

def compare():
     selected_company1 = menu1.get()
     selected_company2 = menu2.get()
     
     
     if menu3.get() == "MONTHLY" and menu4.get() == "MONTHLY":
         if selected_company1 == "RELIANCE":
             name = reliance_monthly
         elif selected_company1 == "TATA MOTORS":
             name = tata_monthly
         elif selected_company1 == "ADANI":
             name = adani_monthly
         elif selected_company1 == "HDFC BANK":
             name = hdfc_monthly
         elif selected_company1 == "INFOSYS":
             name = infosys_monthly
         elif selected_company1 == "ITC":
             name = itc_monthly
         else:
             name = sbi_monthly
         
         
         if selected_company2 == "RELIANCE":
             name2 = reliance_monthly
         elif selected_company2 == "TATA MOTORS":
             name2 = tata_monthly
         elif selected_company2 == "ADANI":
             name2 = adani_monthly
         elif selected_company2 == "HDFC BANK":
             name2 = hdfc_monthly
         elif selected_company2 == "INFOSYS":
             name2 = infosys_monthly
         elif selected_company2 == "ITC":
             name2 = itc_monthly
         else:
             name2 = sbi_monthly
        
         
          # plotting both graphs
        
         plt.plot(name['date'], name['price'],label=selected_company1)
         plt.plot(name2['date'], name2['price'],label=selected_company2)
         plt.xlabel('Date(in months)')
         plt.ylabel('Stock Price')
         plt.title('COMPARISON BETWEEN TWO COMPANIES')
         manager = plt.get_current_fig_manager()
         manager.full_screen_toggle()
         plt.legend(loc="upper right")
         plt.show()
     
     if menu3.get() == "WEEKLY" and menu4.get() == "MONTHLY":
         if selected_company1 == "RELIANCE":
             name = reliance_weekly
         elif selected_company1 == "TATA MOTORS":
             name = tata_weekly             
         elif selected_company1 == "ADANI":
             name = adani_weekly
         elif selected_company1 == "HDFC BANK":
             name = hdfc_weekly
         elif selected_company1 == "INFOSYS":
             name = infosys_weekly
         elif selected_company1 == "ITC":
             name = itc_weekly
         else:
             name = sbi_weekly
    
    
         if selected_company2 == "RELIANCE":
             name2 = reliance_monthly
         elif selected_company2 == "TATA MOTORS":
             name2 = tata_monthly
         elif selected_company2 == "ADANI":
             name2 = adani_monthly
         elif selected_company2 == "HDFC BANK":
             name2 = hdfc_monthly
         elif selected_company2 == "INFOSYS":
             name2 = infosys_monthly
         elif selected_company2 == "ITC":
             name2 = itc_monthly
         else:
             name2 = sbi_monthly
    
        
         # plotting both graphs
     
         plt.plot(name['date'], name['price'],label=selected_company1)
         plt.plot(name2['date'], name2['price'],label=selected_company2)
         plt.xlabel('Date')
         plt.ylabel('Stock Price')
         #fill color
         plt.legend()
         plt.title('COMPARISON BETWEEN TWO COMPANIES')
         manager = plt.get_current_fig_manager()
         manager.full_screen_toggle()
         plt.legend(loc="upper right")
         plt.show()
     
     
     if menu3.get() == "MONTHLY" and menu4.get() == "WEEKLY":
         if selected_company1 == "RELIANCE":
             name = reliance_monthly
         elif selected_company1 == "TATA MOTORS":
             name = tata_monthly
         elif selected_company1 == "ADANI":
             name = adani_monthly
         elif selected_company1 == "HDFC BANK":
             name = hdfc_monthly
         elif selected_company1 == "INFOSYS":
             name = infosys_monthly
         elif selected_company1 == "ITC":
             name = itc_monthly
         else:
             name = sbi_monthly
        

         if selected_company2 == "RELIANCE":
             name2 = reliance_weekly
         elif selected_company2 == "TATA MOTORS":
             name2 = tata_weekly
         elif selected_company2 == "ADANI":
             name2 = adani_weekly
         elif selected_company2 == "HDFC BANK":
             name2 = hdfc_weekly
         elif selected_company2 == "INFOSYS":
             name2 = infosys_weekly
         elif selected_company2 == "ITC":
             name2 = itc_weekly
         else:
             name2 = sbi_weekly
             
    
          # plotting both graphs
         plt.plot(name['date'], name['price'],label=selected_company1)
         plt.plot(name2['date'], name2['price'],label=selected_company2)
         plt.xlabel('Date(in weeks)')
         plt.ylabel('Stock Price')
         #fill color
         plt.title('COMPARISON BETWEEN TWO COMPANIES')
         manager = plt.get_current_fig_manager()
         manager.full_screen_toggle()
         plt.legend(loc="upper right")
         plt.show()
         
        
     if menu3.get() == "WEEKLY" and menu4.get() == "WEEKLY":
         if selected_company1 == "RELIANCE":
             name = reliance_weekly
         elif selected_company1 == "TATA MOTORS":
             name = tata_weekly
         elif selected_company1 == "ADANI":
             name = adani_weekly
         elif selected_company1 == "HDFC BANK":
             name = hdfc_weekly
         elif selected_company1 == "INFOSYS":
             name = infosys_weekly
         elif selected_company1 == "ITC":
             name = itc_weekly
         else: 
             name = sbi_weekly
        

         if selected_company2 == "RELIANCE":
             name2 = reliance_weekly
         elif selected_company2 == "TATA MOTORS":
             name2 = tata_weekly
         elif selected_company2 == "ADANI":
             name2 = adani_weekly
         elif selected_company2 == "HDFC BANK":
             name2 = hdfc_weekly
         elif selected_company2 == "INFOSYS":
             name2 = infosys_weekly
         elif selected_company2 == "ITC":
             name2 = itc_weekly
         else:
             name2 = sbi_weekly
    
    
          # plotting both gr
         plt.plot(name['date'], name['price'],label=selected_company1)
         plt.plot(name2['date'], name2['price'],label=selected_company2)
         plt.xlabel('Date(in weeks)')
         plt.ylabel('Stock Price')
         #fill color
         plt.title('COMPARISON BETWEEN TWO COMPANIES')
    
         manager = plt.get_current_fig_manager()
         manager.full_screen_toggle()
         plt.legend(loc="upper right")
         plt.show()



# main graph_window


graph_window = Tk()
graph_window.title("Graph of several companies")
graph_window.geometry("1535x835")
LBACK=ImageTk.PhotoImage(Image.open("BACK2 - Copy.jpg"))
BACK=Label(graph_window,image=LBACK)
BACK.place(x=0,y=0)


# GUI CONTENT ⇣

# drop down for selecting companies

menu1=StringVar()
menu1.set("COMPANY 1")
drop1=OptionMenu(graph_window,menu1,"RELIANCE","TATA MOTORS","ADANI","HDFC BANK","INFOSYS","ITC","SBI")
drop1.config(font=('times',18,'bold'))
drop1.place(x="500",y="235")

menu2=StringVar()
menu2.set("COMPANY 2")
drop2=OptionMenu(graph_window,menu2,"RELIANCE","TATA MOTORS","ADANI","HDFC BANK","INFOSYS","ITC","SBI")
drop2.config(font=('times',18,"bold"))
drop2.place(x=1000,y=235)
# dropdown for duration 


menu3=StringVar()
menu3.set("Select Duration")
drop3=OptionMenu(graph_window,menu3,"MONTHLY","WEEKLY")
drop3.config(font=('times',18,'bold'))
drop3.place(x=500,y=330)

menu4=StringVar()
menu4.set("Select Duration")
drop4=OptionMenu(graph_window,menu4,"MONTHLY","WEEKLY")
drop4.config(font=("times",18,'bold'))
drop4.place(x=1000,y=330)

# buttons

graph1=Button(graph_window,text="Graph ",command=lambda: brand1(),width=15,height=1,bd=5)
graph1.place(x=500,y=435)
graph1.config(fg="black",font=('times',18,"bold"))

graph2=Button(graph_window,text="Graph",command=lambda: brand2(),width=15,font=("times",18,"bold"),bd=5)
graph2.place(x=1000,y=435)
graph2.config(fg="black")

graph3=Button(graph_window,text="Compare Both",command=lambda: compare(),width=15,font=("times",18,"bold"),bd=5)
graph3.place(x=750,y=600)
graph3.config(bg="red",fg="white")

buy=Button(graph_window,text="BUY STOCKS",command=BUY,font=("times",18,"bold"),width=15,bg="purple4",fg="white",bd=5)
buy.place(x=1300,y=783)

 
graph_window.mainloop()