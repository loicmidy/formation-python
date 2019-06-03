# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

url = ('https://raw.github.com/pandas-dev''/pandas/master/pandas/tests/data/tips.csv')
tips = pd.read_csv(url)

# 1 : SELECTION DE COLONNES (SELECT du SQL)
selectionColonneSerie=tips['tip']
selectionColonneDataframe=tips[['tip']]
selectionColonnesDataframe=tips[['tip', 'sex']]


# 2 : SELECTION DE LIGNES SUR CONDITIONS (WHERE du SQL)
selectionLignesRespectantuneCondition=tips[tips['total_bill']>20]

# les 2 conditions doivent être respectées (& = ET) 
selectionLignesRespectantDeuxConditions=tips[(tips['total_bill']>20) & (tips['tip']>3)]
# au moins une des 2 conditions doit être respectée (| = OU) 
selectionLignesRespectantAuMoinsUneCondition=tips[(tips['total_bill']>20) | (tips['tip']>3)]

df=pd.DataFrame({'x':[1,np.nan,3]})
uneConditionPerteValeursManquantes=df[df['x']>1]
uneConditionEtGarderValeursManquantes=df[(df['x'].isna()) | (df['x']>1)]

# 3 : SELECTION/SLICING SUR POSITIONS  COMME AVEC NUMPY
tips.iloc[0]#sélection première ligne
#s'il y avait un index de ligne on pourrait utiliser tips.loc['valeurIndexPourLigne']
tips.iloc[0:2]#sélection deux premières lignes
tips.iloc[0:2,0:2]#sélection deux premières lignes et colonnes


# 4 : COMBINER filtres colonnes et lignes
selectionColonnesDataframePlusFiltreWhere=tips[tips['total_bill']>20][['tip', 'sex']]


# 5 : OPERATIONS COLONNES
tips['tip_pct']=tips['tip']/tips['total_bill']*100
tips['bucket'] = np.where(tips['total_bill'] < 10, 'low', 'high')

tips.drop(['total_bill_with_taxes'], axis=1,inplace=True)
tips.rename(columns={'total_bill': 'total_bill_2'},inplace=True)
tips.rename(columns={'total_bill_2': 'total_bill'},inplace=True)

tips.sort_values(['sex', 'total_bill'],ascending=[True,False],inplace=True)

def calculsComplexesPlusieursColonnes(total_bill,tip,smoker):
    if smoker=="Yes":return total_bill+tip
    else : return total_bill+2*tip
        
tips['résultat'] = tips.apply(lambda row: calculsComplexesPlusieursColonnes(row['total_bill'], row['tip'],row['sex']), axis=1)


# 6 : CONCATENER dataframes
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],'B': ['B0', 'B1', 'B2', 'B3'],'C': ['C0', 'C1', 'C2', 'C3']},index=[0,1,2,3])
df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],'B': ['B4', 'B5', 'B6', 'B7'],'C': ['C4', 'C5', 'C6', 'C7']}, index=[4,5,6,7])
result = pd.concat([df1,df2],keys=['df1', 'df2'])#keys est optionnel : il donne index de ligne composite : avec le numéro plus le dataframe d'origine

result.loc['df2']


# 7 : JOINTURES
sifa=pd.DataFrame({'nom_sifa':['nom_a','nom_b'],'prenom_sifa':['prenom_a','prenom_b'],'INE':['AAAA','BBB']})
mmo=pd.DataFrame({'nom_mmo':['nom_a','nom_c'],'prenom_mmo':['prenom_a','prenom_c'],'salaire':[10,9]})

sifa_mmo_inner_join= sifa.merge(mmo, left_on=['nom_sifa', 'prenom_sifa'], right_on=['nom_mmo', 'prenom_mmo'], how='inner')
sifa_mmo_left_join= sifa.merge(mmo, left_on=['nom_sifa', 'prenom_sifa'], right_on=['nom_mmo', 'prenom_mmo'], how='left')
sifa_mmo_right_join= sifa.merge(mmo, left_on=['nom_sifa', 'prenom_sifa'], right_on=['nom_mmo', 'prenom_mmo'], how='right')
sifa_mmo_outer_join= sifa.merge(mmo, left_on=['nom_sifa', 'prenom_sifa'], right_on=['nom_mmo', 'prenom_mmo'], how='outer')

#il est possible d'utiliser le paramètre optionnel validate qui détermine le type de jointure : cela permet de détecter des doublons s'il ne doit pas y en avoir
left = pd.DataFrame({'A' : [1,2], 'B' : [1, 2]})
right = pd.DataFrame({'A' : [4,5,6], 'B': [2, 2, 2]})
result = pd.merge(left, right, on='B', how='outer', validate="one_to_one")
#MergeError: Merge keys are not unique in right dataset; not a one-to-one merge


