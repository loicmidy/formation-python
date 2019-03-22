# -*- coding: utf-8 -*-

#listes : liste d'éléments de taille variable dont on peut modifier les éléments
# attention : le premier élément est en position 0 et non pas en position 1
l=[1,2,3,"toto"] #création

l.append("titi") #ajout "titi" à la fin
print(l)

l.pop(0)# enlève l'élément en position 0
print(l)

ll=l[1:3]#coupe/slice des éléments de 1 inclus à 3 exclu donc les éléments en 2e et 3e position
print(ll)

#parcours de liste
for e in l:
    print(e)



#dictionnaires : ensemble de clés/valeurs associées
#création
élèves={"0000000000A":["loïc","midy","02/08/1977","M","fontenay aux roses"],
        "0000000000B":["sophie","bernardini-midy","11/08/1979","F","vernon"]}
#accès à la valeur d'un élément en utilisant la clé ici "0000000000A"
print (élèves["0000000000A"])

print(élèves.keys()) # retourne une liste des clés du dictionnaire
print(élèves.values())# retourne une liste des valeurs du dictionnaire

#accès très très rapide à un élément : on peuple un dictionnaire avec 10 millions de clés/valeurs 
#et ensuite on récupère quasi instantanément la valeur !
i,d=0,{}
while i<10000000:
    d[i]=i
    i=i+1
print(d[5])

#tuples : conteneur de données de taille fixe dont on ne peut pas modifier le contenu si contient des types de base
#création
t=(1,"toto")
print (t)

#accès à une des valeurs données
print (t[0],t[1])

#mise à jour de tuple impossible si contient des types de base => génère une exception
try:
    t[0] = 100
except Exception as exception:
    print("exception : ",exception)

#mise à jour de tuple possible si contient un objet mutable plus complexe
t=([1,2],"toto")
t[0].append(3)
print (t)


#opérations
t=(1, 2, 3) + (4, 5, 6)
print (t)










#sets