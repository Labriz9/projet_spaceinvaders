class Protection:
    def __init__(self,x,y,w,h,canvas):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.id=canvas.create_rectangle(
                self.x, 
                self.y, 
                self.x + self.h, 
                self.y + self.w, 
                outline="white", fill="white")
        

        