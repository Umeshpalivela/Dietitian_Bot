from tkinter import *
#from PIL import ImageTk,Image
from tkinter import messagebox  
from random import randint
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("650x480")
    Label(login_screen, text="Please enter your details below to login",font=( 'Bradley Hand ITC' ,17, 'bold' )).place(x=170,y=0)
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen,font=( 'Bradley Hand ITC' ,17,'bold' ), text="Username").place(x=250,y=50)
    username_login_entry = Entry(login_screen,font=(17) ,textvariable=username_verify)
    username_login_entry.place(x=250,y=100)
    Label(login_screen,font=( 'Bradley Hand ITC' ,17, 'bold' ), text="Password").place(x=250,y=150)
    password_login_entry = Entry(login_screen,font=(17 ), textvariable=password_verify, show= '*')
    password_login_entry.place(x=250,y=200)
    Button(login_screen, text="Login", width=10, height=1,bg='brown',fg='white', command = login_verify).place(x=275,y=250)
 
# Function on Register Button
 
def register_user():
 
    username_info = username.get()
    password_info = password.get()
 
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
    messagebox.showinfo("Registration","Registration Success")

# Funciton on Login Button 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            BMR()
        else:
            password_not_recognised()
 
    else:
        user_not_found()
        
