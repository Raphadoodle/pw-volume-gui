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
    if volume < 100:
        currentvolume_int.set("  "+str(volume)+"  ")
    else:
        currentvolume_int.set(" "+str(volume)+" ")


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
    if volume < 100:
        currentvolume_int.set("  "+str(volume)+"  ")
    else:
        currentvolume_int.set(" "+str(volume)+" ")

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
    if volume < 100:
        currentvolume_int.set("  "+str(volume)+"  ")
    else:
        currentvolume_int.set(" "+str(volume)+" ")



win=Tk()
win.title("Volume")
header=Label(win, text="Volume", font=("Symbols Nerd Font Mono", 25, "bold")).grid(row=1, column="12")
currentvolume_int=StringVar()
mainfont=("Symbols Nerd Font Mono", 15)

volume_down=Button(win, text="-", font=mainfont, command=volumeDown).grid(row=2, column=10)
currentvolume=Label(win, textvariable=currentvolume_int, font=mainfont, bg="grey").grid(row=2, column=11)
volume_up=Button(win, text="+", font=mainfont, command=volumeUp).grid(row=2, column=12)


if start==0:
    getVolume()
    start=1

mainloop()
