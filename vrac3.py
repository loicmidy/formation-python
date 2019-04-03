# -*- coding: utf-8 -*-
import pandas as pd

nombreEleves=pd.DataFrame({'élève':['a','b','c','d','e','f'],'sexe':['H','F','H','F','H','F'],'PCS':['cadre','ouvrier','cadre','employé','cadre','employé'],'annéeScolaire':['1718','1718','1718','1617','1617','1617']})


df=nombreEleves.groupby(['sexe', 'PCS', 'annéeScolaire'])['élève'].size().to_frame()


df2=df.unstack()
df3=df2.unstack()