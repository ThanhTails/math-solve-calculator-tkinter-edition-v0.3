from tkinter import*
def divi_win():
  global divi_main
  divi_main=Tk()
  divi_main.geometry("100x300")
  divi_main.title("Fraction")
  plus=Button(divi_main,text="Plus",fg="violet",command=divi_plus)
  plus.grid(row=0,column=0)
  minus=Button(divi_main,text="Minus",fg="violet",command=divi_min)
  minus.grid(row=1,column=0)
  mul=Button(divi_main,text="Multiple",fg="violet",command=divi_mul)
  mul.grid(row=2,column=0)
  div=Button(divi_main,text="Divide",fg="violet",command=divi_div)
  div.grid(row=3,column=0)
  cl=Button(divi_main,text="CLose",fg="violet",command=main_close)
  cl.grid(row=4,column=0)
def divi_plus():
  global divi_pw,a,b,c,d
  divi_pw=Tk()
  divi_pw.geometry("500x500")
  a=Entry(divi_pw,width=10)
  a.grid(row=0,column=0)
  cross1=Label(divi_pw,text="---------")
  cross1.grid(row=1,column=0)
  b=Entry(divi_pw,width=10)
  b.grid(row=2,column=0)
  pl=Label(divi_pw,text="+")
  pl.grid(row=1,column=1)
  c=Entry(divi_pw,width=10)
  c.grid(row=0,column=2)
  cross2=Label(divi_pw,text="---------")
  cross2.grid(row=1,column=2)
  d=Entry(divi_pw,width=10)
  d.grid(row=2,column=2)
  equal=Label(divi_pw,text="=")
  equal.grid(row=1,column=3)
  start=Button(divi_pw,text="Start",command=start_p)
  start.grid(row=4,column=0)
  clo=Button(divi_pw,text="Close",command=close)
  clo.grid(row=5,column=0)
def start_p():
  a1=a.get()
  b1=b.get()
  c1=c.get()
  d1=d.get()
  a2=int(a1)
  b2=int(b1)
  c2=int(c1)
  d2=int(d1)
  if b2==d2:
    ans=a2+c2
    if ans==b2:
      ans1=Label(divi_pw,text="1")
      ans1.grid(row=1,column=5)
    else:
      if ans%b2==0:
        ans1=ans/b2
        ans2=Label(divi_pw,text=str(ans1))
        ans2.grid(row=1,column=5)
      else:
        ans1=Label(divi_pw,text=str(ans))
        ans1.grid(row=0,column=5)
        cross3=Label(divi_pw,text="-------")
        cross3.grid(row=1,column=5)
        ans2=Label(divi_pw,text=str(b2))
        ans2.grid(row=2,column=5)
  else:
    e1=a2*d2
    e2=b2*c2
    e3=b2*d2
    e=e1+e2
    if e%e3==0:
      ans=e/e3
      ans1=Label(divi_pw,text=str(ans))
      ans1.grid(row=1,column=5)
    else:
      ans1=Label(divi_pw,text=str(e))
      ans1.grid(row=0,column=5)
      cross3=Label(divi_pw,text="-------")
      cross3.grid(row=1,column=5)
      ans2=Label(divi_pw,text=str(e3))
      ans2.grid(row=2,column=5)
def divi_min():
  global divi_pw,a,b,c,d
  divi_pw=Tk()
  divi_pw.geometry("500x500")
  a=Entry(divi_pw,width=10)
  a.grid(row=0,column=0)
  cross1=Label(divi_pw,text="---------")
  cross1.grid(row=1,column=0)
  b=Entry(divi_pw,width=10)
  b.grid(row=2,column=0)
  pl=Label(divi_pw,text="-")
  pl.grid(row=1,column=1)
  c=Entry(divi_pw,width=10)
  c.grid(row=0,column=2)
  cross2=Label(divi_pw,text="---------")
  cross2.grid(row=1,column=2)
  d=Entry(divi_pw,width=10)
  d.grid(row=2,column=2)
  equal=Label(divi_pw,text="=")
  equal.grid(row=1,column=3)
  start=Button(divi_pw,text="Start",command=start_m)
  start.grid(row=4,column=0)
  clo=Button(divi_pw,text="Close",command=close)
  clo.grid(row=5,column=0)
def start_m():
  a1=a.get()
  b1=b.get()
  c1=c.get()
  d1=d.get()
  a2=int(a1)
  b2=int(b1)
  c2=int(c1)
  d2=int(d1)
  if b2==d2:
    ans=a2-c2
    if ans==b2:
      ans1=Label(divi_pw,text="1")
      ans1.grid(row=1,column=5)
    else:
      if ans%b2==0:
        ans1=ans/b2
        ans2=Label(divi_pw,text=str(ans1))
        ans2.grid(row=1,column=5)
      else:
        ans1=Label(divi_pw,text=str(ans))
        ans.grid(row=0,column=5)
        cross3=Label(divi_pw,text="-------")
        cross3.grid(row=1,column=5)
        ans2=Label(divi_pw,text=str(b2))
        ans2.grid(row=2,column=5)
  else:
    e1=a2*d2
    e2=b2*c2
    e3=b2*d2
    e=e1-e2
    if e%e3==0:
      ans=e/e3
      ans1=Label(divi_pw,text=str(ans))
      ans1.grid(row=1,column=5)
    else:
      ans1=Label(divi_pw,text=str(e))
      ans1.grid(row=0,column=5)
      cross3=Label(divi_pw,text="-------")
      cross3.grid(row=1,column=5)
      ans2=Label(divi_pw,text=str(e3))
      ans2.grid(row=2,column=5)
def divi_mul():
  global divi_pw,a,b,c,d
  divi_pw=Tk()
  divi_pw.geometry("500x500")
  a=Entry(divi_pw,width=10)
  a.grid(row=0,column=0)
  cross1=Label(divi_pw,text="---------")
  cross1.grid(row=1,column=0)
  b=Entry(divi_pw,width=10)
  b.grid(row=2,column=0)
  pl=Label(divi_pw,text="x")
  pl.grid(row=1,column=1)
  c=Entry(divi_pw,width=10)
  c.grid(row=0,column=2)
  cross2=Label(divi_pw,text="---------")
  cross2.grid(row=1,column=2)
  d=Entry(divi_pw,width=10)
  d.grid(row=2,column=2)
  equal=Label(divi_pw,text="=")
  equal.grid(row=1,column=3)
  start=Button(divi_pw,text="Start",command=start_p)
  start.grid(row=4,column=0)
  clo=Button(divi_pw,text="Close",command=close)
  clo.grid(row=5,column=0)
def start_mu():
  a1=a.get()
  b1=b.get()
  c1=c.get()
  d1=d.get()
  a2=int(a1)
  b2=int(b1)
  c2=int(c1)
  d2=int(d1)
  if a2==d2:
    if b2==c2:
      ans=Label(divi_pw,text="1")
      ans.grid(row=1,column=5)
    else:
      if b2%c2==0:
        ans=b2/c2
        ans1=Label(divi_pw,text=ans)
        ans1.grid(row=1,column=5)
      else:
        ans1=Label(divi_pw,text=str(b2))
        ans1.grid(row=0,column=5)
        cross3=Label(divi_pw,text="-------")
        cross3.grid(row=1,column=5)
        ans2=Label(divi_pw,text=str(c2))
        ans2.grid(row=2,column=5)
  elif b2==c2:
    if a2==d2:
      ans=Label(divi_pw,text="1")
      ans.grid(row=1,column=5)
    else:
      if a2%c2==0:
        ans=a2/c2
        ans1=Label(divi_pw,text=ans)
        ans1.grid(row=1,column=5)
      else:
        ans1=Label(divi_pw,text=str(a2))
        ans1.grid(row=0,column=5)
        cross3=Label(divi_pw,text="-------")
        cross3.grid(row=1,column=5)
        ans2=Label(divi_pw,text=str(d2))
        ans2.grid(row=2,column=5)
  else:
    e1=a2*b2
    e2=c2*d2
    ans1=Label(divi_pw,text=str(e1))
    ans1.grid(row=0,column=5)
    cross3=Label(divi_pw,text="-------")
    cross3.grid(row=1,column=5)
    ans2=Label(divi_pw,text=str(e2))
    ans2.grid(row=2,column=5)
def divi_div():
  global divi_pw,a,b,c,d
  divi_pw=Tk()
  divi_pw.geometry("500x500")
  a=Entry(divi_pw,width=10)
  a.grid(row=0,column=0)
  cross1=Label(divi_pw,text="--------")
  cross1.grid(row=1,column=0)
  b=Entry(divi_pw,width=10)
  b.grid(row=2,column=0)
  pl=Label(divi_pw,text=":")
  pl.grid(row=1,column=1)
  c=Entry(divi_pw,width=10)
  c.grid(row=0,column=2)
  cross2=Label(divi_pw,text="--------")
  cross2.grid(row=1,column=2)
  d=Entry(divi_pw,width=10)
  d.grid(row=2,column=2)
  equal=Label(divi_pw,text="=")
  equal.grid(row=1,column=3)
  start=Button(divi_pw,text="Start",command=start_div)
  start.grid(row=4,column=0)
  clo=Button(divi_pw,text="Close",command=close)
  clo.grid(row=5,column=0)
def start_div():
  a1=a.get()
  b1=b.get()
  c1=c.get()
  d1=d.get()
  a2=int(a1)
  b2=int(b1)
  c2=int(c1)
  d2=int(d1)
  if a2==c2:
    if b2==d2:
      ans=Label(divi_pw,text="1")
      ans.grid(row=1,column=5)
    else:
      if b2%d2==0:
        ans=b2/d2
        ans1=Label(divi_pw,text=ans)
        ans1.grid(row=1,column=5)
      else:
        ans1=Label(divi_pw,text=str(b2))
        ans1.grid(row=0,column=5)
        cross3=Label(divi_pw,text="-------")
        cross3.grid(row=1,column=5)
        ans2=Label(divi_pw,text=str(d2))
        ans2.grid(row=2,column=5)
  elif b2==d2:
    if a2==c2:
      ans=Label(divi_pw,text="1")
      ans.grid(row=1,column=5)
    else:
      if a2%c2==0:
        ans=a2/c2
        ans1=Label(divi_pw,text=ans)
        ans1.grid(row=1,column=5)
      else:
        ans1=Label(divi_pw,text=str(a2))
        ans1.grid(row=0,column=5)
        cross3=Label(divi_pw,text="-------")
        cross3.grid(row=1,column=5)
        ans2=Label(divi_pw,text=str(c2))
        ans2.grid(row=2,column=5)
  else:
    e1=a2*b2
    e2=c2*d2
    ans1=Label(divi_pw,text=str(e1))
    ans.grid(row=0,column=5)
    cross3=Label(divi_pw,text="-------")
    cross3.grid(row=1,column=5)
    ans2=Label(divi_pw,text=str(e2))
    ans2.grid(row=2,column=5)





def close():
  divi_pw.destroy()
def main_close():
  divi_main.destroy()


  
