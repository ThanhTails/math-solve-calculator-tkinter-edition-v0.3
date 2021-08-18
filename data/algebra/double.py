from tkinter import*
def double_win():
  global plus_main
  global first
  global second
  plus_main=Tk()
  plus_main.geometry("500x500+100+100")
  first=Entry(plus_main,width=5,font=("arial",50,"normal"))
  first.grid(row=0,column=0)
  second=Entry(plus_main,width=5)
  second.grid(row=0,column=1)
  start=Button(plus_main,text="Start",command=start_double)
  start.grid(row=1,column=5)
  destroy=Button(plus_main,text="Close",command=w_plus_destroy)
  destroy.grid(row=2,column=0)
def start_double():
  a=first.get()
  b=second.get()
  c1=int(a)
  c2=int(b)
  c=c1**c2
  ans=str(c)
  lab=Label(plus_main,text="The answer is: "+ans)
  lab.grid(row=2,column=0)
def w_plus_destroy():
  plus_main.destroy()