from tkinter import*
def circle():
  global circle_win
  circle_win=Tk()
  circle_win.geometry("300x300")
  circle_win.title("Circle")
  area=Button(circle_win,text="Area",command=circle_area)
  area.grid(row=0,column=0)
  cp=Button(circle_win,text="Perimeter",command=circle_per)
  cp.grid(row=1,column=0)
  close=Button(circle_win, text="Close",command=close_circle)
  close.grid(row=2,column=0)
def circle_area():
  global c_a_w
  global r1
  c_a_w=Tk()
  c_a_w.geometry("500x300")
  c_a_w.title("Area")
  r=Label(c_a_w,text="R=")
  r.grid(row=0,column=0)
  r1=Entry(c_a_w,width=10)
  r1.grid(row=0,column=1)
  start=Button(c_a_w,text="Start",command=s_c_a_w)
  start.grid(row=1,column=0)
  close=Button(c_a_w,text="CLose",command=c_c_a_w)
  close.grid(row=1,column=1)
def s_c_a_w():
  r2=r1.get()
  r3=int(r2)
  ans=(r3**2)*3.14
  ans1=Label(c_a_w,text="The answer is: "+str(ans))
  ans1.grid(row=2,column=0)
def c_c_a_w():
  c_a_w.destroy()
def circle_per():
  global c_a_w
  global r1
  c_a_w=Tk()
  c_a_w.geometry("500x300")
  c_a_w.title("Perimeter")
  r=Label(c_a_w,text="R=")
  r.grid(row=0,column=0)
  r1=Entry(c_a_w,width=10)
  r1.grid(row=0,column=1)
  start=Button(c_a_w,text="Start",command=s_p_a_w)
  start.grid(row=1,column=0)
  close=Button(c_a_w,text="CLose",command=c_c_a_w)
  close.grid(row=1,column=1)
def s_p_a_w():
  r2=r1.get()
  r3=int(r2)
  ans=(r3*2)*3.14
  ans1=Label(c_a_w,text="The answer is: "+str(ans))
  ans1.grid(row=2,column=0)
def close_circle():
  circle_win.destroy()