##1st Tip

## 2nd Tip
""" 
 Dans  la déclaration on définit le typeBloc Tbloc=[0,[Tnreg]*b]
 le premier élément buf[0] c le buf.NB qui est de type entier initialisé à 0
 le deuxième c'est le tableau d'enregistrement de type enregistrement [Tenreg]*b
"""

## 3rd Tip
""" la fonction créer c'est l'algorithme de chargement initial d'un fichier T~OF
    Dans ce cas les blocs sont remplis à 100% si on veut remplir les blocs avec
     un % donné, on peut juste envoyer à la fonction créer une variable soit par
     exemple mu et pour tester le si le bloc est plein, au lieu de faire j<b on fait 
     si j<b*mu (si on veut remplir les blocs à 50%, mu alors = 0.5 )
 """
 
 
 ## 4th Tip
"""
            RQ: j'ai choisi d'afficher les fichiers supprimés logiquement
            pour faire la difference entre eux et les fichiers supprimés physiquement
            """
## 5th Tip
  # print(f"buff 1{str(buff)}")
  
  
## 6th Tip

                                # print(f"buff 2{str(buff)}")


                                # print("buff1"+str(i))
## 7th tip

     # print("last"+str(i))


                                # print(f'last {buff}')
#8th tip
## i created a Class To try remove the useless bad implementation of engistrement in python (dedicace el hougra)
# class Etudiant:
#     def __init__(self,tnom,tprénom,tnuminscpt):
#         self._tnom=tnom
#         self._tprénom=tprénom
#         self._tnuminscpt=tnuminscpt
#       # getter method
#     def get_tnom(self):
#         return self.tnom
#     # setter method
#     def set_tnom(self, newValue):
#         self.tnom = newValue
# ilyas=Etudiant("Ranim","Benkerri","2312172")