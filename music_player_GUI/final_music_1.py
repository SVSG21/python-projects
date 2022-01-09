import os
import pygame
import random
from pygame.mixer import stop, unpause
from tkinter import *
from pygame import *
from pygame.event import *
from tkinter import filedialog
#Note:hold CTRL+mouse to see documentation for method
#from demo import pausesong, playsong
root=Tk()
root.config(bg='#0B3066')
#creating frames
f1=Frame(root,height=120,width=120)#,highlightbackground='red',highlightthickness=5)-to display the borders of frame 
f2=Frame(root,height=20,width=50)#,highlightbackground='green',highlightthickness=8)-to display the borders of frame 
f1.config(bg='#0B3066')
f2.config(bg='#0B3066')
f1.grid(row=0,column=0,padx=200,pady=100)
# f2.grid(row=1,column=0,padx=600,pady=0)
f2.place(x=300,y=400)
#f1.pack()
def play_song():
    current_song=songs_list.get(ANCHOR)
    current_song=f'/home/gaurav/Music/{current_song}.mp3'
    mixer.music.load(current_song)
    mixer.music.play()
    songs_list.after(1000,check_if_finished) #callng function after 1000 milli seconds
    
    

def pause_song():
    mixer.music.pause()

def resume_song():
    mixer.music.unpause()

def stop_song():
    mixer.music.stop()
def loop():
    return True    
def next_song():
    s=songs_list.index(ACTIVE) #we can also use curselection()
    l=songs_list.size()
    if(s<l):
        songs_list.selection_clear(s) #to clear selection from start to end without disturbing current one(color highlighter)
        s+=1
        songs_list.activate(s)#to activate the index--it will just update the index to next index if not empty
        songs_list.selection_set(s)  #to set selection from start to end without disturbing current one(color highlighter)
        songs_list.selection_anchor(s)#it will set anchor to the given index -Generally we will play song which has anchor to it
        play_song()
            
    print(s) #to print the index of song for the sake if you need it.

def prev_song():
    s=songs_list.index(ACTIVE)
    l=songs_list.size()
    if(l>0):
        songs_list.selection_clear(s) #to clear selection from start to end without disturbing current one(color highlighter)
        s-=1
        songs_list.activate(s)#to activate the index--it will just update the index to next index if not empty
        songs_list.selection_set(s)  #to set selection from start to end without disturbing current one(color highlighter)
        songs_list.selection_anchor(s)#it will set anchor to the given index -Generally we will play song which has anchor to it
        play_song()
    else:
        play_song()
    print(s)#just to print the index for the sake of programmer

def check_if_finished():
    if( pygame.mixer.music.get_busy()==True or pause_song()==True):
        songs_list.after(1000,check_if_finished)
    else:
        # print(pygame.mixer.music.get_busy())
        print("song completed")
        next_song()
def backgrnd():
    hexadecimall = ["#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])]
    if(hexadecimall!='#00000'):
        root.config(bg=hexadecimall)
        root.after(50000,backgrnd)
        f1.config(bg=hexadecimall)
        f2.config(bg=hexadecimall)
        songs_list.config(bg=hexadecimall)

        
    else:
        backgrnd()
    
mixer.init();

imggg=PhotoImage(file="/home/gaurav/Downloads/bg.png")  #to load the image
imggg=imggg.subsample(23)  #size  of image  here height is in reverse i.e;(eg:1>21)
# or we can use zoom(50,....etc) here height of image in normal way i.e; (eg:21>1)  
Label(f1,image=imggg).grid(row=0,column=1,padx=12)  # to print constant text we use Label actually

img1=PhotoImage(file="play_music_2_renewed.png")
img2=PhotoImage(file="pause_music_2.png")
img3=PhotoImage(file="previous_song_2.png")
img4=PhotoImage(file="next_song_2.png")
img5=PhotoImage(file="stop button.png")
img6=PhotoImage(file="resume_button.png")
# img7=PhotoImage(file="repeat.png")
img7=PhotoImage(file="color-wheel.png")
img7=img7.subsample(8)  #to resize image

songs_list=Listbox(f1,bg='white',fg='black',selectbackground="#FF6A3D",selectforeground="white",selectmode=SINGLE,font=('impact',18),width=60,justify=CENTER)
songs_list.grid(row=0,column=6)
# songs=filedialog.askopenfilenames(initialdir='music',defaultextension=".mp3",filetypes=(("mp3 music files","*mp3"),))
# songs=filedialog.askopenfiles(initialdir='music',defaultextension=".mp3",filetypes=(("mp3 music files","*mp3"),))
#scroll bar
scroll_bar=Scrollbar(f1,orient=VERTICAL,command=songs_list.yview)
songs_list.configure(yscrollcommand=scroll_bar.set)
scroll_bar.grid(row=0,column=7,sticky=NS)# to stick scroll bar in North and South direction

folder=filedialog.askdirectory(initialdir='Music')
os.chdir(folder)
songs=os.listdir()
for s in songs:
    s=s.replace('/home/gaurav/Music','')
    # s=s.replace('[iSongs.info]','')
    s=s.replace('.mp3','')
    songs_list.insert(END,s)
#get_songs=Button(root,text="import songs",command=import_songs)
play_btn=Button(f2,image=img1,command=play_song,border=0)
pause_btn=Button(f2,image=img2,command=pause_song,border=0)
resume_btn=Button(f2,image=img6,command=resume_song,border=0)
stop_btn=Button(f2,image=img5,command=stop_song,border=0)
next_btn=Button(f2,image=img4,command=next_song,border=0)
previous_btn=Button(f2,image=img3,command=prev_song,border=0)
loop_btn=Button(f2,image=img7,command=backgrnd,border=0)

play_btn.grid(row=1,column=3,padx=25,pady=15)
pause_btn.grid(row=1,column=4,padx=25,pady=15)
resume_btn.grid(row=1,column=5,padx=25,pady=15)
stop_btn.grid(row=1,column=6,padx=25,pady=15)
next_btn.grid(row=1,column=7,padx=25,pady=15)
previous_btn.grid(row=1,column=2,padx=25,pady=15)
loop_btn.grid(row=1,column=8,padx=25,pady=15)
root.mainloop()
#credits:
#color picker icon:<div>Icons made by <a href="https://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>

