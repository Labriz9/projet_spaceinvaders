class Joueur:
    def __init__(self,canvas):
        self.x=285
        self.y=530
        self.w=30
        self.h=30
        self.vies=3 # les vies
        self.score=0 # le score
        self.id =  canvas.create_rectangle(
                        self.x, 
                        self.y, 
                        self.x + self.h, 
                        self.y + self.w, 
                        outline="gray", fill="gray")
        self.tir=0
        