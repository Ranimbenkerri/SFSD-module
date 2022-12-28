
#Ranim Benekrri 2cp

from pickle import dumps, loads
from sys import getsizeof

global b
global tnom
global tprénom
global tnuminscpt
global taffiliation
# taille du bloc: un bloc peut contenir au max b enregitrements
b = 2
"""parceque les enregitrements sont à taille fixe 
il faut définir pour chaque champ la taille max"""
# taille du champ numéro inscription
tnum = 10
# taille du champ nom
tnom = 20
# taille du champ prénom
tprénom = 20
# taille du champ affiliation
taffiliation = 20
# Tetud  c'est la taille totale d'un enregitrement
Tetud = tnum + tnom + tprénom + taffiliation + 1
# fixer la taille d'un enregitrement
Tnreg = '#' * Tetud
global buf
""" 
Dans  la déclaration on définit le typeBloc Tbloc=[0,[Tnreg]*b]

le premier élément buf[0] c le buf.NB qui est de type entier initialisé à 0

le deuxième c'est le tableau d'enregistrement de type enregistrement [Tenreg]*b
"""
Tbloc = [0, [Tnreg] * b]
global blocsize
"""
l'instruction suivante permet de calculer la taille qui sera occupée par un bloc 

"""
blocsize = getsizeof(dumps(Tbloc)) + len(Tnreg) * (b - 1) + (b - 1)
# print(blocsize)

"""
Dans ce cas lorsque on lit un champ inferieur à la taille max déclarée pour ce champ
on doit compléter le reste par un #
exemple: si le numéro d'inscription=='001', or la taille déclarée =5 alors, on le transforme 
en '001##'. pour garder la notion taille fixe. 

"""


def resize_chaine(chaine, maxtaille):
    for _ in range(len(chaine), maxtaille):
        chaine += '#'
    return chaine


""" la fonction créer c'est l'algorithme de chargement initial d'un fichier T~OF
    Dans ce cas les blocs sont remplis à 100% si on veut remplir les blocs avec
    un % donné, on peut juste envoyer à la fonction créer une variable soit par
    exemple mu et pour tester le si le bloc est plein, au lieu de faire j<b on fait 
    si j<b*mu (si on veut remplir les blocs à 50%, mu alors = 0.5 )
"""


def créer_fichier():
    fn=input('Entrer le nom du fichier à créer: ')
    j=0
    i=0
    n=0
    buf_tab=[Tnreg]*b 
    buf_nb=0
    try:
        f = open(fn,'wb')
        rep='O'
        while rep in {'O', 'o'}:
            print('Entrer les information de l\'étudiant: ')
            num=input('Enter le numéro d\'inscription : ')
            nom=input('Enter le nom: ')
            prénom=input('Entrer le prénom: ')
            affiliation=input('Entrer l\'affiliation: ')
            num=resize_chaine(num,tnum)
            nom=resize_chaine(nom,tnom)
            prénom=resize_chaine(prénom,tprénom)
            affiliation=resize_chaine( affiliation,taffiliation)
            etud=num+nom+prénom+affiliation+'0'
            n=n+1
            if (j<b):
                buf_tab[j]=etud #mettre l'enregitrement dans le tableau  
                buf_nb=buf_nb+1 #augmenter le buf.NB
                j=j+1
            else:
                # mettre le NB et le tableau d'eregistremnt dans une variable buf 
                buf=[buf_nb,buf_tab]
                #ecrire le buf en mémoire centrale
                ecrireBloc(f,i,buf)
                # rénitialiser le tableau d'enregitrement et le Nb
                buf_tab=[Tnreg]*b 
                buf_nb=1
                buf_tab[0]=etud
                j=1
                i=i+1
            rep=input('Avez vous un autre élement à entrer O/N: ')
        buf=[j,buf_tab]
        ecrireBloc(f,i,buf) 
        affecter_entete(f,0,n)
        affecter_entete(f,1,i+1)
    except FileNotFoundError:
        print('impossible d\'ouvrir le fichier en mode d\'écriture ')

# ces fonctions sont déja expliquées
def lireBloc(file, i):
    dp = 2 * getsizeof(dumps(0)) + i * blocsize
    file.seek(dp, 0);
    buf = file.read(blocsize)
    return (loads(buf))


def ecrireBloc(file, i, bf):
    dp = 2 * getsizeof(dumps(0)) + i * blocsize
    file.seek(dp, 0)
    file.write(dumps(bf));

    return


def affecter_entete(file, of, c):
    dp = of * getsizeof(dumps(0))
    file.seek(dp, 0)
    file.write(dumps(c))
    return


def entete(file,offset):
    dp=offset*getsizeof(dumps(0))
    file.seek(dp,0)
    c=file.read(getsizeof(dumps(0)))
    return loads(c)


def afficher_enreg(e):
    # recupérer les champs à partir de chaque enregistrement et remplacer les '#' par un espace
    num = e[:tnum].replace('#', ' ')
    nom = e[tnum:tnom].replace('#', ' ')
    prénom = e[tprénom:taffiliation].replace('#', ' ')
    affiliation = e[taffiliation:-1].replace('#', ' ')
    return f'{num} {nom} {prénom} {affiliation} {e[-1]}'

def fragmentation():
    fn = input('choisir dans quel fichier vous voulez fragmenter: ')
    c1 = int(input('entrez la premiere cle: '))
    c2 = int(input('entrez la deuxieme cle: '))
    try:
        with open(fn,'r+b') as f:
            f1,f2,f3 = open(f'{fn}1','wb'), open(f'{fn}2','wb'),open(f'{fn}3','wb')
            nb,n1,n2,n3 = entete(f,1),0,0,0
            i,j = 0,0
            i1,j1,buff1 = 0,0,[0, [Tnreg] * b]
            i2,j2,buff2 = 0,0,[0, [Tnreg] * b]
            i3,j3,buff3 = 0,0,[0, [Tnreg] * b]
            while i < nb:
                buff = lireBloc(f,i)
                for j in range(b):
                    
                    if buff[1][j].replace('#','') != '':
                        if int(buff[1][j][:tnum].replace('#','')) < c1:
                            n1 += 1
                            if j1 < b:
                                buff1[0] += 1
                                buff1[1][j1] = buff[1][j]                   
                                j1 += 1
                            else: 
                                ecrireBloc(f1,i1,buff1)  
                                i1 += 1
                                buff1 = [0, [Tnreg] * b]
                                buff1[0] += 1
                                buff1[1][0] = buff[1][j]  
                                j1 = 1   
                                
                        elif int(buff[1][j][:tnum].replace('#','')) >= c1 and int(buff[1][j][:tnum].replace('#','')) < c2:
                            n2 += 1
                            if j2 < b:
                                buff2[0] += 1
                                buff2[1][j2] = buff[1][j]               
                                j2 += 1 
                            else:   
                                ecrireBloc(f2,i2,buff2)
                                i2 += 1
                                buff2 = [0, [Tnreg] * b]
                                buff2[0] += 1
                                buff2[1][0] = buff[1][j]  
                                j2 = 1                        
                        elif int(buff[1][j][:tnum].replace('#','')) > c2:
                            n3 += 1
                            if j3 < b:
                                buff3[0] += 1
                                buff3[1][j3] = buff[1][j]
                                j3 += 1       
                            else:   
                                ecrireBloc(f3,i3,buff3)
                                i3 += 1
                                buff3 = [0, [Tnreg] * b]
                                buff3[0] += 1
                                buff3[1][0] = buff[1][j]  
                                j3 = 1                                                      
                i +=1
            ecrireBloc(f1,i1,buff1)
            ecrireBloc(f2,i2,buff2)
            ecrireBloc(f3,i3,buff3)
            affecter_entete(f1,1,i1+1)
            affecter_entete(f2,1,i2+1)
            affecter_entete(f3,1,i3+1)
            affecter_entete(f1,0,n1)
            affecter_entete(f2,0,n2)
            affecter_entete(f3,0,n3)
            f1.close
            f2.close
            f3.close
    except FileNotFoundError:
        print('fichier n\'exicte pas')

def default():
    return "invalid choice"


def choix(ch):
    switcher = {
        1: créer_fichier,
        2: fragmentation
    }
    
    return switcher.get(ch, default)()




def main():
    rep = 'O'
    while (rep == 'O'):
        print("""Entrer votre choix 
                 1: créer_fichier
                 2: fragmentation""")                
        ch = int(input())
        choix(ch)
        rep = input('Avez vous une autre opération O/N? :')

main()


