# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from fancyimpute import KNN, NuclearNormMinimization, SoftImpute, IterativeImputer, BiScaler

#imputation par la moyenne, la médiane ou la valeur la plus fréquente
notesElevesMatières=pd.DataFrame({'math':[2,10,np.nan,18,18,8],'physique':[np.nan,9,14,12,19,19],'chimie':[4,9,14,12,19,np.nan],'sexe':['H','F','H','F','H','F']})
print(notesElevesMatières.describe(include='all'))

notesElevesMatièresImputationMoyenne=notesElevesMatières.fillna(notesElevesMatières.mean())
notesElevesMatièresImputationMediane=notesElevesMatières.fillna(notesElevesMatières.median())

notesElevesMatièresImputationPlusFréquent=notesElevesMatières.apply(lambda col:col.fillna(col.value_counts().index[0]))

notesElevesMatièresImputationInterpolation=notesElevesMatières.interpolate()

#
notesElevesMatièresImputationKnn = KNN(k=3).fit_transform(notesElevesMatières)