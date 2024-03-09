from tkinter import*
from random import*

global fenetre1
global fenetre2
global fenetre3
jeu=0
joueur_actif=1
gagnant=0
stop=0

def solo():
    global lab, lab2, lab3, bouton0, bouton1, bouton2
    lab.pack_forget()
    lab2.pack_forget()
    lab3.pack_forget()
    bouton0.pack_forget()
    bouton1.pack_forget()
    bouton2.pack_forget()
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
    global jeu, mode
    fenetre1.destroy()
    mode=1
    jeu=1

def facile():
    global jeu, mode
    fenetre1.destroy()
    mode=0
    jeu=1

def deux_joueurs():
    global jeu
    fenetre1.destroy()
    jeu=2

def quitter2():
    global jeu,joueur_actif,start,fenetre2
    jeu=0
    joueur_actif=1
    start=0
    master.destroy()
    fenetre2.destroy()

def quitter1():
    fenetre1.destroy()

def presentation():
    global fenetre1, lab, lab2, lab3, bouton0, bouton1, bouton2

    fenetre1 = Tk()
    fenetre1.title("La bataille navale")
    img_fond=PhotoImage(file="presentation_bt.gif")
    bg_label = Label(fenetre1, image=img_fond)
    bg_label.pack()
    lab= Label(fenetre1, text="Bonjour, bienvenue sur la Bataille Navale !")
    lab.pack()
    lab2= Label(fenetre1, text="Voulez vous")
    lab2.pack()
    bouton0 = Button(fenetre1,text=" Solo ", command=solo)
    bouton1 = Button(fenetre1,text=" Deux joueurs ", command=deux_joueurs)
    bouton2 = Button(fenetre1, text=" Quitter ", command=quitter1) 
    bouton0.pack()
    bouton1.pack()
    bouton2.pack(side=RIGHT)
    lab3= Label(fenetre1, text="Par Lola & Renan")
    lab3.pack(side=LEFT)

    #for i in range (31):
    #    img_fond.configure(format="gif -index " + str(i))
    #    bg_label.after(1, bg_label.update())
    #img_fond.configure(format="gif -index 0")
    #bg_label.update()

    fenetre1.mainloop()

def fin():
    global fenetre2,gagnant,stop
    stop=1
    fenetre2= Tk()
    fenetre2.title("La bataille navale")
    img_fond=PhotoImage(file="presentation_bt.gif")
    bg_label = Label(fenetre2, image=img_fond)
    bg_label.pack()
    if gagnant==1:
        lab= Label(fenetre2, text="Joueur 1 gagne !")
        lab.pack()
    elif gagnant==2:
        lab= Label(fenetre2, text="Joueur 2 gagne !")
        lab.pack()
    lab= Label(fenetre2, text="Voulez-vous")
    lab.pack()
    bouton7 = Button(fenetre2,text=" Rejouer ? ", command=recommencer)
    bouton8 = Button(fenetre2, text=" Quitter ", command=quitter2)
    bouton9 = Button
    bouton7.pack()
    bouton8.pack() 


if __name__ == '__main__':
    presentation()

if jeu==1 or jeu==2:
    master=Tk()
    master.title("La bataille navale")
    #master.iconbitmap('A:\Cours\Projet Python\Projet Python L_R\images\icone_bataille_navale.xbm')

NB_CASE_LARGE=11
NB_CASE_HAUT=22
CANVAS_TAILLE=550+20
TAILLE_CASE=(CANVAS_TAILLE-20)//NB_CASE_LARGE//2
x0=NB_CASE_LARGE*TAILLE_CASE+50
FONT=('Ubuntu',15,'bold')
L=["A","B","C","D","E","F","G","H","I","J"]
old=[None, None]

img_eau = PhotoImage(file="eau.png")

cnv1=Canvas(master, width=CANVAS_TAILLE, height=CANVAS_TAILLE, bg='ivory')
cnv2=Canvas(master, width=CANVAS_TAILLE, height=CANVAS_TAILLE, bg='ivory')
eau=cnv1.create_image(TAILLE_CASE*5, TAILLE_CASE*11, image=img_eau)
eau=cnv2.create_image(TAILLE_CASE*5, TAILLE_CASE*11, image=img_eau)

if jeu==0:
    cnv1.pack_forget()
    cnv2.pack_forget()
else:
    cnv1.pack(side=LEFT, padx=10, pady=10)
    cnv2.pack(side=RIGHT, padx=10, pady=10)

def plateau (cnv, case_plat):
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

port_h = PhotoImage(file="porteavionh.gif")
port_v = PhotoImage(file="porteavionv.gif")
crois_h = PhotoImage(file="croiseurh.gif")
crois_v = PhotoImage(file="croiseurv.gif")
ctt1_h = PhotoImage(file="cttorpilleurh.gif")
ctt1_v = PhotoImage(file="cttorpilleurv.gif")
ctt2_h = PhotoImage(file="cttorpilleur2h.gif")
ctt2_v = PhotoImage(file="cttorpilleur2v.gif")
torp_h = PhotoImage(file="torpilleurh.gif")
torp_v = PhotoImage(file="torpilleurv.gif")

porteavion=cnv1.create_image(x0+TAILLE_CASE, 12*TAILLE_CASE+TAILLE_CASE//2, anchor=NW, image=port_h)
croiseur=cnv1.create_image(x0+TAILLE_CASE, 14*TAILLE_CASE+TAILLE_CASE//2, anchor=NW, image=crois_h)
cttorpil1=cnv1.create_image(x0+TAILLE_CASE, 16*TAILLE_CASE+TAILLE_CASE//2, anchor=NW, image=ctt1_h)
cttorpil2=cnv1.create_image(x0+TAILLE_CASE, 18*TAILLE_CASE+TAILLE_CASE//2, anchor=NW, image=ctt2_h)
torpilleur=cnv1.create_image(x0+TAILLE_CASE, 20*TAILLE_CASE+TAILLE_CASE//2, anchor=NW, image=torp_h)
pporteavion=pcroiseur=pcttorpil1=pcttorpil2=ptorpilleur=0
pbateau1=[pporteavion,pcroiseur,pcttorpil1,pcttorpil2,ptorpilleur]
bateau1=[porteavion,croiseur,cttorpil1,cttorpil2,torpilleur]

porteavion=cnv2.create_image(x0+TAILLE_CASE, 12*TAILLE_CASE+TAILLE_CASE//2, anchor=NW, image=port_h)
croiseur=cnv2.create_image(x0+TAILLE_CASE, 14*TAILLE_CASE+TAILLE_CASE//2, anchor=NW, image=crois_h)
cttorpil1=cnv2.create_image(x0+TAILLE_CASE, 16*TAILLE_CASE+TAILLE_CASE//2, anchor=NW, image=ctt1_h)
cttorpil2=cnv2.create_image(x0+TAILLE_CASE, 18*TAILLE_CASE+TAILLE_CASE//2, anchor=NW, image=ctt2_h)
torpilleur=cnv2.create_image(x0+TAILLE_CASE, 20*TAILLE_CASE+TAILLE_CASE//2, anchor=NW, image=torp_h)
pporteavion=pcroiseur=pcttorpil1=pcttorpil2=ptorpilleur=0
pbateau2=[pporteavion,pcroiseur,pcttorpil1,pcttorpil2,ptorpilleur]
bateau2=[porteavion,croiseur,cttorpil1,cttorpil2,torpilleur]

cnv2.create_text(x0+TAILLE_CASE*2, TAILLE_CASE*11, text= "Joueur 2     ",fill="black",font=('Helvetica 15 bold'))
cnv1.create_text(x0+TAILLE_CASE*2, TAILLE_CASE*11, text= "Joueur 1     ",fill="black",font=('Helvetica 15 bold'))

def clic(event):
    old[0]=event.x
    old[1]=event.y

def unclic(event):
    global pos_port1, pos_port2, pos_croi1, pos_croi2, pos_ctorp11, pos_ctorp12, pos_ctorp21, pos_ctorp22, pos_torp1, pos_torp2
    
    if start==0:
        if joueur_actif==1:
            for i in range (len(bateau1)):
                x1, y1 = cnv1.coords(bateau1[i])
                # si le bateau est le porteavion
                if bateau1[i]==porteavion:
                    # si le porteavion est à l'horizontale
                    if pbateau1[i]==0:
                        # coordonnée du rectangle définissant la surface occupé par le porteavion
                        x2 = x1+TAILLE_CASE*5
                        y2 = y1+TAILLE_CASE
                    # idem si le porteavion est à la vertical
                    elif pbateau1[i]==1:
                        x2 = x1+TAILLE_CASE
                        y2 = y1+TAILLE_CASE*5
                # idem pour le croiseur...
                elif bateau1[i]==croiseur:
                    if pbateau1[i]==0:
                        x2 = x1+TAILLE_CASE*4
                        y2 = y1+TAILLE_CASE
                    elif pbateau1[i]==1:
                        x2 = x1+TAILLE_CASE
                        y2 = y1+TAILLE_CASE*4
                elif bateau1[i]==cttorpil1:
                    if pbateau1[i]==0:
                        x2 = x1+TAILLE_CASE*3
                        y2 = y1+TAILLE_CASE
                    elif pbateau1[i]==1:
                        x2 = x1+TAILLE_CASE
                        y2 = y1+TAILLE_CASE*3
                elif bateau1[i]==cttorpil2:
                    if pbateau1[i]==0:
                        x2 = x1+TAILLE_CASE*3
                        y2 = y1+TAILLE_CASE
                    elif pbateau1[i]==1:
                        x2 = x1+TAILLE_CASE
                        y2 = y1+TAILLE_CASE*3
                elif bateau1[i]==torpilleur:
                    if pbateau1[i]==0:
                        x2 = x1+TAILLE_CASE*2
                        y2 = y1+TAILLE_CASE
                    elif pbateau1[i]==1:
                        x2 = x1+TAILLE_CASE
                        y2 = y1+TAILLE_CASE*2
                # si le curseur de la souris se trouve sur le porteavion
                if (old[0] >= x1 and old[0] <= x2 and old[1] >= y1 and old[1] <= y2):
                    # si le porteavion est à l'horizontale
                    if pbateau1[i]==0:
                        # si le bateau se trouve dans la matrice basse du joueur
                        if bateau1[i]==porteavion and (TAILLE_CASE<x1<7*TAILLE_CASE and y1>12*TAILLE_CASE):
                            # positionnement du bateau dans les case directement en haut à gauche par rapport à la position du porteavion
                            cnv1.move(bateau1[i], (event.x-old[0])-(x1%TAILLE_CASE), (event.y-old[1])-(y1%TAILLE_CASE))
                            # sauvegarde des coordonnées du porteavion
                            pos_port1 = x1, y1, x2, y2
                        # idem si le bateau est le croiseur...
                        elif bateau1[i]==croiseur:
                            if (TAILLE_CASE<x1<8*TAILLE_CASE and y1>12*TAILLE_CASE):
                                cnv1.move(bateau1[i], (event.x-old[0])-(x1%TAILLE_CASE), (event.y-old[1])-(y1%TAILLE_CASE))
                                pos_croi1 = x1, y1, x2, y2
                        elif bateau1[i]==cttorpil1:
                            if (TAILLE_CASE<x1<9*TAILLE_CASE and y1>12*TAILLE_CASE):
                                cnv1.move(bateau1[i], (event.x-old[0])-(x1%TAILLE_CASE), (event.y-old[1])-(y1%TAILLE_CASE))
                                pos_ctorp11 = x1, y1, x2, y2
                        elif bateau1[i]==cttorpil2:
                            if (TAILLE_CASE<x1<9*TAILLE_CASE and y1>12*TAILLE_CASE):
                                cnv1.move(bateau1[i], (event.x-old[0])-(x1%TAILLE_CASE), (event.y-old[1])-(y1%TAILLE_CASE))
                                pos_ctorp21 = x1, y1, x2, y2
                        elif bateau1[i]==torpilleur:
                            if (TAILLE_CASE<x1<10*TAILLE_CASE and y1>12*TAILLE_CASE):
                                cnv1.move(bateau1[i], (event.x-old[0])-(x1%TAILLE_CASE), (event.y-old[1])-(y1%TAILLE_CASE))
                                pos_torp1 = x1, y1, x2, y2
                    # si le bateau est à la verticale
                    elif (TAILLE_CASE<x1<11*TAILLE_CASE and y1>12*TAILLE_CASE) and pbateau1[i]==1:
                        cnv1.move(bateau1[i], (event.x-old[0])-(x1%TAILLE_CASE), (event.y-old[1])-(y1%TAILLE_CASE))
                        if bateau1[i]==porteavion:
                            pos_port1 = x1, y1, x2, y2
                        elif bateau1[i]==croiseur:
                            pos_croi1 = x1, y1, x2, y2
                        elif bateau1[i]==cttorpil1:
                            pos_ctorp11 = x1, y1, x2, y2
                        elif bateau1[i]==cttorpil2:
                            pos_ctorp21 = x1, y1, x2, y2
                        elif bateau1[i]==torpilleur:
                            pos_torp1 = x1, y1, x2, y2
        # si le joueur actif est le joueur 2, puis idem...
        elif joueur_actif==2:
            for i in range (len(bateau2)):
                x1, y1, x2, y2 = cnv2.coords(bateau2[i])
                if (old[0] >= x1 and old[0] <= x2 and old[1] >= y1 and old[1] <= y2):
                    if pbateau2[i]==0:
                        if bateau2[i]==porteavion and (TAILLE_CASE<x1<7*TAILLE_CASE and y1>12*TAILLE_CASE):
                            cnv2.move(bateau2[i], (event.x-old[0])-(x1%TAILLE_CASE), (event.y-old[1])-(y1%TAILLE_CASE))
                            pos_port2 = x1, y1, x2, y2
                        elif bateau2[i]==croiseur:
                            if (TAILLE_CASE<x1<8*TAILLE_CASE and y1>12*TAILLE_CASE):
                                cnv2.move(bateau2[i], (event.x-old[0])-(x1%TAILLE_CASE), (event.y-old[1])-(y1%TAILLE_CASE))
                                pos_croi2 = x1, y1, x2, y2
                        elif bateau2[i]==cttorpil1:
                            if (TAILLE_CASE<x1<9*TAILLE_CASE and y1>12*TAILLE_CASE):
                                cnv2.move(bateau2[i], (event.x-old[0])-(x1%TAILLE_CASE), (event.y-old[1])-(y1%TAILLE_CASE))
                                pos_ctorp12 = x1, y1, x2, y2
                        elif bateau2[i]==cttorpil2:
                            if (TAILLE_CASE<x1<9*TAILLE_CASE and y1>12*TAILLE_CASE):
                                cnv2.move(bateau2[i], (event.x-old[0])-(x1%TAILLE_CASE), (event.y-old[1])-(y1%TAILLE_CASE))
                                pos_ctorp22 = x1, y1, x2, y2
                        elif bateau2[i]==torpilleur:
                            if (TAILLE_CASE<x1<10*TAILLE_CASE and y1>12*TAILLE_CASE):
                                cnv2.move(bateau2[i], (event.x-old[0])-(x1%TAILLE_CASE), (event.y-old[1])-(y1%TAILLE_CASE))
                                pos_torp2 = x1, y1, x2, y2
                    elif (TAILLE_CASE<x1<11*TAILLE_CASE and y1>12*TAILLE_CASE) and pbateau2[i]==1:
                        cnv2.move(bateau2[i], (event.x-old[0])-(x1%TAILLE_CASE), (event.y-old[1])-(y1%TAILLE_CASE))
                        if bateau2[i]==porteavion:
                            pos_port2 = x1, y1, x2, y2
                        elif bateau2[i]==croiseur:
                            pos_croi2 = x1, y1, x2, y2
                        elif bateau2[i]==cttorpil1:
                            pos_ctorp12 = x1, y1, x2, y2
                        elif bateau2[i]==cttorpil2:
                            pos_ctorp22 = x1, y1, x2, y2
                        elif bateau2[i]==torpilleur:
                            pos_torp2 = x1, y1, x2, y2
        
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

def glisser(event):
    if start==0:
        if joueur_actif==1:
            for i in range (len(bateau1)):
                x1, y1 = cnv1.coords(bateau1[i])
                # si le bateau est en position horizontale
                if pbateau1[i]==0:
                    #si le bateau la porteavion et que le curseur se trouve à l'interieur d'un rectangle determiné par un rectangle de coté 1*5
                    if bateau1[i]==porteavion and (old[0] >= x1 and old[0] <= x1+TAILLE_CASE*5 and old[1] >= y1 and old[1] <= y1+TAILLE_CASE):
                        # si le bord d'un des cotés du rectangle atteind le bord du canvas
                        if (x1<5 or y1<5 or x1+TAILLE_CASE*5>CANVAS_TAILLE-5 or y1+TAILLE_CASE>CANVAS_TAILLE-5):
                            # bord gauche
                            if x1<5:
                                cnv1.move(bateau1[i], event.x-old[0]+5, event.y-old[1])
                                old[0]=event.x
                                old[1]=event.y
                            # bord haut
                            elif y1<5:
                                cnv1.move(bateau1[i], event.x-old[0], event.y-old[1]+5)
                                old[0]=event.x
                                old[1]=event.y
                            # bord droit
                            elif x1+TAILLE_CASE*5>CANVAS_TAILLE-5:
                                cnv1.move(bateau1[i], event.x-old[0]-5, event.y-old[1])
                                old[0]=event.x
                                old[1]=event.y
                            # bord bas
                            elif y1+TAILLE_CASE>CANVAS_TAILLE-5:
                                cnv1.move(bateau1[i], event.x-old[0], event.y-old[1]-5)
                                old[0]=event.x
                                old[1]=event.y
                        # si le rectangle se trouve dans le canvas
                        else :
                            cnv1.move(porteavion, event.x-old[0], event.y-old[1])
                            old[0]=event.x
                            old[1]=event.y
                    # idem croiseur, etc...
                    elif bateau1[i]==croiseur and (old[0] >= x1 and old[0] <= x1+TAILLE_CASE*4 and old[1] >= y1 and old[1] <= y1+TAILLE_CASE):
                        if (x1<5 or y1<5 or x1+TAILLE_CASE*4>CANVAS_TAILLE-5 or y1+TAILLE_CASE>CANVAS_TAILLE-5):
                            if x1<5:
                                cnv1.move(bateau1[i], event.x-old[0]+5, event.y-old[1])
                                old[0]=event.x
                                old[1]=event.y
                            elif y1<5:
                                cnv1.move(bateau1[i], event.x-old[0], event.y-old[1]+5)
                                old[0]=event.x
                                old[1]=event.y
                            elif x1+TAILLE_CASE*4>CANVAS_TAILLE-5:
                                cnv1.move(bateau1[i], event.x-old[0]-5, event.y-old[1])
                                old[0]=event.x
                                old[1]=event.y
                            elif y1+TAILLE_CASE>CANVAS_TAILLE-5:
                                cnv1.move(bateau1[i], event.x-old[0], event.y-old[1]-5)
                                old[0]=event.x
                                old[1]=event.y
                        else :
                            cnv1.move(croiseur, event.x-old[0], event.y-old[1])
                            old[0]=event.x
                            old[1]=event.y
                    elif bateau1[i]==cttorpil1 and (old[0] >= x1 and old[0] <= x1+TAILLE_CASE*3 and old[1] >= y1 and old[1] <= y1+TAILLE_CASE):
                        if (x1<5 or y1<5 or x1+TAILLE_CASE*3>CANVAS_TAILLE-5 or y1+TAILLE_CASE>CANVAS_TAILLE-5):
                            if x1<5:
                                cnv1.move(bateau1[i], event.x-old[0]+5, event.y-old[1])
                                old[0]=event.x
                                old[1]=event.y
                            elif y1<5:
                                cnv1.move(bateau1[i], event.x-old[0], event.y-old[1]+5)
                                old[0]=event.x
                                old[1]=event.y
                            elif x1+TAILLE_CASE*3>CANVAS_TAILLE-5:
                                cnv1.move(bateau1[i], event.x-old[0]-5, event.y-old[1])
                                old[0]=event.x
                                old[1]=event.y
                            elif y1+TAILLE_CASE>CANVAS_TAILLE-5:
                                cnv1.move(bateau1[i], event.x-old[0], event.y-old[1]-5)
                                old[0]=event.x
                                old[1]=event.y
                        else :
                            cnv1.move(cttorpil1, event.x-old[0], event.y-old[1])
                            old[0]=event.x
                            old[1]=event.y
                    elif bateau1[i]==cttorpil2 and (old[0] >= x1 and old[0] <= x1+TAILLE_CASE*3 and old[1] >= y1 and old[1] <= y1+TAILLE_CASE):
                        if (x1<5 or y1<5 or x1+TAILLE_CASE*3>CANVAS_TAILLE-5 or y1+TAILLE_CASE>CANVAS_TAILLE-5):
                            if x1<5:
                                cnv1.move(bateau1[i], event.x-old[0]+5, event.y-old[1])
                                old[0]=event.x
                                old[1]=event.y
                            elif y1<5:
                                cnv1.move(bateau1[i], event.x-old[0], event.y-old[1]+5)
                                old[0]=event.x
                                old[1]=event.y
                            elif x1+TAILLE_CASE*3>CANVAS_TAILLE-5:
                                cnv1.move(bateau1[i], event.x-old[0]-5, event.y-old[1])
                                old[0]=event.x
                                old[1]=event.y
                            elif y1+TAILLE_CASE>CANVAS_TAILLE-5:
                                cnv1.move(bateau1[i], event.x-old[0], event.y-old[1]-5)
                                old[0]=event.x
                                old[1]=event.y
                        else :
                            cnv1.move(cttorpil2, event.x-old[0], event.y-old[1])
                            old[0]=event.x
                            old[1]=event.y
                    elif bateau1[i]==torpilleur and (old[0] >= x1 and old[0] <= x1+TAILLE_CASE*2 and old[1] >= y1 and old[1] <= y1+TAILLE_CASE):
                        if (x1<5 or y1<5 or x1+TAILLE_CASE*2>CANVAS_TAILLE-5 or y1+TAILLE_CASE>CANVAS_TAILLE-5):
                            if x1<5:
                                cnv1.move(bateau1[i], event.x-old[0]+5, event.y-old[1])
                                old[0]=event.x
                                old[1]=event.y
                            elif y1<5:
                                cnv1.move(bateau1[i], event.x-old[0], event.y-old[1]+5)
                                old[0]=event.x
                                old[1]=event.y
                            elif x1+TAILLE_CASE*2>CANVAS_TAILLE-5:
                                cnv1.move(bateau1[i], event.x-old[0]-5, event.y-old[1])
                                old[0]=event.x
                                old[1]=event.y
                            elif y1+TAILLE_CASE>CANVAS_TAILLE-5:
                                cnv1.move(bateau1[i], event.x-old[0], event.y-old[1]-5)
                                old[0]=event.x
                                old[1]=event.y
                        else :
                            cnv1.move(torpilleur, event.x-old[0], event.y-old[1])
                            old[0]=event.x
                            old[1]=event.y
                elif pbateau1[i]==1:
                    if bateau1[i]==porteavion and (old[0] >= x1 and old[0] <= x1+TAILLE_CASE and old[1] >= y1 and old[1] <= y1+TAILLE_CASE*5):
                        if x1<5 or y1<5 or x1+TAILLE_CASE>CANVAS_TAILLE-5 or y1+TAILLE_CASE*5>CANVAS_TAILLE-5:
                            if x1<5:
                                cnv1.move(bateau1[i], event.x-old[0]+5, event.y-old[1])
                                old[0]=event.x
                                old[1]=event.y
                            elif y1<5:
                                cnv1.move(bateau1[i], event.x-old[0], event.y-old[1]+5)
                                old[0]=event.x
                                old[1]=event.y
                            elif x1+TAILLE_CASE>CANVAS_TAILLE-5:
                                cnv1.move(bateau1[i], event.x-old[0]-5, event.y-old[1])
                                old[0]=event.x
                                old[1]=event.y
                            elif y1+TAILLE_CASE*5>CANVAS_TAILLE-5:
                                cnv1.move(bateau1[i], event.x-old[0], event.y-old[1]-5)
                                old[0]=event.x
                                old[1]=event.y
                        else :
                            cnv1.move(porteavion, event.x-old[0], event.y-old[1])
                            old[0]=event.x
                            old[1]=event.y
                    elif bateau1[i]==croiseur and (old[0] >= x1 and old[0] <= x1+TAILLE_CASE and old[1] >= y1 and old[1] <= y1+TAILLE_CASE*4):
                        if x1<5 or y1<5 or x1+TAILLE_CASE>CANVAS_TAILLE-5 or y1+TAILLE_CASE*5>CANVAS_TAILLE-5:
                            if x1<5:
                                cnv1.move(bateau1[i], event.x-old[0]+5, event.y-old[1])
                                old[0]=event.x
                                old[1]=event.y
                            elif y1<5:
                                cnv1.move(bateau1[i], event.x-old[0], event.y-old[1]+5)
                                old[0]=event.x
                                old[1]=event.y
                            elif x1+TAILLE_CASE>CANVAS_TAILLE-5:
                                cnv1.move(bateau1[i], event.x-old[0]-5, event.y-old[1])
                                old[0]=event.x
                                old[1]=event.y
                            elif y1+TAILLE_CASE*4>CANVAS_TAILLE-5:
                                cnv1.move(bateau1[i], event.x-old[0], event.y-old[1]-5)
                                old[0]=event.x
                                old[1]=event.y
                        else :
                            cnv1.move(croiseur, event.x-old[0], event.y-old[1])
                            old[0]=event.x
                            old[1]=event.y
                    elif bateau1[i]==cttorpil1 and (old[0] >= x1 and old[0] <= x1+TAILLE_CASE and old[1] >= y1 and old[1] <= y1+TAILLE_CASE*3):
                        if x1<5 or y1<5 or x1+TAILLE_CASE>CANVAS_TAILLE-5 or y1+TAILLE_CASE*5>CANVAS_TAILLE-5:
                            if x1<5:
                                cnv1.move(bateau1[i], event.x-old[0]+5, event.y-old[1])
                                old[0]=event.x
                                old[1]=event.y
                            elif y1<5:
                                cnv1.move(bateau1[i], event.x-old[0], event.y-old[1]+5)
                                old[0]=event.x
                                old[1]=event.y
                            elif x1+TAILLE_CASE>CANVAS_TAILLE-5:
                                cnv1.move(bateau1[i], event.x-old[0]-5, event.y-old[1])
                                old[0]=event.x
                                old[1]=event.y
                            elif y1+TAILLE_CASE*3>CANVAS_TAILLE-5:
                                cnv1.move(bateau1[i], event.x-old[0], event.y-old[1]-5)
                                old[0]=event.x
                                old[1]=event.y
                        else :
                            cnv1.move(cttorpil1, event.x-old[0], event.y-old[1])
                            old[0]=event.x
                            old[1]=event.y
                    elif bateau1[i]==cttorpil2 and (old[0] >= x1 and old[0] <= x1+TAILLE_CASE and old[1] >= y1 and old[1] <= y1+TAILLE_CASE*3):
                        if x1<5 or y1<5 or x1+TAILLE_CASE>CANVAS_TAILLE-5 or y1+TAILLE_CASE*5>CANVAS_TAILLE-5:
                            if x1<5:
                                cnv1.move(bateau1[i], event.x-old[0]+5, event.y-old[1])
                                old[0]=event.x
                                old[1]=event.y
                            elif y1<5:
                                cnv1.move(bateau1[i], event.x-old[0], event.y-old[1]+5)
                                old[0]=event.x
                                old[1]=event.y
                            elif x1+TAILLE_CASE>CANVAS_TAILLE-5:
                                cnv1.move(bateau1[i], event.x-old[0]-5, event.y-old[1])
                                old[0]=event.x
                                old[1]=event.y
                            elif y1+TAILLE_CASE*3>CANVAS_TAILLE-5:
                                cnv1.move(bateau1[i], event.x-old[0], event.y-old[1]-5)
                                old[0]=event.x
                                old[1]=event.y
                        else :
                            cnv1.move(cttorpil2, event.x-old[0], event.y-old[1])
                            old[0]=event.x
                            old[1]=event.y
                    elif bateau1[i]==torpilleur and (old[0] >= x1 and old[0] <= x1+TAILLE_CASE and old[1] >= y1 and old[1] <= y1+TAILLE_CASE*2):
                        if x1<5 or y1<5 or x1+TAILLE_CASE>CANVAS_TAILLE-5 or y1+TAILLE_CASE*5>CANVAS_TAILLE-5:
                            if x1<5:
                                cnv1.move(bateau1[i], event.x-old[0]+5, event.y-old[1])
                                old[0]=event.x
                                old[1]=event.y
                            elif y1<5:
                                cnv1.move(bateau1[i], event.x-old[0], event.y-old[1]+5)
                                old[0]=event.x
                                old[1]=event.y
                            elif x1+TAILLE_CASE>CANVAS_TAILLE-5:
                                cnv1.move(bateau1[i], event.x-old[0]-5, event.y-old[1])
                                old[0]=event.x
                                old[1]=event.y
                            elif y1+TAILLE_CASE*2>CANVAS_TAILLE-5:
                                cnv1.move(bateau1[i], event.x-old[0], event.y-old[1]-5)
                                old[0]=event.x
                                old[1]=event.y
                        else :
                            cnv1.move(torpilleur, event.x-old[0], event.y-old[1])
                            old[0]=event.x
                            old[1]=event.y
        # idem si le bateau est à la vertical
        if joueur_actif==1:
            for i in range (len(bateau2)):
                x1, y1 = cnv2.coords(bateau2[i])
                if pbateau2[i]==0:
                    if bateau2[i]==porteavion and (old[0] >= x1 and old[0] <= x1+TAILLE_CASE*5 and old[1] >= y1 and old[1] <= y1+TAILLE_CASE):
                        if (x1<5 or y1<5 or x1+TAILLE_CASE*5>CANVAS_TAILLE-5 or y1+TAILLE_CASE>CANVAS_TAILLE-5):
                            if x1<5:
                                cnv2.move(bateau2[i], event.x-old[0]+5, event.y-old[1])
                                old[0]=event.x
                                old[1]=event.y
                            elif y1<5:
                                cnv2.move(bateau2[i], event.x-old[0], event.y-old[1]+5)
                                old[0]=event.x
                                old[1]=event.y
                            elif x1+TAILLE_CASE*5>CANVAS_TAILLE-5:
                                cnv2.move(bateau2[i], event.x-old[0]-5, event.y-old[1])
                                old[0]=event.x
                                old[1]=event.y
                            elif y1+TAILLE_CASE>CANVAS_TAILLE-5:
                                cnv2.move(bateau2[i], event.x-old[0], event.y-old[1]-5)
                                old[0]=event.x
                                old[1]=event.y
                        else :
                            cnv2.move(porteavion, event.x-old[0], event.y-old[1])
                            old[0]=event.x
                            old[1]=event.y
                    elif bateau2[i]==croiseur and (old[0] >= x1 and old[0] <= x1+TAILLE_CASE*4 and old[1] >= y1 and old[1] <= y1+TAILLE_CASE):
                        if (x1<5 or y1<5 or x1+TAILLE_CASE*4>CANVAS_TAILLE-5 or y1+TAILLE_CASE>CANVAS_TAILLE-5):
                            if x1<5:
                                cnv2.move(bateau2[i], event.x-old[0]+5, event.y-old[1])
                                old[0]=event.x
                                old[1]=event.y
                            elif y1<5:
                                cnv2.move(bateau2[i], event.x-old[0], event.y-old[1]+5)
                                old[0]=event.x
                                old[1]=event.y
                            elif x1+TAILLE_CASE*4>CANVAS_TAILLE-5:
                                cnv2.move(bateau2[i], event.x-old[0]-5, event.y-old[1])
                                old[0]=event.x
                                old[1]=event.y
                            elif y1+TAILLE_CASE>CANVAS_TAILLE-5:
                                cnv2.move(bateau2[i], event.x-old[0], event.y-old[1]-5)
                                old[0]=event.x
                                old[1]=event.y
                        else :
                            cnv2.move(croiseur, event.x-old[0], event.y-old[1])
                            old[0]=event.x
                            old[1]=event.y
                    elif bateau2[i]==cttorpil1 and (old[0] >= x1 and old[0] <= x1+TAILLE_CASE*3 and old[1] >= y1 and old[1] <= y1+TAILLE_CASE):
                        if (x1<5 or y1<5 or x1+TAILLE_CASE*3>CANVAS_TAILLE-5 or y1+TAILLE_CASE>CANVAS_TAILLE-5):
                            if x1<5:
                                cnv2.move(bateau2[i], event.x-old[0]+5, event.y-old[1])
                                old[0]=event.x
                                old[1]=event.y
                            elif y1<5:
                                cnv2.move(bateau2[i], event.x-old[0], event.y-old[1]+5)
                                old[0]=event.x
                                old[1]=event.y
                            elif x1+TAILLE_CASE*3>CANVAS_TAILLE-5:
                                cnv2.move(bateau2[i], event.x-old[0]-5, event.y-old[1])
                                old[0]=event.x
                                old[1]=event.y
                            elif y1+TAILLE_CASE>CANVAS_TAILLE-5:
                                cnv2.move(bateau2[i], event.x-old[0], event.y-old[1]-5)
                                old[0]=event.x
                                old[1]=event.y
                        else :
                            cnv2.move(cttorpil1, event.x-old[0], event.y-old[1])
                            old[0]=event.x
                            old[1]=event.y
                    elif bateau2[i]==cttorpil2 and (old[0] >= x1 and old[0] <= x1+TAILLE_CASE*3 and old[1] >= y1 and old[1] <= y1+TAILLE_CASE):
                        if (x1<5 or y1<5 or x1+TAILLE_CASE*3>CANVAS_TAILLE-5 or y1+TAILLE_CASE>CANVAS_TAILLE-5):
                            if x1<5:
                                cnv2.move(bateau2[i], event.x-old[0]+5, event.y-old[1])
                                old[0]=event.x
                                old[1]=event.y
                            elif y1<5:
                                cnv2.move(bateau2[i], event.x-old[0], event.y-old[1]+5)
                                old[0]=event.x
                                old[1]=event.y
                            elif x1+TAILLE_CASE*3>CANVAS_TAILLE-5:
                                cnv2.move(bateau2[i], event.x-old[0]-5, event.y-old[1])
                                old[0]=event.x
                                old[1]=event.y
                            elif y1+TAILLE_CASE>CANVAS_TAILLE-5:
                                cnv2.move(bateau2[i], event.x-old[0], event.y-old[1]-5)
                                old[0]=event.x
                                old[1]=event.y
                        else :
                            cnv2.move(cttorpil2, event.x-old[0], event.y-old[1])
                            old[0]=event.x
                            old[1]=event.y
                    elif bateau2[i]==torpilleur and (old[0] >= x1 and old[0] <= x1+TAILLE_CASE*2 and old[1] >= y1 and old[1] <= y1+TAILLE_CASE):
                        if (x1<5 or y1<5 or x1+TAILLE_CASE*2>CANVAS_TAILLE-5 or y1+TAILLE_CASE>CANVAS_TAILLE-5):
                            if x1<5:
                                cnv2.move(bateau2[i], event.x-old[0]+5, event.y-old[1])
                                old[0]=event.x
                                old[1]=event.y
                            elif y1<5:
                                cnv2.move(bateau2[i], event.x-old[0], event.y-old[1]+5)
                                old[0]=event.x
                                old[1]=event.y
                            elif x1+TAILLE_CASE*2>CANVAS_TAILLE-5:
                                cnv2.move(bateau2[i], event.x-old[0]-5, event.y-old[1])
                                old[0]=event.x
                                old[1]=event.y
                            elif y1+TAILLE_CASE>CANVAS_TAILLE-5:
                                cnv2.move(bateau2[i], event.x-old[0], event.y-old[1]-5)
                                old[0]=event.x
                                old[1]=event.y
                        else :
                            cnv2.move(torpilleur, event.x-old[0], event.y-old[1])
                            old[0]=event.x
                            old[1]=event.y
                elif pbateau2[i]==1:
                    if bateau2[i]==porteavion and (old[0] >= x1 and old[0] <= x1+TAILLE_CASE and old[1] >= y1 and old[1] <= y1+TAILLE_CASE*5):
                        if x1<5 or y1<5 or x1+TAILLE_CASE>CANVAS_TAILLE-5 or y1+TAILLE_CASE*5>CANVAS_TAILLE-5:
                            if x1<5:
                                cnv2.move(bateau2[i], event.x-old[0]+5, event.y-old[1])
                                old[0]=event.x
                                old[1]=event.y
                            elif y1<5:
                                cnv2.move(bateau2[i], event.x-old[0], event.y-old[1]+5)
                                old[0]=event.x
                                old[1]=event.y
                            elif x1+TAILLE_CASE>CANVAS_TAILLE-5:
                                cnv2.move(bateau2[i], event.x-old[0]-5, event.y-old[1])
                                old[0]=event.x
                                old[1]=event.y
                            elif y1+TAILLE_CASE*5>CANVAS_TAILLE-5:
                                cnv2.move(bateau2[i], event.x-old[0], event.y-old[1]-5)
                                old[0]=event.x
                                old[1]=event.y
                        else :
                            cnv2.move(porteavion, event.x-old[0], event.y-old[1])
                            old[0]=event.x
                            old[1]=event.y
                    elif bateau2[i]==croiseur and (old[0] >= x1 and old[0] <= x1+TAILLE_CASE and old[1] >= y1 and old[1] <= y1+TAILLE_CASE*4):
                        if x1<5 or y1<5 or x1+TAILLE_CASE>CANVAS_TAILLE-5 or y1+TAILLE_CASE*5>CANVAS_TAILLE-5:
                            if x1<5:
                                cnv2.move(bateau2[i], event.x-old[0]+5, event.y-old[1])
                                old[0]=event.x
                                old[1]=event.y
                            elif y1<5:
                                cnv2.move(bateau2[i], event.x-old[0], event.y-old[1]+5)
                                old[0]=event.x
                                old[1]=event.y
                            elif x1+TAILLE_CASE>CANVAS_TAILLE-5:
                                cnv2.move(bateau2[i], event.x-old[0]-5, event.y-old[1])
                                old[0]=event.x
                                old[1]=event.y
                            elif y1+TAILLE_CASE*4>CANVAS_TAILLE-5:
                                cnv2.move(bateau2[i], event.x-old[0], event.y-old[1]-5)
                                old[0]=event.x
                                old[1]=event.y
                        else :
                            cnv2.move(croiseur, event.x-old[0], event.y-old[1])
                            old[0]=event.x
                            old[1]=event.y
                    elif bateau2[i]==cttorpil1 and (old[0] >= x1 and old[0] <= x1+TAILLE_CASE and old[1] >= y1 and old[1] <= y1+TAILLE_CASE*3):
                        if x1<5 or y1<5 or x1+TAILLE_CASE>CANVAS_TAILLE-5 or y1+TAILLE_CASE*5>CANVAS_TAILLE-5:
                            if x1<5:
                                cnv2.move(bateau2[i], event.x-old[0]+5, event.y-old[1])
                                old[0]=event.x
                                old[1]=event.y
                            elif y1<5:
                                cnv2.move(bateau2[i], event.x-old[0], event.y-old[1]+5)
                                old[0]=event.x
                                old[1]=event.y
                            elif x1+TAILLE_CASE>CANVAS_TAILLE-5:
                                cnv2.move(bateau2[i], event.x-old[0]-5, event.y-old[1])
                                old[0]=event.x
                                old[1]=event.y
                            elif y1+TAILLE_CASE*3>CANVAS_TAILLE-5:
                                cnv2.move(bateau2[i], event.x-old[0], event.y-old[1]-5)
                                old[0]=event.x
                                old[1]=event.y
                        else :
                            cnv2.move(cttorpil1, event.x-old[0], event.y-old[1])
                            old[0]=event.x
                            old[1]=event.y
                    elif bateau2[i]==cttorpil2 and (old[0] >= x1 and old[0] <= x1+TAILLE_CASE and old[1] >= y1 and old[1] <= y1+TAILLE_CASE*3):
                        if x1<5 or y1<5 or x1+TAILLE_CASE>CANVAS_TAILLE-5 or y1+TAILLE_CASE*5>CANVAS_TAILLE-5:
                            if x1<5:
                                cnv2.move(bateau2[i], event.x-old[0]+5, event.y-old[1])
                                old[0]=event.x
                                old[1]=event.y
                            elif y1<5:
                                cnv2.move(bateau2[i], event.x-old[0], event.y-old[1]+5)
                                old[0]=event.x
                                old[1]=event.y
                            elif x1+TAILLE_CASE>CANVAS_TAILLE-5:
                                cnv2.move(bateau2[i], event.x-old[0]-5, event.y-old[1])
                                old[0]=event.x
                                old[1]=event.y
                            elif y1+TAILLE_CASE*3>CANVAS_TAILLE-5:
                                cnv2.move(bateau2[i], event.x-old[0], event.y-old[1]-5)
                                old[0]=event.x
                                old[1]=event.y
                        else :
                            cnv2.move(cttorpil2, event.x-old[0], event.y-old[1])
                            old[0]=event.x
                            old[1]=event.y
                    elif bateau2[i]==torpilleur and (old[0] >= x1 and old[0] <= x1+TAILLE_CASE and old[1] >= y1 and old[1] <= y1+TAILLE_CASE*2):
                        if x1<5 or y1<5 or x1+TAILLE_CASE>CANVAS_TAILLE-5 or y1+TAILLE_CASE*5>CANVAS_TAILLE-5:
                            if x1<5:
                                cnv2.move(bateau2[i], event.x-old[0]+5, event.y-old[1])
                                old[0]=event.x
                                old[1]=event.y
                            elif y1<5:
                                cnv2.move(bateau2[i], event.x-old[0], event.y-old[1]+5)
                                old[0]=event.x
                                old[1]=event.y
                            elif x1+TAILLE_CASE>CANVAS_TAILLE-5:
                                cnv2.move(bateau2[i], event.x-old[0]-5, event.y-old[1])
                                old[0]=event.x
                                old[1]=event.y
                            elif y1+TAILLE_CASE*2>CANVAS_TAILLE-5:
                                cnv2.move(bateau2[i], event.x-old[0], event.y-old[1]-5)
                                old[0]=event.x
                                old[1]=event.y
                        else :
                            cnv2.move(torpilleur, event.x-old[0], event.y-old[1])
                            old[0]=event.x
                            old[1]=event.y

def rotation(event):
    global port_h, port_v, porteavion, crois_h, crois_v, croiseur, ctt1_h, ctt1_v, cttorpil1, ctt2_h, ctt2_v, cttorpil2, torp_h, torp_v, torpilleur

    # Si le jeu n'a commence (variable start=0)
    if start==0:
        old[0]=event.x
        old[1]=event.y
        if joueur_actif==1:
            for i in range(len(bateau1)):
                x1, y1 = cnv1.coords(bateau1[i])
                # si le curseur est sur le bateau[i], exemple ici : si bateau[i]=porteavion et si le bateau est à l'horizontale
                if bateau1[i]==porteavion:
                    if pbateau1[i]==0 and ((old[0] >= x1 and old[0] <= x1+TAILLE_CASE*5 and old[1] >= y1 and old[1] <= y1+TAILLE_CASE)):
                        # on supprime l'image du bateau à l'horizontale et on créer au même coordonnée l'image du bateau à la verticale
                        cnv1.delete(porteavion)
                        porteavion=cnv1.create_image(x1, y1, image=port_v)
                        # on remplace le précédent item bateau par le nouveau
                        bateau1[i]=porteavion
                        pbateau1[i]=1
                    # si le bateau est à la verticale
                    elif pbateau1[i]==1 and ((old[0] >= x1 and old[0] <= x1+TAILLE_CASE and old[1] >= y1 and old[1] <= y1+TAILLE_CASE*5)):
                        cnv1.delete(porteavion)
                        porteavion=cnv1.create_image(x1, y1, image=port_h)
                        bateau1[i]=porteavion
                        pbateau1[i]=0
                # idem mais dans le cas ou un autre bateau est ciblé...
                elif bateau1[i]==croiseur:
                    if pbateau1[i]==0 and ((old[0] >= x1 and old[0] <= x1+TAILLE_CASE*4 and old[1] >= y1 and old[1] <= y1+TAILLE_CASE)):
                        cnv1.delete(croiseur)
                        croiseur=cnv1.create_image(x1, y1, image=port_v)
                        bateau1[i]=croiseur
                        pbateau1[i]=1
                    elif pbateau1[i]==1 and ((old[0] >= x1 and old[0] <= x1+TAILLE_CASE and old[1] >= y1 and old[1] <= y1+TAILLE_CASE*4)):
                        cnv1.delete(croiseur)
                        croiseur=cnv1.create_image(x1, y1, image=port_h)
                        bateau1[i]=croiseur
                        pbateau1[i]=0
                elif bateau1[i]==cttorpil1:
                    if pbateau1[i]==0 and ((old[0] >= x1 and old[0] <= x1+TAILLE_CASE*3 and old[1] >= y1 and old[1] <= y1+TAILLE_CASE)):
                        cnv1.delete(cttorpil1)
                        cttorpil1=cnv1.create_image(x1, y1, image=port_v)
                        bateau1[i]=cttorpil1
                        pbateau1[i]=1
                    elif pbateau1[i]==1 and ((old[0] >= x1 and old[0] <= x1+TAILLE_CASE and old[1] >= y1 and old[1] <= y1+TAILLE_CASE*3)):
                        cnv1.delete(cttorpil1)
                        cttorpil1=cnv1.create_image(x1, y1, image=port_h)
                        bateau1[i]=cttorpil1
                        pbateau1[i]=0
                elif bateau1[i]==cttorpil2:
                    if pbateau1[i]==0 and ((old[0] >= x1 and old[0] <= x1+TAILLE_CASE*3 and old[1] >= y1 and old[1] <= y1+TAILLE_CASE)):
                        cnv1.delete(cttorpil2)
                        cttorpil2=cnv1.create_image(x1, y1, image=port_v)
                        bateau1[i]=cttorpil2
                        pbateau1[i]=1
                    elif pbateau1[i]==1 and ((old[0] >= x1 and old[0] <= x1+TAILLE_CASE and old[1] >= y1 and old[1] <= y1+TAILLE_CASE*3)):
                        cnv1.delete(cttorpil2)
                        cttorpil2=cnv1.create_image(x1, y1, image=port_h)
                        bateau1[i]=cttorpil2
                        pbateau1[i]=0
                elif bateau1[i]==torpilleur:
                    if pbateau1[i]==0 and ((old[0] >= x1 and old[0] <= x1+TAILLE_CASE*2 and old[1] >= y1 and old[1] <= y1+TAILLE_CASE)):
                        cnv1.delete(torpilleur)
                        torpilleur=cnv1.create_image(x1, y1, image=port_v)
                        bateau1[i]=torpilleur
                        pbateau1[i]=1
                    elif pbateau1[i]==1 and ((old[0] >= x1 and old[0] <= x1+TAILLE_CASE and old[1] >= y1 and old[1] <= y1+TAILLE_CASE*2)):
                        cnv1.delete(torpilleur)
                        torpilleur=cnv1.create_image(x1, y1, image=port_h)
                        bateau1[i]=torpilleur
                        pbateau1[i]=0                    

        # idem si le joueur actif est le joueur 2...
        elif joueur_actif==2:
            for i in range(len(bateau2)):
                x1, y1 = cnv1.coords(bateau2[i])
                if bateau2[i]==porteavion:
                    if pbateau2[i]==0 and ((old[0] >= x1 and old[0] <= x1+TAILLE_CASE*5 and old[1] >= y1 and old[1] <= y1+TAILLE_CASE)):
                        cnv2.delete(porteavion)
                        porteavion=cnv2.create_image(x1, y1, image=port_v)
                        bateau2[i]=porteavion
                        pbateau2[i]=1
                    elif pbateau2[i]==1 and ((old[0] >= x1 and old[0] <= x1+TAILLE_CASE and old[1] >= y1 and old[1] <= y1+TAILLE_CASE*5)):
                        cnv2.delete(porteavion)
                        porteavion=cnv2.create_image(x1, y1, image=port_h)
                        bateau2[i]=porteavion
                        pbateau2[i]=0
                elif bateau2[i]==croiseur:
                    if pbateau2[i]==0 and ((old[0] >= x1 and old[0] <= x1+TAILLE_CASE*4 and old[1] >= y1 and old[1] <= y1+TAILLE_CASE)):
                        cnv2.delete(croiseur)
                        croiseur=cnv2.create_image(x1, y1, image=port_v)
                        bateau2[i]=croiseur
                        pbateau2[i]=1
                    elif pbateau2[i]==1 and ((old[0] >= x1 and old[0] <= x1+TAILLE_CASE and old[1] >= y1 and old[1] <= y1+TAILLE_CASE*4)):
                        cnv2.delete(croiseur)
                        croiseur=cnv2.create_image(x1, y1, image=port_h)
                        bateau2[i]=croiseur
                        pbateau2[i]=0
                elif bateau2[i]==cttorpil1:
                    if pbateau2[i]==0 and ((old[0] >= x1 and old[0] <= x1+TAILLE_CASE*3 and old[1] >= y1 and old[1] <= y1+TAILLE_CASE)):
                        cnv2.delete(cttorpil1)
                        cttorpil1=cnv2.create_image(x1, y1, image=port_v)
                        bateau2[i]=cttorpil1
                        pbateau2[i]=1
                    elif pbateau2[i]==1 and ((old[0] >= x1 and old[0] <= x1+TAILLE_CASE and old[1] >= y1 and old[1] <= y1+TAILLE_CASE*3)):
                        cnv2.delete(cttorpil1)
                        cttorpil1=cnv2.create_image(x1, y1, image=port_h)
                        bateau2[i]=cttorpil1
                        pbateau2[i]=0
                elif bateau2[i]==cttorpil2:
                    if pbateau2[i]==0 and ((old[0] >= x1 and old[0] <= x1+TAILLE_CASE*3 and old[1] >= y1 and old[1] <= y1+TAILLE_CASE)):
                        cnv2.delete(cttorpil2)
                        cttorpil2=cnv2.create_image(x1, y1, image=port_v)
                        bateau2[i]=cttorpil2
                        pbateau2[i]=1
                    elif pbateau2[i]==1 and ((old[0] >= x1 and old[0] <= x1+TAILLE_CASE and old[1] >= y1 and old[1] <= y1+TAILLE_CASE*3)):
                        cnv2.delete(cttorpil2)
                        cttorpil2=cnv2.create_image(x1, y1, image=port_h)
                        bateau2[i]=cttorpil2
                        pbateau2[i]=0
                elif bateau2[i]==torpilleur:
                    if pbateau2[i]==0 and ((old[0] >= x1 and old[0] <= x1+TAILLE_CASE*2 and old[1] >= y1 and old[1] <= y1+TAILLE_CASE)):
                        cnv2.delete(torpilleur)
                        torpilleur=cnv2.create_image(x1, y1, image=port_v)
                        bateau2[i]=torpilleur
                        pbateau2[i]=1
                    elif pbateau2[i]==1 and ((old[0] >= x1 and old[0] <= x1+TAILLE_CASE and old[1] >= y1 and old[1] <= y1+TAILLE_CASE*2)):
                        cnv2.delete(torpilleur)
                        torpilleur=cnv2.create_image(x1, y1, image=port_h)
                        bateau2[i]=torpilleur
                        pbateau2[i]=0

def tirer(event):
    global joueur_actif
    old[0]=event.x
    old[1]=event.y

    if start==1:
        if TAILLE_CASE<old[0]<TAILLE_CASE*11 and TAILLE_CASE<old[1]<TAILLE_CASE*11 and old[0]%TAILLE_CASE!=0 and old[1]%TAILLE_CASE!=0:
        # si le curseur de la sourie se situe dans une matrice haute:
            if case_plat1[(old[1]//TAILLE_CASE)-1][(old[0]//TAILLE_CASE)-1]==0 and joueur_actif==1:
            # si la case ciblée est égale à 0 (c.a.d qu'elle ne contient ni bateau, ni tir lui ayant précédé) :
                t1=cnv1.create_oval((old[0]-old[0]%TAILLE_CASE+TAILLE_CASE//2)-5, (old[1]-old[1]%TAILLE_CASE+TAILLE_CASE//2)-5, (old[0]-old[0]%TAILLE_CASE+TAILLE_CASE//2)+5, (old[1]-old[1]%TAILLE_CASE+TAILLE_CASE//2)+5, fill='yellow', outline='black')
                t2=cnv2.create_oval((old[0]-old[0]%TAILLE_CASE+TAILLE_CASE//2)-5, ((old[1]-old[1]%TAILLE_CASE+TAILLE_CASE//2)-5)+11*TAILLE_CASE, (old[0]-old[0]%TAILLE_CASE+TAILLE_CASE//2)+5, ((old[1]-old[1]%TAILLE_CASE+TAILLE_CASE//2)+5)+11*TAILLE_CASE, fill='yellow', outline='black')
                case_plat1[(old[1]//TAILLE_CASE)-1][(old[0]//TAILLE_CASE)-1]+=1
                case_plat2[(old[1]//TAILLE_CASE)-1+10][(old[0]//TAILLE_CASE)-1]+=1
                tire1.append(t1)
                tire2.append(t2)
                if jeu==1:
                    cnv1.unbind("<B1-Motion>")
                    cnv1.unbind("<Double-Button-1>")
                    cnv1.unbind("<Button-1>")
                    cnv1.unbind("<ButtonRelease-1>")
                    cnv1.unbind("<Button-3>")
                    joueur_actif=0
                # on créer un rond au centre de la case ciblé
            elif case_plat2[(old[1]//TAILLE_CASE)-1][(old[0]//TAILLE_CASE)-1]==0 and joueur_actif==2:
                t1=cnv2.create_oval((old[0]-old[0]%TAILLE_CASE+TAILLE_CASE//2)-5, (old[1]-old[1]%TAILLE_CASE+TAILLE_CASE//2)-5, (old[0]-old[0]%TAILLE_CASE+TAILLE_CASE//2)+5, (old[1]-old[1]%TAILLE_CASE+TAILLE_CASE//2)+5, fill='yellow', outline='black')
                t2=cnv1.create_oval((old[0]-old[0]%TAILLE_CASE+TAILLE_CASE//2)-5, ((old[1]-old[1]%TAILLE_CASE+TAILLE_CASE//2)-5)+11*TAILLE_CASE, (old[0]-old[0]%TAILLE_CASE+TAILLE_CASE//2)+5, ((old[1]-old[1]%TAILLE_CASE+TAILLE_CASE//2)+5)+11*TAILLE_CASE, fill='yellow', outline='black')
                case_plat2[(old[1]//TAILLE_CASE)-1][(old[0]//TAILLE_CASE)-1]+=1
                case_plat1[(old[1]//TAILLE_CASE)-1+10][(old[0]//TAILLE_CASE)-1]+=1
                tire1.append(t1)
                tire2.append(t2)
            # Meme chose mais dans le cas ou le case touché est occupée par un bateau
            elif case_plat1[(old[1]//TAILLE_CASE)-1][(old[0]//TAILLE_CASE)-1]==2 and joueur_actif==1:
                t1=cnv1.create_oval((old[0]-old[0]%TAILLE_CASE+TAILLE_CASE//2)-5, (old[1]-old[1]%TAILLE_CASE+TAILLE_CASE//2)-5, (old[0]-old[0]%TAILLE_CASE+TAILLE_CASE//2)+5, (old[1]-old[1]%TAILLE_CASE+TAILLE_CASE//2)+5, fill='red', outline='black')
                t2=cnv2.create_oval((old[0]-old[0]%TAILLE_CASE+TAILLE_CASE//2)-5, ((old[1]-old[1]%TAILLE_CASE+TAILLE_CASE//2)-5)+11*TAILLE_CASE, (old[0]-old[0]%TAILLE_CASE+TAILLE_CASE//2)+5, ((old[1]-old[1]%TAILLE_CASE+TAILLE_CASE//2)+5)+11*TAILLE_CASE, fill='red', outline='black')
                case_plat1[(old[1]//TAILLE_CASE)-1][(old[0]//TAILLE_CASE)-1]+=1
                case_plat2[(old[1]//TAILLE_CASE)-1+10][(old[0]//TAILLE_CASE)-1]+=1
                tire1.append(t1)
                tire2.append(t2)
                if jeu==1:
                    cnv1.unbind("<B1-Motion>")
                    cnv1.unbind("<Double-Button-1>")
                    cnv1.unbind("<Button-1>")
                    cnv1.unbind("<ButtonRelease-1>")
                    cnv1.unbind("<Button-3>")
                    joueur_actif=0
            elif case_plat2[(old[1]//TAILLE_CASE)-1][(old[0]//TAILLE_CASE)-1]==2 and joueur_actif==2 :
                t1=cnv2.create_oval((old[0]-old[0]%TAILLE_CASE+TAILLE_CASE//2)-5, (old[1]-old[1]%TAILLE_CASE+TAILLE_CASE//2)-5, (old[0]-old[0]%TAILLE_CASE+TAILLE_CASE//2)+5, (old[1]-old[1]%TAILLE_CASE+TAILLE_CASE//2)+5, fill='red', outline='white')
                t2=cnv1.create_oval((old[0]-old[0]%TAILLE_CASE+TAILLE_CASE//2)-5, ((old[1]-old[1]%TAILLE_CASE+TAILLE_CASE//2)-5)+11*TAILLE_CASE, (old[0]-old[0]%TAILLE_CASE+TAILLE_CASE//2)+5, ((old[1]-old[1]%TAILLE_CASE+TAILLE_CASE//2)+5)+11*TAILLE_CASE, fill='red', outline='white')
                case_plat2[(old[1]//TAILLE_CASE)-1][(old[0]//TAILLE_CASE)-1]+=1
                case_plat1[(old[1]//TAILLE_CASE)-1+10][(old[0]//TAILLE_CASE)-1]+=1
                tire1.append(t1)
                tire2.append(t2)

    if jeu==2:
        if joueur_actif==1:
            # on supprime la possibilité d'interraction du joueur actif
            cnv1.unbind("<B1-Motion>")
            cnv1.unbind("<Double-Button-1>")
            cnv1.unbind("<Button-1>")
            cnv1.unbind("<ButtonRelease-1>")
            cnv1.unbind("<Button-3>")
            joueur_actif=2
        elif joueur_actif==2:
            cnv2.unbind("<B1-Motion>")
            cnv2.unbind("<Double-Button-1>")
            cnv2.unbind("<Button-1>")
            cnv2.unbind("<ButtonRelease-1>")
            cnv2.unbind("<Button-3>")
            joueur_actif=1

    joueur(joueur_actif)
    cache_plateau()
    test_fin()

def rnd_tire():
    global joueur_actif
    a, b = randint(0, 9), randint(0, 9)
    print(a,b)

    if mode==0:
        if case_plat2[a][b]==0:
            t1=cnv2.create_oval(((b+1)*TAILLE_CASE)+TAILLE_CASE//2-5, ((a+1)*TAILLE_CASE)+TAILLE_CASE//2-5, ((b+1)*TAILLE_CASE)+TAILLE_CASE//2+5, ((a+1)*TAILLE_CASE)+TAILLE_CASE//2+5, fill='yellow', outline='black')
            t2=cnv1.create_oval(((b+1)*TAILLE_CASE)+TAILLE_CASE//2-5, ((a+12)*TAILLE_CASE)+TAILLE_CASE//2-5, ((b+1)*TAILLE_CASE)+TAILLE_CASE//2+5, ((a+12)*TAILLE_CASE)+TAILLE_CASE//2+5, fill='yellow', outline='black')
            case_plat2[a][b]+=1
            case_plat1[a+10][b]+=1
            tire1.append(t1)
            tire2.append(t2)
            joueur_actif=1
            joueur(joueur_actif)
            cache_plateau()
            test_fin()
        elif case_plat2[a][b]==2:
            t1=cnv2.create_oval(((b+1)*TAILLE_CASE)+TAILLE_CASE//2-5, ((a+1)*TAILLE_CASE)+TAILLE_CASE//2-5, ((b+1)*TAILLE_CASE)+TAILLE_CASE//2+5, ((a+1)*TAILLE_CASE)+TAILLE_CASE//2+5, fill='red', outline='black')
            t2=cnv1.create_oval(((b+1)*TAILLE_CASE)+TAILLE_CASE//2-5, ((a+12)*TAILLE_CASE)+TAILLE_CASE//2-5, ((b+1)*TAILLE_CASE)+TAILLE_CASE//2+5, ((a+12)*TAILLE_CASE)+TAILLE_CASE//2+5, fill='red', outline='black')
            case_plat2[a][b]+=1
            case_plat1[a+10][b]+=1
            tire1.append(t1)
            tire2.append(t2)
            joueur_actif=1
            joueur(joueur_actif)
            cache_plateau()
            test_fin()
        else :
            rnd_tire()

    if mode==1:
        if case_plat2[a][b]==1 or case_plat2[a][b]==3:
            rnd_tire()
        elif case_plat2[a][b]==0:
            if b==0 and a!=0 and a!=9 and (case_plat1[a-1][b]==1 or case_plat1[a-1][b]==3 or case_plat1[a+1][b]==1 or case_plat1[a+1][b]==3 or case_plat1[a][b+1]==1 or case_plat1[a][b+1]==3):
                rnd_tire()
            elif b==0 and a==0 and (case_plat1[a+1][b]==1 or case_plat1[a+1][b]==3 or case_plat1[a][b+1]==1 or case_plat1[a][b+1]==3):
                rnd_tire()
            elif b==0 and a==9 and (case_plat1[a-1][b]==1 or case_plat1[a-1][b]==3) and (case_plat1[a][b+1]==1 or case_plat1[a][b+1]==3):
                rnd_tire()
            elif b==9 and a!=0 and a!=9 and (case_plat1[a-1][b]==1 or case_plat1[a-1][b]==3 or case_plat1[a+1][b]==1 or case_plat1[a+1][b]==3 or case_plat1[a][b-1]==1 or case_plat1[a][b-1]==3):
                rnd_tire()
            elif b==9 and a==0 and (case_plat1[a+1][b]==1 or case_plat1[a+1][b]==3 or case_plat1[a][b-1]==1 or case_plat1[a][b-1]==3):
                rnd_tire()
            elif b==9 and a==9 and (case_plat1[a-1][b]==1 or case_plat1[a-1][b]==3 or case_plat1[a][b-1]==1 or case_plat1[a][b-1]==3):
                rnd_tire()
            elif a==9 and b!=0 and b!=9 and (case_plat1[a-1][b]==1 or case_plat1[a-1][b]==3 or case_plat1[a][b-1]==1 or case_plat1[a][b-1]==3 or case_plat1[a][b+1]==1 or case_plat1[a][b+1]==3):
                rnd_tire()
            elif a==9 and b==0 and (case_plat1[a-1][b]==1 or case_plat1[a-1][b]==3 or case_plat1[a][b+1]==1 or case_plat1[a][b+1]==3):
                rnd_tire()
            elif a==9 and b==9 and (case_plat1[a-1][b]==1 or case_plat1[a-1][b]==3 or case_plat1[a][b-1]==1 or case_plat1[a][b-1]==3):
                rnd_tire()
            elif a==0 and b!=0 and b!=9 and (case_plat1[a+1][b]==1 or case_plat1[a+1][b]==3 or case_plat1[a][b-1]==1 or case_plat1[a][b-1]==3 or case_plat1[a][b+1]==1 or case_plat1[a][b+1]==3):
                rnd_tire()
            elif a==0 and b==0 and (case_plat1[a+1][b]==1 or case_plat1[a+1][b]==3 or case_plat1[a][b+1]==1 or case_plat1[a][b+1]==3):
                rnd_tire()
            elif a==0 and b==9 and (case_plat1[a+1][b]==1 or case_plat1[a+1][b]==3 or case_plat1[a][b-1]==1 or case_plat1[a][b-1]==3):
                rnd_tire()
            elif a!=0 and a!=9 and b!=0 and b!=9 and (case_plat1[a-1][b]==1 or case_plat1[a-1][b]==3 or case_plat1[a+1][b]==1 or case_plat1[a+1][b]==3 or case_plat1[a][b-1]==1 or case_plat1[a][b-1]==3 or case_plat1[a][b+1]==1 or case_plat1[a][b+1]==3):
                rnd_tire()
            else :
                t1=cnv2.create_oval(((b+1)*TAILLE_CASE)+TAILLE_CASE//2-5, ((a+1)*TAILLE_CASE)+TAILLE_CASE//2-5, ((b+1)*TAILLE_CASE)+TAILLE_CASE//2+5, ((a+1)*TAILLE_CASE)+TAILLE_CASE//2+5, fill='yellow', outline='black')
                t2=cnv1.create_oval(((b+1)*TAILLE_CASE)+TAILLE_CASE//2-5, ((a+12)*TAILLE_CASE)+TAILLE_CASE//2-5, ((b+1)*TAILLE_CASE)+TAILLE_CASE//2+5, ((a+12)*TAILLE_CASE)+TAILLE_CASE//2+5, fill='yellow', outline='black')
                case_plat2[a][b]+=1
                case_plat1[a+10][b]+=1
                tire1.append(t1)
                tire2.append(t2)
                joueur_actif=1
                joueur(joueur_actif)
                cache_plateau()
                test_fin()
        elif case_plat2[a][b]==2:
            t1=cnv2.create_oval(((b+1)*TAILLE_CASE)+TAILLE_CASE//2-5, ((a+1)*TAILLE_CASE)+TAILLE_CASE//2-5, ((b+1)*TAILLE_CASE)+TAILLE_CASE//2+5, ((a+1)*TAILLE_CASE)+TAILLE_CASE//2+5, fill='red', outline='black')
            t2=cnv1.create_oval(((b+1)*TAILLE_CASE)+TAILLE_CASE//2-5, ((a+12)*TAILLE_CASE)+TAILLE_CASE//2-5, ((b+1)*TAILLE_CASE)+TAILLE_CASE//2+5, ((a+12)*TAILLE_CASE)+TAILLE_CASE//2+5, fill='red', outline='black')
            case_plat2[a][b]+=1
            case_plat1[a+10][b]+=1
            tire1.append(t1)
            tire2.append(t2)
            joueur_actif=1
            joueur(joueur_actif)
            cache_plateau()
            test_fin()
        else :
            rnd_tire()

def recommencer():
    global start, joueur_actif ,stop,fenetre2, porteavion, croiseur, cttorpil1, cttorpil2, torpilleur, bateau1, bateau2

    # si la partie est terminé, on repasse la variable définissant si le jeu est fini à 0 et on détruit la fenetre de fin de jeu 
    if (stop==1):
        stop=0
        fenetre2.destroy()
    # remise à 0 de la variable indiquant si le jeu à commencé
    start=0
    # on supprime les images des tires sur les 2 canevas
    for i in range(len(tire1)):
        cnv1.delete(tire1[i])
        cnv2.delete(tire2[i])
    # on vide les listes contenant les coordonnées des tires 
    tire1.clear()
    tire2.clear()
    # remise à 0 des matrices correspondant aux 2 canevas
    for i in range(NB_CASE_HAUT-2):
        for j in range(NB_CASE_LARGE-1):
            case_plat1[i][j]=0
            case_plat2[i][j]=0
    # les valeurs d'orientation des bateaux est redéfini à 0 (position horizontale)
    for i in range(len(pbateau1)):
        pbateau1[i]=0
        pbateau2[i]=0

    # on supprime tous les bateaux sur les 2 canevas
    cnv1.delete(porteavion)
    cnv2.delete(porteavion)
    cnv1.delete(croiseur)
    cnv2.delete(croiseur)
    cnv1.delete(cttorpil1)
    cnv2.delete(cttorpil1)
    cnv1.delete(cttorpil2)
    cnv2.delete(cttorpil2)
    cnv1.delete(torpilleur)
    cnv2.delete(torpilleur)

    # on récreer les bateaux à leur coordonnées d'origines dans les 2 canevas, et on réinitialise leur coordonnées dans la liste de bateau
    porteavion=cnv1.create_image(x0+TAILLE_CASE, 12*TAILLE_CASE+TAILLE_CASE//2, anchor=NW, image=port_h)
    croiseur=cnv1.create_image(x0+TAILLE_CASE, 14*TAILLE_CASE+TAILLE_CASE//2, anchor=NW, image=crois_h)
    cttorpil1=cnv1.create_image(x0+TAILLE_CASE, 16*TAILLE_CASE+TAILLE_CASE//2, anchor=NW, image=ctt1_h)
    cttorpil2=cnv1.create_image(x0+TAILLE_CASE, 18*TAILLE_CASE+TAILLE_CASE//2, anchor=NW, image=ctt2_h)
    torpilleur=cnv1.create_image(x0+TAILLE_CASE, 20*TAILLE_CASE+TAILLE_CASE//2, anchor=NW, image=torp_h)
    bateau1=[porteavion,croiseur,cttorpil1,cttorpil2,torpilleur]
    porteavion=cnv2.create_image(x0+TAILLE_CASE, 12*TAILLE_CASE+TAILLE_CASE//2, anchor=NW, image=port_h)
    croiseur=cnv2.create_image(x0+TAILLE_CASE, 14*TAILLE_CASE+TAILLE_CASE//2, anchor=NW, image=crois_h)
    cttorpil1=cnv2.create_image(x0+TAILLE_CASE, 16*TAILLE_CASE+TAILLE_CASE//2, anchor=NW, image=ctt1_h)
    cttorpil2=cnv2.create_image(x0+TAILLE_CASE, 18*TAILLE_CASE+TAILLE_CASE//2, anchor=NW, image=ctt2_h)
    torpilleur=cnv2.create_image(x0+TAILLE_CASE, 20*TAILLE_CASE+TAILLE_CASE//2, anchor=NW, image=torp_h)
    bateau2=[porteavion,croiseur,cttorpil1,cttorpil2,torpilleur]

    # suppression des commandes pour le joueur 2
    if joueur_actif==2:
        cnv2.unbind("<B1-Motion>")
        cnv2.unbind("<Double-Button-1>")
        cnv2.unbind("<Button-1>")
        cnv2.unbind("<ButtonRelease-1>")
        cnv2.unbind("<Button-3>")

    # attribution des commandes au joueur 1 et cache du plateau du joueur 2
    joueur_actif=1
    joueur(joueur_actif)
    cache_plateau()

def commencer():
    global start, joueur_actif
    
    start=1
    bouton5.pack_forget()

    if jeu==1:
        rnd_bateau()
    
    global pos_port1, pos_port2, pos_croi1, pos_croi2, pos_ctorp11, pos_ctorp12, pos_ctorp21, pos_ctorp22, pos_torp1, pos_torp2

    # Placement de la liste de bateau dans la matrice du plateau 1
    if pbateau1[0] == 0:
        for i in range (5):
            case_plat1[int((pos_port1[1]//TAILLE_CASE)-2)][int((pos_port1[0]//TAILLE_CASE)-1)+i]+=2
            case_plat2[int((pos_port1[1]//TAILLE_CASE)-12)][int((pos_port1[0]//TAILLE_CASE)-1)+i]+=2
    elif pbateau1[0] == 1:
        for i in range (5):
            case_plat1[int((pos_port1[1]//TAILLE_CASE)-2)+i][int((pos_port1[0]//TAILLE_CASE)-1)]+=2
            case_plat2[int((pos_port1[1]//TAILLE_CASE)-12)+i][int((pos_port1[0]//TAILLE_CASE)-1)]+=2
    
    if pbateau1[1] == 0:
        for j in range (4):
            case_plat1[int((pos_croi1[1]//TAILLE_CASE)-2)][int((pos_croi1[0]//TAILLE_CASE)-1)+j]+=2
            case_plat2[int((pos_croi1[1]//TAILLE_CASE)-12)][int((pos_croi1[0]//TAILLE_CASE)-1)+j]+=2
    elif pbateau1[1] == 1:
        for j in range (4):
            case_plat1[int((pos_croi1[1]//TAILLE_CASE)-2)+j][int((pos_croi1[0]//TAILLE_CASE)-1)]+=2
            case_plat2[int((pos_croi1[1]//TAILLE_CASE)-12)+j][int((pos_croi1[0]//TAILLE_CASE)-1)]+=2
     
    if pbateau1[2] == 0:
        for j in range (3):
            case_plat1[int((pos_ctorp11[1]//TAILLE_CASE)-2)][int((pos_ctorp11[0]//TAILLE_CASE)-1)+j]+=2
            case_plat2[int((pos_ctorp11[1]//TAILLE_CASE)-12)][int((pos_ctorp11[0]//TAILLE_CASE)-1)+j]+=2
    elif pbateau1[2] == 1:
        for j in range (3):
            case_plat1[int((pos_ctorp11[1]//TAILLE_CASE)-2)+j][int((pos_ctorp11[0]//TAILLE_CASE)-1)]+=2
            case_plat2[int((pos_ctorp11[1]//TAILLE_CASE)-12)+j][int((pos_ctorp11[0]//TAILLE_CASE)-1)]+=2
            
    if pbateau1[3] == 0:
        for j in range (3):
            case_plat1[int((pos_ctorp21[1]//TAILLE_CASE)-2)][int((pos_ctorp21[0]//TAILLE_CASE)-1)+j]+=2
            case_plat2[int((pos_ctorp21[1]//TAILLE_CASE)-12)][int((pos_ctorp21[0]//TAILLE_CASE)-1)+j]+=2
    elif pbateau1[3] == 1:
        for j in range (3):
            case_plat1[int((pos_ctorp21[1]//TAILLE_CASE)-2)+j][int((pos_ctorp21[0]//TAILLE_CASE)-1)]+=2
            case_plat2[int((pos_ctorp21[1]//TAILLE_CASE)-12)+j][int((pos_ctorp21[0]//TAILLE_CASE)-1)]+=2
    
    if pbateau1[4] == 0:
        for j in range (2):
            case_plat1[int((pos_torp1[1]//TAILLE_CASE)-2)][int((pos_torp1[0]//TAILLE_CASE)-1)+j]+=2
            case_plat2[int((pos_torp1[1]//TAILLE_CASE)-12)][int((pos_torp1[0]//TAILLE_CASE)-1)+j]+=2
    elif pbateau1[4] == 1:
        for j in range (2):
            case_plat1[int((pos_torp1[1]//TAILLE_CASE)-2)+j][int((pos_torp1[0]//TAILLE_CASE)-1)]+=2
            case_plat2[int((pos_torp1[1]//TAILLE_CASE)-12)+j][int((pos_torp1[0]//TAILLE_CASE)-1)]+=2


    # Placement de la liste de bateau dans la matrice du plateau 2
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
            case_plat2[int((pos_croi2[1]//TAILLE_CASE)-2)][int((pos_croi2[0]//TAILLE_CASE)-1)+j]+=2
            case_plat1[int((pos_croi2[1]//TAILLE_CASE)-12)][int((pos_croi2[0]//TAILLE_CASE)-1)+j]+=2
    elif pbateau2[1] == 1:
        for j in range (4):
            case_plat2[int((pos_croi2[1]//TAILLE_CASE)-2)+j][int((pos_croi2[0]//TAILLE_CASE)-1)]+=2
            case_plat1[int((pos_croi2[1]//TAILLE_CASE)-12)+j][int((pos_croi2[0]//TAILLE_CASE)-1)]+=2
     
    if pbateau2[2] == 0:
        for j in range (3):
            case_plat2[int((pos_ctorp12[1]//TAILLE_CASE)-2)][int((pos_ctorp12[0]//TAILLE_CASE)-1)+j]+=2
            case_plat1[int((pos_ctorp12[1]//TAILLE_CASE)-12)][int((pos_ctorp12[0]//TAILLE_CASE)-1)+j]+=2
    elif pbateau2[2] == 1:
        for j in range (3):
            case_plat2[int((pos_ctorp12[1]//TAILLE_CASE)-2)+j][int((pos_ctorp12[0]//TAILLE_CASE)-1)]+=2
            case_plat1[int((pos_ctorp12[1]//TAILLE_CASE)-12)+j][int((pos_ctorp12[0]//TAILLE_CASE)-1)]+=2
            
    if pbateau2[3] == 0:
        for j in range (3):
            case_plat2[int((pos_ctorp22[1]//TAILLE_CASE)-2)][int((pos_ctorp22[0]//TAILLE_CASE)-1)+j]+=2
            case_plat1[int((pos_ctorp22[1]//TAILLE_CASE)-12)][int((pos_ctorp22[0]//TAILLE_CASE)-1)+j]+=2
    elif pbateau2[3] == 1:
        for j in range (3):
            case_plat2[int((pos_ctorp22[1]//TAILLE_CASE)-2)+j][int((pos_ctorp22[0]//TAILLE_CASE)-1)]+=2
            case_plat1[int((pos_ctorp22[1]//TAILLE_CASE)-12)+j][int((pos_ctorp22[0]//TAILLE_CASE)-1)]+=2
    
    if pbateau2[4] == 0:
        for j in range (2):
            case_plat2[int((pos_torp2[1]//TAILLE_CASE)-2)][int((pos_torp2[0]//TAILLE_CASE)-1)+j]+=2
            case_plat1[int((pos_torp2[1]//TAILLE_CASE)-12)][int((pos_torp2[0]//TAILLE_CASE)-1)+j]+=2
    elif pbateau2[4] == 1:
        for j in range (2):
            case_plat2[int((pos_torp2[1]//TAILLE_CASE)-2)+j][int((pos_torp2[0]//TAILLE_CASE)-1)]+=2
            case_plat1[int((pos_torp2[1]//TAILLE_CASE)-12)+j][int((pos_torp2[0]//TAILLE_CASE)-1)]+=2

    # suppression des commandes pour les deux joueurs, seul le joueur 1 peut cliquer dans la fenetre    
    if jeu==2:
        joueur_actif=randint(1,2)
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
    elif jeu==1:
        joueur_actif=randint(0,1)
        if joueur_actif==0:
            cnv1.unbind("<B1-Motion>")
            cnv1.unbind("<Double-Button-1>")
            cnv1.unbind("<Button-1>")
            cnv1.unbind("<ButtonRelease-1>")
            cnv1.unbind("<Button-3>")

    print("Le joueur ", joueur_actif, " commence !")
    
    joueur(joueur_actif)
    cache_plateau()

def pret():
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

    if joueur_actif==1:
        joueur_actif=2
    elif joueur_actif==2:
        joueur_actif=1

    joueur(joueur_actif)
    cache_plateau()

def test_commencer():
    global pos_port1, pos_port2, pos_croi1, pos_croi2, pos_ctorp11, pos_ctorp12, pos_ctorp21, pos_ctorp22, pos_torp1, pos_torp2

    val_test=0
    
    if joueur_actif==1:
        x1, y1, x2, y2 = pos_port1
        a12, b12, a22, b22 = pos_croi1
        a13, b13, a23, b23 = pos_ctorp11
        a14, b14, a24, b24 = pos_ctorp21
        a15, b15, a25, b25 = pos_torp1
        pos_bat = [pos_port1, pos_croi1, pos_ctorp11, pos_ctorp21, pos_torp1]
        # Test si un bateau est collé à un autre :
        for i in range (len(bateau1)):
            x1, y1, x2, y2 = pos_bat[i]
            a12, b12, a22, b22 = pos_bat[i-1]
            a13, b13, a23, b23 = pos_bat[i-2]
            a14, b14, a24, b24 = pos_bat[i-3]
            a15, b15, a25, b25 = pos_bat[i-4]
            # Si deux bateaux sont collé, apparission d'un message d'erreur qui disparait au bout de 4 secondes. + valeur test incrémenté
            if (y1>b12-5 and x1<a22+5 and x2>a12-5 and y1<b22+5) or (y2>b13-5 and x1<a23+5 and x2>a13-5 and y1<b23+5) or (y2>b14-5 and x1<a24+5 and x2>a14-5 and y1<b24+5) or (y2>b15-5 and x1<a25+5 and x2>a15-5 and y1<b25+5):
                msg = Label(cnv1, text="  Attention, vos bateaux doivent être placés à une case d'écart au minimum  ", fg='black', bg='red')
                msg.pack()
                cnv1.create_window(TAILLE_CASE*10, TAILLE_CASE*11, window=msg)
                cnv1.after(4000, msg.destroy)
                val_test+=1
                
        # Test si tout les bateaux sont contenu dans la matrice basse du joueur, sinon, incrémentation de la valeur test
        x1, y1, x2, y2 = pos_port1
        a12, b12, a22, b22 = pos_croi1
        a13, b13, a23, b23 = pos_ctorp11
        a14, b14, a24, b24 = pos_ctorp21
        a15, b15, a25, b25 = pos_torp1
        if (TAILLE_CASE<=x1<TAILLE_CASE*11 and TAILLE_CASE*12<=y1) and (TAILLE_CASE<=a12<TAILLE_CASE*11 and TAILLE_CASE*12<=b12) and (TAILLE_CASE<=a13<TAILLE_CASE*11 and TAILLE_CASE*12<=b13) and (TAILLE_CASE<=a14<TAILLE_CASE*11 and TAILLE_CASE*12<=b14) and (TAILLE_CASE<=a15<=TAILLE_CASE*11 and TAILLE_CASE*12<=b15):
            val_test=val_test
        else :
            val_test+=1
        
        # sur le jeu est à deux joueurs
        if jeu==2:
            # si la valeur test est égale à 0, la bouton "Pret" apparait
            if val_test==0:
                bouton6.pack()
            else :
                bouton6.pack_forget()
        if jeu==1:
            if val_test==0:
                bouton5.pack()
            else :
                bouton5.pack_forget()
            
    elif joueur_actif==2:
        x1, y1, x2, y2 = pos_port2
        a12, b12, a22, b22 = pos_croi2
        a13, b13, a23, b23 = pos_ctorp12
        a14, b14, a24, b24 = pos_ctorp22
        a15, b15, a25, b25 = pos_torp2
        pos_bat = [pos_port2, pos_croi2, pos_ctorp12, pos_ctorp22, pos_torp2]
        for i in range (len(bateau2)):
            x1, y1, x2, y2 = pos_bat[i]
            a12, b12, a22, b22 = pos_bat[i-1]
            a13, b13, a23, b23 = pos_bat[i-2]
            a14, b14, a24, b24 = pos_bat[i-3]
            a15, b15, a25, b25 = pos_bat[i-4]
            if (y2>b12-5 and x1<a22+5 and x2>a12-5 and y1<b22+5) or (y2>b13-5 and x1<a23+5 and x2>a13-5 and y1<b23+5) or (y2>b14-5 and x1<a24+5 and x2>a14-5 and y1<b24+5) or (y2>b15-5 and x1<a25+5 and x2>a15-5 and y1<b25+5):
                msg = Label(cnv2, text="  Attention, vos bateaux doivent être placés à une case d'écart au minimum  ", fg='black', bg='red')
                msg.pack()
                cnv2.create_window(TAILLE_CASE*10, TAILLE_CASE*11, window=msg)
                cnv2.after(4000, msg.destroy)
                val_test+=1
        x1, y1, x2, y2 = pos_port2
        a12, b12, a22, b22 = pos_croi2
        a13, b13, a23, b23 = pos_ctorp12
        a14, b14, a24, b24 = pos_ctorp22
        a15, b15, a25, b25 = pos_torp2
        if (TAILLE_CASE<=x1<TAILLE_CASE*11 and TAILLE_CASE*12<=y1) and (TAILLE_CASE<=a12<TAILLE_CASE*11 and TAILLE_CASE*12<=b12) and (TAILLE_CASE<=a13<TAILLE_CASE*11 and TAILLE_CASE*12<=b13) and (TAILLE_CASE<=a14<TAILLE_CASE*11 and TAILLE_CASE*12<=b14) and (TAILLE_CASE<=a15<=TAILLE_CASE*11 and TAILLE_CASE*12<=b15):
            val_test=val_test
        else :
            val_test+=1
        
        # si la valeur test est égale à 0, la bouton "Commencer" apparait
        if val_test==0:
            bouton5.pack()
        else :
            bouton5.pack_forget()

def test_fin():
    global joueur_actif, start,gagnant, case_plat1, case_plat2
    compt1=0
    compt2=0
    for i in range((NB_CASE_HAUT-2)//2):
        for j in range(NB_CASE_LARGE-1):
            if case_plat1[i][j]==3:
                compt1+=1
            
            if case_plat2[i][j]==3:
                compt2+=1

    if compt1==17:
        gagnant=1
        fin()
    elif compt2==17:
        gagnant=2
        fin()

    if compt1==17 or compt2==17:
        cnv1.coords(cache_plat1, 0, 0, 0, 0)
        cnv2.coords(cache_plat2, 0, 0, 0, 0)
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

def joueur(player):
    if player==1:
        cnv1.bind("<B1-Motion>",glisser)
        cnv1.bind("<Double-Button-1>", tirer)
        cnv1.bind("<Button-1>", clic)
        cnv1.bind("<ButtonRelease-1>",unclic)
        cnv1.bind("<Button-3>",rotation)
    elif player==2:        
        cnv2.bind("<B1-Motion>",glisser)
        cnv2.bind("<Double-Button-1>", tirer)
        cnv2.bind("<Button-1>", clic)
        cnv2.bind("<ButtonRelease-1>",unclic)
        cnv2.bind("<Button-3>",rotation)
    elif player==0:
        cnv2.after(2000, rnd_tire)

def cache_plateau():
    global joueur_actif

    if joueur_actif==1:
        cnv2.coords(cache_plat2, 0, 0, CANVAS_TAILLE, CANVAS_TAILLE)
        cnv2.tag_raise(cache_plat2)
        cnv1.coords(cache_plat1, 0, 0, 0, 0)
    elif joueur_actif==2:
        cnv1.coords(cache_plat1, 0, 0, CANVAS_TAILLE, CANVAS_TAILLE)
        cnv1.tag_raise(cache_plat1)
        cnv2.coords(cache_plat2, 0, 0, 0, 0)

start=0
cache_plat1=cnv1.create_rectangle(0, 0, 0, 0, fill="black")
cache_plat2=cnv2.create_rectangle(0, 0, CANVAS_TAILLE, CANVAS_TAILLE, fill="black")

joueur(joueur_actif)

bouton3 = Button(master, text="Quitter", command=master.destroy)
bouton4 = Button(master, text="Recommencer", command=recommencer)
bouton5 = Button(master, text="Commencer", command=commencer)
bouton6 = Button(master, text="Prêt", command=pret)

if jeu==1 or jeu==2:
    bouton3.pack()
    bouton4.pack()

master.mainloop()