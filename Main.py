
#Header
"""
Que fait ce programme ? : c'est un jeu : space invaders
Qui l'a fait : Guillaume TRUONG - Maya AL FARRA
Quand a-t-il été réalisé ? : déc-jan 2022/2023

"""

# Importations nécessaires
from tkinter import *
from Monde import *
from random import *
from tkinter import messagebox

#création de la femêtre graphique
root = Tk()
root.title('Space Invader')

photo=PhotoImage(file= "background.png")
#dimension du canvas
canvas_width= 600
canvas_height= 600
canvas = Canvas(root, width=canvas_width, height=canvas_height)
item = canvas.create_image(0, 0, anchor=NW, image=photo)
print("Image de fond (item",item,")")

#Variables nécessaires
m=None
c1=0 #compteur de déplacement alien horizontal
c2=0 #compteur de déplacement alien vertical
dx=5 #déplacement selon x


#Fonctions nécessaires au programme
def Start():
    """
    rôle de la fonction: commencer le jeu
    entrées (s) : /
    sortie (s) : /
    """
    global m
    
    m = Monde(canvas,root)
    root.after(1000, Game_loop)
    
    

def End():
    """
    rôle de la fonction: fin du jeu sur commande
    entrées (s) : /
    sortie (s) : /
    """
    global m
    m.j.vies = 0 # condition de fin de jeu
    
    

def a_propos():
    """
    rôle de la fonction: donner des information sur le jeu
    entrées (s) : /
    sortie (s) : affichage d'un messagebox à propos du jeu
    """
    messagebox.showinfo('à propos', 'jeu créée par Guillaume et Maya :) \n Tuez les aliens pour gagner!')


# Créatioln du menu
menu = Menu(root)
menufichier = Menu(menu, tearoff=0)
menufichier.add_command(label="Quitter", command = root.destroy)
menufichier.add_command(label="jouer", command = Start)
menufichier.add_command(label="fin de partie", command = End)
menufichier.add_command(label="à propos", command = a_propos)
menu.add_cascade(label = "Menu", menu = menufichier)
root.config(menu = menu)

canvas.pack()



    

def Clear():  
    """
    rôle de la fonction: effacer le contenu canvas (vider les listes) à la fin d'une partie
    entrées (s) : /
    sortie (s) : /
    """
    global m
    if m.l_a == []:
        messagebox.showinfo('wooooow','Tu as gagné champion !!!!  \n score: '+ str(m.j.score)) # selon le résultat du jeu on affiche des messages différents

    else : 
        messagebox.showwarning('DEFAITE','Tu as perdu !!!!!  \n score:' + str(m.j.score))
                 

    #suppression des objets canvas
    for i_prot in range(len(m.l_prot)): #protections
        canvas.delete(m.l_prot[i_prot].id)        
    for i_a in range(len(m.l_a)): #aliens
        canvas.delete(m.l_a[i_a].id)  
    for i_pa in range(len(m.l_pa)): #projectiles aliens
        canvas.delete(m.l_pa[i_pa].id)  
    for i_pj in range(len(m.l_pj)): #projectiles joueurs
        canvas.delete(m.l_pj[i_pj].id)  
    canvas.delete(m.j.id)
    
    #reset des listes/score/vies
    m.l_prot=[] 
    m.l_a=[]
    m.l_pa=[] 
    m.l_pj=[]
    canvas.delete("score")
    canvas.delete("vies")
    




def Game_loop():
    """
    rôle de la fonction: fonctionnement du jeu
    entrées (s) : /
    sortie (s) : /
    """
    global c1,c2,dx,m

    (j_xa,j_ya,j_xb,j_yb)=canvas.coords(m.j.id) #coordonnées du joueur
    
    #listes d'objets à détruire après les boucles (pour ne pas modifier les listes avant la fin des boucles)
    remove_list_a = [] 
    remove_list_prot = []
    remove_list_pa = []
    remove_list_pj = []


    #affichage du score et des vies 
    root.score = canvas.create_text(50, 30, text="Score : " + str(m.j.score), fill= 'white', font = "Arial", tag="score")
    root.vies = canvas.create_text(45, 50, text="Vies : " + str(m.j.vies),  fill= 'white', font = "Arial", tag="vies")
        
    
    #déplacement ennemis (compteurs c1:horizontal, c2:vertical)
    c1 += 1 #vitesse des aliens
    if c1 >= 10 : 
        c2 += 1
        if c2 >= 13 :
            dx *= -1 #change direction déplacement horizontale
            for alien in m.l_a:
                canvas.move(alien.id, 0, 10)
                if canvas.coords(alien.id)[3] >= 450 :#si les aliens arrivent au niveau du joueur = fin de partie
                    m.j.vies = 0
                    break
                
            c2=0
        else : #sinon décente d'un niveau
            for alien in m.l_a:
                canvas.move(alien.id, dx, 0)
        c1=0
        
        
    #tirs ennemis
    for alien in m.l_a:
        r1000 = randint(1, 1000) #nbr int aléatoire entre 1 et 1000
        (a_xa,a_ya,a_xb,a_yb)=canvas.coords(alien.id)


        #différente façon d'attaque selon le type de l'alien
        if alien.type == 1:
            if r1000 >= 998  : #3/1000  chances de tirer 
                m.l_pa.append(Projectile(a_xa+12.5, a_yb, pa_h, pa_w,canvas))

        elif alien.type == 2:
            if r1000 >= 999  : #1/1000  chances de tirer 2 proj
                m.l_pa.append(Projectile(a_xa-5, a_yb, pa_h, pa_w,canvas))
                m.l_pa.append(Projectile(a_xa+35, a_yb, pa_h, pa_w,canvas))


    #déplacement projectiles alien
    for p_alien in m.l_pa:
        canvas.move(p_alien.id, 0, 5)
        if canvas.coords(p_alien.id)[3] > 600: #le proj sort du jeu -> kill
            remove_list_pa.append(p_alien.id)
            

        if p_alien.collision(m.j.id,canvas): #le proj touche le joueur
            remove_list_pa.append(p_alien.id)
            m.j.vies -= 1
            if m.j.vies <= 0:
                break

            m.j.score -=500 # perte d'une vie = perte de points
            canvas.delete("vies") # effacer pour réafficher et donc éviter les superposition des vies en le supprimant à l'aide du tag 
            canvas.delete("score") # idem

        for prot in m.l_prot:
            if p_alien.collision(prot.id,canvas): #le projectile touche une protection
                remove_list_prot.append(prot.id)
                remove_list_pa.append(p_alien.id)
                

    #tir joueur
    if m.j.tir == 5: #le joueur tire
        m.l_pj.append(Projectile(j_xa+12.5, j_ya-20, pj_h, pj_w,canvas)) #crée un projectile joueur
    if m.j.tir >= 1 :
        m.j.tir -= 1 #le tir se recharge
        
        
    #déplacement projectiles joueur
    for p_joueur in m.l_pj:
        canvas.move(p_joueur.id, 0, -10)
        if canvas.coords(p_joueur.id)[3] < 0: #le projectile sort du jeu -> kill
            remove_list_pj.append(p_joueur.id)
        
        
        for alien in m.l_a: 
            #le proj touche un alien
            if p_joueur.collision(alien.id,canvas): 

                #ajoute du score en fonction de l'ennemi touché
                if alien.type==1: 
                    m.j.score = m.j.score + 100
                if alien.type==2:
                    m.j.score = m.j.score + 50
                if alien.type==3:
                    m.j.score = m.j.score + 10
                remove_list_a.append(alien.id)
                remove_list_pj.append(p_joueur.id)
                # effacer pour réafficher et donc éviter les superposition des scores en le supprimant à l'aide du tag 
                canvas.delete("score")
        
        for prot in m.l_prot:
            #le proj touche une protection
            if p_joueur.collision(prot.id,canvas): 
                remove_list_prot.append(prot.id)
                remove_list_pj.append(p_joueur.id)

    #suppression des objets       
    for id in remove_list_a: 
        for alien in m.l_a :
            if alien.id == id:
                canvas.delete(alien.id)
                m.l_a.remove(alien)
    for id in remove_list_prot:
        for prot in m.l_prot :
            if prot.id == id:
                canvas.delete(prot.id)
                m.l_prot.remove(prot)
    for id in remove_list_pa:
        for p_alien in m.l_pa :
            if p_alien.id == id:
                canvas.delete(p_alien.id)
                m.l_pa.remove(p_alien)
    for id in remove_list_pj:
        for p_joueur in m.l_pj :
            if p_joueur.id == id:
                canvas.delete(p_joueur.id)
                m.l_pj.remove(p_joueur)
    
    
   

    # rappelle Game_loop après 0.05 seconde (1/20s) si joueur pas tué
    if m.j.vies >= 1 and m.l_a != [] :
        root.after(50, Game_loop)
    else : #fin de partie (vies=0)
        Clear()    


def Key_control(event):
    """
    rôle de la fonction: déplacement du joueur avec les touches du clavier
    entrées (s) : "les touches du claviers"
    sortie (s) : "déplacement du joueur "event" "
    """
    if m.j.vies >= 1 :
        (j_xa,j_ya,j_xb,j_yb)=canvas.coords(m.j.id)
        x = 0
        y = 0
        if event.keysym == "Left":
            if j_xa >= 5: 
                x = -5 
        elif event.keysym == "Right":
            if j_xb <= canvas_width-5:
                x = 5
        elif event.keysym == "Up":
            if j_ya >= 505:
                y = -5
        elif event.keysym == "Down":
            if j_yb <= canvas_height-5:
                y = 5
        elif m.j.tir == 0 and event.keysym == "space":
            m.j.tir = 5
        canvas.move(m.j.id, x, y) # déplace le joueur




buttonQuitt = Button (root,text="Quitter",command = root.destroy)
buttonQuitt.pack()


root.bind("<Key>", Key_control)
root.mainloop()