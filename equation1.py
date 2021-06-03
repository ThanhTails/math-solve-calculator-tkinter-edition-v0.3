from tkinter import*
from math import*
def eq1():
  global eq_win
  global a1
  global b
  global c
  eq_win=Tk()
  eq_win.geometry("800x500")
  lab=Label(eq_win,text="Equation")
  lab.grid(row=0,column=0)
  a1=Entry(eq_win,width=5)
  a1.grid(row=1,column=0)
  a2=Label(eq_win,text="x+")
  a2.grid(row=1,column=1)
  b=Entry(eq_win,width=5)
  b.grid(row=1,column=2)
  b2=Label(eq_win,text="=")
  b2.grid(row=1,column=3)
  c=Entry(eq_win,width=10)
  c.grid(row=1,column=4)
  Start=Button(eq_win,text="Start",fg="yellow",bg="red",command=start_eq1)
  Start.grid(row=2,column=0)
  close=Button(eq_win,text="Close",command=close_eq1)
  close.grid(row=5,column=0)
def close_eq1():
  eq_win.destroy()
def start_eq1():
  a1_1=a1.get()
  b1=b.get()
  c1=c.get()
  a2_2=int(a1_1)
  b2_2=int(b1)
  c2_2=int(c1)

  ans=(c2_2-b2_2)/a2_2
  ans1=str(ans)
  ans2=Label(eq_win,text="The answer is: "+ans1)
  ans2.grid(row=3,column=0)