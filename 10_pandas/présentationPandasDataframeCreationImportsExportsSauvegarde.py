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

#EXPORTS
notesElevesMatières.to_csv("C:/Users/lmidy/Documents/GitHub/dataFormationPython/elevesModifie.csv",sep="|")


#SAUVEGARDE : on peut sauvegarder des dataframes dans un fichier au format HDF5 puis charger le contenu du fichier dans un dataframe
#c'est très performant : pour 6 millions de lignes l'écriture ou la lecture prend quelques secondes et le fichier HDF5 pèse 118 Mo seulement
#écriture
i=0
while i<20:
    i=i+1
    notesElevesMatières=notesElevesMatières.append(notesElevesMatières)

store=pd.HDFStore('C:/Users/lmidy/Documents/GitHub/dataFormationPython/eleves.h5')
store['notesElevesMatieres'] = notesElevesMatières
store.close()

#lecture
notes=pd.read_hdf('C:/Users/lmidy/Documents/GitHub/dataFormationPython/eleves.h5','notesElevesMatieres')


#AUTRE FORMAT SAUVEGARDE : en cours de développement joint entre communauté Python et R
import feather
import pandas as pd
import numpy as np
import datetime as dt
arr = np.random.randn(10000000) # 10% nulls
arr[::10] = np.nan
df = pd.DataFrame({'column_{0}'.format(i): arr for i in range(10)})



a=dt.datetime.now()
feather.write_dataframe(df, 'C:/Users/lmidy/Documents/GitHub/dataFormationPython/test.feather')
durée=dt.datetime.now()-a
print("écriture dans fichier feather : ",durée.seconds)

a=dt.datetime.now()
store=pd.HDFStore('C:/Users/lmidy/Documents/GitHub/dataFormationPython/test.h5')
store['test'] = df
store.close()
durée=dt.datetime.now()-a
print("écriture dans fichier hdf5 : ",durée.seconds)

a=dt.datetime.now()
df_feather = feather.read_dataframe('C:/Users/lmidy/Documents/GitHub/dataFormationPython/test.feather')
durée=dt.datetime.now()-a
print("lecture dans fichier feather : ",durée.seconds)

a=dt.datetime.now()
df_hdf5=pd.read_hdf('C:/Users/lmidy/Documents/GitHub/dataFormationPython/test.h5','test')
durée=dt.datetime.now()-a
print("lecture dans fichier hdf5 : ",durée.seconds)


