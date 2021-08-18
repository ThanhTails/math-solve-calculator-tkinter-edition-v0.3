from tkinter import*
import square_all,square_round,rectangle_round,rectangle_all

def open_square_round():
  square_round.open_round_square()

def open_square_all():
  square_all.open_round_square()

def open_rect_round():
  rectangle_round.rect_round_open()

def open_rect_all():
  rectangle_all.main_window()

def qui():
  box_main.destroy()

def box_win():
  global box_main
  box_main=Tk()
  box_main.geometry("500x500")
  box_main.title("Box")
  sq_round=Button(box_main,text="Round square",bg="red",command=open_square_round)
  sq_round.grid(row=0,column=1)

  sq_all=Button(box_main,text="All aquare",bg="red",command=open_square_all)
  sq_all.grid(row=1,column=1)

  rect_round=Button(box_main,text="Round rectangle",bg="red",command=open_rect_round)
  rect_round.grid(row=2,column=1)

  rect_all=Button(box_main,text="All rectangle",bg="red",command=open_rect_all)
  rect_all.grid(row=3,column=1)

  q=Button(box_main,text="Back",bg="red",command=qui)
  q.grid(row=4,column=1)

