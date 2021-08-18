from tkinter import*
from math import*

def cal():
    a=leng_e.get()
    b=wid_e.get()
    h=he_e.get()
    length=int(a)
    width=int(b)
    height=int(h)

    ans=2*height*(width+height)
    answer=Label(main,text="The abswer is: "+str(ans))
    answer.grid(row=4,column=0)

def cl():
    main.destroy()

def rect_round_open():
    global main,leng_e,wid_e,he_e
    main=Tk()
    main.geometry("1000x500")

    leng_L=Label(main,text="Length= ")
    leng_L.grid(row=0,column=0)

    leng_e=Entry(main,width=20)
    leng_e.grid(row=0,column=1)

    wid_L=Label(main,text="Width= ")
    wid_L.grid(row=1,column=0)

    wid_e=Entry(main,width=20)
    wid_e.grid(row=1,column=1)

    he_L=Label(main,text="Height= ")
    he_L.grid(row=2,column=0)

    he_e=Entry(main,width=20)
    he_e.grid(row=2,column=1)

    st=Button(main,text="Start",bg="red",command=cal)
    st.grid(row=3,column=0)

    q=Button(main,text="Back",bg="red",command=cl)
    q.grid(row=8,column=0)
