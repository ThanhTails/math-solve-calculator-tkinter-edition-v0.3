from tkinter import *
from math import*

def cal_ar_sq():
    ed=ed_entry.get()
    ans=6*(int(ed)**2)
    answer=Label(main,text="The answer is: "+str(ans),fg="red")
    answer.grid(row=2,column=1)

def qu():
    main.destroy()

def open_round_square():
    global main,ed_entry
    main=Tk()
    main.geometry("1000x500")
    ed_L=Label(main,text="Edge= ",)
    ed_L.grid(row=0,column=0)

    ed_entry=Entry(main,width=20)
    ed_entry.grid(row=0,column=1)

    cal=Button(main,text="Start",command=cal_ar_sq)
    cal.grid(row=1,column=1)

    exi=Button(main,text="Back",command=qu)
    exi.grid(row=3,column=1)
    
