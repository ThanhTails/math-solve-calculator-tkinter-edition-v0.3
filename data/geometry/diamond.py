from tkinter import*
def dia_win():
  global dia_main
  dia_main=Tk()
  dia_main.geometry("500x500")
  dia_main.title("Trapzoid")
  area=Button(dia_main,text="Area",fg="green",command=trap_area)
  area.grid(row=0,column=0)
  per=Button(dia_main,text="Perimter",fg="green",command=trap_per)
  per.grid(row=1,column=0)
  clo=Button(dia_main,text="Close",fg="green",command=close_trap)
  clo.grid(row=2,column=0)
def close_trap():
  dia_main.destroy()
def trap_area():
  global trap_aw
  global a,h
  trap_aw=Tk()
  trap_aw.geometry("300x300")
  trap_aw.title("Area")
  a=Entry(trap_aw,width=5)
  a.grid(row=0,column=0)
  plus=Label(trap_aw,text="x")
  plus.grid(row=0,column=1)
  h=Entry(trap_aw,width=5)
  h.grid(row=0,column=2)
  start=Button(trap_aw,text="Start",command=start_atrap)
  start.grid(row=1,column=0)
  quit=Button(trap_aw,text="Close",command=close_atrap)
  quit.grid(row=2,column=0)
def close_atrap():
  trap_aw.destroy()
def start_atrap():
  a1=a.get()
  h1=h.get()
  a2=int(a1)
  h2=int(h1)
  ans=str(a2*h2)
  ans1=Label(trap_aw,text="The answer is: "+ans)
  ans1.grid(row=5,column=0)
def trap_per():
  global trap_pw
  global a,b,c,d
  trap_pw=Tk()
  trap_pw.geometry("300x300")
  trap_pw.title("Perimeter")
  a=Entry(trap_pw,width=5)
  a.grid(row=0,column=0)
  plus=Label(trap_pw,text="x")
  plus.grid(row=0,column=1)
  four=Label(trap_pw,text="4")
  four.grid(row=0,column=2)
  equal=Label(trap_pw,text="=")
  equal.grid(row=0,column=3)
  start=Button(trap_pw,text="Start",command=start_ptrap)
  start.grid(row=1,column=0)
  quit=Button(trap_pw,text="Close",command=close_ptrap)
  quit.grid(row=2,column=0)
def close_ptrap():
  trap_pw.destroy()
def start_ptrap():
  a1=a.get()
  a2=int(a1)
  ans=str(a2*4)
  ans1=Label(trap_pw,text="The answer is: "+ans)
  ans1.grid(row=3,column=0)