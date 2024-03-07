from tkinter import *
class Alien:
    def __init__(self,x,y,w,h,type,canvas,root,im):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.type=type # plusieurs types d'aliens
        if self.type == 1: #rouge
            color="red"
        elif self.type == 2: #violet
            color="magenta"
        elif self.type == 3: #bleu
            color="blue"
        self.id =  canvas.create_rectangle(
                        self.x, 
                        self.y, 
                        self.x + self.h, 
                        self.y + self.w, 
                        outline=color, fill=color)
        