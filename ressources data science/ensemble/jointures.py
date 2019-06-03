# -*- coding: utf-8 -*-
import pandas as pd

sifa=pd.DataFrame({'nom_sifa':['nom_a','nom_b'],'prenom_sifa':['prenom_a','prenom_b'],'INE':['AAAA','BBB']})
mmo=pd.DataFrame({'nom_mmo':['nom_a','nom_c'],'prenom_mmo':['prenom_a','prenom_c'],'salaire':[10,9]})

sifa_mmo_inner_join= sifa.merge(mmo, left_on=['nom_sifa', 'prenom_sifa'], right_on=['nom_mmo', 'prenom_mmo'], how='inner')
sifa_mmo_left_join= sifa.merge(mmo, left_on=['nom_sifa', 'prenom_sifa'], right_on=['nom_mmo', 'prenom_mmo'], how='left')
sifa_mmo_right_join= sifa.merge(mmo, left_on=['nom_sifa', 'prenom_sifa'], right_on=['nom_mmo', 'prenom_mmo'], how='right')
sifa_mmo_outer_join= sifa.merge(mmo, left_on=['nom_sifa', 'prenom_sifa'], right_on=['nom_mmo', 'prenom_mmo'], how='outer')

#il est possible d'utiliser le paramètre optionnel validate qui détermine le type de jointure : 
#cela permet de détecter des doublons s'il ne doit pas y en avoir
left = pd.DataFrame({'A' : [1,2], 'B' : [1, 2]})
right = pd.DataFrame({'A' : [4,5,6], 'B': [2, 2, 2]})
result = pd.merge(left, right, on='B', how='outer', validate="one_to_one")
#MergeError: Merge keys are not unique in right dataset; not a one-to-one merge
