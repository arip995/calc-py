from tkinter import *
w=Tk()
v=StringVar()
expr=""
def btnclk(n):
    global expr
    expr=expr+str(n)
    v.set(expr)
def calculate():
    global expr
    result=eval(expr)
    v.set(result)
def clear():
    global expr
    expr=""
    v.set(expr)
E=Entry(w,font=("arial",20,"bold"),textvariable=v,justify="right")
B1=Button(w,text="1",font=("arial",20,"bold"),\
          command=lambda:btnclk(1))
B2=Button(w,text="2",font=("arial",20,"bold"),command=lambda:btnclk(2))
B3=Button(w,text="3",font=("arial",20,"bold"),command=lambda:btnclk(3))
B4=Button(w,text="4",font=("arial",20,"bold"),command=lambda:btnclk(4))
B5=Button(w,text="5",font=("arial",20,"bold"),command=lambda:btnclk(5))
B6=Button(w,text="6",font=("arial",20,"bold"),command=lambda:btnclk(6))
B7=Button(w,text="7",font=("arial",20,"bold"),command=lambda:btnclk(7))
B8=Button(w,text="8",font=("arial",20,"bold"),command=lambda:btnclk(8))
B9=Button(w,text="9",font=("arial",20,"bold"),command=lambda:btnclk(9))
B0=Button(w,text="0",font=("arial",20,"bold"),command=lambda:btnclk(0))
Bequal=Button(w,text="=",font=("arial",20,"bold"),command=lambda:calculate())
Bclear=Button(w,text="C",font=("arial",20,"bold"),command=lambda:clear())
Bplus=Button(w,text="+",font=("arial",20,"bold"),command=lambda:btnclk('+'))
Bminus=Button(w,text="-",font=("arial",20,"bold"),command=lambda:btnclk('-'))
Bmul=Button(w,text="*",font=("arial",20,"bold"),command=lambda:btnclk('*'))
Bdiv=Button(w,text="/",font=("arial",20,"bold"),command=lambda:btnclk('/'))
#####################################################################
E.grid(row=1,column=1,columnspan=4)
B1.grid(row=2,column=1)
B2.grid(row=2,column=2)
B3.grid(row=2,column=3)
B4.grid(row=2,column=4)
############################
B5.grid(row=3,column=1)
B6.grid(row=3,column=2)
B7.grid(row=3,column=3)
B8.grid(row=3,column=4)
##################
B9.grid(row=4,column=1)
B0.grid(row=4,column=2)
Bequal.grid(row=4,column=3)
Bclear.grid(row=4,column=4)
###############3
Bplus.grid(row=5,column=1)
Bminus.grid(row=5,column=2)
Bmul.grid(row=5,column=3)
Bdiv.grid(row=5,column=4)



w.mainloop()
