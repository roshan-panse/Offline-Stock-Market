# LOGIN WINDOW 
#importing liabraries

from tkinter import *
from PIL  import Image,ImageTk
from tkinter import messagebox
import mysql.connector

# defining commands
def donthaveanacc():
    login_window.destroy()
    import sign
    
def login():
    if usernameentry.get()=="" or passwordentry.get()=="" :
        messagebox.showerror('ERROR','INSERT ALL DETAILS')
    else:
        myconn=mysql.connector.connect(host="localhost",user="root",passwd="2952007",database="school_project",auth_plugin="mysql_native_password")
        c=myconn.cursor(buffered=True)
       
        uname=usernameentry.get()
        passw=passwordentry.get()
         


        query = "SELECT username ,password FROM login  WHERE username = %s and password=%s"
        c.execute(query, [(uname),(passw)])
       
        ce=c.fetchall()
        if ce == NONE :
            messagebox.showerror('ERROR','INVALID DETAILS :<')
        elif ce:
             messagebox.showinfo('WELCOME','LOGIN SUCCESSFUL ^_^')
             login_window.destroy()
             import access
        else:
            messagebox.showerror('ERROR','INVALID DETAILS ＞︿＜')
        

# create login window

login_window=Tk()
login_window.title("LOGIN_WINDOW")
login_window.configure(bg="purple4")
login_window.geometry("1535x835")
login_window.resizable(0,0)

# importing imgs

LBACK=ImageTk.PhotoImage(Image.open("LOGIN.jpg"))
BACK=Label(login_window,image=LBACK)
BACK.place(x=0,y=0)

logimage=ImageTk.PhotoImage(Image.open("logins.jpg"))
logLabel=Label(login_window,image=logimage)
logLabel.place(x=20,y=110)




# GUI CONTENT ⇣

#LABELS AND ENTRY BOX

username=Label(login_window,text="USERNAME:",font=("Times",20,"bold"),bg="white",fg="black")
username.place(x=980,y=165)
usernameentry=Entry(login_window,width=31,font=("Times",20,"bold"),bg="white",fg="black",bd=0)
usernameentry.place(x=980,y=210)
frame1=Frame(login_window,bg='black',width=435,height=2).place(x=980,y=240)


password=Label(login_window,text="PASSWORD:",font=("Times",20,"bold"),bg="white",fg="black")
password.place(x=980,y=282)
passwordentry=Entry(login_window,width=31,font=("Times",20,"bold"),bg="white",fg="black",bd=0,show="*")
passwordentry.place(x=980,y=325)
frame2=Frame(login_window,bg='black',width=435,height=2).place(x=980,y=355)


# BUTTONS 

login=Button(login_window,text="LOGIN",font=("Times",20,"bold"),bg="dodger blue2",fg="white",width=20,command=login,foreground="white",bd=8)
login.place(x=980,y=550)

dont_have_an_account=Button(login_window,text="create_account",command=donthaveanacc,bg="white",fg="red",bd=8,font=("Times",20,"bold"),width=22)
dont_have_an_account.place(x=960,y=640)
login_window.mainloop()