#SIGNUP WINDOW 
# importing liabraries 

from tkinter import *
from PIL import ImageTk,Image
import mysql.connector 
from tkinter import messagebox

# defining 

def signup():
    
    if usernameEntry.get()=="" or passwordEntry.get()=="" :
        messagebox.showerror('ERROR','INSERT ALL DETAILS')
    else:
        myconn=mysql.connector.connect(host="localhost",user="root",passwd="291516",database="clg_project",auth_plugin="mysql_native_password")
        c=myconn.cursor(buffered=True)
        query="INSERT INTO users (username,password) VALUES (%s,%s)"
        c.execute(query,(usernameEntry.get(),passwordEntry.get()))
        myconn.commit()
        myconn.close()
        messagebox.showinfo('success','successful')
        signup_window.destroy()
        import access
        

def alreadyhaveanacc( ):
    signup_window.destroy()
    import login

# create signup window 

signup_window=Tk()
signup_window.title("SIGNUP_WINDOW")
signup_window.configure(bg="purple4")
signup_window.geometry("1535x835")
signup_window.resizable(0,0) 

# importing imgs

LBACK=ImageTk.PhotoImage(Image.open("sign.jpg"))
BACK=Label(signup_window,image=LBACK)
BACK.place(x=0,y=0)

background=ImageTk.PhotoImage(file=("logins.jpg"))
bglabel=Label(signup_window,image=background)
bglabel.place(x=50,y=100)


    

# GUI CONTENT ⇣

# LABELS AND ENTRY BOX

usernamelabel=Label(signup_window,text="USERNAME:",font=("times",20,"bold"),bg="white",fg="black")
usernamelabel.place(x=980,y=170)
usernameEntry=Entry(signup_window,width=31,font=("Times",20,"bold"),bg="WHITE",fg="black",bd=0)
usernameEntry.place(x=980,y=210)
frame1=Frame(signup_window,bg='black',width=435,height=2).place(x=980,y=241)


passwordlabel=Label(signup_window,text="PASSWORD:",font=("Times",20,"bold"),bg="white",fg="black")
passwordlabel.place(x=980,y=285)
passwordEntry=Entry(signup_window,width=31,font=("Times",20,"bold"),bg="white",fg="black",bd=0,show="*")
passwordEntry.place(x=980,y=325)
frame2=Frame(signup_window,bg='black',width=435,height=2).place(x=980,y=355)




# BUTTONS

signupbutton=Button(signup_window,text="SIGN UP",width=20,bg="dodger blue2",font=("Times",20,"bold"),command=signup,foreground="white",bd=8)
signupbutton.place(x=1050,y=550)

already_have_an_account=Button(signup_window,text="already_have_an_account",command=alreadyhaveanacc,bg="white",fg="red",bd=8,font=("Times",20,"bold"),width=22)
already_have_an_account.place(x=1041,y=640)


signup_window.mainloop()