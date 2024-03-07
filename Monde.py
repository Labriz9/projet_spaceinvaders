from Joueur import *
from Alien import *
from Protection import *
from Projectile import *


#caractéristiques projectiles aliens
pa_h=20
pa_w=5

#caractéristiques projectiles joueur
pj_h=20
pj_w=5

#images

#im2 = PhotoImage(file = 'alien_type_1.gif', master=root)
#id = canvas.create_image(15, 15, image = im1)

#Alien(100,100,30,30,1,canvas,root)


class Monde:

    def __init__(self, canvas, root):
        self.j = Joueur(canvas)

        im1 = PhotoImage(file = 'alien_type_1.gif', master=root)
        canvas.create_image(100, 100, image = im1)

        #Creation aliens
        self.l_a=[] #liste des aliens
        a_w=30
        a_h=30
        for i in range(4):
            for j in range(11):
                a_xi=5+j*50 #adapter
                a_yi=(i+1)*50
                self.l_a.append(Alien(a_xi,a_yi,a_w,a_h, 1 if i < 2 else i,canvas,root,im1))
        
        #Creation protections
        self.l_prot=[] #liste des protections
        prot_xi=[200,340,60,480] #ajouter commentaires
        prot_yi=[450,450,450,450]
        prot_h=10
        prot_w=10
        dx=[0,10,40,50,00,10,20,30,40,50,10,20,30,40,20,30]
        dy=[30,30,30,30,20,20,20,20,20,20,10,10,10,10,0,0]
        for i in range(len(prot_xi)): # itère sur le nombre de protection (les groupements de cubes)
            for j in range(len(dx)): # itère sur le nombre de cube par protection
                self.l_prot.append(Protection(prot_xi[i]+dx[j], prot_yi[i]+dy[j], prot_h, prot_w,canvas))
                
        self.l_pa = [] #liste des id projectiles aliens

        self.l_pj = [] #liste des id projectiles joueurs
        
        




      