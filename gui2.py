import tkinter as tk
import sqlite3
from tkinter import *
from PIL import Image, ImageTk
root = Tk()

conn = sqlite3.connect('info.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS users(
        name text,
        age integer,
        email text,
        password text
        )""")
conn.commit()
conn.close()

def reg_button2_pressed():
    global name_label_field, age_label_field, password_label_field, email_label_field
    conn = sqlite3.connect('info.db')
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES(:name_label_field, :age_label_field, :email_label_field, :password_label_field)",
              {
                  'name_label_field': name_label_field.get(),
                  'age_label_field': age_label_field.get(),
                  'email_label_field': email_label_field.get(),
                  'password_label_field': password_label_field.get(),
                  })
    conn.commit()
    conn.close()
    name_label_field.delete(0, tk.END)
    age_label_field.delete(0, tk.END)
    email_label_field.delete(0, tk.END)
    password_label_field.delete(0, tk.END)
    
def reg_button_pressed():
    global name_label_field, age_label_field, password_label_field, email_label_field
    reg_window = tk.Toplevel()
    reg_window.title("Register as a new user")
    reg_window.geometry("1440x900")
    name_label = Label(reg_window, text="Enter Name: ")
    name_label.grid(column=0, row=1, padx=5, pady=10)
    name_label_field = Entry(reg_window)  
    name_label_field.grid(column=1, row=1, padx=5, pady=10)
    age_label = Label(reg_window, text="Enter Age: ")
    age_label.grid(column=0, row=2, padx=10, pady=20)
    age_label_field = Entry(reg_window)  
    age_label_field.grid(column=1, row=2, padx=5, pady=20)
    email_label = Label(reg_window, text="Enter E-mail: ")
    email_label.grid(column=0, row=3, padx=10, pady=20)
    email_label_field = Entry(reg_window)  
    email_label_field.grid(column=1, row=3, padx=5, pady=20)
    password_label = Label(reg_window, text="Enter Password: ")
    password_label.grid(column=0, row=4, padx=10, pady=20)
    password_label_field = Entry(reg_window, show='*')  
    password_label_field.grid(column=1, row=4, padx=10, pady=20)
    regbtn2 = Button(reg_window, text = 'REGISTER AS NEW USER', height=5, width=75, bg="white", fg="black",
                        font=("Calibri", 15, "bold"),command=reg_button2_pressed)
    regbtn2.grid(column=1, row=5, pady=200)  

def sign_in_button2_pressed():
    sign_in2_window=tk.Toplevel()
    sign_in2_window.title("Sign in")
    sign_in2_window.geometry("1440x900")
    name_label = Label(sign_in2_window, text="Enter Name: ")
    name_label.grid(column=0, row=1, padx=5, pady=10)
    name_label_field = Entry(sign_in2_window)  
    name_label_field.grid(column=1, row=1, padx=5, pady=10)
    email_label = Label(sign_in2_window, text="Enter E-mail: ")
    email_label.grid(column=0, row=3, padx=10, pady=20)
    email_label_field = Entry(sign_in2_window)  
    email_label_field.grid(column=1, row=3, padx=5, pady=20)
    password_label = Label(sign_in2_window, text="Enter Password: ")
    password_label.grid(column=0, row=4, padx=10, pady=20)
    password_label_field = Entry(sign_in2_window, show='*')  
    password_label_field.grid(column=1, row=4, padx=10, pady=20)
    regbtn2 = Button(sign_in2_window, text = 'Sign In', height=5, width=75, bg="white", fg="black",
                        font=("Calibri", 15, "bold"), command=reg_button2_pressed)
    regbtn2.grid(column=1, row=5, pady=200)  

def sign_in_button_pressed():
    sign_in_window=tk.Toplevel()
    sign_in_window.title("Sign in")
    sign_in_window.geometry("1440x900")
    signinbtn2 = Button(sign_in_window, text = 'SIGN IN AS EXISTING USER', height=45, width=65, bg="white", fg="black",
                        font=("Calibri", 15, "bold"), command=sign_in_button2_pressed)
    signinbtn2.place(x=0, y=0)
    regbtn = Button(sign_in_window, text = 'REGISTER AS NEW USER',  height=45, width=65, bg="white", fg="black",
                        font=("Calibri", 15, "bold"), command=reg_button_pressed)
    regbtn.place(x=650, y=0)

def any_bike_pressed():
    message_window=tk.Toplevel()
    message_window.title("Register or sign in to view this bike")
    message_window.geometry("500x300")
    Label(message_window, text='Please sign in or register to view this bike', compound='center',
          font=('Calibri', 24, 'bold'), fg='red').pack()
    signinbtn = Button(message_window, text = 'SIGN IN OR REGISTER', height=5, width=25, bg="white", fg="black", command = sign_in_button_pressed)
    signinbtn.place(x=30, y=50)

def dbbtn_pressed():
    db_window = tk.Toplevel()
    db_window.title("All Bikes")
    db_window.geometry("1440x900")

def road_bike_button_pressed():
    roadbike_window = tk.Toplevel()
    roadbike_window.title("Road Bikes")
    roadbike_window.geometry("1440x900")
    Label(roadbike_window, text='Our Road Bike Collection', image=image2, compound='center',
          font=('Calibri', 50, 'bold'), fg='White').pack()
    roadbike1btn = Button(roadbike_window,compound='top',text=' The Trek Emonda SL 6',image=image5,command=any_bike_pressed)
    roadbike1btn.place(x=250, y=350)
    roadbike2btn = Button(roadbike_window,compound='top',text='Giant Contend Sl 1 Disc 2024 ',image=image12, command=any_bike_pressed)
    roadbike2btn.place(x=550, y=350)
    roadbike3btn = Button(roadbike_window,compound='top',text='XDS RX280 L-Twoo Road Bike ',image=image13,command=any_bike_pressed)
    roadbike3btn.place(x=850, y=350)  
    signinbtn = Button(roadbike_window,text='SIGN IN TO VIEW ALL ROAD BIKES',height=5,width=25,bg="white",fg="black",command=sign_in_button_pressed)
    signinbtn.place(x=0, y=600)
    dbbtn = Button(roadbike_window,text='VIEW OUR FULL COLLECTION',height=5,width=25,bg="white",fg="black",command=dbbtn_pressed)
    dbbtn.place(x=1015, y=600)

def mount_bike_button_pressed():
    mountbike_window=tk.Toplevel()
    mountbike_window.title("Mountain Bikes")
    mountbike_window.geometry("1440x900")
    Label(mountbike_window, text='Our Mountain Bike Collection', image=image3, compound='center',
    font=('Calibri', 50, 'bold'), fg='White').pack()
    mountbike1btn = Button(mountbike_window,compound='top',text='  Ceres TR2 MTB Mountain Bike',image=image6,command=any_bike_pressed)
    mountbike1btn.place(x=250, y=350)
    mountbike2btn = Button(mountbike_window,compound='top',text=' Marlin+ 8 2024 Mountain Bike ',image=image7,command=any_bike_pressed)
    mountbike2btn.place(x=550, y=350)
    mountbike3btn = Button(mountbike_window,compound='top',text=' Mountain Bike Hardtail XL',image=image8,command=any_bike_pressed)
    mountbike3btn.place(x=850, y=350)
    signinbtn = Button(mountbike_window, text = 'SIGN IN TO VIEW ALL MOUNTAIN BIKES', height=5, width=25, bg="white", fg="black", command = sign_in_button_pressed)
    signinbtn.place(x=0, y=600)
    dbbtn = Button(mountbike_window,text='VIEW OUR FULL COLLECTION',height=5,width=25,bg="white",fg="black",command=dbbtn_pressed)
    dbbtn.place(x=1015, y=600)

def e_bike_button_presssed():
    ebike_window=tk.Toplevel()
    ebike_window.title("Electric Bikes")
    ebike_window.geometry("1440x900")
    Label(ebike_window, text='Our Electric Bike Collection', image=image4, compound='center',
    font=('Calibri', 50, 'bold'), fg='White').pack()
    ebike1btn = Button(ebike_window,compound='top',text='ENGWE X Series Electric Bike',image=image9,command=any_bike_pressed)
    ebike1btn.place(x=250, y=350)
    ebike2btn = Button(ebike_window,compound='top',text='Cyrusher XF500 Folding E-Bike',image=image10,command=any_bike_pressed)
    ebike2btn.place(x=550, y=350)
    ebike3btn = Button(ebike_window,compound='top',text='ADO A20+ Electric Bicycle',image=image11,command=any_bike_pressed)
    ebike3btn.place(x=850, y=350)
    signinbtn = Button(ebike_window, text = 'SIGN IN TO VIEW ALL E-BIKES', height=5, width=25, bg="white", fg="black", command = sign_in_button_pressed)
    signinbtn.place(x=0, y=600)
    dbbtn = Button(ebike_window,text='VIEW OUR FULL COLLECTION',height=5,width=25,bg="white",fg="black",command=dbbtn_pressed)
    dbbtn.place(x=1015, y=600)

root.geometry("1440x900")
root.title("Smith & Sons Cycling Welcome Page")
image1 = ImageTk.PhotoImage(Image.open(r'heading.jpg')) 
image2 = ImageTk.PhotoImage(Image.open(r'roadbikeheader.jpg')) 
image3 = ImageTk.PhotoImage(Image.open(r'mountbikeheader.jpg'))
image4 = ImageTk.PhotoImage(Image.open(r'ebikeheader.jpg'))
image5 = ImageTk.PhotoImage(Image.open(r'roadbike1.jpg'))
image6 = ImageTk.PhotoImage(Image.open(r'mountbike1.jpg'))
image7 = ImageTk.PhotoImage(Image.open(r'mountbike2.jpg'))
image8 = ImageTk.PhotoImage(Image.open(r'mountbike3.jpg'))
image9 = ImageTk.PhotoImage(Image.open(r'ebike1.png'))
image10 = ImageTk.PhotoImage(Image.open(r'ebike2.jpg'))
image11 = ImageTk.PhotoImage(Image.open(r'ebike3.jpg'))
image12 = ImageTk.PhotoImage(Image.open(r'roadbike2.jpg'))
image13 = ImageTk.PhotoImage(Image.open(r'roadbike3.jpg'))
Label(root, text='Smith & Sons Cycling', image=image1, compound='center',
    font=('Calibri', 50, 'bold'), fg='White').pack()
signinbtn = Button(root, text = 'SIGN IN', height=5, width=75, bg="white", fg="black", command = sign_in_button_pressed)
signinbtn.place(x=300, y=350)
roadbikebtn = Button(root, text = 'VIEW OUR ROAD BIKES',height=5, width=25, bg="white", fg="black", command = road_bike_button_pressed)
roadbikebtn.place(x=250, y=500)
mountbikebtn = Button(root, text = 'VIEW OUR MOUNTAIN BIKES',height=5, width=25, bg="white", fg="black",  command = mount_bike_button_pressed)
mountbikebtn.place(x=550, y=500)
ebikebtn = Button(root, text = 'VIEW OUR ELECTRIC BIKES',height=5, width=25, bg="white", fg="black",  command = e_bike_button_presssed)
ebikebtn.place(x=850, y=500)
root.mainloop()