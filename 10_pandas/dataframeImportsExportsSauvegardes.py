# -*- coding: utf-8 -*-
import pandas as pd

notesElevesMatières=pd.read_csv("C:/Users/lmidy/Documents/GitHub/dataFormationPython/eleves.csv",sep="|",dtype={'élève':str,'moyenneMath':float,'moyennePhysique':str,'sexe':str,'PCS':int,'dateNaissance':str})
#notesElevesMatières=pd.read_sas("")

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



