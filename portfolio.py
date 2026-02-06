# PORTFOLIO WINDOW 
#importing libraries
from tkinter import *

import pandas as pd
import mysql.connector as sqltor
from tkinter import messagebox
def exit():
    portfolio_win.destroy()
 # definig comands
def sell():
    portfolio_win.destroy()
    import sellwindow

# Function to update the displayed data based on user input
def update_display():
    if entry.get()== "":
        messagebox.showerror('error','empty set')
    else:
            
            user_input = entry.get()

    
            mycon = sqltor.connect(host="localhost", user="root", passwd="291516", database="clg_project", auth_plugin="mysql_native_password")
            mycursor = mycon.cursor()
  
    
            query = f"SELECT username, company, priceperunit, qty, amntpaid, date FROM buy WHERE username = '{user_input}'"

            df = pd.read_sql(query, mycon)

   
            for text_widget in text_widgets:
              text_widget.delete("1.0", "end")

    # Display data in Text widgets
            for i, col in enumerate(df.columns):
                data_str = df[col].to_string(index=False)
                text_widgets[i].insert("1.0", data_str)

 
            mycon.close()

   


# Create window
portfolio_win = Tk()
portfolio_win.title('portfolio')
portfolio_win.config(bg='white')
portfolio_win.geometry("1535x835")
portfolio_win.configure(bg='cyan')
portfolio_win.resizable(0,0)

wintitle=Label(portfolio_win,text='PORTFOLIO',font=('times',45,'bold'),bg='seagreen',fg='white',bd=8)
wintitle.place(x=550,y=0)


entry_label = Label(portfolio_win, text="Username:", width=15,font=('times', 20, 'bold'),bg='coral',fg='white')
entry_label.place(x=10, y=150)
entry = Entry(portfolio_win, font=('times', 20, 'bold'))
entry.place(x=300, y=150)

# Create a button to trigger the data retrieval based on user input
search_button = Button(portfolio_win, text="Search", command=update_display, bg='purple4',fg='white',width=17, font=('times', 18, 'bold'),bd=5)
search_button.place(x=650, y=145)

# Create Text widgets for displaying data

text_widgets = []

# Create labels for each Text widget
label_text = ["Username:", "Company:", "Price per Unit:", "Quantity:", "Amount Paid:", "Date:"]
for i, text in enumerate(label_text):
    label = Label(portfolio_win, text=text, font=('times', 20, 'bold'), bg='coral',fg='white',width=15)
    label.place(x=i * 250 + 20, y=200)

    text_widget = Text(portfolio_win, font=('times', 20, 'bold'), height=10, width=20)
    text_widget.place(x=i * 250 + 20, y=240)
    text_widgets.append(text_widget)



sel=Button(portfolio_win,text='SELL STOCKS ',command=sell,font=('times',20,'bold'),bg='purple4',fg='white',bd=8)
sel.place(x=1320,y=770)

EXIT_button = Button(portfolio_win, text="EXIT", command=exit, bg='purple4',fg='white',width=17, font=('times', 18, 'bold'),bd=5)
EXIT_button.place(x=1280, y=0)
portfolio_win.mainloop()
