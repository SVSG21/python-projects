import datetime as dt
import time
from tkinter import *    
#print(dir(dt.datetime)) to get list of functions in datetime
root=Tk()
root.title="clock"
root.config(bg="white")
#creating frame
f=Frame(root,height=50,width=50)#,highlightbackground="red",highlightthickness=5,highlightcolor="blue",bg="white")-to display frame with border
f.pack(ipadx=50,ipady=50,padx=50,pady=50)
f.config(bg="white")
photo=PhotoImage(file='final_bg_clock.png')
photo=photo.subsample(2)
l=Label(f,image=photo,border=0)
def clock():
    curr_time=dt.datetime.now()
    # c_hour=(str)(curr_time.hour)
    # c_min=str(curr_time.minute)
    # c_sec=str(curr_time.second)
    # ------    or else we can use following-----------------
    c_hour=curr_time.strftime('%I')
    c_min=curr_time.strftime('%M')
    c_sec=curr_time.strftime('%S')

    l2.config(text=c_hour+":"+c_min+":"+c_sec)
    l2.after(1000,clock)#to call  function after 1 sec

l2=Label(f,text="")
l2.config(font=("Arial ",25),bg="#021344",fg="white")
l2.place(x=75,y=120)
l.grid(row=0,column=1,padx=12,pady=15)
clock()
root.mainloop()