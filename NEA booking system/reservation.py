from tkinter import *

import datetime
from tkcalendar import Calendar
import sqlite3
import sqlite3 as lite


def prepareDB():#creates the databse and table
    try:

        conn=sqlite3.connect("reservations.db")
        c = conn.cursor()
      

        c.execute("""CREATE TABLE IF NOT EXISTS dates
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
             owner TEXT NOT NULL,
             howmanypeople INT NOT NULL,
             dateOf DATE NOT NULL,
             timeOf INT NOT NULL,
             child TEXT NOT NULL,
             Mobile INT NOT NULL,
             Email TEXT NOT NULL,
             event TEXT NOT NULL ,
             allergy TEXT NOT NULL,
             other TEXT NOT NULL);""")


        
        conn.commit()
        conn.close()

    except:
        print("n")
        raise

def OpentimeS():
    import Inputform
    bookpageO.destroy()
    
    return


def main_menu():
    import run
    return


def exitpage():
    bookpageO.destroy()
    return

prepareDB()

bookpageO= Tk()
bookpageO.attributes('-fullscreen',True)
bookpageO.title('bookings')
ProgressB=Label(bookpageO,text="HAHAHAHAHAHAHAHAHAHA",fg="orange",bg="orange", borderwidth=2,relief="solid")
ProgressB.place(x=500,y=10)
ProgressBa=Label(bookpageO,text="HAHAHAHAHAHAHAHAHAHA",fg="white",bg="white", borderwidth=2,relief="solid")
ProgressBa.place(x=675,y=10)
nextbutton = Button(bookpageO, text="next", command=OpentimeS).place(x=600, y=300)
mainbutton= Button(bookpageO, text="Main Menu", bg="orange",command=main_menu).place(x=1150,y=675)
exitbutton= Button(bookpageO, text="Exit",bg="red",command=exitpage).place(x=1225,y=675)



tkc = Calendar(bookpageO,selectmode = 'day', year=2023,month=4,date=1,date_pattern="dd-mm-y")
tkc.place(x=550,y=40)

#tkc.pack(pady=40)

def fetch_date():
    date.config(text = "" + tkc.get_date())
    

buttonOne = Button( bookpageO,text="Select date", command = fetch_date, bg="green",fg='black')
buttonOne.place(x=600,y=250)
date = Label(bookpageO,text="",bg='green', fg='black')
date.place(x=600,y=275)
dateSel=tkc.get_date()












