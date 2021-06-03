from tkinter import*
def squarex():
  global square_win
  square_win=Tk()
  square_win.geometry("400x400")
  square_win.title("Square")
  area=Button(square_win,text="Area",fg="yellow",bg="blue",command=square_a)
  area.grid(row=0,column=0)
  p=Button(square_win,text="Perimeter",fg="yellow",bg="blue",command=square_p)
  p.grid(row=1,column=0)
  clos=Button(square_win,text="Close",fg="yellow",bg="blue",command=close_square)
  clos.grid(row=2,column=0)
def square_a():
  global square_a_w
  global b
  square_a_w=Tk()
  square_a_w.title("Area")
  a=Label(square_a_w,text="Edge=")
  a.pack()
  b=Entry(square_a_w,width=20)
  b.pack()
  Start=Button(square_a_w,text="Start",command=start_area_square)
  Start.pack()
  cl=Button(square_a_w,text="Close",command=close_square_area)
  cl.pack()
def start_area_square():
  edge=b.get()
  edge1=int(edge)
  ans=edge1**2
  ans1=Label(square_a_w,text="The answer is: "+str(ans))
  ans1.pack()
def close_square_area():
  square_a_w.destroy()
def square_p():
  global square_a_w
  global b
  square_a_w=Tk()
  square_a_w.title("Area")
  a=Label(square_a_w,text="Edge=")
  a.pack()
  b=Entry(square_a_w,width=20)
  b.pack()
  Start=Button(square_a_w,text="Start",command=start_per_square)
  Start.pack()
  cl=Button(square_a_w,text="Close",command=close_square_area)
  cl.pack()
def start_per_square():
  edge=b.get()
  edge1=int(edge)
  ans=edge1*4
  ans1=Label(square_a_w,text="The answer is: "+str(ans))
  ans1.pack()
def close_square():
  square_win.destroy()
  