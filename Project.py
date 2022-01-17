#                                                                                                Add Medicine
from tkinter import * #import tkinter library
import tkinter.messagebox as msg # to display message box
import sqlite3 #to store data
root = Tk()
root.geometry(700*450+300+100)
regimage = PhotoImage(file = "AddMedicine.png");
bg_Label = Label(root,image = regimage)
bg_Label.place(x=0,y=0,relwidth=1,relheight=1)
root.title("Add Medicine Page-Medicine Management System")
root.config
#                                      Lets create the table for medicine
conn = sqlite3.connect("medicine.db")
cursor = conn.cursor()
cursor.execute("create table if not exists 'medicine'(MedicineID int, MedicineName text,Company text, ChemicalComp text,ManuDate text,ExpDate text, Costfor10 text)")
conn.commit()
#             Declare variables for the columns to access
MedicineName = StringVar()
MedicineID = IntVar()
Company= StringVar()
ChemicalComp= StringVar()
ManuDate= StringVar()
ExpDate= StringVar()
Costfor10= StringVar()
MedicineName.set("")
MedicineID.set("")
Company.set("")
ChemicalComp.set("")
ManuDate.set("")
ExpDate.set("")
Costfor10.set("")
############## Lets write functions for the button ############
def addmedicine():
    conn = sqlite3.connect('medicine.db')
    cursor = conn.cursor()
    cursor.execute("insert into 'medicine'(MedicineName,MedicineID,Company,ChemicalComp,ManuDate,ExpDate,Costfor10) values(?,?,?,?,?,?,?)",(str(MedicineName.get()),str(MedicineID.get()),str(Company.get()),str(ChemicalComp.get()),str(ManuDate.get()),str(ExpDate.get()),str(Costfor10.get())))
    conn.commit()
    print(cursor.rowcount)
if cursor.rowcount >0:
    msg.showinfo("Confirmation Message","Medicine Added Successfully",icon="info")
else:
    msg.showinfo("Error Message","medicine not Added",icon="warning")

def cancel():
    root.destroy()
import home

def back():
    root.destroy()
import home
##################Top Frame ###########
TopHeadingFrame = Frame(root,width=600,bd=1)
TopHeadingFrame.pack(side=TOP)

HeadingLabel = Label(TopHeadingFrame,text=”Add Medicine”,
font=("Helvetica",16),fg="brown", bg="white")
HeadingLabel.grid(row=0,column=1,padx=10,pady=10)

MidFrame = Frame(root,width=600)
MidFrame.pack(side=TOP)

MedicineNameLabel = Label(MidFrame,text=”Medicine Name”,
font=(“Helvetica”,10),fg=”brown”, bg=”white”)
MedicineNameLabel.grid(row=1,padx=10,pady=10)

MedicineIDLabel = Label(MidFrame,text=”Medicine ID”,
font=(“Helvetica”,10),fg=”brown”, bg=”white”)
MedicineIDLabel.grid(row=2,padx=10,pady=10)

CompanyLabel = Label(MidFrame,text=”Company”,
font=(“Helvetica”,10),fg=”brown”, bg=”white”)
CompanyLabel.grid(row=3,padx=10,pady=10)

ChemicalCompLabel = Label(MidFrame,text=”Chemical Composition”,
font=(“Helvetica”,10),fg=”brown”, bg=”white”)
ChemicalCompLabel.grid(row=4,padx=10,pady=10)

ManuDateLabel = Label(MidFrame,text=”Manufacturing Date”,
font=(“Helvetica”,10),fg=”brown”, bg=”white”)
ManuDateLabel.grid(row=5,padx=10,pady=10)

ExpDateLabel = Label(MidFrame,text=”Expiry Date”,
font=(“Helvetica”,10),fg=”brown”, bg=”white”)
ExpDateLabel.grid(row=6,padx=10,pady=10)

Costfor10Label = Label(MidFrame,text=”Cost for 10″,
font=(“Helvetica”,10),fg=”brown”, bg=”white”)
Costfor10Label.grid(row=7,padx=10,pady=10)

MedicineNameTextbox = Entry(MidFrame,textvariable=MedicineName,
font=(“Helvetica”,10))
MedicineNameTextbox.grid(row=1,column=1,padx=10,pady=10)

MedicineIDTextbox = Entry(MidFrame,textvariable=MedicineID,
font=(“Helvetica”,10))
MedicineIDTextbox.grid(row=2,column=1,padx=10,pady=10)

CompanyTextbox = Entry(MidFrame,textvariable=Company,
font=(“Helvetica”,10))
CompanyTextbox.grid(row=3,column=1,padx=10,pady=10)

ChemicalCompTextbox = Entry(MidFrame,textvariable=ChemicalComp,
font=(“Helvetica”,10))
ChemicalCompTextbox.grid(row=4,column=1,padx=10,pady=10)

ManuDateTextbox = Entry(MidFrame,textvariable=ManuDate,
font=(“Helvetica”,10))
ManuDateTextbox.grid(row=5,column=1,padx=10,pady=10)

ExpDateTextbox = Entry(MidFrame,textvariable=ExpDate,
font=(“Helvetica”,10))
ExpDateTextbox.grid(row=6,column=1,padx=10,pady=10)

Costfor10Textbox = Entry(MidFrame,textvariable=Costfor10,
font=(“Helvetica”,10))
Costfor10Textbox.grid(row=7,column=1,padx=10,pady=10)

RegisterButton = Button(MidFrame,text=”Register”, command=addmedicine,
font=(“Helvetica”,10))
RegisterButton.grid(row=8,column=0,padx=10,pady=10)

CancelButton = Button(MidFrame,text=”Cancel”, command=cancel,
font=(“Helvetica”,10))
CancelButton.grid(row=8,column=1,padx=10,pady=10)

BackButton = Button(MidFrame,text=”Back”, command = back,
font=(“Helvetica”,10))
BackButton.grid(row=10,column=0,padx=10,pady=10)

#                                                                Delete Medicine
from tkinter import * #import tkinter library
import tkinter.messagebox as msg # to display message box
import sqlite3 #to store data
import tkinter.ttk as ttk

root = Tk()
root.geometry(“700×450+300+100”) #width height xoffset #yoffset
regimage = PhotoImage(file = “DeleteMedicine.png”);
bg_Label = Label(root,image = regimage)
bg_Label.place(x=0,y=0,relwidth=1,relheight=1)
root.title(“Delete Medicine Page – Medicine Management System”)
root.config
##################Top Frame ###########
TopHeadingFrame = Frame(root,width=600,bd=1)
TopHeadingFrame.pack(side=TOP)

HeadingLabel = Label(TopHeadingFrame,text=”Delete Medicine”,
font=(“Helvetica”,16),fg=”brown”, bg=”white”)
HeadingLabel.grid(row=0,column=1,padx=10,pady=10)
###################Declare variables for the columns to access######3
MedicineName = StringVar()
MedicineName.set(“”)

MidFrame = Frame(root,width=600)
MidFrame.pack(side=TOP)
##########
MedicineNameLabel = Label(MidFrame,text=”Medicine Name”,
font=(“Helvetica”,10),fg=”brown”, bg=”white”)
MedicineNameLabel.grid(row=1,padx=10,pady=10)

##########
MedicineNameTextbox = Entry(MidFrame,textvariable=MedicineName,
font=(“Helvetica”,10))
MedicineNameTextbox.grid(row=1,column=1,padx=10,pady=10)
##########

##########
def back():
    root.destroy()
import home
##########
def View():
    for i in treeview.get_children() :
        treeview.delete(i)
conn = sqlite3.connect(“medicine.db”)
cursor = conn.cursor()
cursor.execute(“select * from ‘medicine'”)
dataselect = cursor.fetchall()
### insert in the parent container and append it in the end
for data in dataselect:
treeview.insert(”,’end’,value=(data))
cursor.close()
conn.commit()
##########
##########
def Delete():
for i in treeview.get_children() :
treeview.delete(i)
conn = sqlite3.connect(“medicine.db”)
cursor = conn.cursor()
medname = str(MedicineName.get())
cursor.execute(“delete from ‘medicine’ where MedicineName=?”,(medname,))
print(cursor.rowcount)
if cursor.rowcount >0:
msg.showinfo(“Confirm Message”,”Medicine deletion success”,icon=”info”)
else:
msg.showinfo(“Error Message”,”medicine couldn’t be deleted”,icon=”warning”)
cursor.close()
conn.commit()
##########
DeleteButton = Button(MidFrame,text=”Delete Med”, command = Delete,
font=(“Helvetica”,10))
DeleteButton.grid(row=1,column=2,padx=10,pady=10)
##########
ViewButton = Button(MidFrame,text=”View”, command = View,
font=(“Helvetica”,10))
ViewButton.grid(row=1,column=3,padx=10,pady=10)
##########
BackButton = Button(MidFrame,text=”Back”, command = back,
font=(“Helvetica”,10))
BackButton.grid(row=1,column=4,padx=10,pady=10)
##########
ViewFrame = Frame(root,width=400)
ViewFrame.pack(side=TOP)
#################create a treeview in ViewFrame #######
treeview = ttk.Treeview(ViewFrame,columns=(“MedicineID”, “MedicineName” ,”Company”, “ChemicalComp”,”ManuDate” ,”ExpDate”, “Costfor10″),height=200,selectmode=”extended” )
treeview.heading(“MedicineID” , text=”MedicineID” , anchor =”w”)
treeview.heading(“MedicineName” , text=”MedicineName” , anchor =”w”)
treeview.heading(“Company” , text=”Company” , anchor =”w”)
treeview.heading(“ChemicalComp” , text=”ChemicalComp” , anchor =”w”)
treeview.heading(“ManuDate” , text=”ManuDate” , anchor =”w”)
treeview.heading(“ExpDate” , text=”ExpDate” , anchor =”w”)
treeview.heading(“Costfor10″ , text=”Costfor10″ , anchor =”w”)
treeview.column(“#0” ,stretch=NO,width=10,minwidth=0)
treeview.column(“#1” ,stretch=NO,width=70,minwidth=0)
treeview.column(“#2” ,stretch=NO,width=120,minwidth=0)
treeview.column(“#3” ,stretch=NO,width=120,minwidth=0)
treeview.column(“#4” ,stretch=NO,width=160,minwidth=0)
treeview.column(“#5” ,stretch=NO,width=70,minwidth=0)
treeview.column(“#6” ,stretch=NO,width=70,minwidth=0)
treeview.column(“#7” ,stretch=NO,width=70,minwidth=0)
treeview.pack()

home
from tkinter import * #import tkinter library
import tkinter.messagebox as msg # to display message box
import sqlite3 #to store data
root = Tk()
root.geometry(“700×450+300+100”) #width height xoffset #yoffset
regimage = PhotoImage(file = “home.png”);
bg_Label = Label(root,image = regimage)
bg_Label.place(x=0,y=0,relwidth=1,relheight=1)
root.title(“Home Page – Medicine Management System”)
root.config
############## Lets write functions for the button ############
def AddMedicine():
    root.destroy()
import AddMedicine

def ViewMedicine():
    root.destroy()
import ViewMedicine

def SearchMedicine():
    root.destroy()
import SearchMedicine

def DeleteMedicine():
    root.destroy()
import DeleteMedicine
##################Top Frame ###########
TopHeadingFrame = Frame(root,width=600,bd=1)
TopHeadingFrame.pack(side=TOP)

HeadingLabel = Label(TopHeadingFrame,text=”Options to choose”,
font=(“Helvetica”,16),fg=”brown”, bg=”white”)
HeadingLabel.grid(row=0,column=1,padx=10,pady=10)
##########
MidFrame = Frame(root,width=600)
MidFrame.pack(side=TOP)
##########
AddMedicine = Button(MidFrame,text=”Add Medicine”, command=AddMedicine,
font=(“Helvetica”,10))
AddMedicine.grid(row=2,column=1,padx=10,pady=10)
##########
ViewMedicine = Button(MidFrame,text=”View Medicine”, command=ViewMedicine,
font=(“Helvetica”,10))
ViewMedicine.grid(row=4,column=1,padx=10,pady=10)
##########
SearchMedicine = Button(MidFrame,text=”Search Medicine”, command=SearchMedicine,
font=(“Helvetica”,10))
SearchMedicine.grid(row=6,column=1,padx=10,pady=10)
##########
DeleteMedicine = Button(MidFrame,text=”Delete Medicine”, command=DeleteMedicine,
font=(“Helvetica”,10))
DeleteMedicine.grid(row=8,column=1,padx=10,pady=10)

#                                                              Login
from tkinter import * #import tkinter library
import tkinter.messagebox as msg # to display message box
import sqlite3 #to store data
root = Tk()
root.geometry(“700×450+300+100”) #width height xoffset #yoffset
regimage = PhotoImage(file = “login.png”);
bg_Label = Label(root,image = regimage)
bg_Label.place(x=0,y=0,relwidth=1,relheight=1)
root.title(“Login Page – Medicine Management System”)
root.config
########### Variable declaration #########
UserName= StringVar()
Password= StringVar()
############## Lets write functions for the button ############
def register():
    root.destroy()
import Reg

def login():
    #conn = sqlite3.connect(“medicine.db”)
conn = mysql.connect(
host=”localhost”,
user=”root”,
password=””,
database=”medicine”
)
cursor = conn.cursor()
user= str(UserName.get())

pwd = str(Password.get())
print (user)
print (pwd)
print (“select UserName from ‘usertable1’ where ‘UserName’=? and Pwd=?”,(user,pwd))
cursor.execute(“select UserName from usertable1 where UserName=? and Pwd=?”,(user,pwd))
resultset = cursor.fetchall();
for data in resultset:
    print (data)
if data:
    msg.showinfo(“Confirmation Message”,”Login successful Added”,icon=”info”)
    root.destroy()
import home

else:
    msg.showinfo(“Error Message”,”Invalid user”,icon=”warning”)
    cursor.close()

def back():
    root.destroy()
import home
#################### Lets put the controls ############
TopHeadingFrame = Frame(root,width=600,bd=1)
TopHeadingFrame.pack(side=TOP)

HeadingLabel = Label(TopHeadingFrame,text=”Login Page”,
font=(“Helvetica”,16),fg=”brown”, bg=”white”)
HeadingLabel.grid(row=0,column=1,padx=10,pady=10)
##########
MidFrame = Frame(root,width=600)
MidFrame.pack(side=TOP)
##########
UserNameLabel = Label(MidFrame,text=”UserName”,
font=(“Helvetica”,10),fg=”brown”, bg=”white”)
UserNameLabel.grid(row=3,padx=10,pady=10)
##########
PasswordLabel = Label(MidFrame,text=”Password”,
font=(“Helvetica”,10),fg=”brown”, bg=”white”)
PasswordLabel.grid(row=4,padx=10,pady=10)
##########
UserNameTextbox = Entry(MidFrame,textvariable=UserName,
font=(“Helvetica”,10))
UserNameTextbox.grid(row=3,column=1,padx=10,pady=10)
##########
PasswordTextbox = Entry(MidFrame,textvariable=Password,
font=(“Helvetica”,10))
PasswordTextbox.grid(row=4,column=1,padx=10,pady=10)
##########
RegisterButton = Button(MidFrame,text=”Login”, command = login,
font=(“Helvetica”,10))
RegisterButton.grid(row=7,column=1,padx=10,pady=10)
##########
AlreadyUserLabel = Label(MidFrame,text=”Not registered ???”,
font=(“Helvetica”,10),fg=”brown”, bg=”white”)
AlreadyUserLabel.grid(row=9,padx=10,pady=10)
##########
LoginButton = Button(MidFrame,text=”Register”, command=register ,
font=(“Helvetica”,10))
LoginButton.grid(row=9,column=1,padx=10,pady=10)

Reg
from tkinter import * #import tkinter library
import tkinter.messagebox as msg # to display message box
import sqlite3 #to store data
import mysql.connector as mysql
root = Tk()
root.geometry(“700×450+300+100”) #width height xoffset #yoffset
regimage = PhotoImage(file = “reg.png”);
bg_Label = Label(root,image = regimage)
bg_Label.place(x=0,y=0,relwidth=1,relheight=1)
root.title(“Medicine Management System”)
root.config
#########################Lets connect the database now #########
conn = mysql.connect(
host=”localhost”,
user=”root”,
password=””,
database=”medicine”
)

# conn = sqlite3.connect(“medicine.db”)
cursor = conn.cursor()
cursor.execute(“create table if not exists usertable1(Name varchar(100),ID int, UserName varchar(100),Pwd varchar(100),mobile varchar(100), email varchar(100))”)
conn.commit()
########################Lets insert the data into table now #######
Name = StringVar()
ID= IntVar()
UserName= StringVar()
Password= StringVar()
Mobile= StringVar()
Email= StringVar()
Name.set(“”)
ID.set(“”)
UserName.set(“”)
Password.set(“”)
Mobile.set(“”)
Email.set(“”)
############## Lets write functions for the button ############
def register():
#conn = sqlite3.connect(“medicine.db”)
conn = mysql.connect(
host=”localhost”,
user=”root”,
password=””,
database=”medicine”
)
cursor = conn.cursor()
cursor.execute(“insert into usertable1(Name ,ID, UserName,Pwd ,mobile, email) values(%s,%s,%s,%s,%s,%s)”,(str(Name.get()), str(ID.get()),str(UserName.get()),str(Password.get()),str(Mobile.get()),str(Email.get())))
conn.commit()
print(cursor.rowcount)
if cursor.rowcount >0:
    msg.showinfo(“Confirmation Message”,”User Added”,icon=”info”)
else:
    msg.showinfo(“Error Message”,”User not Added”,icon=”warning”)

def login():
    root.destroy()
import login
#################### Lets put the controls ############
TopHeadingFrame = Frame(root,width=600,bd=1)
TopHeadingFrame.pack(side=TOP)
HeadingLabel = Label(TopHeadingFrame,text=”Medicine Mgnt System”,
font=(“Helvetica”,16),fg=”brown”, bg=”white”)
HeadingLabel.grid(row=0,column=1,padx=10,pady=10)
########################Plan for the controls in the mid####
MidFrame = Frame(root,width=600)
MidFrame.pack(side=TOP)
NameLabel = Label(MidFrame,text=”Name”,
font=(“Helvetica”,10),fg=”brown”, bg=”white”)
NameLabel.grid(row=1,padx=10,pady=10)
##########
IDLabel = Label(MidFrame,text=”ID”,
font=(“Helvetica”,10),fg=”brown”, bg=”white”)
IDLabel.grid(row=2,padx=10,pady=10)
##########
UserNameLabel = Label(MidFrame,text=”UserName”,
font=(“Helvetica”,10),fg=”brown”, bg=”white”)
UserNameLabel.grid(row=3,padx=10,pady=10)
##########
PasswordLabel = Label(MidFrame,text=”Password”,
font=(“Helvetica”,10),fg=”brown”, bg=”white”)
PasswordLabel.grid(row=4,padx=10,pady=10)
##########
MobileLabel = Label(MidFrame,text=”Mobile”,
font=(“Helvetica”,10),fg=”brown”, bg=”white”)
MobileLabel.grid(row=5,padx=10,pady=10)
##########
EmailLabel = Label(MidFrame,text=”E-Mail”,
font=(“Helvetica”,10),fg=”brown”, bg=”white”)
EmailLabel.grid(row=6,padx=10,pady=10)
##########
NameTextbox = Entry(MidFrame,textvariable=Name,
font=(“Helvetica”,10))
NameTextbox.grid(row=1,column=1,padx=10,pady=10)
##########
IDTextbox = Entry(MidFrame,textvariable=ID,
font=(“Helvetica”,10))
IDTextbox.grid(row=2,column=1,padx=10,pady=10)
##########
UserNameTextbox = Entry(MidFrame,textvariable=UserName,
font=(“Helvetica”,10))
UserNameTextbox.grid(row=3,column=1,padx=10,pady=10)
##########
PasswordTextbox = Entry(MidFrame,textvariable=Password,
font=(“Helvetica”,10))
PasswordTextbox.grid(row=4,column=1,padx=10,pady=10)
##########
MobileTextbox = Entry(MidFrame,textvariable=Mobile,
font=(“Helvetica”,10))
MobileTextbox.grid(row=5,column=1,padx=10,pady=10)
##########
EmailTextbox = Entry(MidFrame,textvariable=Email,
font=(“Helvetica”,10))
EmailTextbox.grid(row=6,column=1,padx=10,pady=10)
##########
RegisterButton = Button(MidFrame,text=”Register”, command=register,
font=(“Helvetica”,10))
RegisterButton.grid(row=7,column=1,padx=10,pady=10)
##########
AlreadyUserLabel = Label(MidFrame,text=”Already User ???”,
font=(“Helvetica”,10),fg=”brown”, bg=”white”)
AlreadyUserLabel.grid(row=9,padx=10,pady=10)
##########
LoginButton = Button(MidFrame,text=”Login”, command=login,
font=(“Helvetica”,10))
LoginButton.grid(row=9,column=1,padx=10,pady=10)
# SearchMedicine
from tkinter import * #import tkinter library
import tkinter.messagebox as msg # to display message box
import sqlite3 #to store data
import tkinter.ttk as ttk
root = Tk()
root.geometry(“700×450+300+100”) #width height xoffset #yoffset
regimage = PhotoImage(file = “SearchMedicine.png”);
bg_Label = Label(root,image = regimage)
bg_Label.place(x=0,y=0,relwidth=1,relheight=1)
root.title(“Search Medicine – Medicine Management System”)
root.config
##################Top Frame ###########
TopHeadingFrame = Frame(root,width=600,bd=1)
TopHeadingFrame.pack(side=TOP)

HeadingLabel = Label(TopHeadingFrame,text=”Search Medicine”,
font=(“Helvetica”,16),fg=”brown”, bg=”white”)
HeadingLabel.grid(row=0,column=1,padx=10,pady=10)
###################Declare variables for the columns to access######3
MedicineName = StringVar()
MedicineName.set(“”)
##########
MidFrame = Frame(root,width=600)
MidFrame.pack(side=TOP)
##########
MedicineNameLabel = Label(MidFrame,text=”Medicine Name”,
font=(“Helvetica”,10),fg=”brown”, bg=”white”)
MedicineNameLabel.grid(row=1,padx=10,pady=10)
##########
MedicineNameTextbox = Entry(MidFrame,textvariable=MedicineName,
font=(“Helvetica”,10))
MedicineNameTextbox.grid(row=1,column=1,padx=10,pady=10)
##########
def back():
    root.destroy()
import home
##########
def search():
    for i in treeview.get_children() :
        treeview.delete(i)
conn = sqlite3.connect(“medicine.db”)
cursor = conn.cursor()
medname = str(MedicineName.get())
cursor.execute(“select * from ‘medicine’ where MedicineName=?”,(medname,))
dataselect = cursor.fetchall()
### insert in the parent container and append it in the end
for data in dataselect:
treeview.insert(”,’end’,value=(data))
cursor.close()
conn.commit()
##########
SearchButton = Button(MidFrame,text=”Search”, command = search,
font=(“Helvetica”,10))
SearchButton.grid(row=1,column=2,padx=10,pady=10)
##########
BackButton = Button(MidFrame,text=”Back”, command = back,
font=(“Helvetica”,10))
BackButton.grid(row=1,column=3,padx=10,pady=10)
##########
ViewFrame = Frame(root,width=400)
ViewFrame.pack(side=TOP)
#################create a treeview in ViewFrame #######
treeview = ttk.Treeview(ViewFrame,columns=(“MedicineID”, “MedicineName” ,”Company”, “ChemicalComp”,”ManuDate” ,”ExpDate”, “Costfor10″),height=200,selectmode=”extended” )
treeview.heading(“MedicineID” , text=”MedicineID” , anchor =”w”)
treeview.heading(“MedicineName” , text=”MedicineName” , anchor =”w”)
treeview.heading(“Company” , text=”Company” , anchor =”w”)
treeview.heading(“ChemicalComp” , text=”ChemicalComp” , anchor =”w”)
treeview.heading(“ManuDate” , text=”ManuDate” , anchor =”w”)
treeview.heading(“ExpDate” , text=”ExpDate” , anchor =”w”)
treeview.heading(“Costfor10″ , text=”Costfor10″ , anchor =”w”)

treeview.column(“#0” ,stretch=NO,width=10,minwidth=0)
treeview.column(“#1” ,stretch=NO,width=70,minwidth=0)
treeview.column(“#2” ,stretch=NO,width=120,minwidth=0)
treeview.column(“#3” ,stretch=NO,width=120,minwidth=0)
treeview.column(“#4” ,stretch=NO,width=160,minwidth=0)
treeview.column(“#5” ,stretch=NO,width=70,minwidth=0)
treeview.column(“#6” ,stretch=NO,width=70,minwidth=0)
treeview.column(“#7” ,stretch=NO,width=70,minwidth=0)
treeview.pack()
#########################Lets connect the database and fetch values #########
ViewMedicine
from tkinter import * #import tkinter library
import tkinter.messagebox as msg # to display message box
import sqlite3 #to store data
import tkinter.ttk as ttk

root = Tk()
root.geometry(“700×450+300+100”) #width height xoffset #yoffset
regimage = PhotoImage(file = “SearchMedicine.png”);
bg_Label = Label(root,image = regimage)
bg_Label.place(x=0,y=0,relwidth=1,relheight=1)
root.title(“Search Medicine – Medicine Management System”)
root.config
##################Top Frame ###########
TopHeadingFrame = Frame(root,width=600,bd=1)
TopHeadingFrame.pack(side=TOP)

HeadingLabel = Label(TopHeadingFrame,text=”Search Medicine”,
font=(“Helvetica”,16),fg=”brown”, bg=”white”)
HeadingLabel.grid(row=0,column=1,padx=10,pady=10)
###################Declare variables for the columns to access######3
MedicineName = StringVar()
MedicineName.set(“”)
##########
MidFrame = Frame(root,width=600)
MidFrame.pack(side=TOP)
##########
MedicineNameLabel = Label(MidFrame,text=”Medicine Name”,
font=(“Helvetica”,10),fg=”brown”, bg=”white”)
MedicineNameLabel.grid(row=1,padx=10,pady=10)
MedicineNameTextbox = Entry(MidFrame,textvariable=MedicineName,
font=(“Helvetica”,10))
MedicineNameTextbox.grid(row=1,column=1,padx=10,pady=10)
##########
def back():
    root.destroy()
import home
##########
def search():
    for i in treeview.get_children() :
        treeview.delete(i)
conn = sqlite3.connect(“medicine.db”)
cursor = conn.cursor()
medname = str(MedicineName.get())
cursor.execute(“select * from ‘medicine’ where MedicineName=?”,(medname,))
dataselect = cursor.fetchall()
### insert in the parent container and append it in the end
for data in dataselect:
    treeview.insert(”,’end’,value=(data))
cursor.close()
conn.commit()
##########
SearchButton = Button(MidFrame,text=”Search”, command = search,
font=(“Helvetica”,10))
SearchButton.grid(row=1,column=2,padx=10,pady=10)
##########
BackButton = Button(MidFrame,text=”Back”, command = back,
font=(“Helvetica”,10))
BackButton.grid(row=1,column=3,padx=10,pady=10)
##########
ViewFrame = Frame(root,width=400)
ViewFrame.pack(side=TOP)
#################create a treeview in ViewFrame #######
treeview = ttk.Treeview(ViewFrame,columns=(“MedicineID”, “MedicineName” ,”Company”, “ChemicalComp”,”ManuDate” ,”ExpDate”, “Costfor10″),height=200,selectmode=”extended” )
treeview.heading(“MedicineID” , text=”MedicineID” , anchor =”w”)
treeview.heading(“MedicineName” , text=”MedicineName” , anchor =”w”)
treeview.heading(“Company” , text=”Company” , anchor =”w”)
treeview.heading(“ChemicalComp” , text=”ChemicalComp” , anchor =”w”)
treeview.heading(“ManuDate” , text=”ManuDate” , anchor =”w”)
treeview.heading(“ExpDate” , text=”ExpDate” , anchor =”w”)
treeview.heading(“Costfor10″ , text=”Costfor10″ , anchor =”w”)

treeview.column(“#0” ,stretch=NO,width=10,minwidth=0)
treeview.column(“#1” ,stretch=NO,width=70,minwidth=0)
treeview.column(“#2” ,stretch=NO,width=120,minwidth=0)
treeview.column(“#3” ,stretch=NO,width=120,minwidth=0)
treeview.column(“#4” ,stretch=NO,width=160,minwidth=0)
treeview.column(“#5” ,stretch=NO,width=70,minwidth=0)
treeview.column(“#6” ,stretch=NO,width=70,minwidth=0)
treeview.column(“#7” ,stretch=NO,width=70,minwidth=0)
treeview.pack()
#########################Lets connect the database and fetch values #########