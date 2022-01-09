import pywhatkit
from tkinter import *
root=Tk()  #creating root window
root.title("whatsapp message sender")
root.config(bg='#899420',padx=100,pady=50)
def send_msg():
    num=e1.get()   #return type is string
    msg=e2.get()
    htime=val1.get()
    mtime=val2.get()#return type is int as given IntVar()
    wtime=val3.get() #you can avoid this 
    pywhatkit.sendwhatmsg(num,msg,htime,mtime,wtime)

l1=Label(root,text="Enter the phone number:",fg="white",bg='#899420',font=("Times", "24", "bold italic"))
e1=Entry(root,width=25,fg='black',bg='#568C78',font=("Times",24,'bold'))
l2=Label(root,text="Enter the message:",fg="white",bg='#899420',font=("Times", "24", "bold italic"))
e2=Entry(root,width=25,fg='black',bg='#568C78',font=("Times",24,'bold'))

val1=IntVar()
val2=IntVar()
val3=IntVar()

l3=Label(root,text="select time in hours:",fg="white",bg='#899420',font=("Times", "24", "bold italic"))
s1=Spinbox(root,from_=0,to=24,textvariable=val1,width=12,fg="black",bg='#568C78',font=("Times",14))

l4=Label(root,text="select time in minutes:",fg="white",bg='#899420',font=("Times", "24", "bold italic"))
s2=Spinbox(root,from_=0,to=59,textvariable=val2,width=12,fg="black",bg='#568C78',font=("Times",14))

l5=Label(root,text="select waiting time in minutes:",fg="white",bg='#899420',font=("Times", "24", "bold italic"))
s3=Spinbox(root,from_=15,to=20,textvariable=val3,width=12,fg="black",bg='#568C78',font=("Times",14))
b1=Button(root,text="submit",bg='white',fg="black",activebackground='blue',activeforeground='white',font=("Times", "14", "bold italic"),command=send_msg)


l1.grid(row=0,column=1)
e1.grid(row=0,column=2)
l2.grid(row=1,column=1)
e2.grid(row=1,column=2)
l3.grid(row=2,column=1)
s1.grid(row=2,column=2)
l4.grid(row=3,column=1)
s2.grid(row=3,column=2)
l5.grid(row=4,column=1)
s3.grid(row=4,column=2)
b1.grid(row=6,column=2)
root.mainloop()