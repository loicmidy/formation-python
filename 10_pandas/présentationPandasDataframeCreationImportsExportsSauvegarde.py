# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

#PREMIER DATAFRAME
notesElevesMatières=pd.DataFrame({'math':[2,10,15,17,20,8],'physique':[np.nan,9,14,12,17,17],'sexe':['H','F','H','F','H','F']},index=['a','b','c','d','e','f'])
print(notesElevesMatières)
print(notesElevesMatières.describe(include='all'))#les calculs sont faits hors NaN

#IMPORTS
notesElevesMatières=pd.read_csv("eleves.csv",sep="|")
#notesElevesMatières=pd.read_sas("")


#EXPORTS
notesElevesMatières.to_csv("elevesModifie.csv")


#SAUVEGARDE : on peut sauvegarder des dataframes dans un fichier au format HDF5 puis charger le contenu du fichier dans un dataframe
#c'est très performant : pour 6 millions de lignes l'écriture ou la lecture prend quelques secondes et le fichier HDF5 pèse 118 Mo seulement
#écriture
i=0
while i<20:
    i=i+1
    notesElevesMatières=notesElevesMatières.append(notesElevesMatières)

store=pd.HDFStore('eleves.h5')
store['notesElevesMatieres'] = notesElevesMatières
store.close()

#lecture
notes=pd.read_hdf('eleves.h5','notesElevesMatieres')

#


