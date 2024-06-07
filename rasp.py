# !/usr/bin/python3
from tkinter import *
import time
from tkinter import ttk
import fileinput
import datetime
from time import strftime
from PIL import ImageTk, Image
Image.CUBIC = Image.BICUBIC
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import speedtest
import os
#saat-tarih(date)-hiz-sicaklik-hava durumu


#def clearToTextInput():
#   T.delete("1.0","end")

#Tk=Tk()
Tk= ttk.Window(themename='cyborg')
Tk.title("METER")
Tk.geometry("1000x1000")
width= Tk.winfo_screenwidth()               
height= Tk.winfo_screenheight()               
Tk.geometry("%dx%d" % (width, height))


#bg = PhotoImage(file = "bg2.png")
bg= ImageTk.PhotoImage(Image.open("bg2.png"))
label1 = Label( Tk, image = bg)
label1.place(x=0,y=0,relwidth=1,relheight=1)

mytext=Label(Tk,text="INSTRUMENT PANEL",font=("Arial Black",50),fg="red",background="cyan")
mytext.place(x=425,y=80)


# Not done yet
heattext=Label(Tk,text="14°C",font = ('calibri', 30, 'bold'),fg="red",background="cyan")
heattext.place(y=650,x=950)





file = open('input.txt', 'r')
def mtr():
    line = file.readline()
    if type(eval(line))== int : 
        meter.configure(amountused = line)
    meter.after(1000, mtr)


meter = ttk.Meter(
    Tk,
    metersize=500,
    padding=5,
    amountused=150,
    amounttotal=320,
    metertype="semi",
    subtext="kilometer per hour",
    interactive=True,
    stripethickness=2,
    textright="km"
    )

meter2 = ttk.Meter(
    Tk,
    metersize=500,
    padding=5,
    amountused=150,
    amounttotal=320,
    metertype="semi",
    subtext="kilometer per hour",
    interactive=True,
    stripethickness=2,
    textright="x1000r/min"
    )

meter.place(x=220,y=220)
meter2.place(x=820 ,y=220)

#meter.step(x)



def time():
    string = strftime('%H:%M:%S')
    lbl.config(text = string)
    lbl.after(1000, time)

def date():
    str = datetime.datetime.now()
    datetext.config(text = str.strftime("%x"))
    datetext.after(1000, date)


datetext = Label(Tk, font = ('calibri', 30, 'bold'),
            background = 'cyan',
            foreground = 'white')

lbl = Label(Tk, font = ('calibri', 30, 'bold'),
            background = 'cyan',
            foreground = 'white')



lbl.place(y=650,x=1250)
datetext.place(y=650,x=1050)

def callback():
    os.system('python3 map2.py')

icon = Image.open("icon.png")
render = ImageTk.PhotoImage(icon)

B=ttk.Button(
   Tk, 
   text="MAP", 
   command=callback,
   image= render
)

B.place(y=610,x=75)



date()
time()
mtr()

#T=Text(Tk,fg="red",height=5,width=52,font="Times 20 italic bold")

#for i in range (0,101):
#    text=str(i)
#    T.insert(INSERT,text)
#    T.grid()
# Add image file

#Tk.after(milisaniye,)

#T.grid()


#for line in fileinput.input(files ='input.txt'):
#   text=str(line)
#   T.insert(INSERT,text)
#   time.sleep(1)
 #  a=int(input())
  # if(a==0):
   #   clearToTextInput()

Tk.mainloop()
