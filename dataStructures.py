# -*- coding: utf-8 -*-

#1 : LISTES : liste d'éléments de taille variable dont on peut modifier les éléments
# attention : le premier élément est en position 0 et non pas en position 1
l=[1,2,3,"toto"] #création

l.append("titi") #ajout "titi" à la fin
print(l)

l.pop(0)# enlève l'élément en position 0
print(l)

#coupe/slice des éléments de 1 inclus à 3 exclu donc les éléments en 2e et 3e position
# le slicing est une notion importante qu'on va revoir avec numpy et pandas
ll=l[1:3]
print(ll)

#parcours de liste
for e in l:
    print(e)



#2 DICTIONNAIRES : ensemble de clés/valeurs associées
#création
dictionnaireElèves={"0000000000A":["loïc","midy","02/08/1977","M","fontenay aux roses"],
        "0000000000B":["sophie","bernardini-midy","11/08/1979","F","vernon"]}
#accès à la valeur d'un élément en utilisant la clé ici "0000000000A"
print (dictionnaireElèves["0000000000A"])

print(dictionnaireElèves.keys()) # retourne une liste des clés du dictionnaire
print(dictionnaireElèves.values())# retourne une liste des valeurs du dictionnaire

#accès très très rapide à un élément : on peuple un dictionnaire avec 10 millions de clés/valeurs 
#et ensuite on récupère quasi instantanément la valeur !
i,d=0,{}
while i<10000000:
    d[i]=i
    i=i+1
print(d[5])

#3 TUPLES : conteneur de données de taille fixe dont on ne peut pas modifier le contenu si contient des types de base
#création
tupleTest=(1,"toto")
print (tupleTest)

#accès à une des valeurs données
print (tupleTest[0],tupleTest[1])

#mise à jour de tuple impossible si contient des types de base => génère une exception
try:
    tupleTest[0] = 100
except Exception as exception:
    print("exception : ",exception)

#mise à jour de tuple possible si contient un objet mutable plus complexe
tupleTest=([1,2],"toto")
tupleTest[0].append(3)
print (tupleTest)


#opérations
tupleTest=(1, 2, 3) + (4, 5, 6)
print (tupleTest)

#4 SET : liste non ordonnée d'éléments uniques (donc pas de doublons dans des set)
#création
setTest={1,2,3,1}
print (setTest)#1 n'apparait bien qu'une fois et pas deux

#opérations ensemblistes
a={1,2,3,4}
b={3,4,5,6}
c=a.union(b)
print(c)
c=a.intersection(b)
print(c)
c=a-b
print(c)

#ajout et suppression
a.add(10)
print(a)
a.discard(1)
print(a)


#sets