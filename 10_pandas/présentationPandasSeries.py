# -*- coding: utf-8 -*-
import pandas as pd

#BASES
#on peut voir une série comme une variable aléatoire avec clé/valeur
notesElevesMath=pd.Series([2,10,15,17,20],index=['a','b','c','d','e'])
print(notesElevesMath)

#mettre des labels sur la série
notesElevesMath.name="notes des élèves en Mathématiques"
notesElevesMath.index.name="nom de l'élève"
print(notesElevesMath)

#sélection
print(notesElevesMath['e'])
print(notesElevesMath[notesElevesMath>14])

#STATISTIQUES 1 VA
#VA quantitative
notesElevesMath=pd.Series(list(range(101)))
print(notesElevesMath.describe())
print(notesElevesMath.describe(percentiles=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]))
print(notesElevesMath.mean())
print(notesElevesMath.median())
print(notesElevesMath.std())
print(notesElevesMath.skew())#coefficient d'asymétrie (skewness en anglais) 
print(notesElevesMath.kurtosis())#

#VA qualitative
notesElevesMath=pd.Series(['excellent','bien','bien','moyen','moyen'],index=['a','b','c','d','e'])
print(notesElevesMath.describe())
print(notesElevesMath.value_counts())

notesElevesMathCSP=pd.Series([18,12,10,20,9,14],index=['cadre','employé','ouvrier','cadre','ouvrier','employé'])
notesElevesMathCSP.index.name="CSP représentant légal"
print(notesElevesMathCSP.groupby(notesElevesMathCSP).mean())

#jointure entre 2 VA
notesElevesMath=pd.Series([2,10,15,17,20],index=['a','b','c','d','e'])
notesElevesPhysique=pd.Series([9,14,12,17],index=['b','c','d','e'])

moyenneEleves=notesElevesMath.add(notesElevesPhysique, fill_value=0)/2
print(moyenneEleves)

#statistiques entre 2 VA
print(notesElevesMath.corr(notesElevesPhysique))
