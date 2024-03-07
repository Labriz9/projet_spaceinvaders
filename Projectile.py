class Projectile:
    def __init__(self,x,y,w,h,canvas):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.id =  canvas.create_rectangle(
                        self.x, 
                        self.y, 
                        self.x + self.h, 
                        self.y + self.w, 
                        outline="white", fill="white")
        
    def collision(self,id2,canvas): #prend en arg l'id de l'objet de test de collision(id2) et le canvas
        xa1, ya1, xb1, yb1 = canvas.coords(self.id)  #2 quadruplets positions des 2 objets dont la collision est à tester
        xa2, ya2, xb2, yb2 = canvas.coords(id2)
        return (((xa2 <= xa1 <= xb2) and (ya2 <= ya1 <= yb2)) #coin haut gauche de 1 est dans 2
            or  ((xa2 <= xa1 <= xb2) and (ya2 <= yb1 <= yb2)) #coin bas gauche de 1 est dans 2
            or  ((xa2 <= xb1 <= xb2) and (ya2 <= ya1 <= yb2)) #coin haut droit de 1 est dans 2
            or  ((xa2 <= xb1 <= xb2) and (ya2 <= yb1 <= yb2)) #coin bas droit de 1 est dans 2
        )