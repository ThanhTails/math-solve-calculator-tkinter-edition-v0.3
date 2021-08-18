from tkinter import*
def para_win():
  global para_main
  para_main=Tk()
  para_main.geometry("500x500")
  para_main.title("Perimeter")
  area=Button(para_main,text="Area",fg="red",command=para_area)
  area.grid(row=0,column=0)
  per=Button(para_main,text="Perimeter",fg="red",command=para_per)
  per.grid(row=1,column=0)
  close=Button(para_main,text="CLose",command=para_close)
  close.grid(row=2,column=0)

def para_close():
  para_main.destroy()
def para_area():
  global para_col_win
  global width,height
  para_col_win=Tk()
  para_col_win.geometry("500x500")
  para_col_win.title("Area")
  width1=Label(para_col_win,text="Width=")
  width1.grid(row=0,column=0)
  width=Entry(para_col_win,width=30)
  width.grid(row=0,column=1)
  height1=Label(para_col_win,text="Height=")
  height1.grid(row=1,column=0)
  height=Entry(para_col_win,width=30)
  height.grid(row=1,column=1)
  start=Button(para_col_win,text="Start",command=start_area)
  start.grid(row=2,column=0)
  close=Button(para_col_win,text="Close",command=close_para)
  close.grid(row=3,column=0)
def start_area():
  width2=width.get()
  height2=height.get()
  width3=int(width2)
  height3=int(height2)
  ans=str(width3*height3)
  ans1=Label(para_col_win,text="The answer is: "+ans)
  ans1.grid(row=4,column=0)
def close_para():
  para_col_win.destroy()
def para_per():
  global para_col_win
  global a,b
  para_col_win=Tk()
  para_col_win.geometry("500x500")
  para_col_win.title("Perimeter")
  a1=Label(para_col_win,text="A=")
  a1.grid(row=0,column=0)
  a=Entry(para_col_win,width=30)
  a.grid(row=0,column=1)
  b1=Label(para_col_win,text="B=")
  b1.grid(row=1,column=0)
  b=Entry(para_col_win,width=30)
  b.grid(row=1,column=1)
  start=Button(para_col_win,text="Start",command=start_per)
  start.grid(row=2,column=0)
  close=Button(para_col_win,text="Close",command=close_para)
  close.grid(row=3,column=0)
def start_per():
  a2=a.get()
  b2=b.get()
  a3=int(a2)
  b3=int(b2)
  ans=str((a3+b3)*2)
  ans1=Label(para_col_win,text="The answer is: "+ans)
  ans1.grid(row=4,column=0)
