# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

url = ('https://raw.github.com/pandas-dev''/pandas/master/pandas/tests/data/tips.csv')
tips = pd.read_csv(url)

#SELECT du SQL
selectionColonnes=tips[['tip', 'sex']]

#WHERE du SQL
# les 2 conditions doivent être respectées (& = ET) 
selectionLignesRespectantDeuxConditions=tips[(tips['total_bill']>20) & (tips['tip']>3)]

# au moins une des 2 conditions doivent être respectées (| = OU) 
selectionLignesRespectantAuMoinsUneCondition=tips[(tips['total_bill']>20) | (tips['tip']>3)]


#GROUP BY du SQL
effectifsParSexe=tips.groupby('sex')['sex'].count()

pourboireMoyenEtNombreRepasParJour=tips.groupby('day').agg({'tip': np.mean, 'day': np.size})

pourboireMoyenParStatutFumeurETJour=tips.groupby(['smoker', 'day']).agg({'tip': [np.size, np.mean]})