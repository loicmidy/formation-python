# -*- coding: utf-8 -*-
import datetime as dt
import numpy as np

# 1 : PERFORMANCES
#numpy est très performant pour faire des calculs sur des tableaux
tableauUnMillions = np.arange(1000000)
listeUnMillions =  list(range(1000000))

a=dt.datetime.now()
i=0
while i<50 :
    tableauUnMillions = tableauUnMillions * 2
    i=i+1
durée=dt.datetime.now()-a
print("temps de traitement tableauUnMillions : ",durée.seconds)

a=dt.datetime.now()
i=0
while i<50 :
    listeUnMillions=[x*2 for x in listeUnMillions]
    i=i+1
durée=dt.datetime.now()-a
print("temps de traitement listeUnMillions : ",durée.seconds)


#2 INFORMATIONS DE BASE SUR TABLEAUX
# dans un tableau tous les éléments sont de même type
print(tableauUnMillions.shape)#shape=forme du tableau => ici 1 dimension avec 10 millions d'éléments
print(tableauUnMillions.dtype)#type de données => ici des entiers (numpy "devine" le bon type d'après les données fournies)

#on peut fixer soit même le type des données
tableau=np.array([1,2,3],dtype=np.int16)#ici entier sur 16 bits donc ne pas dépasser 2^16 soit 65536

#conversion (synonymes : transtypage/cast en Anglais) types de données
tableau=tableau.astype(np.float64)
print(tableau.dtype)


#3 SLICING
tableau = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(tableau)

sliceRéalisée=tableau[:2,1:]
print("sélection: ",sliceRéalisée,"forme: ",sliceRéalisée.shape,"dimension: ",sliceRéalisée.ndim)

sliceRéalisée=tableau[2]
print("sélection: ",sliceRéalisée,"forme: ",sliceRéalisée.shape,"dimension: ",sliceRéalisée.ndim)

sliceRéalisée=tableau[:,:2]
print("sélection: ",sliceRéalisée,"forme: ",sliceRéalisée.shape,"dimension: ",sliceRéalisée.ndim)

sliceRéalisée=tableau[1:2,:2]
print("sélection: ",sliceRéalisée,"forme: ",sliceRéalisée.shape,"dimension: ",sliceRéalisée.ndim)


#4 OPERATIONS
#multiplication élément par élément (fonctionnement analogue *,/,-)
tableau = np.array([[1,2,3],[4,5,6]])
print(tableau*tableau)

tab1= np.array([1,4,5])
tab2= np.array([2,3,6])
tabMax=np.maximum(tab1,tab2)
print(tabMax)

tableau = np.array([[1,2,3],[4,5,6]])
print(tableau.mean(),tableau.std())

#moyenne suivant axe 1 donc moyenne sur chaque ligne, écart type suivant axe 0 donc suivant les colonnes
print(tableau.mean(axis=1),tableau.std(axis=0))


#5 ALGEBRE LINEAIRE
#transposition
tableau = np.array([[1,2,3],[4,5,6]])
print(tableau.T)

#produit matriciel
tab1= np.array([1,2,3])
tab2= np.array([[4],[5],[6]])
print(tab1.dot(tab2))

#produit matriciel reste performant sur des matrices 2000*2000 => 5s
n=2000
tab1=np.arange(n*n).reshape((n,n))
tab2=np.arange(n*n).reshape((n,n),order='F')
#print(tab1.flags,tab2.flags)

a=dt.datetime.now()
tab3=tab1.dot(tab2)
durée=dt.datetime.now()-a
print("durée : ",durée.seconds)


#6 CHANGEMENT DE FORME DE TABLEAUX : reshaping and ravel
#reshaping
tab1 = np.arange(8)
print(tab1)
tab2=tableau.reshape((4, 2))
print(tab2)
tab3=tableau.reshape((4, 2),order='F')
print(tab3)

#l'inverse : ravel
print(tab2)
tab4=tab2.ravel()
print(tab4)
tab5=tab2.ravel(order='F')
print(tab5)





