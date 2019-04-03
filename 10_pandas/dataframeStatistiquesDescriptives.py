# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

url = ('https://raw.github.com/pandas-dev''/pandas/master/pandas/tests/data/tips.csv')
tips = pd.read_csv(url)

#1 : STATISTIQUES BASIQUES
print(tips.info())
print(tips.describe(include='all'))
print(tips['sex'].describe())


#2 : TABULATIONS CROISEES : essayer de refaire proc FREQ
res=pd.crosstab(tips['sex'], [tips['smoker'], tips['day']])
print(res)

res=pd.crosstab(tips['sex'], [tips['smoker']])
print(res)
res2=pd.crosstab(tips['sex'], tips['smoker']).apply(lambda row: row/row.sum(), axis = 1)
print(res2)
res3=pd.crosstab(tips['sex'], tips['smoker']).apply(lambda col: col/col.sum(), axis = 0)
print(res3)


#3 : GROUP BY 
effectifsParSexe=tips.groupby('sex')['sex'].count()
pourboireMoyenParSexe=tips.groupby('sex').agg({'tip': np.mean})

pourboireMoyenEtNombreRepasParJour=tips.groupby('day').agg({'tip': np.mean, 'day': np.size})

pourboireMoyenParSexeStatutFumeurETJour=tips.groupby(['sex','smoker', 'day']).agg({'tip': [np.size, np.mean]})

pourboireMoyenEtnbFumeurparSexe=tips.groupby('sex').agg({'smoker': lambda row: row.value_counts()['Yes'],'tip': lambda row: sum(row) / len(row)})


#4 : INDEX COMPOSITES : permet de modifier facilement l'arrangement des variables groupées
#parallèle avec le décisionnel : dans le décisionnel il y a :
# les mesures : ici une/des variables quantitative (count ici)
# les dimensions : les variables qualitatives utilisées dans group by

#passer day (dernier et 3e niveau) de ligne en colonne
df2=pourboireMoyenParSexeStatutFumeurETJour.unstack()
#passer sexe (1e niveau => indice 0) de ligne en colonne
df3=pourboireMoyenParSexeStatutFumeurETJour.unstack(level=0)

#opération dans l'autre sens (ici retour arrière)
df3=df2.stack()

df4=pourboireMoyenParSexeStatutFumeurETJour.swaplevel('sex','smoker')


#5 : CORRELATION/COVARIANCE
print(tips.cov())
print(tips.corr())
print(tips.corr(method='kendall'))
print(tips.corr(method='spearman'))

