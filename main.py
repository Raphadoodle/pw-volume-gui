#!/usr/bin/python3
volume=None
start=0
from tkinter import *
from os import system
from os import remove
def roundUp(x):
    return round(x, -1)

geo="200x120"
muted=0
beforemute=0

def volumeUp():
    global currentvolume_int
    system("pw-volume change +5%")
    system("pw-volume status > ./.pwvolumeguitmp")
    temp=open("./.pwvolumeguitmp").read()
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
    remove("./.pwvolumeguitmp")

def volumeDown():
    global currentvolume_int
    system("pw-volume change -5%")
    system("pw-volume status > ./.pwvolumeguitmp")
    temp=open("./.pwvolumeguitmp").read()
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
    remove("./.pwvolumeguitmp")

def getVolume():
    global currentvolume_int
    system("pw-volume status > ./.pwvolumeguitmp")
    temp=open("./.pwvolumeguitmp").read()
    i=14
    volume=""
    while temp[i] != ",":
        if temp[i] == ",":
            break
        volume=volume+temp[i]
        i+=1
    volume=int(volume)
    system("pw-volume change -{}%".format(volume))
    volume=roundUp(volume)
    system("pw-volume change +{}%".format(volume))
    if volume < 100:
        currentvolume_int.set("  "+str(volume)+"  ")
    else:
        currentvolume_int.set(" "+str(volume)+" ")
    remove("./.pwvolumeguitmp")

def volumeMute():
    global muted
    global beforemute
    global mute
    if muted == 0:
        global currentvolume_int
        system("pw-volume change +5%")
        system("pw-volume status > ./.pwvolumeguitmp")
        temp=open("./.pwvolumeguitmp").read()
        i=14
        volume=""
        while temp[i] != ",":
            if temp[i] == ",":
                break
            volume=volume+temp[i]
            i+=1
        volume=int(volume)
        beforemute=volume-5
        system("pw-volume change -{}%".format(volume))
        currentvolume_int.set("  0  ")
        remove("./.pwvolumeguitmp")
        muted=1
        mute.config(text="Unmute")
    else:
        system("pw-volume change +{}%".format(beforemute))
        volume=beforemute
        if volume < 100:
            currentvolume_int.set("  "+str(volume)+"  ")
        else:
            currentvolume_int.set(" "+str(volume)+" ")
        beforemute=0
        muted=0
        mute.config(text="Mute")
        

    

win=Tk()
win.title("Volume")
win.geometry(geo)
header=Label(win, text="Volume", font=("Symbols Nerd Font Mono", 25, "bold")).grid(row=1, column=81)
currentvolume_int=StringVar()
mainfont=("Symbols Nerd Font Mono", 15)

volume_down=Button(win, text="-", font=mainfont, command=volumeDown).grid(row=2, column=80)
currentvolume=Label(win, textvariable=currentvolume_int, font=mainfont, bg="grey").grid(row=2, column=81)
volume_up=Button(win, text="+", font=mainfont, command=volumeUp).grid(row=2, column=82)
mute=Button(win, text="Mute", font=mainfont, command=volumeMute)
mute.grid(row=3, column=81)

if start==0:
    getVolume()
    start=1

mainloop()
