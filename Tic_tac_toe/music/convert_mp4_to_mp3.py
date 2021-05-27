from tkinter import *
from moviepy.editor import *

#Functions
def convert():
    mp4_path = mp4.get()
    mp3_name = mp3.get()
    try:
        mp4Clip = AudioFileClip(mp4_path)
        # mp3Clip = mp4Clip.audio
        mp4Clip.write_audiofile(mp3_name)
        #mp3Clip.close()
        mp4Clip.close()
    except Exception as e:
        print(e)
        

#Main Screen
master = Tk()
master.title("Convert mp4 to mp3")

#Labels
Label(master, text="Convert mp4 to mp3", fg="red", font=("Calibri",15)).grid(sticky=N,padx=100,row=0)
Label(master,text="Please enter the path of your mp4 below : ", font=("Calibri",12)).grid(sticky=N,row=1,pady=15)
notif = Label(master,font=("Calibri",12))
notif.grid(sticky=N,pady=1,row=4)
#Vars
mp4 = StringVar()
#Entry
Entry(master,width=50,textvariable=mp4).grid(sticky=N,row=2)
mp3 = StringVar()
#Entry
Entry(master,width=50,textvariable=mp3).grid(sticky=N,row=3)
#Button
Button(master,width=20,text="Convert",font=("Calibri",12),command=convert).grid(sticky=N,row=3,pady=15)
master.mainloop()
