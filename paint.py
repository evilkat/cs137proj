""""Paint program by Dave Michell.

Subject: tkinter "paint" example
From: Dave Mitchell <davem@magnet.com>
To: python-list@cwi.nl
Date: Fri, 23 Jan 1998 12:18:05 -0500 (EST)

  Not too long ago (last week maybe?) someone posted a request
for an example of a paint program using Tkinter. Try as I might
I can't seem to find it in the archive, so i'll just post mine
here and hope that the person who requested it sees this!

  All this does is put up a canvas and draw a smooth black line
whenever you have the mouse button down, but hopefully it will
be enough to start with.. It would be easy enough to add some
options like other shapes or colors...

                                                yours,
                                                dave mitchell
                                                davem@magnet.com


paint.py: not exactly a paint program.. just a smooth line drawing demo."""


from tkinter import *
from PIL import Image
import subprocess
import os
import numpy as np
import time

b1 = "up"
xold, yold = None, None
root = Tk()
root.geometry("600x600")
    
def get_name(frame):
    frame.pack_forget()
    frame2 = PanedWindow(bg="yellow",orient=VERTICAL)
    label_name = Label(frame2,text="Enter Name")
    name = Entry(frame2,bd=5)
    enter = Button(root,text="Submit",command=lambda: main_drawing(frame2,name.get()))
    frame2.add(label_name)
    frame2.add(name)
    frame2.add(enter)
    frame2.pack(fill=BOTH)
    mainloop()

def main():
    frame = PanedWindow(bg="yellow",orient=VERTICAL)
    title = Label(text="Draw my Thing")
    start = Button(frame, text="Start",command= lambda: get_name(frame))
    exit = Button(frame, text="Exit", command = lambda: root.destroy())
    frame.add(title)
    frame.add(start)
    frame.add(exit)
    frame.pack(fill=BOTH)
    mainloop()

def show(img_array):
    convert_image = Image.fromarray(img_array)
    #print(type(convert_image))
    #convert_image.show()
    convert_image.save('sample2.jpg')

def send_drawing(drawing):
    print(type(drawing))
    drawing.postscript(file="sample.eps",colormode='color',width=600,height=600,pagewidth=499,pageheight=499)
    im = Image.open("sample.eps")
    im.thumbnail((500,500),Image.ANTIALIAS)
    im.save('sample.jpg')

    ima = Image.open('sample.jpg')
    print(ima)
    im2arr = np.array(ima)
    print(im2arr)
    show(im2arr)
    
def main_drawing(frame,name):
    frame.pack_forget()
    player_name=Label(root,text="Hello! "+name,justify="center")
    word = Label(root, text="Toy Car",justify="center",bg="yellow",fg="black")
    player_name.pack(side="top")
    word.pack(side="top")
    timer = Label(root,text="120",justify="center")
    timer.pack(side="top") 
   
 


    #drawing area of the canvas
    drawing_area = Canvas(root,width=500,height=500)
    drawing_area.pack(expand=YES,fill=BOTH)
    submit = Button(text="Submit", command = lambda: send_drawing(drawing_area))
    submit.pack(side="bottom")
    
    drawing_area.bind("<Motion>", motion)
    drawing_area.bind("<ButtonPress-1>", b1down)
    drawing_area.bind("<ButtonRelease-1>", b1up)

    root.mainloop()

def b1down(event):
    global b1
    b1 = "down"           # you only want to draw when the button is down
                          # because "Motion" events happen -all the time-

def b1up(event):
    global b1, xold, yold
    b1 = "up"
    xold = None           # reset the line when you let go of the button
    yold = None

def motion(event):
    if b1 == "down":
        global xold, yold
        if xold is not None and yold is not None:
            event.widget.create_line(xold,yold,event.x,event.y,smooth=TRUE)
                          # here's where you draw it. smooth. neat.
        xold = event.x
        yold = event.y

if __name__ == "__main__":
    main()
