from tkinter import *
from functools import partial

import sqlite3
import sqlite3 as lite


def validateRef(RefNoIn):
     return RefNoIn.isdigit()   


def deletebookingO():
        connection = sqlite3.connect('reservations.db')
        connection.execute("DELETE from dates WHERE id=?",[RefEntry.get()])
        print("Booking deleted")
        
  
        # display row by row
        cursor = connection.execute("SELECT * from dates")
        for row in cursor:
          print(row)

        return

def stopcancellation():
        Nolabel= Label(CancelWO,text="Cancellation was stopped",fg="red",).place(x=450,y=400)
        return

def deleteBooking():
        connection = sqlite3.connect('reservations.db')
        cursor=connection.execute("SELECT * from dates WHERE id=?",[RefEntry.get()])
        for row in cursor:
            t=row
        
        reconfirmL= Label(CancelWO, text="Are you sure?").place(x=450,y=200)
        YesB= Button(CancelWO, text="Yes", command=deletebookingO,).place(x=450,y=250)
        NoB=Button(CancelWO, text="No", command=stopcancellation).place(x=550,y=250)
        bookinfo= Label(CancelWO,text=t,fg="orange").place(x=200,y=300)
        return

def main_menu():
    import run
    return

def exitpage():
    CancelWO.destroy()
    return

#window
CancelWO= Tk()
CancelWO.attributes('-fullscreen',True)
CancelWO.configure(bg='beige')
CancelWO.title('Reference input')

RefInLabel= Label(CancelWO, text="Enter reference number").place(x=450, y=100)
RefNoIn= StringVar()
Ref_valid = CancelWO.register(validateRef)
RefEntry= Entry(CancelWO,validate='key',validatecommand=(Ref_valid,'%S'), textvariable=RefNoIn)
RefEntry.place(x=600,y=100)
SubButton= Button(CancelWO, text="submit", command=deleteBooking).place(x=550, y=150)
mainbutton= Button(CancelWO, text="Main Menu", bg="orange",command=main_menu).place(x=1150,y=675)
exitbutton= Button(CancelWO, text="Exit",bg="red",command=exitpage).place(x=1225,y=675)

        


CancelWO.mainloop()
