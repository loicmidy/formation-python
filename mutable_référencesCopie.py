# -*- coding: utf-8 -*-

#mutable/immutable
nom="loïc midy"
print(nom[0])

#les strings sont immutables
try:
    nom[0] ="a"
except Exception as exception:
    print("exception : ",exception)


#Références sur le même objet/copie
l=[1,2,3,4,5]
ll=l # attention ll et l référencent tous les deux la même liste : si ll change alors l change
ll[0]="toto"
print(l)

l=[1,2,3,4,5]
ll=l.copy() #ll est une nouvelle liste issue de la copie de l
ll[0]="toto"
print(l)