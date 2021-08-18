from tkinter import*
from math import*

def start():
    a=a_en.get()
    b=b_en.get()
    c=c_en.get()
    a1=int(a)
    b1=int(b)
    h1=int(c)

    ans=2*h1*(a1+b1)+2*a1*b1
    answer=Label(main,text="The answer is: "+str(ans))
    answer.grid(row=4,column=1)

def quiting():
    main.destroy()

def main_window():
    global main
    global a_en,b_en,c_en
    main=Tk()
    main.geometry("700x500")

    a_lab=Label(main,text="Length= ",fg="grey")
    a_lab.grid(row=0,column=0)

    a_en=Entry(main,width=30)
    a_en.grid(row=0,column=1)

    b_lab=Label(main,text="Width= ",fg="grey")
    b_lab.grid(row=1,column=0)

    b_en=Entry(main,width=30)
    b_en.grid(row=1,column=1)

    c_lab=Label(main,text="Height= ",fg="grey")
    c_lab.grid(row=2,column=0)

    c_en=Entry(main,width=30)
    c_en.grid(row=2,column=1)

    s=Button(main,text="Start",bg="red",command=start)
    s.grid(row=3,column=0)

    q=Button(main,text="Quit",bg="red",command=quiting)
    q.grid(row=8,column=0)
    
