# -*- coding: utf-8 -*-
import pandas as pd

#on peut voir une série comme une variable aléatoire avec clé/valeur
notesElevesMath=pd.Series([2,10,15,17,20],index=['a','b','c','d','midy'])
print(notesElevesMath)

#mettre des labels sur la série
notesElevesMath.name="notes des élèves en Mathématiques"
notesElevesMath.index.name="nom de l'élève"
print(notesElevesMath)

#sélection
print(notesElevesMath['midy'])
print(notesElevesMath[notesElevesMath>14])

#statistiques
print(notesElevesMath.describe())
print(notesElevesMath.mean())
print(notesElevesMath.median())
print(notesElevesMath.std())
print(notesElevesMath.skew())#coefficient d'asymétrie (skewness en anglais) 
print(notesElevesMath.kurtosis())#

notesElevesMathCSP=pd.Series([18,12,10,20,9,14],index=['cadre','employé','ouvrier','cadre','ouvrier','employé'])
notesElevesMathCSP.index.name="CSP représentant légal"
print(notesElevesMathCSP.groupby(notesElevesMathCSP).mean())

#jointure entre 2 VA
notesElevesPhysique=pd.Series([9,14,12,17],index=['b','c','d','midy'])

moyenneEleves=notesElevesMath.add(notesElevesPhysique, fill_value=0)/2
print(moyenneEleves)

#statistiques entre 2 VA
print(notesElevesMath.corr(notesElevesPhysique))
