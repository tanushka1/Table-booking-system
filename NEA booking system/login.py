from tkinter import *
from functools import partial
#from reservation import *
import sqlite3
import sqlite3 as lite


#Actual function that runs


def validateLogin(username,password):
      
    #actual username and password
      correctuser='Tanushka'
      correctpass='Ukidve'
      def search():
            connection = sqlite3.connect('reservations.db')
            cursor=connection.execute("SELECT * from dates WHERE id=?",[refEntry.get()])
            for row in cursor:
              t=row

            bookinfo= Label(tkWindowV,text=t,fg="orange").place(x=200,y=300)
        

      
      if usernameEntry.get() == correctuser and passwordEntry.get() == correctpass :
          tkWindowV = Tk()
          tkWindowV.geometry('400x150')
          tkWindowV.configure(bg='beige')
          tkWindowV.title('Valid')
          ValidLabel= Label(tkWindowV, text='Reservations').grid(row=0, column=0)
          refL=Label(tkWindowV,text='enter reference number:').place(x=100,y=50)
          reIn=StringVar
          refEntry=Entry(tkWindowV,textvariable=reIn)
          refEntry.place(x=250,y=50)
          sub=Button(tkWindowV,text="submit",command=search).place(x=100,y=100)
          sqliteConnection = sqlite3.connect('reservations.db')
          sql_query = """SELECT * FROM dates"""
          cursor = sqliteConnection.cursor()
          cursor.execute(sql_query)
          print(cursor.fetchall())

          
      else:
          tkWindowV = Tk()
          tkWindowV.geometry('400x150')
          tkWindowV.title('Invalid')
          ValidLabel= Label(tkWindowV, text= "Login unsuccesful").grid(row=0, column=0)
      
          return



def main_menu():
    import run
    return

def exitpage():
    tkWindow.destroy()
    return

#window
tkWindow = Tk()
tkWindow.attributes('-fullscreen',True)
tkWindow.configure(bg='beige')
tkWindow.title('Tkinter Login Form')

#username label and text entry box
usernameLabel =Label(tkWindow, text="User Name").place(x=450,y=200)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username)
usernameEntry.place(x=550,y=200)

#password label and password entry box
passwordLabel = Label(tkWindow, text="Password").place(x=450,y=225)
password= StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*')
passwordEntry.place(x=550,y=225)

ManageL=Label(tkWindow,text=" Management Login",font=('Times',25)).place(x=450,y=100)

validateLogin=partial(validateLogin,username,password)
 
#login button
loginbutton= Button(tkWindow, text="login", command=validateLogin).place(x=450,y=250)
mainbutton= Button(tkWindow, text="Main Menu", bg="orange",command=main_menu).place(x=1150,y=675)
exitbutton= Button(tkWindow, text="Exit",bg="red",command=exitpage).place(x=1225,y=675)

 
