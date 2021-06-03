from tkinter import*
def div_win():
  global plus_main
  global first
  global second
  plus_main=Tk()
  first=Entry(plus_main,width=50)
  first.pack()
  p=Label(plus_main,text=":")
  p.pack()
  second=Entry(plus_main,width=50)
  second.pack()
  start=Button(plus_main,text="Start",command=start_div)
  start.pack()
  destroy=Button(plus_main,text="Close",command=w_plus_destroy)
  destroy.pack()
def start_div():
  a=first.get()
  b=second.get()
  c1=int(a)
  c2=int(b)
  c=c1/c2
  ans=str(c)
  lab=Label(plus_main,text="The answer is: "+ans)
  lab.pack()
def w_plus_destroy():
  plus_main.destroy()