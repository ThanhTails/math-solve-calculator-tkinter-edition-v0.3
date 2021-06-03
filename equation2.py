from tkinter import*
from math import*
def eq2():
  global eq_win1
  global a1
  global b
  global c
  eq_win1=Tk()
  eq_win1.geometry("800x500")
  lab=Label(eq_win1,text="Equation")
  lab.grid(row=0,column=0)
  a1=Entry(eq_win1,width=5)
  a1.grid(row=1,column=0)
  a2=Label(eq_win1,text="x**2+")
  a2.grid(row=1,column=1)
  b=Entry(eq_win1,width=5)
  b.grid(row=1,column=2)
  b2=Label(eq_win1,text="x+")
  b2.grid(row=1,column=3)
  c=Entry(eq_win1,width=10)
  c.grid(row=1,column=4)
  c1=Label(eq_win1,text="=0")
  c1.grid(row=1,column=5)
  Start=Button(eq_win1,text="Start",fg="yellow",bg="red",command=start_eq2)
  Start.grid(row=2,column=0)
  close=Button(eq_win1,text="Close",command=close_eq2)
  close.grid(row=3,column=0)
def close_eq2():
  eq_win1.destroy()
def start_eq2():
  a1_1=a1.get()
  b1=b.get()
  c1=c.get()
  a2=int(a1_1)
  b2=int(b1)
  c2=int(c1)
  if a2==0:
    if b2==0:
      if c2==0:
        ans=Label(eq_win1,text="This equation have a lot of experiments")
        ans.grid(row=4,column=0)
      else: 
        ans=Label(eq_win1,text="This equation have no experiment")
        ans.grid(row=4,column=0)
    else:
      if c2==0:
        ans=Label(eq_win1,text="This equation have 1 experiment: x=0")
        ans.grid(row=4,column=0)
      else: 
        ans1=-c2/b2
        ans2=str(ans1)
        ans=Label(eq_win1,text="This equation have 1 experiment: x="+ans2)
        ans.grid(row=4,column=0)
  else:
    delta=b2**2-4*a2*c2  
    if delta<0:
      ans=Label(eq_win1,text="This equation have no experiment")
      ans.grid(row=4,column=0)
    elif delta==0:
      ans1=-b2/(2*a2)
      ans2=str(ans1)
      ans=Label(eq_win1,text="This equation have a lot of experiments: x="+ans2)
      ans.grid(row=4,column=0)
    else:
      ans=Label(eq_win1,text="This equation have 2 experiments")
      ans.grid(row=4,column=0)
      ans_1=str((-b2-sqrt(delta))/(2*a2))
      ans_1_1=Label(eq_win1,text="x1="+ans_1)
      ans_1_1.grid(row=5,column=0)
      ans_2=str((-b2+sqrt(delta))/(2*a2))
      ans_2_1=Label(eq_win1,text="x2="+ans_1)
      ans_2_1.grid(row=6,column=0)