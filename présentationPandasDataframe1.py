# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

notesElevesMatières=pd.DataFrame({'math':[2,10,15,17,20],'physique':[np.nan,9,14,12,17]},index=['a','b','c','d','midy'])
print(notesElevesMatières)
print(notesElevesMatières.describe(include='all'))#les calculs sont faits hors NaN