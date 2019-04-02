# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

#PREMIER DATAFRAME
notesElevesMatières=pd.DataFrame({'math':[2,10,15,17,20,8],'physique':[np.nan,9,14,12,17,17],'sexe':['H','F','H','F','H','F']},index=['a','b','c','d','e','f'])
print(notesElevesMatières)
print(notesElevesMatières.describe(include='all'))#les calculs sont faits hors NaN


#IMPORTS
notesElevesMatières=pd.read_csv("C:/Users/lmidy/Documents/GitHub/dataFormationPython/eleves.csv",sep="|",dtype={'élève':str,'moyenneMath':float,'moyennePhysique':str,'sexe':str,'PCS':int,'dateNaissance':str})
#notesElevesMatières=pd.read_sas("")
print(notesElevesMatières.info())


#DOUBLONS suppression des doublons : il y a 2 fois l'élève a dans le fichier
notesElevesMatièresSansDoublons=notesElevesMatières.drop_duplicates(['élève'])#notesElevesMatières pas modifié
notesElevesMatières.drop_duplicates(['élève'],inplace=True) #inplace=True=>notesElevesMatières est modifié


#CONVERSIONS
#conversion avec astype()
notesElevesMatières['PCS']=notesElevesMatières['PCS'].astype('int16')#car astype retourne une copie
print(notesElevesMatières.info())

#conversion avec fonction ad hoc
def convertirvariableSexe(sexe):
    if sexe=="H":return 1
    else: return 2

notesElevesMatières['sexe']=notesElevesMatières['sexe'].apply(convertirvariableSexe)
print(notesElevesMatières.info())

#conversion avec to_numeric() et to_datetime()
notesElevesMatières['moyennePhysique']=pd.to_numeric(notesElevesMatières['moyennePhysique'], errors='coerce')
print(notesElevesMatières.info())

notesElevesMatières['dateNaissance']= pd.to_datetime(notesElevesMatières['dateNaissance'], format='%d%m%Y', errors='coerce')

notesElevesMatières['jourNaissance'] = pd.DatetimeIndex(notesElevesMatières['dateNaissance']).day
notesElevesMatières['moisNaissance'] = pd.DatetimeIndex(notesElevesMatières['dateNaissance']).month
notesElevesMatières['annéeNaissance'] = pd.DatetimeIndex(notesElevesMatières['dateNaissance']).year

print(notesElevesMatières.info())

