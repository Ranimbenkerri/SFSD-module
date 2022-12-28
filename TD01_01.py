from ast import dump
from json import load
from pickle import dumps, loads
from sys import getsizeof

b = 5
tnom = 20
tprenom = 20
tnuminc = 10
teng = tnom + tprenom + tnuminc + 1
etud = '#' * teng

bloc = [0, [etud]*b]


blocSize = getsizeof(dumps(bloc))+(len(etud)+1)*(b-1)



def resize_chaine (chaine , TailleMax):

    for i in range (len(chaine),TailleMax):
        chaine = chaine + '#'

    return chaine


def LireBlock(f,i):
    ## 2 ===> les caracterstiques de fichie
    ad = 2 * getsizeof(dumps(0))+i*blocSize
    f.seek(ad,0) 
    ## 0 ====> form begin  \ f ===> fichie
    buf = f.read(blocSize)
    return buf

def EcrireBlock(f,i,buf):
    ## 2 ===> les caracterstiques de fichie
    ad = 2 * getsizeof(dumps(0))+i*blocSize
    f.seek(ad,0) 
    ## 0 ====> form begin  \ f ===> fichie
    f.write(dumps(buf))
    return 

f = open(file="test.txt",mode="r")
print(LireBlock(f,0))

def entete(f,ind):
    ad = ind * getsizeof(dumps(0))
    f.seek(ad,0)
    car = f.read(getsizeof(dumps))
    return (loads(car))
    
def affentete(f,ind,car):
    ad = ind * getsizeof(dumps(0))
    f.seek(ad,0) 
    f.write(dumps(car))
    return 
with open("test.txt","r") as fic:
    a = fic.readline()
