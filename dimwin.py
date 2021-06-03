from tkinter import*
def dim_win():
  global dim_main
  global first
  global second
  dim_main=Tk()
  dim_main.title("Plus")
  first=Entry(dim_main,width=50)
  first.pack()
  p=Label(dim_main,text="and")
  p.pack()
  second=Entry(dim_main,width=50)
  second.pack()
  start=Button(dim_main,text="Start",command=start_dim)
  start.pack()
  destroy=Button(dim_main,text="Close",command=dim_close)
  destroy.pack()
def dim_close():
  dim_main.destroy()
def start_dim():
  a=first.get()
  b=second.get()
  c1=int(a)
  c2=int(b)
  c=divmod(c1,c2)
  ans=str(c)
  lab=Label(dim_main,text="The answer is:"+ans)
  lab.pack()
