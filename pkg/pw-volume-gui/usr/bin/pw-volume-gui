#!/usr/bin/python3
volume=None
start=0
from tkinter import *
from os import system
def roundUp(x):
    return round(x, -1)



def volumeUp():
    global currentvolume_int
    system("pw-volume change +5%")
    system("pw-volume status > ./.pwvolumegui")
    temp=open("./.pwvolumegui").read()
    i=14
    volume=""
    while temp[i] != ",":
        if temp[i] == ",":
            break
        volume=volume+temp[i]
        i+=1
    volume=int(volume)
    currentvolume_int.set(volume)

def volumeDown():
    global currentvolume_int
    system("pw-volume change -5%")
    system("pw-volume status > ./.pwvolumegui")
    temp=open("./.pwvolumegui").read()
    i=14
    volume=""
    while temp[i] != ",":
        if temp[i] == ",":
            break
        volume=volume+temp[i]
        i+=1
    volume=int(volume)
    currentvolume_int.set(volume)

def getVolume():
    global currentvolume_int
    system("pw-volume status > ./.pwvolumegui")
    temp=open("./.pwvolumegui").read()
    i=14
    volume=""
    while temp[i] != ",":
        if temp[i] == ",":
            break
        volume=volume+temp[i]
        i+=1
    volume=int(volume)
    volume=roundUp(volume)
    currentvolume_int.set(volume)


win=Tk()
win.title("Volume")
header=Label(win, text="Volume", font=("Symbols Nerd Font Mono", 25, "bold")).pack()
currentvolume_int=StringVar()
mainfont=("Symbols Nerd Font Mono", 15)
volume_down=Button(win, text="-", font=mainfont, command=volumeDown).pack()
currentvolume=Label(win, textvariable=currentvolume_int, font=mainfont, bg="grey").pack()
volume_up=Button(win, text="+", font=mainfont, command=volumeUp).pack()



if start==0:
    getVolume()
    start=1

mainloop()
