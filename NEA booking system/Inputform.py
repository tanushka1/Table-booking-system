from tkinter import *
from reservation import *
import datetime
import sqlite3
#from testCal import *
from tkcalendar import Calendar
from email.message import EmailMessage
import ssl
import smtplib
import re


class Booking:

    

    def setDate(self,dateOfParameter):
        self.dateOf=dateOfParameter

    def setOwner(self,ownerParameter):
        self.owner=ownerParameter

    def setPeople(self,numberOfPeopleParameter):
        self.numberOfPeople=numberOfPeopleParameter

    def setTime(self,timeOfParameter):
        self.timeOf=timeOfParameter

    def setChild(self,childParameter):
        self.child=childParameter

    def setMobile(self,mobileParameter):
        self.Mobile=mobileParameter

    def setEmail(self,emailParameter):
        self.Email=emailParameter

    def setEvent(self,eventParameter):
        self.event=eventParameter

    def setAllergy(self,allergyParameter):
        self.allergy=allergyParameter

    def setOther(self,otherParameter):
        self.other=otherParameter

    def saveToDB(self):
        conn= sqlite3.connect("reservations.db")
        c = conn.cursor()
        c.execute('insert into dates(owner,howmanypeople,dateOf,timeOf,child,Mobile,Email,event,allergy,other) values(?,?,?,?,?,?,?,?,?,?)', [str(self.owner),str(self.numberOfPeople),str(self.dateOf),str(self.timeOf),str(self.child),str(self.Mobile),str(self.Email),str(self.event),str(self.allergy),str(self.other)])
        
        conn.commit()
        return c.lastrowid
        conn.close()

def validate_NOguest(NOguestIn):
    return NOguestIn.isdigit()

def validate_mobile(MobileIn):
    return MobileIn.isdigit()

def validate_time(TimeIn):
    return TimeIn.isdigit()

def validate_name(NameIn):
    return NameIn.isalpha()

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w{2,3}$'
def validate_email(EmailIn):
    if(re.search(regex,EmailIn) and EmailIn.isapha):
        return True
    else:
        return False
    



def newBooking():

    aBooking=Booking()
    
    dateRaw=dateSel
    aBooking.setDate(dateRaw)

    ownerRaw=NameEntry.get()
    aBooking.setOwner(ownerRaw)

    numberOfPeople=NOguestEntry.get()
    aBooking.setPeople(numberOfPeople)
    
    

    timeRaw=TimeEntry.get()
    aBooking.setTime(timeRaw)

    childRaw=ChildEntry.get()
    aBooking.setChild(childRaw)

    MobileRaw=MobileEntry.get()
    aBooking.setMobile(MobileRaw)

    EmailRaw=EmailEntry.get()
    aBooking.setEmail(EmailRaw)

    EventRaw=EventEntry.get()
    aBooking.setEvent(EventRaw)

    AllergyRaw=AllergyEntry.get()
    aBooking.setAllergy(AllergyRaw)

    OtherRaw=OtherEntry.get()
    aBooking.setOther(OtherRaw)

    bookingID=aBooking.saveToDB()
    bId= Label(inputWin,text='your reference number is: '+str(bookingID),fg='blue',bg='beige').place(x=800,y=200)
    EnL=Label(inputWin,text='Thank You!',fg='blue',bg='beige').place(x=800,y=225)

    
    refId=bookingID
    email_sender='pythontest7825@gmail.com'
    email_password='wkbfjlbfsalcolyi'
    email_receiver=(str(EmailEntry.get()))

    subject='Test'
    body= (""" Name - """ + str(NameEntry.get()+ """Booking is confirmed, your reference number is """+ str(refId) + """ time- """ + str(TimeEntry.get())))

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject']= subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
         smtp.login(email_sender,email_password)
         smtp.sendmail(email_sender,email_receiver,em.as_string())


    



def exitpage():
    inputWin.destroy()
    return

def main_menu():
    import run
    return







inputWin=Tk()


inputWin.attributes('-fullscreen',True)
inputWin.configure(bg='beige')
inputWin.title('Form input')

ProgressBar=Label(inputWin, text="HAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA", fg="orange",bg="orange", borderwidth=2,relief="solid").place(x=500,y=10)



SelecttimeL= Label(inputWin, text='enter time').place(x=100, y=50)
TimeIn=StringVar()
valid_time= inputWin.register(validate_time)
TimeEntry= Entry(inputWin,validate='key',validatecommand=(valid_time,'%S'), textvariable=TimeIn)
TimeEntry.place(x=350, y=50)


NameL= Label(inputWin, text='Name: ').place(x=100, y=100)
NameIn=StringVar()
valid_name= inputWin.register(validate_name)
NameEntry= Entry(inputWin,validate='key',validatecommand=(valid_name,'%S'), textvariable=NameIn)
NameEntry.place(x=350, y=100)


NOguestL=Label(inputWin, text='No. of guests: ').place(x=100, y=150)
NOguestIn = StringVar()
my_valid = inputWin.register(validate_NOguest)
NOguestEntry= Entry(inputWin,validate='key',validatecommand=(my_valid,'%S'),textvariable=NOguestIn)
NOguestEntry.place(x=350, y=150)




    

ChildL= Label(inputWin, text='Are there any children? (Y/N) ').place(x=100, y=200)
ChildIn=StringVar()
ChildEntry= Entry(inputWin, textvariable=ChildIn)

def child():
    global ChildEntry
    global ChildIn
    ChildIn=StringVar()
    ChildEntry= Entry(inputWin, textvariable=ChildIn)
    ChildEntry.place(x=555,y=205)
    CL=Label(inputWin,text='number of children',fg='red',bg='beige').place(x=450,y=205)
    EventIn= StringVar()
    

ChildYes=Button(inputWin, text='yes',command=child).place(x=350,y=200)
ChildNo=Button(inputWin,text='no').place(x=400,y=200)

MobileL=Label(inputWin, text='Mobile number: ').place(x=100, y=250)
MobileIn= StringVar()
valid_mobile= inputWin.register(validate_mobile)
MobileEntry= Entry(inputWin,validate='key', validatecommand=(valid_mobile,'%S'), textvariable=MobileIn)
MobileEntry.place(x=350, y=250)

   
    

EmailL=Label(inputWin, text='Email: ').place(x=100, y=300)
EmailIn=StringVar()
valid_email= inputWin.register(validate_email)
EmailEntry= Entry(inputWin,validate='focusout',validatecommand=(valid_email,'%P'), textvariable=EmailIn)
EmailEntry.place(x=350, y=300)


EventL=Label(inputWin, text='Special Event?').place(x=100, y=350)
EventIn= StringVar()
EventEntry= Entry(inputWin, textvariable=EventIn)
def event():
    global EventIn
    global EventEntry
    El=Label(inputWin, text='Specify event',fg='red',bg='beige').place(x=450,y=355)
    EventIn= StringVar()
    EventEntry= Entry(inputWin, textvariable=EventIn)
    EventEntry.place(x=550,y=355)
    
 
EventYes=Button(inputWin, text='yes',command=event).place(x=350,y=350)
EventNo=Button(inputWin,text='no').place(x=400,y=350)
                
AllergyL=Label(inputWin, text='Any allergies? ').place(x=100, y=400)
AllergyIn= StringVar()
AllergyEntry= Entry(inputWin, textvariable=AllergyIn)

def allergy():
    global AllergyIn
    global AllergyEntry
    Al=Label(inputWin, text='Specify allergy',fg='red',bg='beige').place(x=450,y=405)
    AllergyIn= StringVar()
    AllergyEntry= Entry(inputWin, textvariable=AllergyIn)
    AllergyEntry.place(x=550,y=405)

AllergyYes=Button(inputWin, text='yes',command=allergy).place(x=350,y=400)
AllergyNo=Button(inputWin,text='no').place(x=400,y=400)

WheechairL=Label(inputWin, text='Do you require wheelchair access?(Y/N)').place(x=100, y=450)
WheelchairIn= StringVar()
WheelchairEntry= Entry(inputWin, textvariable=WheelchairIn)

def wheel():
    global WheelchairIn
    global WheelchairEntry
    WheelchairIn= StringVar()
    WheelchairEntry= Entry(inputWin, textvariable=WheelchairIn)
    WheelchairEntry.place(x=550, y=455)
    Wl=Label(inputWin, text='Number of users:',fg='red',bg='beige').place(x=450,y=455)
    
    
    

WheelYes=Button(inputWin, text='yes',command=wheel).place(x=350,y=450)
WheelNo=Button(inputWin,text='no').place(x=400,y=450)

OtherL=Label(inputWin, text='Other Requirements:(NA for none) ').place(x=100, y=500)
OtherIn= StringVar()
OtherEntry= Entry(inputWin, textvariable=OtherIn)

def other():
    global OtherIn
    global OtherEntry
    Ol=Label(inputWin, text='Please specify',fg='red',bg='beige').place(x=450,y=505)
    OtherIn= StringVar()
    OtherEntry= Entry(inputWin, textvariable=OtherIn)
    OtherEntry.place(x=550,y=505)

OtherYes=Button(inputWin, text='yes',command=other).place(x=350,y=500)
OtherNo=Button(inputWin,text='no').place(x=400,y=500)

DoneButton= Button( inputWin,text="Done",bg="orange", command=newBooking).place(x=100, y=550)
exitbutton= Button(inputWin, text="Exit",bg="red",command=exitpage).place(x=1225,y=675)
mainbutton= Button(inputWin, text="Main Menu", bg="orange",command=main_menu).place(x=1150,y=675)


