from tkinter import *
from functools import partial

import datetime


#window
MainWindow= Tk()
MainWindow.attributes('-fullscreen',True)
MainWindow.configure(bg='beige')
MainWindow.title('Main menu')

#title of system
NameLabel= Label(MainWindow, text="Eat Out" , font=('Times',50)).place(x=525, y=100) #underline, increase font size, change font size
StateLabel= Label(MainWindow, text="Main Menu").grid(row=1,column=1)#increase size and change font

def OpenLogin():
     import login 
     return

  
def OpenCancel():
     import cancellation 
     return

def OpenReservation():
    import reservation 
    return
     
def exitpage():
    MainWindow.destroy()
    return


#Buttons
Bookingbutton = Button(MainWindow, text=" Make Reservation",bg="orange",command= OpenReservation).place(x=575, y=250)#reposition + link to new tab
CancellationButton = Button(MainWindow, text=" Cancel reservation",bg="orange",command = OpenCancel).place(x=575,y=300)#reposition+ link to new tab
Managebutton = Button(MainWindow, text="Management",bg="orange", command =OpenLogin)
Managebutton.place(relx=0.0,
                   rely=1.0,
                   anchor='sw')
Websitebutton = Button(MainWindow, text="Visit Website",bg="orange")
Websitebutton.place(relx=1.0,
                    rely=1.0,
                    anchor='se')
exitbutton= Button(MainWindow, text="Exit",bg="red",command=exitpage).place(x=615,y=350)
MainWindow.mainloop()

