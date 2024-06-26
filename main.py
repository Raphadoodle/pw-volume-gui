#!/usr/bin/python3
volume=None
start=0
from tkinter import *
from os import system, remove
from os.path import isdir
from getpass import getuser
from sys import path

def roundUp(x):
    return round(x, -1)

geo="200x120"
muted=0
beforemute=0


autogenconf = """
#Autogenerated pw-volume-gui config file.

default=("Courier New", 25, "bold")



header_config = {"fg":"black", "bg":"white", "afg":None, "abg":None}

volume_button_config = {"bg":"white", "fg":"black", "afg":None, "abg":None}
current_volume_label_config = {"bg":"grey", "fg":"white", "afg":None, "abg":None}
mute_button_config = {"bg":"white", "fg":"black", "afg":None, "abg":None}



"""

confdir = f"/home/{getuser()}/.config/pw-volume-gui"
if isdir(confdir):
    path.append(confdir)
else:
    system(f"mkdir {confdir}")
    system(f"touch {confdir}/config.py")
    f=open(f"{confdir}/config.py", "w")
    f.write(autogenconf)
    f.close()
    path.append(confdir)



from config import *


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

volume_down=Button(win, text="-", bg=volume_button_config["bg"], fg=volume_button_config["fg"], font=mainfont, command=volumeDown).grid(row=2, column=80)
currentvolume=Label(win, textvariable=currentvolume_int, font=mainfont, bg=current_volume_label_config["bg"], fg=current_volume_label_config["fg"]).grid(row=2, column=81)
volume_up=Button(win, text="+", bg=volume_button_config["bg"], fg=volume_button_config["fg"], font=mainfont, command=volumeUp).grid(row=2, column=82)
mute=Button(win, text="Mute", font=mainfont, command=volumeMute, bg=mute_button_config["bg"], fg=mute_button_config["fg"])
mute.grid(row=3, column=81)

if start==0:
    getVolume()
    start=1

mainloop()
