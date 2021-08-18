from tkinter import*

def rectan_close():
  rectan_main.destroy()
def rectan_win():
  global rectan_main
  global width,length
  rectan_main=Tk()
  rectan_main.geometry("500x500")
  rectan_main.title("Area")
  width1=Label(rectan_main,text="Width=")
  width1.grid(row=0,column=0)
  width=Entry(rectan_main,width=30)
  width.grid(row=0,column=1)
  length1=Label(rectan_main,text="Height=")
  length1.grid(row=1,column=0)
  length=Entry(rectan_main,width=30)
  length.grid(row=1,column=1)
  area=Button(rectan_main,text="Area",fg="red",command=start_area)
  area.grid(row=2,column=0)
  per=Button(rectan_main,text="Perimeter",fg="red",command=start_per)
  per.grid(row=2,column=1)
  note=Label(rectan_main,text="Note: choose area or perimeter to calculate.",fg="red")
  note.grid(row=3,column=1)
  close=Button(rectan_main,text="Close",command=close_rectan)
  close.grid(row=3,column=0)
def start_area():
  width2=width.get()
  length2=length.get()
  width3=int(width2)
  length3=int(length2)
  ans=str(width3*length3)
  ans1=Label(rectan_main,text="The answer of area is: "+ans,fg="green")
  ans1.grid(row=4,column=0)
def close_rectan():
  rectan_main.destroy()


def start_per():
  width2=width.get()
  length2=length.get()
  width3=int(width2)
  length3=int(length2)
  ans=str((width3+length3)*2)
  ans1=Label(rectan_main,text="The answer of perimeter is: "+ans,fg="blue")
  ans1.grid(row=4,column=0)
