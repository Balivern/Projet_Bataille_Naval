from tkinter import*
from random import*

global fenetre1

# variable de lancement de la boucle de la fenetre de jeu "master". 0 la fenetre de jeu ne se lance pas, 1 jeu démarre en mode solo, 2 jeu démarre en mode deux joueurs
jeu=0

# variable de détermination du joueur actif
joueur_actif=1

# variable déterminant le gagnant de la partie, 1 pour joueur 1, 2 pour joueur 2, 3 pour ordinateur
gagnant=0

def solo():
    # mode de jeu contre ordinateur, choix de difficulté
    global lab, lab2, lab3, bouton0, bouton1, bouton2

    # clear de la fenetre
    lab.pack_forget()
    lab2.pack_forget()
    lab3.pack_forget()
    bouton0.pack_forget()
    bouton1.pack_forget()
    bouton2.pack_forget()

    # remise en page de la fenetre avec choix de difficuté
    lab = Label(fenetre1, text=" Choisissez un mode de difficulté ")
    lab.pack()
    bouton0 = Button(fenetre1,text=" Facile ", command=facile)
    bouton1 = Button(fenetre1,text=" Difficile ", command=difficile)
    bouton2 = Button(fenetre1, text=" Quitter ", command=quitter1) 
    bouton0.pack()
    bouton1.pack()
    bouton2.pack(side=RIGHT)
    lab3= Label(fenetre1, text="Par Lola & Renan")
    lab3.pack(side=LEFT)

def difficile():
    # mode de jeu contre ordinateur difficile
    global jeu, mode

    fenetre1.destroy()
    mode=1
    jeu=1

def facile():
    # mode de jeu contre ordinateur facile
    global jeu, mode

    fenetre1.destroy()
    mode=0
    jeu=1

def deux_joueurs():
    # mode de jeu à 2 joueurs
    global jeu
    fenetre1.destroy()
    jeu=2

def quitter2():
    # bouton quitter en jeu

    global jeu,joueur_actif,start
    jeu=0
    joueur_actif=1
    start=0
    master.destroy()

def quitter1():
    # bouton quitter de la fenetre de présentation

    fenetre1.destroy()

def presentation():
    # fenetre d'accueil
    global fenetre1, lab, lab2, lab3, bouton0, bouton1, bouton2

    fenetre1 = Tk()
    fenetre1.title("La bataille navale")
    img_fond = PhotoImage(file="presentation_bt.gif")
    bg_label = Label(fenetre1, image=img_fond)
    bg_label.pack()
    lab = Label(fenetre1, text="Bonjour, bienvenue sur la Bataille Navale !")
    lab.pack()
    lab2 = Label(fenetre1, text="Voulez vous")
    lab2.pack()
    bouton0 = Button(fenetre1,text=" Solo ", command=solo)
    bouton1 = Button(fenetre1,text=" Deux joueurs ", command=deux_joueurs)
    bouton2 = Button(fenetre1, text=" Quitter ", command=quitter1) 
    bouton0.pack()
    bouton1.pack()
    bouton2.pack(side=RIGHT)
    lab3 = Label(fenetre1, text="Par Lola & Renan")
    lab3.pack(side=LEFT)
    fenetre1.mainloop()

def fin():
    global stat_port1, stat_port2, stat_crois1, stat_crois2, stat_ctorp11, stat_ctorp12, stat_ctorp21, stat_ctorp22, stat_torp1, stat_torp2
    global bouton7, bouton4

    # les plateaux des 2 joueurs sont dévoilés
    cnv1.coords(cache_plat1, 0, 0, 0, 0)
    cnv2.coords(cache_plat2, 0, 0, 0, 0)
    
    # suppression du bouton "pret1" si le jeu est en mode 2 joueurs
    if jeu==2:
        bouton7.pack_forget()

    # suppression du bouton "recommencer"
    bouton4.pack_forget()
    
    # création des canevas de fin de jeu
    cnv_taille_larg = 478
    cnv_taille_long = 269
    cnv_fin=Canvas(master, width=cnv_taille_larg, height=cnv_taille_long, bg="white")
    cnv_fin2=Canvas(master, width=478, height=150, bg="white")
    cnv_fin.pack()
    cnv_fin2.pack()
    # affichage de l'image en fonction de la partie gagné ou perdu, et génération du 1er label en fonction du gagnant
    if gagnant==1 or gagnant==2:
        cnv_fin.create_image(0, 0, anchor=NW, image=img_gagne)
        cnv_fin.create_image(119, 67, anchor=NW, image=img_vict)
        lab = "Bien joué, le joueur " + str(gagnant) + " l'emporte !"
    elif gagnant==3:
        cnv_fin.create_image(0, 0, anchor=NW, image=img_perdu)
        cnv_fin.create_image(119, 79, anchor=NW, image=img_def)
        lab = "Bien joué, mais l'adversaire vous a submergé..."
    cnv_fin2.create_text(cnv_taille_larg/2, 10, text=lab)

    # affichage stat joueur 2
    lab1 = "Résumé de l'état des bateaux du joueur 1 :"
    cnv_fin2.create_text(cnv_taille_larg/4, 40, text=lab1)
    lab2 = "Porte-avion : " + stat_port1 + "    Croiseur : " + stat_crois1 + "    Frégate : " + stat_ctorp11
    cnv_fin2.create_text(cnv_taille_larg/2, 60, text=lab2)
    lab3 = "Sous-marin : " + stat_ctorp21 + "    Torpilleur : " + stat_torp1
    cnv_fin2.create_text(cnv_taille_larg/2, 80, text=lab3)

    # affichage stat joueur 2
    lab4 = "Résumé de l'état des bateaux du joueur 2 :"
    cnv_fin2.create_text(cnv_taille_larg/4, 100, text=lab4)
    lab5 = "Porte-avion : " + stat_port2 + "    Croiseur : " + stat_crois2 + "    Frégate : " + stat_ctorp12
    cnv_fin2.create_text(cnv_taille_larg/2, 120, text=lab5)
    lab6 = "Sous-marin : " + stat_ctorp22 + "    Torpilleur : " + stat_torp2
    cnv_fin2.create_text(cnv_taille_larg/2, 140, text=lab6)
    
if __name__ == '__main__':
    presentation()

if jeu==1 or jeu==2:
    master=Tk()
    master.title("La bataille navale")

NB_CASE_LARGE=11
NB_CASE_HAUT=22
CANVAS_TAILLE=550+20
TAILLE_CASE=(CANVAS_TAILLE-20)//NB_CASE_LARGE//2
x0=NB_CASE_LARGE*TAILLE_CASE+50
FONT=('Ubuntu',15,'bold')
L=["A","B","C","D","E","F","G","H","I","J"]
old=[None, None]

cnv1=Canvas(master, width=CANVAS_TAILLE, height=CANVAS_TAILLE, bg='ivory')
cnv2=Canvas(master, width=CANVAS_TAILLE, height=CANVAS_TAILLE, bg='ivory')

img_eau = PhotoImage(file="eau.png")
eau=cnv1.create_image(TAILLE_CASE*5, TAILLE_CASE*11, image=img_eau)
eau=cnv2.create_image(TAILLE_CASE*5, TAILLE_CASE*11, image=img_eau)

img_gagne=PhotoImage(file="_victoire.png")
img_perdu=PhotoImage(file="defaite.png")
img_vict=PhotoImage(file="_victoire_text.png")
img_def=PhotoImage(file="defeat_text.png")

if jeu==0:
    cnv1.pack_forget()
    cnv2.pack_forget()
else:
    cnv1.pack(side=LEFT, padx=10, pady=10)
    cnv2.pack(side=RIGHT, padx=10, pady=10)

def plateau (cnv, case_plat):
    # fonction de création des grilles de jeu

    for i in range(NB_CASE_HAUT):
        if i!=0 and i!=11:
            case_plat.append([0,0,0,0,0,0,0,0,0,0])
        for j in range(NB_CASE_LARGE):
            a,b,c,d = j*TAILLE_CASE, i*TAILLE_CASE,(1+j)*TAILLE_CASE, (1+i)*TAILLE_CASE
            A=(a+TAILLE_CASE//2,b+TAILLE_CASE//2)
            if j==0 and 0<=i<11:
                cnv.create_rectangle(a,b,c,d,fill="grey")
                cnv.create_text(A, text=[i][j],fill="black",font=FONT)
            elif j==0 and 11<=i<22:
                cnv.create_rectangle(a,b,c,d,fill="grey")
                cnv.create_text(A, text=[i-11][j],fill="black",font=FONT)
            elif i==0:
                cnv.create_rectangle(a,b,c,d, fill="grey")
                cnv.create_text(A, text=L[j-1],fill="black",font=FONT)
            elif i==11:
                cnv.create_rectangle(a,b,c,d, fill="grey")
                cnv.create_text(A, text=L[j-1],fill="black",font=FONT)
            else:
                cnv.create_rectangle(a,b,c,d, fill="", outline="black")

case_plat1=[]
case_plat2=[]
pos_port1 = pos_port2 = pos_croi1 = pos_croi2 = pos_ctorp11 = pos_ctorp12 = pos_ctorp21 = pos_ctorp22 = pos_torp1 = pos_torp2 = 0, 0
tire1=[]
tire2=[]

plateau(cnv1, case_plat1)
plateau(cnv2, case_plat2)

bateau1=[]
bateau2=[]
pbateau1=[]
pbateau2=[]

porteavion=cnv1.create_rectangle(x0,12*TAILLE_CASE,x0+5*TAILLE_CASE,TAILLE_CASE*12+TAILLE_CASE, fill='black',outline='black')
croiseur=cnv1.create_rectangle(x0,TAILLE_CASE*14,x0+4*TAILLE_CASE,TAILLE_CASE*14+TAILLE_CASE, fill='black',outline='black')
cttorpil1=cnv1.create_rectangle(x0,TAILLE_CASE*16,x0+3*TAILLE_CASE,TAILLE_CASE*16+TAILLE_CASE, fill='black',outline='black')
cttorpil2=cnv1.create_rectangle(x0,TAILLE_CASE*18,x0+3*TAILLE_CASE,TAILLE_CASE*18+TAILLE_CASE, fill='black',outline='black')
torpilleur=cnv1.create_rectangle(x0,TAILLE_CASE*20,x0+2*TAILLE_CASE,TAILLE_CASE*20+TAILLE_CASE, fill='black',outline='black')
pporteavion=pcroiseur=pcttorpil1=pcttorpil2=ptorpilleur=0
pbateau1=[pporteavion,pcroiseur,pcttorpil1,pcttorpil2,ptorpilleur]
bateau1=[porteavion,croiseur,cttorpil1,cttorpil2,torpilleur]

porteavion=cnv2.create_rectangle(x0,12*TAILLE_CASE,x0+5*TAILLE_CASE,TAILLE_CASE*12+TAILLE_CASE, fill='black',outline='black')
croiseur=cnv2.create_rectangle(x0,TAILLE_CASE*14,x0+4*TAILLE_CASE,TAILLE_CASE*14+TAILLE_CASE, fill='black',outline='black')
cttorpil1=cnv2.create_rectangle(x0,TAILLE_CASE*16,x0+3*TAILLE_CASE,TAILLE_CASE*16+TAILLE_CASE, fill='black',outline='black')
cttorpil2=cnv2.create_rectangle(x0,TAILLE_CASE*18,x0+3*TAILLE_CASE,TAILLE_CASE*18+TAILLE_CASE, fill='black',outline='black')
torpilleur=cnv2.create_rectangle(x0,TAILLE_CASE*20,x0+2*TAILLE_CASE,TAILLE_CASE*20+TAILLE_CASE, fill='black',outline='black')
pporteavion=pcroiseur=pcttorpil1=pcttorpil2=ptorpilleur=0
pbateau2=[pporteavion,pcroiseur,pcttorpil1,pcttorpil2,ptorpilleur]
bateau2=[porteavion,croiseur,cttorpil1,cttorpil2,torpilleur]

cnv2.create_text(x0+TAILLE_CASE*2, TAILLE_CASE*11, text= "Joueur 2     ",fill="black", font=('Helvetica 15 bold'))
cnv1.create_text(x0+TAILLE_CASE*2, TAILLE_CASE*11, text= "Joueur 1     ",fill="black", font=('Helvetica 15 bold'))

mess1="Placez vos bateaux dans\nle cadrillage du bas"
m1=cnv1.create_text(TAILLE_CASE*16, TAILLE_CASE*8, fill="red", font=('Helvetica 10 bold'), text=mess1)
m2=cnv2.create_text(TAILLE_CASE*16, TAILLE_CASE*8, fill="red", font=('Helvetica 10 bold'), text=mess1)


def clic(event):
    old[0]=event.x
    old[1]=event.y

def unclic(event):
    global pos_port1, pos_port2, pos_croi1, pos_croi2, pos_ctorp11, pos_ctorp12, pos_ctorp21, pos_ctorp22, pos_torp1, pos_torp2

    if start==0:
        if joueur_actif==1:
            for i in range (len(bateau1)):
                x1, y1, x2, y2 = cnv1.coords(bateau1[i])
                if (old[0] >= x1 and old[0] <= x2 and old[1] >= y1 and old[1] <= y2):
                    # si le bateau est à l'horizontal
                    if pbateau1[i]==0:
                        # si le bateau est le porteavion et qu'il se trouve dans le quadrillage bas
                        if bateau1[i]==porteavion and (TAILLE_CASE<x1<7*TAILLE_CASE and y1>12*TAILLE_CASE):
                            # aligne le bateau avec le quadrillage directement en haut à gauche par rapport à lui-même
                            cnv1.move(bateau1[i], (event.x-old[0])-(x1%TAILLE_CASE), (event.y-old[1])-(y1%TAILLE_CASE))
                        # idem croiseur...
                        elif bateau1[i]==croiseur:
                            if (TAILLE_CASE<x1<8*TAILLE_CASE and y1>12*TAILLE_CASE):
                                cnv1.move(bateau1[i], (event.x-old[0])-(x1%TAILLE_CASE), (event.y-old[1])-(y1%TAILLE_CASE))
                        elif bateau1[i]==cttorpil1:
                            if (TAILLE_CASE<x1<9*TAILLE_CASE and y1>12*TAILLE_CASE):
                                cnv1.move(bateau1[i], (event.x-old[0])-(x1%TAILLE_CASE), (event.y-old[1])-(y1%TAILLE_CASE))
                        elif bateau1[i]==cttorpil2:
                            if (TAILLE_CASE<x1<9*TAILLE_CASE and y1>12*TAILLE_CASE):
                                cnv1.move(bateau1[i], (event.x-old[0])-(x1%TAILLE_CASE), (event.y-old[1])-(y1%TAILLE_CASE))
                        elif bateau1[i]==torpilleur:
                            if (TAILLE_CASE<x1<10*TAILLE_CASE and y1>12*TAILLE_CASE):
                                cnv1.move(bateau1[i], (event.x-old[0])-(x1%TAILLE_CASE), (event.y-old[1])-(y1%TAILLE_CASE))
                    # idem bateau à la vertical...
                    elif (TAILLE_CASE<x1<11*TAILLE_CASE and y1>12*TAILLE_CASE) and pbateau1[i]==1:
                        cnv1.move(bateau1[i], (event.x-old[0])-(x1%TAILLE_CASE), (event.y-old[1])-(y1%TAILLE_CASE))
        # idem si le joueur actif est le joueur 2...
        elif joueur_actif==2:
            for i in range (len(bateau2)):
                x1, y1, x2, y2 = cnv2.coords(bateau2[i])
                if (old[0] >= x1 and old[0] <= x2 and old[1] >= y1 and old[1] <= y2):
                    if pbateau2[i]==0:
                        if bateau2[i]==porteavion and (TAILLE_CASE<x1<7*TAILLE_CASE and y1>12*TAILLE_CASE):
                            cnv2.move(bateau2[i], (event.x-old[0])-(x1%TAILLE_CASE), (event.y-old[1])-(y1%TAILLE_CASE))
                        elif bateau2[i]==croiseur:
                            if (TAILLE_CASE<x1<8*TAILLE_CASE and y1>12*TAILLE_CASE):
                                cnv2.move(bateau2[i], (event.x-old[0])-(x1%TAILLE_CASE), (event.y-old[1])-(y1%TAILLE_CASE))
                        elif bateau2[i]==cttorpil1:
                            if (TAILLE_CASE<x1<9*TAILLE_CASE and y1>12*TAILLE_CASE):
                                cnv2.move(bateau2[i], (event.x-old[0])-(x1%TAILLE_CASE), (event.y-old[1])-(y1%TAILLE_CASE))
                        elif bateau2[i]==cttorpil2:
                            if (TAILLE_CASE<x1<9*TAILLE_CASE and y1>12*TAILLE_CASE):
                                cnv2.move(bateau2[i], (event.x-old[0])-(x1%TAILLE_CASE), (event.y-old[1])-(y1%TAILLE_CASE))
                        elif bateau2[i]==torpilleur:
                            if (TAILLE_CASE<x1<10*TAILLE_CASE and y1>12*TAILLE_CASE):
                                cnv2.move(bateau2[i], (event.x-old[0])-(x1%TAILLE_CASE), (event.y-old[1])-(y1%TAILLE_CASE))
                    elif (TAILLE_CASE<x1<11*TAILLE_CASE and y1>12*TAILLE_CASE) and pbateau2[i]==1:
                        cnv2.move(bateau2[i], (event.x-old[0])-(x1%TAILLE_CASE), (event.y-old[1])-(y1%TAILLE_CASE))

        # stockage des coordonnées de tous les bateaux
        pos_port1 = cnv1.coords(bateau1[0])
        pos_port2 = cnv2.coords(bateau2[0])
        pos_croi1 = cnv1.coords(bateau1[1])
        pos_croi2 = cnv2.coords(bateau2[1])
        pos_ctorp11 = cnv1.coords(bateau1[2])
        pos_ctorp12 = cnv2.coords(bateau2[2])
        pos_ctorp21 = cnv1.coords(bateau1[3])
        pos_ctorp22 = cnv2.coords(bateau2[3])
        pos_torp1 = cnv1.coords(bateau1[4])
        pos_torp2 = cnv2.coords(bateau2[4])

        # fonction de test, pour savoir si le jeu est pret à démarrer, alors apparition du bouton "pret", ou "commencer"
        test_commencer()

def rnd_bateau():
    global pos_port2, pos_croi2, pos_ctorp12, pos_ctorp22, pos_torp2

    val_test=0

    # tirage aléatoire de la position verticale ou horizontal des bateaux
    for k in range (len(pbateau2)):
        rnd = randint(0, 1)
        pbateau2[k]=rnd

    i=0
    # placement aléatoire des bateaux dans la matrice
    while i<5:
        if pbateau2[i]==0:
            if bateau2[i]==porteavion:
                x1, y1 = randint(1,6), randint(12, 21)
                cnv2.coords(porteavion,x1*TAILLE_CASE,y1*TAILLE_CASE,(x1+5)*TAILLE_CASE,(y1+1)*TAILLE_CASE)
                x1, y1, x2, y2 = cnv2.coords(bateau2[i])
                pos_port2 = x1, y1
            elif bateau2[i]==croiseur:
                x1, y1 = randint(1,7), randint(12, 21)
                cnv2.coords(croiseur,x1*TAILLE_CASE,y1*TAILLE_CASE,(x1+4)*TAILLE_CASE,(y1+1)*TAILLE_CASE)
                x1, y1, x2, y2 = cnv2.coords(bateau2[i])
                pos_croi2 = x1, y1
            elif bateau2[i]==cttorpil1:
                x1, y1 = randint(1,8), randint(12, 21)
                cnv2.coords(cttorpil1,x1*TAILLE_CASE,y1*TAILLE_CASE,(x1+3)*TAILLE_CASE,(y1+1)*TAILLE_CASE)
                x1, y1, x2, y2 = cnv2.coords(bateau2[i])
                pos_ctorp12 = x1, y1
            elif bateau2[i]==cttorpil2:
                x1, y1 = randint(1,8), randint(12, 21)
                cnv2.coords(cttorpil2,x1*TAILLE_CASE,y1*TAILLE_CASE,(x1+3)*TAILLE_CASE,(y1+1)*TAILLE_CASE)
                x1, y1, x2, y2 = cnv2.coords(bateau2[i])
                pos_ctorp22 = x1, y1
            elif bateau2[i]==torpilleur:
                x1, y1 = randint(1,9), randint(12, 21)
                cnv2.coords(torpilleur,x1*TAILLE_CASE,y1*TAILLE_CASE,(x1+2)*TAILLE_CASE,(y1+1)*TAILLE_CASE)
                x1, y1, x2, y2 = cnv2.coords(bateau2[i])
                pos_torp2 = x1, y1
        elif pbateau2[i]==1:
            if bateau2[i]==porteavion:
                x1, y1 = randint(1,10), randint(12, 17)
                cnv2.coords(porteavion,x1*TAILLE_CASE,y1*TAILLE_CASE,(x1+1)*TAILLE_CASE,(y1+5)*TAILLE_CASE)
                x1, y1, x2, y2 = cnv2.coords(bateau2[i])
                pos_port2 = x1, y1
            elif bateau2[i]==croiseur:
                x1, y1 = randint(1,10), randint(12, 18)
                cnv2.coords(croiseur,x1*TAILLE_CASE,y1*TAILLE_CASE,(x1+1)*TAILLE_CASE,(y1+4)*TAILLE_CASE)
                x1, y1, x2, y2 = cnv2.coords(bateau2[i])
                pos_croi2 = x1, y1
            elif bateau2[i]==cttorpil1:
                x1, y1 = randint(1,10), randint(12, 19)
                cnv2.coords(cttorpil1,x1*TAILLE_CASE,y1*TAILLE_CASE,(x1+1)*TAILLE_CASE,(y1+3)*TAILLE_CASE)
                x1, y1, x2, y2 = cnv2.coords(bateau2[i])
                pos_ctorp12 = x1, y1
            elif bateau2[i]==cttorpil2:
                x1, y1 = randint(1,10), randint(12, 19)
                cnv2.coords(cttorpil2,x1*TAILLE_CASE,y1*TAILLE_CASE,(x1+1)*TAILLE_CASE,(y1+3)*TAILLE_CASE)
                x1, y1, x2, y2 = cnv2.coords(bateau2[i])
                pos_ctorp22 = x1, y1
            elif bateau2[i]==torpilleur:
                x1, y1 = randint(1,10), randint(12, 20)
                cnv2.coords(torpilleur,x1*TAILLE_CASE,y1*TAILLE_CASE,(x1+1)*TAILLE_CASE,(y1+2)*TAILLE_CASE)
                x1, y1, x2, y2 = cnv2.coords(bateau2[i])
                pos_torp2 = x1, y1
        
        # test si le bateau en cours de placement est collé à un bateau. Si ce n'est pas le cas, incrémentation de l'indice i
        for j in range (len(bateau2)):
            x1, y1, x2, y2 = cnv2.coords(bateau2[j])
            a12, b12, a22, b22 = cnv2.coords(bateau2[j-1])
            a13, b13, a23, b23 = cnv2.coords(bateau2[j-2])
            a14, b14, a24, b24 = cnv2.coords(bateau2[j-3])
            a15, b15, a25, b25 = cnv2.coords(bateau2[j-4])
            if (y2>b12-5 and x1<a22+5 and x2>a12-5 and y1<b22+5) or (y2>b13-5 and x1<a23+5 and x2>a13-5 and y1<b23+5) or (y2>b14-5 and x1<a24+5 and x2>a14-5 and y1<b24+5) or (y2>b15-5 and x1<a25+5 and x2>a15-5 and y1<b25+5):
                val_test+=1
        
        if val_test==0:
            i+=1

        val_test=0

        pos_port2 = cnv2.coords(bateau2[0])
        pos_croi2 = cnv2.coords(bateau2[1])
        pos_ctorp12 = cnv2.coords(bateau2[2])
        pos_ctorp22 = cnv2.coords(bateau2[3])
        pos_torp2 = cnv2.coords(bateau2[4])

def glisser(event):
    if start==0:
        if joueur_actif==1:
            for i in range (len(bateau1)):
                x1, y1, x2, y2 = cnv1.coords(bateau1[i])
                a12, b12, a22, b22 = cnv1.coords(bateau1[i-1])
                a13, b13, a23, b23 = cnv1.coords(bateau1[i-2])
                a14, b14, a24, b24 = cnv1.coords(bateau1[i-3])
                a15, b15, a25, b25 = cnv1.coords(bateau1[i-4])
                # si la souris se trouve dans le bateau
                if (old[0] >= x1 and old[0] <= x2 and old[1] >= y1 and old[1] <= y2):
                    # si le bateau est trop proche du bord du canevas
                    if (x1<5 or y1<5 or x2>CANVAS_TAILLE-5 or y2>CANVAS_TAILLE-5):
                        # si le bateau est trop proche du bord gauche, bateau repoussé
                        if x1<5:
                            cnv1.move(bateau1[i], event.x-old[0]+5, event.y-old[1])
                            old[0]=event.x
                            old[1]=event.y
                        # idem bord haut...
                        elif y1<5:
                            cnv1.move(bateau1[i], event.x-old[0], event.y-old[1]+5)
                            old[0]=event.x
                            old[1]=event.y
                        elif x2>CANVAS_TAILLE-5:
                            cnv1.move(bateau1[i], event.x-old[0]-5, event.y-old[1])
                            old[0]=event.x
                            old[1]=event.y
                        elif y2>CANVAS_TAILLE-5:
                            cnv1.move(bateau1[i], event.x-old[0], event.y-old[1]-5)
                            old[0]=event.x
                            old[1]=event.y
                    # idem par rapport aux autres bateaux...
                    elif (y2>b12-5 and x1<a22+5 and x2>a12-5 and y1<b22+5):
                        if (y1<b12-5 and y2>b12-5):
                            cnv1.move(bateau1[i], event.x-old[0], -(event.y-old[1]+5))
                            old[0]=event.x
                            old[1]=event.y
                        elif (y1<b22+5 and y2>b22+5):
                            cnv1.move(bateau1[i], event.x-old[0], event.y-old[1]+5)
                            old[0]=event.x
                            old[1]=event.y
                        elif (x1<a12-5 and x2>a12-5):
                            cnv1.move(bateau1[i], -(event.x-old[0]+5), event.y-old[1])
                            old[0]=event.x
                            old[1]=event.y
                        else :
                            cnv1.move(bateau1[i], event.x-old[0]+5, event.y-old[1])
                            old[0]=event.x
                            old[1]=event.y
                    elif (y2>b13-5 and x1<a23+5 and x2>a13-5 and y1<b23+5):
                        if (y1<b13-5 and y2>b13-5):
                            cnv1.move(bateau1[i], event.x-old[0], -(event.y-old[1]+5))
                            old[0]=event.x
                            old[1]=event.y
                        elif (y1<b23+5 and y2>b23+5):
                            cnv1.move(bateau1[i], event.x-old[0], event.y-old[1]+5)
                            old[0]=event.x
                            old[1]=event.y
                        elif (x1<a13-5 and x2>a13-5):
                            cnv1.move(bateau1[i], -(event.x-old[0]+5), event.y-old[1])
                            old[0]=event.x
                            old[1]=event.y
                        else :
                            cnv1.move(bateau1[i], event.x-old[0]+5, event.y-old[1])
                            old[0]=event.x
                            old[1]=event.y
                    elif (y2>b14-5 and x1<a24+5 and x2>a14-5 and y1<b24+5):
                        if (y1<b14-5 and y2>b14-5):
                            cnv1.move(bateau1[i], event.x-old[0], -(event.y-old[1]+5))
                            old[0]=event.x
                            old[1]=event.y
                        elif (y1<b24+5 and y2>b24+5):
                            cnv1.move(bateau1[i], event.x-old[0], event.y-old[1]+5)
                            old[0]=event.x
                            old[1]=event.y
                        elif (x1<a14-5 and x2>a14-5):
                            cnv1.move(bateau1[i], -(event.x-old[0]+5), event.y-old[1])
                            old[0]=event.x
                            old[1]=event.y
                        else :
                            cnv1.move(bateau1[i], event.x-old[0]+5, event.y-old[1])
                            old[0]=event.x
                            old[1]=event.y
                    elif (y2>b15-5 and x1<a25+5 and x2>a15-5 and y1<b25+5):
                        if (y1<b15-5 and y2>b15-5):
                            cnv1.move(bateau1[i], event.x-old[0], -(event.y-old[1]+5))
                            old[0]=event.x
                            old[1]=event.y
                        elif (y1<b25+5 and y2>b25+5):
                            cnv1.move(bateau1[i], event.x-old[0], event.y-old[1]+5)
                            old[0]=event.x
                            old[1]=event.y
                        elif (x1<a15-5 and x2>a15-5):
                            cnv1.move(bateau1[i], -(event.x-old[0]+5), event.y-old[1])
                            old[0]=event.x
                            old[1]=event.y
                        else :
                            cnv1.move(bateau1[i], event.x-old[0]+5, event.y-old[1])
                            old[0]=event.x
                            old[1]=event.y
                    # sinon déplacement libre du bateau
                    else :
                        cnv1.move(bateau1[i], event.x-old[0], event.y-old[1])
                        old[0]=event.x
                        old[1]=event.y
        # idem si le joueur actif est le joueur 2...
        if joueur_actif==2:
            for i in range (len(bateau2)):
                x1, y1, x2, y2 = cnv2.coords(bateau2[i])
                a12, b12, a22, b22 = cnv2.coords(bateau2[i-1])
                a13, b13, a23, b23 = cnv2.coords(bateau2[i-2])
                a14, b14, a24, b24 = cnv2.coords(bateau2[i-3])
                a15, b15, a25, b25 = cnv2.coords(bateau2[i-4])
                if (old[0] >= x1 and old[0] <= x2 and old[1] >= y1 and old[1] <= y2):
                    if (x1<5 or y1<5 or x2>CANVAS_TAILLE-5 or y2>CANVAS_TAILLE-5):
                        if x1<5:
                            cnv2.move(bateau2[i], event.x-old[0]+5, event.y-old[1])
                            old[0]=event.x
                            old[1]=event.y
                        elif y1<5:
                            cnv2.move(bateau2[i], event.x-old[0], event.y-old[1]+5)
                            old[0]=event.x
                            old[1]=event.y
                        elif x2>CANVAS_TAILLE-5:
                            cnv2.move(bateau2[i], event.x-old[0]-5, event.y-old[1])
                            old[0]=event.x
                            old[1]=event.y
                        elif y2>CANVAS_TAILLE-5:
                            cnv2.move(bateau2[i], event.x-old[0], event.y-old[1]-5)
                            old[0]=event.x
                            old[1]=event.y
                    elif (y2>b12-5 and x1<a22+5 and x2>a12-5 and y1<b22+5):
                        if (y1<b12-5 and y2>b12-5):
                            cnv2.move(bateau2[i], event.x-old[0], -(event.y-old[1]+5))
                            old[0]=event.x
                            old[1]=event.y
                        elif (y1<b22+5 and y2>b22+5):
                            cnv2.move(bateau2[i], event.x-old[0], event.y-old[1]+5)
                            old[0]=event.x
                            old[1]=event.y
                        elif (x1<a12-5 and x2>a12-5):
                            cnv2.move(bateau2[i], -(event.x-old[0]+5), event.y-old[1])
                            old[0]=event.x
                            old[1]=event.y
                        else :
                            cnv2.move(bateau2[i], event.x-old[0]+5, event.y-old[1])
                            old[0]=event.x
                            old[1]=event.y
                    elif (y2>b13-5 and x1<a23+5 and x2>a13-5 and y1<b23+5):
                        if (y1<b13-5 and y2>b13-5):
                            cnv2.move(bateau2[i], event.x-old[0], -(event.y-old[1]+5))
                            old[0]=event.x
                            old[1]=event.y
                        elif (y1<b23+5 and y2>b23+5):
                            cnv2.move(bateau2[i], event.x-old[0], event.y-old[1]+5)
                            old[0]=event.x
                            old[1]=event.y
                        elif (x1<a13-5 and x2>a13-5):
                            cnv2.move(bateau2[i], -(event.x-old[0]+5), event.y-old[1])
                            old[0]=event.x
                            old[1]=event.y
                        else :
                            cnv2.move(bateau2[i], event.x-old[0]+5, event.y-old[1])
                            old[0]=event.x
                            old[1]=event.y
                    elif (y2>b14-5 and x1<a24+5 and x2>a14-5 and y1<b24+5):
                        if (y1<b14-5 and y2>b14-5):
                            cnv2.move(bateau2[i], event.x-old[0], -(event.y-old[1]+5))
                            old[0]=event.x
                            old[1]=event.y
                        elif (y1<b24+5 and y2>b24+5):
                            cnv2.move(bateau2[i], event.x-old[0], event.y-old[1]+5)
                            old[0]=event.x
                            old[1]=event.y
                        elif (x1<a14-5 and x2>a14-5):
                            cnv2.move(bateau2[i], -(event.x-old[0]+5), event.y-old[1])
                            old[0]=event.x
                            old[1]=event.y
                        else :
                            cnv2.move(bateau2[i], event.x-old[0]+5, event.y-old[1])
                            old[0]=event.x
                            old[1]=event.y
                    elif (y2>b15-5 and x1<a25+5 and x2>a15-5 and y1<b25+5):
                        if (y1<b15-5 and y2>b15-5):
                            cnv2.move(bateau2[i], event.x-old[0], -(event.y-old[1]+5))
                            old[0]=event.x
                            old[1]=event.y
                        elif (y1<b25+5 and y2>b25+5):
                            cnv2.move(bateau2[i], event.x-old[0], event.y-old[1]+5)
                            old[0]=event.x
                            old[1]=event.y
                        elif (x1<a15-5 and x2>a15-5):
                            cnv2.move(bateau2[i], -(event.x-old[0]+5), event.y-old[1])
                            old[0]=event.x
                            old[1]=event.y
                        else :
                            cnv2.move(bateau2[i], event.x-old[0]+5, event.y-old[1])
                            old[0]=event.x
                            old[1]=event.y
                    else :
                        cnv2.move(bateau2[i], event.x-old[0], event.y-old[1])
                        old[0]=event.x
                        old[1]=event.y

def rotation(event):
    if start==0:
        old[0]=event.x
        old[1]=event.y
        if joueur_actif==1:
            for i in range(len(bateau1)):
                x1,y1,x2,y2 = cnv1.coords(bateau1[i])
                # si le curseur se trouve dans le bateau
                if ( x1 <= old[0] <= x2) and (y1 < old[1] < y2):
                    # rotation du bateau
                    cnv1.coords(bateau1[i],x1,y1,x1+(y2-y1),y1+(x2-x1))
                    # modification de la variable déterminant l'orientation du bateau 
                    if pbateau1[i]==0:
                        pbateau1[i]=1
                    elif pbateau1[i]==1:
                        pbateau1[i]=0
        # idem joueur 2..
        elif joueur_actif==2:
            for i in range(len(bateau2)):
                x1,y1,x2,y2 = cnv2.coords(bateau2[i])
                if ( x1 <= old[0] <= x2) and (y1 < old[1] < y2):
                        cnv2.coords(bateau2[i],x1,y1,x1+(y2-y1),y1+(x2-x1))
                        if pbateau2[i]==0:
                            pbateau2[i]=1
                        elif pbateau2[i]==1:
                            pbateau2[i]=0

def tirer(event):
    global joueur_actif
    old[0]=event.x
    old[1]=event.y

    if start==1:
        # si le curseur de la sourie se situe dans une matrice haute:
        if TAILLE_CASE<old[0]<TAILLE_CASE*11 and TAILLE_CASE<old[1]<TAILLE_CASE*11 and old[0]%TAILLE_CASE!=0 and old[1]%TAILLE_CASE!=0:
            # si la case ciblée est égale à 0 (c.a.d qu'elle ne contient ni bateau, ni tir lui ayant précédé) :
            if case_plat1[(old[1]//TAILLE_CASE)-1][(old[0]//TAILLE_CASE)-1]==0 and joueur_actif==1:
                # on créer un rond au centre de la case ciblé
                t1=cnv1.create_oval((old[0]-old[0]%TAILLE_CASE+TAILLE_CASE//2)-5, (old[1]-old[1]%TAILLE_CASE+TAILLE_CASE//2)-5, (old[0]-old[0]%TAILLE_CASE+TAILLE_CASE//2)+5, (old[1]-old[1]%TAILLE_CASE+TAILLE_CASE//2)+5, fill='yellow', outline='black')
                t2=cnv2.create_oval((old[0]-old[0]%TAILLE_CASE+TAILLE_CASE//2)-5, ((old[1]-old[1]%TAILLE_CASE+TAILLE_CASE//2)-5)+11*TAILLE_CASE, (old[0]-old[0]%TAILLE_CASE+TAILLE_CASE//2)+5, ((old[1]-old[1]%TAILLE_CASE+TAILLE_CASE//2)+5)+11*TAILLE_CASE, fill='yellow', outline='black')
                # on remonte les caches des plateaux
                cnv2.tag_raise(cache_plat2)
                cnv1.tag_raise(cache_plat1)
                # incrémentation de la case correspondante dans la matrice des 2 joueurs
                case_plat1[(old[1]//TAILLE_CASE)-1][(old[0]//TAILLE_CASE)-1]+=1
                case_plat2[(old[1]//TAILLE_CASE)-1+10][(old[0]//TAILLE_CASE)-1]+=1
                # on retient le rond dans les listes de tirs
                tire1.append(t1)
                tire2.append(t2)
                # fonction de test de bateau coulé
                test_coulé()
                # délai laissant du temps au joueur pour voir l'action avant de passer au joueur suivant
                cnv1.after(1500, joueur)
            # idem joueur 2...
            elif case_plat2[(old[1]//TAILLE_CASE)-1][(old[0]//TAILLE_CASE)-1]==0 and joueur_actif==2:
                t1=cnv2.create_oval((old[0]-old[0]%TAILLE_CASE+TAILLE_CASE//2)-5, (old[1]-old[1]%TAILLE_CASE+TAILLE_CASE//2)-5, (old[0]-old[0]%TAILLE_CASE+TAILLE_CASE//2)+5, (old[1]-old[1]%TAILLE_CASE+TAILLE_CASE//2)+5, fill='yellow', outline='black')
                t2=cnv1.create_oval((old[0]-old[0]%TAILLE_CASE+TAILLE_CASE//2)-5, ((old[1]-old[1]%TAILLE_CASE+TAILLE_CASE//2)-5)+11*TAILLE_CASE, (old[0]-old[0]%TAILLE_CASE+TAILLE_CASE//2)+5, ((old[1]-old[1]%TAILLE_CASE+TAILLE_CASE//2)+5)+11*TAILLE_CASE, fill='yellow', outline='black')
                cnv2.tag_raise(cache_plat2)
                cnv1.tag_raise(cache_plat1)
                case_plat2[(old[1]//TAILLE_CASE)-1][(old[0]//TAILLE_CASE)-1]+=1
                case_plat1[(old[1]//TAILLE_CASE)-1+10][(old[0]//TAILLE_CASE)-1]+=1
                tire1.append(t1)
                tire2.append(t2)
                test_coulé()
                cnv2.after(1500, joueur)
            # Meme chose mais dans le cas ou le case touché est occupée par un bateau
            elif case_plat1[(old[1]//TAILLE_CASE)-1][(old[0]//TAILLE_CASE)-1]!=0 and case_plat1[(old[1]//TAILLE_CASE)-1][(old[0]//TAILLE_CASE)-1]%2==0 and joueur_actif==1:
                t1=cnv1.create_oval((old[0]-old[0]%TAILLE_CASE+TAILLE_CASE//2)-5, (old[1]-old[1]%TAILLE_CASE+TAILLE_CASE//2)-5, (old[0]-old[0]%TAILLE_CASE+TAILLE_CASE//2)+5, (old[1]-old[1]%TAILLE_CASE+TAILLE_CASE//2)+5, fill='red', outline='black')
                t2=cnv2.create_oval((old[0]-old[0]%TAILLE_CASE+TAILLE_CASE//2)-5, ((old[1]-old[1]%TAILLE_CASE+TAILLE_CASE//2)-5)+11*TAILLE_CASE, (old[0]-old[0]%TAILLE_CASE+TAILLE_CASE//2)+5, ((old[1]-old[1]%TAILLE_CASE+TAILLE_CASE//2)+5)+11*TAILLE_CASE, fill='red', outline='black')
                cnv2.tag_raise(cache_plat2)
                cnv1.tag_raise(cache_plat1)
                case_plat1[(old[1]//TAILLE_CASE)-1][(old[0]//TAILLE_CASE)-1]+=1
                case_plat2[(old[1]//TAILLE_CASE)-1+10][(old[0]//TAILLE_CASE)-1]+=1
                tire1.append(t1)
                tire2.append(t2)
                test_coulé()
                cnv1.after(1500, joueur)
            # idem joueur 2...
            elif case_plat2[(old[1]//TAILLE_CASE)-1][(old[0]//TAILLE_CASE)-1]!=0 and case_plat2[(old[1]//TAILLE_CASE)-1][(old[0]//TAILLE_CASE)-1]%2==0 and joueur_actif==2 :
                t1=cnv2.create_oval((old[0]-old[0]%TAILLE_CASE+TAILLE_CASE//2)-5, (old[1]-old[1]%TAILLE_CASE+TAILLE_CASE//2)-5, (old[0]-old[0]%TAILLE_CASE+TAILLE_CASE//2)+5, (old[1]-old[1]%TAILLE_CASE+TAILLE_CASE//2)+5, fill='red', outline='white')
                t2=cnv1.create_oval((old[0]-old[0]%TAILLE_CASE+TAILLE_CASE//2)-5, ((old[1]-old[1]%TAILLE_CASE+TAILLE_CASE//2)-5)+11*TAILLE_CASE, (old[0]-old[0]%TAILLE_CASE+TAILLE_CASE//2)+5, ((old[1]-old[1]%TAILLE_CASE+TAILLE_CASE//2)+5)+11*TAILLE_CASE, fill='red', outline='white')
                cnv2.tag_raise(cache_plat2)
                cnv1.tag_raise(cache_plat1)
                case_plat2[(old[1]//TAILLE_CASE)-1][(old[0]//TAILLE_CASE)-1]+=1
                case_plat1[(old[1]//TAILLE_CASE)-1+10][(old[0]//TAILLE_CASE)-1]+=1
                tire1.append(t1)
                tire2.append(t2)
                test_coulé()
                cnv2.after(1500, joueur)

def rnd_tire():
    # tirage aléatoire du n° de ligne et de colonne à ciblé
    if mode==0 or mode==1:
        a, b = randint(0, 9), randint(0, 9)

    # si le jeu est en mode facile
    if mode==0:
        # si la case est vide
        if case_plat2[a][b]==0:
            # on créer un rond au centre de la case ciblé
            t1=cnv2.create_oval(((b+1)*TAILLE_CASE)+TAILLE_CASE//2-5, ((a+1)*TAILLE_CASE)+TAILLE_CASE//2-5, ((b+1)*TAILLE_CASE)+TAILLE_CASE//2+5, ((a+1)*TAILLE_CASE)+TAILLE_CASE//2+5, fill='yellow', outline='black')
            t2=cnv1.create_oval(((b+1)*TAILLE_CASE)+TAILLE_CASE//2-5, ((a+12)*TAILLE_CASE)+TAILLE_CASE//2-5, ((b+1)*TAILLE_CASE)+TAILLE_CASE//2+5, ((a+12)*TAILLE_CASE)+TAILLE_CASE//2+5, fill='yellow', outline='black')
            # on remonte le cache du plateau
            cnv2.tag_raise(cache_plat2)
            # incrémentation de la case correspondante dans la matrice des 2 joueurs
            case_plat2[a][b]+=1
            case_plat1[a+10][b]+=1
            # on retient le rond dans les listes de tirs
            tire1.append(t1)
            tire2.append(t2)
            # on passe la main au joueur
            joueur()
            # fonction de test de bateau coulé
            test_coulé()
        # idem si la case est occupé par un bateau
        elif case_plat2[a][b]!=0 and case_plat2[a][b]%2==0:
            t1=cnv2.create_oval(((b+1)*TAILLE_CASE)+TAILLE_CASE//2-5, ((a+1)*TAILLE_CASE)+TAILLE_CASE//2-5, ((b+1)*TAILLE_CASE)+TAILLE_CASE//2+5, ((a+1)*TAILLE_CASE)+TAILLE_CASE//2+5, fill='red', outline='black')
            t2=cnv1.create_oval(((b+1)*TAILLE_CASE)+TAILLE_CASE//2-5, ((a+12)*TAILLE_CASE)+TAILLE_CASE//2-5, ((b+1)*TAILLE_CASE)+TAILLE_CASE//2+5, ((a+12)*TAILLE_CASE)+TAILLE_CASE//2+5, fill='red', outline='black')
            cnv2.tag_raise(cache_plat2)
            case_plat2[a][b]+=1
            case_plat1[a+10][b]+=1
            tire1.append(t1)
            tire2.append(t2)
            joueur()
            test_coulé()
        # si la case à déja été ciblé par un tir, on relance la fonction
        else :
            rnd_tire()

    if mode==1:
        # si la case est occupé par un bateaux et que cette case est touchée
        if case_plat2[a][b]%2==1:
            rnd_tire()
        # si la case ciblé est vide
        elif case_plat2[a][b]==0:
            # si une case à coté à déja été ciblé par un tir, on relance la fonction
            if (b==0 and a!=0 and a!=9 and (case_plat2[a-1][b]%2==1 or case_plat2[a+1][b]%2==1 or case_plat2[a][b+1]%2==1)) or (b==0 and a==0 and (case_plat2[a+1][b]%2==1 or case_plat2[a][b+1]%2==1)) or (b==0 and a==9 and (case_plat2[a-1][b]%2==1 and case_plat2[a][b+1]%2==1)) or (b==9 and a!=0 and a!=9 and (case_plat2[a-1][b]%2==1 or case_plat2[a+1][b]%2==1 or case_plat2[a][b-1]%2==1)) or (b==9 and a==0 and (case_plat2[a+1][b]%2==1 or case_plat2[a][b-1]%2==1)) or (b==9 and a==9 and (case_plat2[a-1][b]%2==1 or case_plat2[a][b-1]%2==1)) or (a==9 and b!=0 and b!=9 and (case_plat2[a-1][b]%2==1 or case_plat2[a][b-1]%2==1 or case_plat2[a][b+1]%2==1)) or (a==0 and b!=0 and b!=9 and (case_plat2[a+1][b]%2==1 or case_plat2[a][b-1]%2==1 or case_plat2[a][b+1]%2==1)) or (a!=0 and a!=9 and b!=0 and b!=9 and (case_plat2[a-1][b]%2==1 or case_plat2[a+1][b]%2==1 or case_plat2[a][b-1]%2==1 or case_plat2[a][b+1]%2==1)):
                rnd_tire()
            # sinon, tir
            else :
                t1=cnv2.create_oval(((b+1)*TAILLE_CASE)+TAILLE_CASE//2-5, ((a+1)*TAILLE_CASE)+TAILLE_CASE//2-5, ((b+1)*TAILLE_CASE)+TAILLE_CASE//2+5, ((a+1)*TAILLE_CASE)+TAILLE_CASE//2+5, fill='yellow', outline='black')
                t2=cnv1.create_oval(((b+1)*TAILLE_CASE)+TAILLE_CASE//2-5, ((a+12)*TAILLE_CASE)+TAILLE_CASE//2-5, ((b+1)*TAILLE_CASE)+TAILLE_CASE//2+5, ((a+12)*TAILLE_CASE)+TAILLE_CASE//2+5, fill='yellow', outline='black')
                cnv2.tag_raise(cache_plat2)
                case_plat2[a][b]+=1
                case_plat1[a+10][b]+=1
                tire1.append(t1)
                tire2.append(t2)
                joueur()
                test_coulé()
        # si la case est occupée par un bateau
        else :
            t1=cnv2.create_oval(((b+1)*TAILLE_CASE)+TAILLE_CASE//2-5, ((a+1)*TAILLE_CASE)+TAILLE_CASE//2-5, ((b+1)*TAILLE_CASE)+TAILLE_CASE//2+5, ((a+1)*TAILLE_CASE)+TAILLE_CASE//2+5, fill='red', outline='black')
            t2=cnv1.create_oval(((b+1)*TAILLE_CASE)+TAILLE_CASE//2-5, ((a+12)*TAILLE_CASE)+TAILLE_CASE//2-5, ((b+1)*TAILLE_CASE)+TAILLE_CASE//2+5, ((a+12)*TAILLE_CASE)+TAILLE_CASE//2+5, fill='red', outline='black')
            cnv2.tag_raise(cache_plat2)
            case_plat2[a][b]+=1
            case_plat1[a+10][b]+=1
            tire1.append(t1)
            tire2.append(t2)
            joueur()
            test_coulé()

def recommencer():
    global start, joueur_actif
    global port1, port2, crois1, crois2, ctorp11, ctorp12, ctorp21, ctorp22, torp1, torp2
    
    # réinitialisation de la variable déterminant si le jeu à démarré
    start=0

    # suppression des tirs et de leurs "images"
    for i in range(len(tire1)):
        cnv1.delete(tire1[i])
    tire1.clear()
    for i in range(len(tire2)):
        cnv2.delete(tire2[i])
    tire2.clear()

    # remise à 0 de case des matrices
    for i in range(NB_CASE_HAUT-2):
        for j in range(NB_CASE_LARGE-1):
            case_plat1[i][j]=0
            case_plat2[i][j]=0

    # réinitialisation des listes d'orientation des bateaux
    for i in range(len(pbateau1)):
        pbateau1[i]=0
        pbateau2[i]=0
    
    # replacement des bateaux à leurs coordonnés d'origine
    cnv1.coords(porteavion,x0,12*TAILLE_CASE,x0+5*TAILLE_CASE,TAILLE_CASE*12+TAILLE_CASE)
    cnv1.coords(croiseur,x0,TAILLE_CASE*14,x0+4*TAILLE_CASE,TAILLE_CASE*14+TAILLE_CASE)
    cnv1.coords(cttorpil1,x0,TAILLE_CASE*16,x0+3*TAILLE_CASE,TAILLE_CASE*16+TAILLE_CASE)
    cnv1.coords(cttorpil2,x0,TAILLE_CASE*18,x0+3*TAILLE_CASE,TAILLE_CASE*18+TAILLE_CASE)
    cnv1.coords(torpilleur,x0,TAILLE_CASE*20,x0+2*TAILLE_CASE,TAILLE_CASE*20+TAILLE_CASE)
    cnv2.coords(porteavion,x0,12*TAILLE_CASE,x0+5*TAILLE_CASE,TAILLE_CASE*12+TAILLE_CASE)
    cnv2.coords(croiseur,x0,TAILLE_CASE*14,x0+4*TAILLE_CASE,TAILLE_CASE*14+TAILLE_CASE)
    cnv2.coords(cttorpil1,x0,TAILLE_CASE*16,x0+3*TAILLE_CASE,TAILLE_CASE*16+TAILLE_CASE)
    cnv2.coords(cttorpil2,x0,TAILLE_CASE*18,x0+3*TAILLE_CASE,TAILLE_CASE*18+TAILLE_CASE)
    cnv2.coords(torpilleur,x0,TAILLE_CASE*20,x0+2*TAILLE_CASE,TAILLE_CASE*20+TAILLE_CASE)
    
    # suppression des "images" des bateaux en grille haute
    cnv1.delete(port1)
    cnv1.delete(crois1)
    cnv1.delete(ctorp11)
    cnv1.delete(ctorp21)
    cnv1.delete(torp1)
    cnv2.delete(port2)
    cnv2.delete(crois2)
    cnv2.delete(ctorp12)
    cnv2.delete(ctorp22)
    cnv2.delete(torp2)

    joueur_actif=1
    
    # suppresion des possibilités d'interraction du joueur 2, on les donnes au joueurs 1
    if jeu == 1 :
        cnv1.bind("<B1-Motion>",glisser)
        cnv1.bind("<Double-Button-1>", tirer)
        cnv1.bind("<Button-1>", clic)
        cnv1.bind("<ButtonRelease-1>",unclic)
        cnv1.bind("<Button-3>",rotation)
    elif jeu == 2 :
        cnv1.bind("<B1-Motion>",glisser)
        cnv1.bind("<Double-Button-1>", tirer)
        cnv1.bind("<Button-1>", clic)
        cnv1.bind("<ButtonRelease-1>",unclic)
        cnv1.bind("<Button-3>",rotation)
        cnv2.unbind("<B1-Motion>")
        cnv2.unbind("<Double-Button-1>")
        cnv2.unbind("<Button-1>")
        cnv2.unbind("<ButtonRelease-1>")
        cnv2.unbind("<Button-3>")
        # réapparition du cache sur le plateau 2
        cnv2.coords(cache_plat2, 0, 0, CANVAS_TAILLE, CANVAS_TAILLE)
        cnv2.tag_raise(cache_plat2)
        cnv1.coords(cache_plat1, 0, 0, 0, 0)

def commencer():
    global start, joueur_actif, jeu
    global pos_port1, pos_port2, pos_croi1, pos_croi2, pos_ctorp11, pos_ctorp12, pos_ctorp21, pos_ctorp22, pos_torp1, pos_torp2
    global port1, port2, crois1, crois2, ctorp11, ctorp12, ctorp21, ctorp22, torp1, torp2
    global m1, m2

    # la variable déterminant si le jeu à commencer passe à 1
    start=1
    # on supprime le bateau "commmencé"
    bouton5.pack_forget()

    # suppression du message d'indication du placement des bateaux
    cnv1.delete(m1)
    cnv2.delete(m2)
    
    # si le jeu solo a été sélectionné
    if jeu==1:
        # appel de la fonction de placement aléatoire des bateaux du joueur ordinateur
        rnd_bateau()

    # Placement de la liste de bateau dans la matrice du plateau 1
    if pbateau1[0] == 0:
        # si le porteavion est à l'horizontale
        for i in range (5):
            case_plat1[int((pos_port1[1]//TAILLE_CASE)-2)][int((pos_port1[0]//TAILLE_CASE)-1)+i]+=2
            case_plat2[int((pos_port1[1]//TAILLE_CASE)-12)][int((pos_port1[0]//TAILLE_CASE)-1)+i]+=2
    elif pbateau1[0] == 1:
        for i in range (5):
        # si le porteavion est à la verticale
            case_plat1[int((pos_port1[1]//TAILLE_CASE)-2)+i][int((pos_port1[0]//TAILLE_CASE)-1)]+=2
            case_plat2[int((pos_port1[1]//TAILLE_CASE)-12)+i][int((pos_port1[0]//TAILLE_CASE)-1)]+=2
    
    if pbateau1[1] == 0:
        for j in range (4):
        # idem croiseur horizontale...
            case_plat1[int((pos_croi1[1]//TAILLE_CASE)-2)][int((pos_croi1[0]//TAILLE_CASE)-1)+j]+=4
            case_plat2[int((pos_croi1[1]//TAILLE_CASE)-12)][int((pos_croi1[0]//TAILLE_CASE)-1)+j]+=4
    elif pbateau1[1] == 1:
        for j in range (4):
            case_plat1[int((pos_croi1[1]//TAILLE_CASE)-2)+j][int((pos_croi1[0]//TAILLE_CASE)-1)]+=4
            case_plat2[int((pos_croi1[1]//TAILLE_CASE)-12)+j][int((pos_croi1[0]//TAILLE_CASE)-1)]+=4
     
    if pbateau1[2] == 0:
        for j in range (3):
            case_plat1[int((pos_ctorp11[1]//TAILLE_CASE)-2)][int((pos_ctorp11[0]//TAILLE_CASE)-1)+j]+=6
            case_plat2[int((pos_ctorp11[1]//TAILLE_CASE)-12)][int((pos_ctorp11[0]//TAILLE_CASE)-1)+j]+=6
    elif pbateau1[2] == 1:
        for j in range (3):
            case_plat1[int((pos_ctorp11[1]//TAILLE_CASE)-2)+j][int((pos_ctorp11[0]//TAILLE_CASE)-1)]+=6
            case_plat2[int((pos_ctorp11[1]//TAILLE_CASE)-12)+j][int((pos_ctorp11[0]//TAILLE_CASE)-1)]+=6
            
    if pbateau1[3] == 0:
        for j in range (3):
            case_plat1[int((pos_ctorp21[1]//TAILLE_CASE)-2)][int((pos_ctorp21[0]//TAILLE_CASE)-1)+j]+=8
            case_plat2[int((pos_ctorp21[1]//TAILLE_CASE)-12)][int((pos_ctorp21[0]//TAILLE_CASE)-1)+j]+=8
    elif pbateau1[3] == 1:
        for j in range (3):
            case_plat1[int((pos_ctorp21[1]//TAILLE_CASE)-2)+j][int((pos_ctorp21[0]//TAILLE_CASE)-1)]+=8
            case_plat2[int((pos_ctorp21[1]//TAILLE_CASE)-12)+j][int((pos_ctorp21[0]//TAILLE_CASE)-1)]+=8
    
    if pbateau1[4] == 0:
        for j in range (2):
            case_plat1[int((pos_torp1[1]//TAILLE_CASE)-2)][int((pos_torp1[0]//TAILLE_CASE)-1)+j]+=10
            case_plat2[int((pos_torp1[1]//TAILLE_CASE)-12)][int((pos_torp1[0]//TAILLE_CASE)-1)+j]+=10
    elif pbateau1[4] == 1:
        for j in range (2):
            case_plat1[int((pos_torp1[1]//TAILLE_CASE)-2)+j][int((pos_torp1[0]//TAILLE_CASE)-1)]+=10
            case_plat2[int((pos_torp1[1]//TAILLE_CASE)-12)+j][int((pos_torp1[0]//TAILLE_CASE)-1)]+=10

    # Idem de la liste de bateau dans la matrice du plateau 2...
    if pbateau2[0] == 0:
        for i in range (5):
            case_plat2[int((pos_port2[1]//TAILLE_CASE)-2)][int((pos_port2[0]//TAILLE_CASE)-1)+i]+=2
            case_plat1[int((pos_port2[1]//TAILLE_CASE)-12)][int((pos_port2[0]//TAILLE_CASE)-1)+i]+=2
    elif pbateau2[0] == 1:
        for i in range (5):
            case_plat2[int((pos_port2[1]//TAILLE_CASE)-2)+i][int((pos_port2[0]//TAILLE_CASE)-1)]+=2
            case_plat1[int((pos_port2[1]//TAILLE_CASE)-12)+i][int((pos_port2[0]//TAILLE_CASE)-1)]+=2

    if pbateau2[1] == 0:
        for j in range (4):
            case_plat2[int((pos_croi2[1]//TAILLE_CASE)-2)][int((pos_croi2[0]//TAILLE_CASE)-1)+j]+=4
            case_plat1[int((pos_croi2[1]//TAILLE_CASE)-12)][int((pos_croi2[0]//TAILLE_CASE)-1)+j]+=4
    elif pbateau2[1] == 1:
        for j in range (4):
            case_plat2[int((pos_croi2[1]//TAILLE_CASE)-2)+j][int((pos_croi2[0]//TAILLE_CASE)-1)]+=4
            case_plat1[int((pos_croi2[1]//TAILLE_CASE)-12)+j][int((pos_croi2[0]//TAILLE_CASE)-1)]+=4
     
    if pbateau2[2] == 0:
        for j in range (3):
            case_plat2[int((pos_ctorp12[1]//TAILLE_CASE)-2)][int((pos_ctorp12[0]//TAILLE_CASE)-1)+j]+=6
            case_plat1[int((pos_ctorp12[1]//TAILLE_CASE)-12)][int((pos_ctorp12[0]//TAILLE_CASE)-1)+j]+=6
    elif pbateau2[2] == 1:
        for j in range (3):
            case_plat2[int((pos_ctorp12[1]//TAILLE_CASE)-2)+j][int((pos_ctorp12[0]//TAILLE_CASE)-1)]+=6
            case_plat1[int((pos_ctorp12[1]//TAILLE_CASE)-12)+j][int((pos_ctorp12[0]//TAILLE_CASE)-1)]+=6
            
    if pbateau2[3] == 0:
        for j in range (3):
            case_plat2[int((pos_ctorp22[1]//TAILLE_CASE)-2)][int((pos_ctorp22[0]//TAILLE_CASE)-1)+j]+=8
            case_plat1[int((pos_ctorp22[1]//TAILLE_CASE)-12)][int((pos_ctorp22[0]//TAILLE_CASE)-1)+j]+=8
    elif pbateau2[3] == 1:
        for j in range (3):
            case_plat2[int((pos_ctorp22[1]//TAILLE_CASE)-2)+j][int((pos_ctorp22[0]//TAILLE_CASE)-1)]+=8
            case_plat1[int((pos_ctorp22[1]//TAILLE_CASE)-12)+j][int((pos_ctorp22[0]//TAILLE_CASE)-1)]+=8
    
    if pbateau2[4] == 0:
        for j in range (2):
            case_plat2[int((pos_torp2[1]//TAILLE_CASE)-2)][int((pos_torp2[0]//TAILLE_CASE)-1)+j]+=10
            case_plat1[int((pos_torp2[1]//TAILLE_CASE)-12)][int((pos_torp2[0]//TAILLE_CASE)-1)+j]+=10
    elif pbateau2[4] == 1:
        for j in range (2):
            case_plat2[int((pos_torp2[1]//TAILLE_CASE)-2)+j][int((pos_torp2[0]//TAILLE_CASE)-1)]+=10
            case_plat1[int((pos_torp2[1]//TAILLE_CASE)-12)+j][int((pos_torp2[0]//TAILLE_CASE)-1)]+=10

    # création de "copies" invisibles des bateaux du joueurs 2 dans la matrice haute du joueurs 1
    port1=cnv1.create_rectangle(pos_port2[0], pos_port2[1]-TAILLE_CASE*11, pos_port2[2], pos_port2[3]-TAILLE_CASE*11, fill='',outline='')
    crois1=cnv1.create_rectangle(pos_croi2[0], pos_croi2[1]-TAILLE_CASE*11, pos_croi2[2], pos_croi2[3]-TAILLE_CASE*11, fill='',outline='')
    ctorp11=cnv1.create_rectangle(pos_ctorp12[0], pos_ctorp12[1]-TAILLE_CASE*11, pos_ctorp12[2], pos_ctorp12[3]-TAILLE_CASE*11, fill='',outline='')
    ctorp21=cnv1.create_rectangle(pos_ctorp22[0], pos_ctorp22[1]-TAILLE_CASE*11, pos_ctorp22[2], pos_ctorp22[3]-TAILLE_CASE*11, fill='',outline='')
    torp1=cnv1.create_rectangle(pos_torp2[0], pos_torp2[1]-TAILLE_CASE*11, pos_torp2[2], pos_torp2[3]-TAILLE_CASE*11, fill='',outline='')
    # inversement...   
    port2=cnv2.create_rectangle(pos_port1[0], pos_port1[1]-TAILLE_CASE*11, pos_port1[2], pos_port1[3]-TAILLE_CASE*11, fill='',outline='')
    crois2=cnv2.create_rectangle(pos_croi1[0], pos_croi1[1]-TAILLE_CASE*11, pos_croi1[2], pos_croi1[3]-TAILLE_CASE*11, fill='',outline='')
    ctorp12=cnv2.create_rectangle(pos_ctorp11[0], pos_ctorp11[1]-TAILLE_CASE*11, pos_ctorp11[2], pos_ctorp11[3]-TAILLE_CASE*11, fill='',outline='')
    ctorp22=cnv2.create_rectangle(pos_ctorp21[0], pos_ctorp21[1]-TAILLE_CASE*11, pos_ctorp21[2], pos_ctorp21[3]-TAILLE_CASE*11, fill='',outline='')
    torp2=cnv2.create_rectangle(pos_torp1[0], pos_torp1[1]-TAILLE_CASE*11, pos_torp1[2], pos_torp1[3]-TAILLE_CASE*11, fill='',outline='')

    # tirage au sort pour savoir quelle joueur commence si le jeu est en solo
    if jeu==1:
        joueur_actif=randint(0,1)
        if joueur_actif==0:
            # génération du texte indiquant quelle joueur commence
            msg1="\nL'adversaire\ncommence\n "
        elif joueur_actif==1:
            msg1="\nLe joueur " + str(joueur_actif) + "\ncommence\n "
        if joueur_actif==0:
            joueur_actif=1
        elif joueur_actif==1:
            joueur_actif=0
    # idem si le jeu est en mode deux joueurs
    elif jeu==2:
        joueur_actif=randint(1,2)
        msg1="\nLe joueur " + str(joueur_actif) + "\ncommence\n "
        if joueur_actif==1:
            joueur_actif=2
        elif joueur_actif==2:
            joueur_actif=1
    
    # création du texte indiquant quelle joueur commence
    texte = Label(master, text=msg1)
    texte.config(bg="red")
    texte.pack()
    # délai avant disparition du texte
    master.after(4000, texte.pack_forget)

    # fonction pour donner la possibilité d'interaction au joueur actif
    joueur()

def pret():
    # bouton pour le mode deux joueurs, apparait quand le joueur 1 est pret
    global joueur_actif

    if joueur_actif==1:
        cnv2.unbind("<B1-Motion>")
        cnv2.unbind("<Double-Button-1>")
        cnv2.unbind("<Button-1>")
        cnv2.unbind("<ButtonRelease-1>")
        cnv2.unbind("<Button-3>")
    elif joueur_actif==2:
        cnv1.unbind("<B1-Motion>")
        cnv1.unbind("<Double-Button-1>")
        cnv1.unbind("<Button-1>")
        cnv1.unbind("<ButtonRelease-1>")
        cnv1.unbind("<Button-3>")

    bouton6.pack_forget()

    joueur()

def test_commencer():
    val_test=0
    
    if joueur_actif==1:
        # Test si un bateau est collé à un autre :
        for i in range (len(bateau1)):
            x1, y1, x2, y2 = cnv1.coords(bateau1[i])
            a12, b12, a22, b22 = cnv1.coords(bateau1[i-1])
            a13, b13, a23, b23 = cnv1.coords(bateau1[i-2])
            a14, b14, a24, b24 = cnv1.coords(bateau1[i-3])
            a15, b15, a25, b25 = cnv1.coords(bateau1[i-4])
            # Si deux bateaux sont collé, apparission d'un message d'erreur qui disparait au bout de 4 secondes. + valeur test incrémenté
            if (y2>b12-5 and x1<a22+5 and x2>a12-5 and y1<b22+5) or (y2>b13-5 and x1<a23+5 and x2>a13-5 and y1<b23+5) or (y2>b14-5 and x1<a24+5 and x2>a14-5 and y1<b24+5) or (y2>b15-5 and x1<a25+5 and x2>a15-5 and y1<b25+5):
                msg = Label(cnv1, text="  Attention, vos bateaux doivent être placés à une case d'écart au minimum  ", fg='black', bg='red')
                msg.pack()
                cnv1.create_window(TAILLE_CASE*10, TAILLE_CASE*11, window=msg)
                cnv1.after(4000, msg.destroy)
                val_test+=1
                
        # Test si tout les bateaux sont contenu dans la matrice basse du joueur, sinon, incrémentation de la valeur test
        x1, y1, x2, y2 = cnv1.coords(bateau1[0])
        a12, b12, a22, b22 = cnv1.coords(bateau1[1])
        a13, b13, a23, b23 = cnv1.coords(bateau1[2])
        a14, b14, a24, b24 = cnv1.coords(bateau1[3])
        a15, b15, a25, b25 = cnv1.coords(bateau1[4])
        if (TAILLE_CASE<=x1<TAILLE_CASE*11 and TAILLE_CASE*12<=y1) and (TAILLE_CASE<=a12<TAILLE_CASE*11 and TAILLE_CASE*12<=b12) and (TAILLE_CASE<=a13<TAILLE_CASE*11 and TAILLE_CASE*12<=b13) and (TAILLE_CASE<=a14<TAILLE_CASE*11 and TAILLE_CASE*12<=b14) and (TAILLE_CASE<=a15<=TAILLE_CASE*11 and TAILLE_CASE*12<=b15):
            val_test=val_test
        else :
            val_test+=1
        
        # sur le jeu est à deux joueurs
        if jeu==2:
            # si la valeur test est égale à 0, la bouton "Pret" apparait
            if val_test==0:
                bouton6.pack(pady=225)
            else :
                bouton6.pack_forget()
        if jeu==1:
            if val_test==0:
                bouton5.pack(pady=225)
            else :
                bouton5.pack_forget()
    
    # idem joueur 2...
    elif joueur_actif==2:
        for i in range (len(bateau2)):
            x1, y1, x2, y2 = cnv2.coords(bateau2[i])
            a12, b12, a22, b22 = cnv2.coords(bateau2[i-1])
            a13, b13, a23, b23 = cnv2.coords(bateau2[i-2])
            a14, b14, a24, b24 = cnv2.coords(bateau2[i-3])
            a15, b15, a25, b25 = cnv2.coords(bateau2[i-4])
            if (y2>b12-5 and x1<a22+5 and x2>a12-5 and y1<b22+5) or (y2>b13-5 and x1<a23+5 and x2>a13-5 and y1<b23+5) or (y2>b14-5 and x1<a24+5 and x2>a14-5 and y1<b24+5) or (y2>b15-5 and x1<a25+5 and x2>a15-5 and y1<b25+5):
                msg = Label(cnv2, text="  Attention, vos bateaux doivent être placés à une case d'écart au minimum  ", fg='black', bg='red')
                msg.pack()
                cnv2.create_window(TAILLE_CASE*10, TAILLE_CASE*11, window=msg)
                cnv2.after(4000, msg.destroy)
                val_test+=1
        x1, y1, x2, y2 = cnv2.coords(bateau2[0])
        a12, b12, a22, b22 = cnv2.coords(bateau2[1])
        a13, b13, a23, b23 = cnv2.coords(bateau2[2])
        a14, b14, a24, b24 = cnv2.coords(bateau2[3])
        a15, b15, a25, b25 = cnv2.coords(bateau2[4])
        if (TAILLE_CASE<=x1<TAILLE_CASE*11 and TAILLE_CASE*12<=y1) and (TAILLE_CASE<=a12<TAILLE_CASE*11 and TAILLE_CASE*12<=b12) and (TAILLE_CASE<=a13<TAILLE_CASE*11 and TAILLE_CASE*12<=b13) and (TAILLE_CASE<=a14<TAILLE_CASE*11 and TAILLE_CASE*12<=b14) and (TAILLE_CASE<=a15<=TAILLE_CASE*11 and TAILLE_CASE*12<=b15):
            val_test=val_test
        else :
            val_test+=1
        
        # si la valeur test est égale à 0, la bouton "Commencer" apparait
        if val_test==0:
            bouton5.pack(pady=225)
        else :
            bouton5.pack_forget()

def test_coulé():
    global compt_port1, compt_port2, compt_croi1, compt_croi2, compt_ctorp11, compt_ctorp12, compt_ctorp21, compt_ctorp22, compt_torp1, compt_torp2
    global port1, port2, crois1, crois2, ctorp11, ctorp12, ctorp21, ctorp22, torp1, torp2
    global stat_port1, stat_port2, stat_crois1, stat_crois2, stat_ctorp11, stat_ctorp12, stat_ctorp21, stat_ctorp22, stat_torp1, stat_torp2

    stat_port1 = stat_port2 = stat_crois1 = stat_crois2 = stat_ctorp11 = stat_ctorp12 = stat_ctorp21 = stat_ctorp22 = stat_torp1 = stat_torp2 = "À flot"
    compt_port1 = compt_port2 = compt_croi1 = compt_croi2 = compt_ctorp11 = compt_ctorp12 = compt_ctorp21 = compt_ctorp22 = compt_torp1 = compt_torp2 = 0

    # test de toutes les cases de la matrice haute pour les deux joueurs avec variable de vérification de bateaux touché
    for i in range((NB_CASE_HAUT-2)//2):
        for j in range(NB_CASE_LARGE-1):
            # si une case occupée par le porteavion est à été touché, la variable associé au porteavion gagne +1
            if case_plat1[i][j]==3:
                compt_port2+=1
            # idem pour les autres bateaux...
            elif case_plat1[i][j]==5:
                compt_croi2+=1
            elif case_plat1[i][j]==7:
                compt_ctorp12+=1
            elif case_plat1[i][j]==9:
                compt_ctorp22+=1
            elif case_plat1[i][j]==11:
                compt_torp2+=1
            
            # idem pour la matrice du joueur 2...
            if case_plat2[i][j]==3:
                compt_port1+=1
            elif case_plat2[i][j]==5:
                compt_croi1+=1
            elif case_plat2[i][j]==7:
                compt_ctorp11+=1
            elif case_plat2[i][j]==9:
                compt_ctorp21+=1
            elif case_plat2[i][j]==11:
                compt_torp1+=1
    
    # si la variable de test associé au porteavion du joueur 2 (situé dans la matrice haute du joueur 1) est égale à 5, la bateau apparait
    if compt_port2==5:
        cnv1.itemconfigure(port1, fill="red")
        # "statut" du bateau devient coulé pour le résumé de fin de partie
        stat_port2 = "Coulé"
    # idem pour les autres variable...
    if compt_croi2==4:
        cnv1.itemconfigure(crois1, fill="red")
        stat_crois2 = "Coulé"
    if compt_ctorp12==3:
        cnv1.itemconfigure(ctorp11, fill="red")
        stat_ctorp12 = "Coulé"
    if compt_ctorp22==3:
        cnv1.itemconfigure(ctorp21, fill="red")
        stat_ctorp22 = "Coulé"
    if compt_torp2==2:
        cnv1.itemconfigure(torp1, fill="red")
        stat_torp2 = "Coulé"
    
    # idem pour la matrice du joueur 1...
    if compt_port1==5:
        cnv2.itemconfigure(port2, fill="red")
        stat_port1 = "Coulé"
    if compt_croi1==4:
        cnv2.itemconfigure(crois2, fill="red")
        stat_crois1 = "Coulé"
    if compt_ctorp11==3:
        cnv2.itemconfigure(ctorp12, fill="red")
        stat_ctorp11 = "Coulé"
    if compt_ctorp21==3:
        cnv2.itemconfigure(ctorp22, fill="red")
        stat_ctorp21 = "Coulé"
    if compt_torp1==2:
        cnv2.itemconfigure(torp2, fill="red")
        stat_torp1 = "Coulé"
    
    test_fin()

def test_fin():
    global joueur_actif, start, gagnant, case_plat1, case_plat2, compt_port1, compt_port2, compt_croi1, compt_croi2, compt_ctorp11, compt_ctorp12, compt_ctorp21, compt_ctorp22, compt_torp1, compt_torp2

    # si les tous les bateaux du joueur 2 sont coulé
    if compt_port2 + compt_croi2 + compt_ctorp12 + compt_ctorp22 + compt_torp2 == 17 :
        gagnant=1
        # fonction de fin de jeu
        fin()
    # idem pour les bateaux du joueurs 1
    elif compt_port1 + compt_croi1 + compt_ctorp11 + compt_ctorp21 + compt_torp1 == 17 :
        # si mode deux joueurs
        if jeu==2:
            gagnant=2
            fin()
        # si mode solo
        elif jeu==1:
            gagnant=3
            fin()

    # suppression des commandes pour les 2 joueurs, seul le clic est disponible pour le joueur 1
    if gagnant==1 or gagnant==2:
        if jeu==2:
            if joueur_actif==2:
                joueur_actif=1
                cnv2.unbind("<B1-Motion>")
                cnv2.unbind("<Double-Button-1>")
                cnv2.unbind("<Button-1>")
                cnv2.unbind("<ButtonRelease-1>")
                cnv2.unbind("<Button-3>")
                cnv1.bind("<Button-1>", clic)
            else :
                cnv1.unbind("<B1-Motion>")
                cnv1.unbind("<Double-Button-1>")
                cnv1.unbind("<ButtonRelease-1>")
                cnv1.unbind("<Button-3>")

def joueur():
    # fonction pour donner la possibilité d'interaction au joueur actif
    global joueur_actif, gagnant

    # si il n'y a pas encore de gagnant (jeu en cours)
    if gagnant==0:
        # si mode solo
        if jeu == 1 :
            if joueur_actif==1:
                cnv1.unbind("<B1-Motion>")
                cnv1.unbind("<Double-Button-1>")
                cnv1.unbind("<Button-1>")
                cnv1.unbind("<ButtonRelease-1>")
                cnv1.unbind("<Button-3>")
                cache_plateau()
                joueur_actif=0
                # tir "aléatoire" de l'ordinateur
                rnd_tire()
            elif joueur_actif==0:
                cnv1.bind("<Double-Button-1>", tirer)
                cnv1.bind("<Button-1>", clic)
                joueur_actif=1

        # si le jeu est en mode 2 joueurs
        elif jeu == 2 :
            # si le joueur actif est le joueur 1
            if joueur_actif==1:
                # on donne la possibilité d'interraction au joueur 2
                cnv2.bind("<B1-Motion>",glisser)
                cnv2.bind("<Double-Button-1>", tirer)
                cnv2.bind("<Button-1>", clic)
                cnv2.bind("<ButtonRelease-1>",unclic)
                cnv2.bind("<Button-3>",rotation)
                # on supprime la possibilité d'interraction du joueur 1
                cnv1.unbind("<B1-Motion>")
                cnv1.unbind("<Double-Button-1>")
                cnv1.unbind("<Button-1>")
                cnv1.unbind("<ButtonRelease-1>")
                cnv1.unbind("<Button-3>")
                joueur_actif=2
                cache_plateau()
            # idem si le joueur actif est le joueur 2..
            elif joueur_actif==2: 
                cnv1.bind("<B1-Motion>",glisser)
                cnv1.bind("<Double-Button-1>", tirer)
                cnv1.bind("<Button-1>", clic)
                cnv1.bind("<ButtonRelease-1>",unclic)
                cnv1.bind("<Button-3>",rotation)
                cnv2.unbind("<B1-Motion>")
                cnv2.unbind("<Double-Button-1>")
                cnv2.unbind("<Button-1>")
                cnv2.unbind("<ButtonRelease-1>")
                cnv2.unbind("<Button-3>")
                joueur_actif=1
                cache_plateau()

def cache_plateau():
    # fonction permettant de caché le plateau des deux joueurs jusqu'à ce que le nouveau joueur actif clic sur le bouton "pret" 
    global bouton7

    if jeu==2:
        cnv1.coords(cache_plat1, 0, 0, CANVAS_TAILLE, CANVAS_TAILLE)
        cnv2.coords(cache_plat2, 0, 0, CANVAS_TAILLE, CANVAS_TAILLE)
        bouton7 = Button(master, text=" Joueur " + str(joueur_actif) + " " + "\n prêt ", bg="yellow", fg="red", command=pret1)
        bouton7.pack(pady=225)
    elif jeu==1:
        cache_plat_att

def cache_plat_att():
    # fonction de cache du plateau du joueur non actif
    global joueur_actif

    if joueur_actif==1:
        cnv2.coords(cache_plat2, 0, 0, CANVAS_TAILLE, CANVAS_TAILLE)
        cnv2.tag_raise(cache_plat2)
        cnv1.coords(cache_plat1, 0, 0, 0, 0)
    elif joueur_actif==2:
        cnv1.coords(cache_plat1, 0, 0, CANVAS_TAILLE, CANVAS_TAILLE)
        cnv1.tag_raise(cache_plat1)
        cnv2.coords(cache_plat2, 0, 0, 0, 0)

def pret1():
    # bouton faisant disparaitre le case "d'entre tour" si mode 2 joueurs
    bouton7.pack_forget()
    cache_plat_att()

start=0

if jeu==1 or jeu==2:
    cnv1.bind("<B1-Motion>",glisser)
    cnv1.bind("<Double-Button-1>", tirer)
    cnv1.bind("<Button-1>", clic)
    cnv1.bind("<ButtonRelease-1>",unclic)
    cnv1.bind("<Button-3>",rotation)

cache_plat1=cnv1.create_rectangle(0, 0, 0, 0, fill="black")
cache_plat2=cnv2.create_rectangle(0, 0, CANVAS_TAILLE, CANVAS_TAILLE, fill="black")

bouton3 = Button(master, text="Quitter", bg="grey", fg="white", command=master.destroy)
bouton4 = Button(master, text="Recommencer", bg="grey", fg="white", command=recommencer)
bouton5 = Button(master, text="Commencer", bg="grey", fg="white", command=commencer)
bouton6 = Button(master, text="Prêt", bg="grey", fg="white", command=pret)

if jeu==1 or jeu==2:
    bouton3.pack()
    bouton4.pack()

master.mainloop()