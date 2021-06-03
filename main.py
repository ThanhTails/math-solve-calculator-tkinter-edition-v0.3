from tkinter import*
from math import *
import triangle
import square
import circle
import dimwin
import plus
import minus
import multi
import divide
import equation1
import equation2
import double
#algebra window

def algebra_win():
  global al_main
  al_main=Tk()
  al_main.title("Algebra")
  al_lab=Label(al_main,text="Algebra",font=("arial",20,"bold"))
  plus=Button(al_main,text="Plus",fg="yellow",bg="red",command=plus_win1)#plus button
  plus.pack()
  minus=Button(al_main,text="Minus",fg="yellow",bg="red",command=minus_win1)#minus button
  minus.pack()
  mul=Button(al_main,text="Multi",fg="yellow",bg="red",command=multi_win1)#multiple button
  mul.pack()
  div=Button(al_main,text="Divide",fg="yellow",bg="red",command=div_win1)
  div.pack()#divide button
  double=Button(al_main,text="Double",fg="yellow",bg="red",command=double_win1)
  double.pack()#double button
  equation_t1=Button(al_main,text="Equation type 1",fg="yellow",bg="red",command=eq11)#equation type 1 button
  equation_t1.pack()
  equation_t2=Button(al_main,text="Equation type 2",fg="yellow",bg="red",command=eq21)#equation type 2 button
  equation_t2.pack()
  dim=Button(al_main,text="Div and mod",command=dim_win1,fg="yellow",bg="red")
  dim.pack()# div mod button
  back=Button(al_main,text="Back",fg="yellow",bg="red",command=close_al)#back to mainh
  back.pack()
def close_al():
  al_main.destroy()

def plus_win1():#plus
  plus.plus_win()
def minus_win1():
  minus.minus_win()

def multi_win1():#multiple
  multi.multi_win()
def div_win1():#divide
  divide.div_win()

def double_win1():#double
  double.double_win()

def eq11():#equation 1
  equation1.eq1()
def eq21():#equation 2
  equation2.eq2()
def dim_win1():#div and mod
  dimwin.dim_win()


  

#geometry Window
def geometry_w():
  global geometry_win
  geometry_win=Tk()
  l=Label(geometry_win,text="Geometry")
  l.pack()
  triangle=Button(geometry_win,text="Triangle",fg="yellow",bg="blue",command=triangle_w1)
  triangle.pack()
  circlek=Button(geometry_win,text="Circle",fg="yellow",bg="blue",command=circles)
  circlek.pack()
  squarek=Button(geometry_win,text="Square",fg="yellow",bg="blue",command=squares)
  squarek.pack()
  close=Button(geometry_win,text="close",command=gd_close)
  close.pack()
  
def gd_close():
  geometry_win.destroy()

def triangle_w1():#triangle
  triangle.triangle_w()


#square
def squares():#square
  square.squarex()
  


def circles():#circle
  circle.circle()




def break_on():
  main.destroy()
#main window
def main_win():#the main engine
  global main
  main=Tk()
  lab=Label(main,text="Welcome to math solve calculator v0.1",font=("Arial",20,"bold"))
  lab.pack()
  lab_choose_type=Label(main,text="Please choose type of math")
  lab_choose_type.pack()
  #algebra button
  algebra=Button(main,text="Algebra",fg="yellow",bg="red",command=algebra_win)
  algebra.pack()
  
  #geometry button
  geometry=Button(main,text="Geometry",fg="yellow",bg="red",command=geometry_w)
  geometry.pack()

  #analysis button
  analysis=Button(main,text="Analysis(exit)",fg="yellow",bg="red",command=break_on)
  analysis.pack()
  #credits
  credits=Label(main,text="By ThanhTails")
  credits.pack()

  
main_win()
main.mainloop()

#Notes
print("if you fork, you can advertise me if you want.")
