# -*- coding: utf-8 -*-
import pandas as pd


notesElevesMatières=pd.read_csv('C:/Users/loicm/ressources data science/ensemble/eleves.csv',sep="|",
                                dtype={'élève':str,
                                       'moyenneMath':float,
                                       'moyennePhysique':str,
                                       'sexe':str,
                                       'dateNaissance':str,
                                       'PCS':int})
print(notesElevesMatières.info())

#1 : conversion avec astype()
notesElevesMatières['PCS']=notesElevesMatières['PCS'].astype('int16')#car astype retourne une copie
print(notesElevesMatières.info())

#2 : conversion avec fonction ad hoc
def convertirvariableSexe(sexe):
    if sexe=="H":return 1
    else: return 2

notesElevesMatières['sexe']=notesElevesMatières['sexe'].apply(convertirvariableSexe)
print(notesElevesMatières.info())

#3 : conversion avec to_numeric() et to_datetime()
notesElevesMatières['moyennePhysique']=pd.to_numeric(notesElevesMatières['moyennePhysique'], errors='coerce')
"""
errors ='raise'  => the default and will generate an error on something like [1,2,'apple']. 
errors ='ignore' => the problem values will not be converted at all. 
errors ='coerce' => force the column to float and problem values to NaN
"""
print(notesElevesMatières.info())

notesElevesMatières['dateNaissance']= pd.to_datetime(notesElevesMatières['dateNaissance'], format='%d%m%Y', errors='coerce')

notesElevesMatières['jourNaissance'] = pd.DatetimeIndex(notesElevesMatières['dateNaissance']).day
notesElevesMatières['moisNaissance'] = pd.DatetimeIndex(notesElevesMatières['dateNaissance']).month
notesElevesMatières['annéeNaissance'] = pd.DatetimeIndex(notesElevesMatières['dateNaissance']).year

print(notesElevesMatières.info())

