# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

url = ('https://raw.github.com/pandas-dev''/pandas/master/pandas/tests/data/tips.csv')
tips = pd.read_csv(url)

#SELECT du SQL
selectionColonneSerie=tips['tip']
selectionColonneDataframe=tips[['tip']]
selectionColonnesDataframe=tips[['tip', 'sex']]


#OPERATIONS COLONNES
tips['total_bill_with_taxes'] = tips['total_bill'] + 2
tips['bucket'] = np.where(tips['total_bill'] < 10, 'low', 'high')

tips.drop(['total_bill_with_taxes'], axis=1,inplace=True)
tips.rename(columns={'total_bill': 'total_bill_2'},inplace=True)
tips.rename(columns={'total_bill_2': 'total_bill'},inplace=True)

tips.sort_values(['sex', 'total_bill'],inplace=True)

def calculsComplexesPlusieursColonnes(total_bill,tip,smoker):
    if smoker=="Yes":return total_bill+tip
    else : return total_bill+2*tip
        
tips['résultat'] = tips.apply(lambda row: calculsComplexesPlusieursColonnes(row['total_bill'], row['tip'],row['sex']), axis=1)


#WHERE du SQL
selectionLignesRespectantuneCondition=tips[tips['total_bill']>20]
# les 2 conditions doivent être respectées (& = ET) 
selectionLignesRespectantDeuxConditions=tips[(tips['total_bill']>20) & (tips['tip']>3)]
# au moins une des 2 conditions doit être respectée (| = OU) 
selectionLignesRespectantAuMoinsUneCondition=tips[(tips['total_bill']>20) | (tips['tip']>3)]


#COMBINER OPERATEURS SQL
selectionColonnesDataframePlusFiltreWhere=tips[tips['total_bill']>20][['tip', 'sex']]


#GROUP BY du SQL
effectifsParSexe=tips.groupby('sex')['sex'].count()

pourboireMoyenEtNombreRepasParJour=tips.groupby('day').agg({'tip': np.mean, 'day': np.size})

pourboireMoyenParStatutFumeurETJour=tips.groupby(['smoker', 'day']).agg({'tip': [np.size, np.mean]})


#JOINTURES
sifa=pd.DataFrame({'nom_sifa':['nom_a','nom_b'],'prenom_sifa':['prenom_a','prenom_b'],'INE':['AAAA','BBB']})
mmo=pd.DataFrame({'nom_mmo':['nom_a','nom_c'],'prenom_mmo':['prenom_a','prenom_c'],'salaire':[10,9]})

sifa_mmo_inner_join= sifa.merge(mmo, left_on=['nom_sifa', 'prenom_sifa'], right_on=['nom_mmo', 'prenom_mmo'], how='inner')
sifa_mmo_left_join= sifa.merge(mmo, left_on=['nom_sifa', 'prenom_sifa'], right_on=['nom_mmo', 'prenom_mmo'], how='left')
sifa_mmo_right_join= sifa.merge(mmo, left_on=['nom_sifa', 'prenom_sifa'], right_on=['nom_mmo', 'prenom_mmo'], how='right')
sifa_mmo_outer_join= sifa.merge(mmo, left_on=['nom_sifa', 'prenom_sifa'], right_on=['nom_mmo', 'prenom_mmo'], how='outer')








