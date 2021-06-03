from tkinter import*
def para_win():
  global para_main
  para_main=Tk()
  para_main.geometry("500x500")
  para_main.title("Perimeter")
  area=Button(para_main,text="Area",fg="red",command=para_area)
  area.grid(row=0,column=0)




def para_area():
  global para_col_win
  global width,height
  para_col_win=Tk()
  para_col_win.geometry("500x500")
  para_col_win.title("Area")
  width1=Label(para_col_win,text="Width=")
  width1.grod(row=0,column=0)
  width=Entry(para_col_win,width=30)
  width.grid(row=0,column=1)
  height1=Label(para_col_win,text="Width=")
  height1.grod(row=1,column=0)
  height=Entry(para_col_win,width=30)
  height.grid(row=1,column=1)
  start=Button(para_col_win,text="Start",command=start_area)
  start.grid(row=2,column=0)
  close=Button(para_col_win,text="Close",command=close_para)
  close.grid(row=3,column=0)
def start_area():
  width2=int(width)
  height2=int(height)
  ans=str(width2*height2)
  ans1=Label(para_col_win,text="The answer is: "+ans)
  ans1.grid(row=4,column=0)
def close_para():
  para_col_win.destroy()
