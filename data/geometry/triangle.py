from tkinter import*
def triangle_w():
  global triangle_main
  triangle_main=Tk()
  triangle_main.title("Triangle")
  pytago=Button(triangle_main,text="Square",command=pytago_w,fg="green")
  pytago.pack()
  Normal_area=Button(triangle_main,text="Normal area",fg="green",command=triangle_normal)
  Normal_area.pack()
  Normal_per=Button(triangle_main,text="Normal Perimeter",fg="green",command=triangle_normal_per)
  Normal_per.pack()
  close=Button(triangle_main,text="Close",command=close_triangle_m)
  close.pack()
def close_triangle_m():
  triangle_main.destroy()

def pytago_w():
  global pytago_main
  global a1,b1,c1
  pytago_main=Tk()
  pytago_main.title("Square")
  pytago_main.geometry("600x400")
  note=Label(pytago_main,text="Choose your edge to calculate by write a choosen edge number 0")
  note.grid(row=0,column=0)
  a=Label(pytago_main,text="AB=")
  a.grid(row=1,column=0)
  a1=Entry(pytago_main,width=5)
  a1.grid(row=1,column=1)
  b=Label(pytago_main,text="AC=")
  b.grid(row=2,column=0)
  b1=Entry(pytago_main,width=5)
  b1.grid(row=2,column=1)
  c=Label(pytago_main,text="BC=")
  c.grid(row=3,column=0)
  c1=Entry(pytago_main,width=5)
  c1.grid(row=3,column=1)
  start=Button(pytago_main,text="Start",command=start_pytago)
  start.grid(row=4,column=0)
  close=Button(pytago_main,text="Close",command=close_win)
  close.grid(row=5,column=0)
def close_win():
  pytago_main.destroy()
def start_pytago():
  a2=a1.get()
  b2=b1.get()
  c2=c1.get()
  a3=int(a2)
  b3=int(b2)
  c3=int(c2)
  if a3==0:
    ans=sqrt((c3**2)-(b3**2))
    ans1=str(ans)
    ans2=Label(pytago_main,text="AB="+ans1)
    ans2.grid(row=5,column=0)
  elif b3==0:
    ans=sqrt((c3**2)-(a3**2))
    ans1=str(ans)
    ans2=Label(pytago_main,text="AC="+ans1)
    ans2.grid(row=5,column=0)
  elif c3==0:
    ans=sqrt((a3**2)+(b3**2))
    ans1=str(ans)
    ans2=Label(pytago_main,text="BC="+ans1)
    ans2.grid(row=5,column=0)
def triangle_normal():
  global pytago_main
  global Edge1,Height1
  pytago_main=Tk()
  pytago_main.title("Normal")
  pytago_main.geometry("700x400")
  lab=Label(pytago_main,text="Normal (area)")
  lab.grid(row=0,column=0)
  Edge=Label(pytago_main,text="Edge=")
  Edge.grid(row=1,column=0)
  Edge1=Entry(pytago_main,width=20)
  Edge1.grid(row=1,column=1)
  Height=Label(pytago_main,text="Height=")
  Height.grid(row=2,column=0)
  Height1=Entry(pytago_main,width=20)
  Height1.grid(row=2,column=1)
  But=Button(pytago_main,text="Start area",command=start_normal_area)
  But.grid(row=3,column=0)
  Close=Button(pytago_main,text="CLose",command=close_normal_area)
  Close.grid(row=4,column=0)
def start_normal_area():
  edge2=Edge1.get()
  height2=Height1.get()
  height3=int(height2)
  edge3=int(edge2)
  ans=(height3*edge3)/2
  ans1=Label(pytago_main,text="The answer is: "+str(ans))
  ans1.grid(row=4,column=0)
def close_normal_area():
  pytago_main.destroy()
def triangle_normal_per():
  global pytago_main
  global a,b,c
  pytago_main=Tk()
  pytago_main.title("Perimeter")
  pytago_main.geometry("700x400")
  lab=Label(pytago_main,text="Normal (perimeter)")
  lab.grid(row=0,column=0)
  a1=Label(pytago_main,text="a=")
  a1.grid(row=1,column=0)
  a=Entry(pytago_main,width=30)
  a.grid(row=1,column=1)
  b1=Label(pytago_main,text="b=")
  b1.grid(row=2,column=0)
  b=Entry(pytago_main,width=30)
  b.grid(row=2,column=1)
  c1=Label(pytago_main,text="c=")
  c1.grid(row=3,column=0)
  c=Entry(pytago_main,width=30)
  c.grid(row=3,column=1)
  But=Button(pytago_main,text="Start perimeter",command=start_normal_per)
  But.grid(row=4,column=0)
  Close=Button(pytago_main,text="CLose",command=close_normal_area)
  Close.grid(row=5,column=0)
def start_normal_per():
  a2=a.get()
  b2=b.get()
  c2=c.get()
  a3=int(a2)
  b3=int(b2)
  c3=int(c2)

  ans=a3+b3+c3
  ans1=Label(pytago_main,text="The answer is: "+str(ans))
  ans1.grid(row=6,column=0)
