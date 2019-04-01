# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 15:56:45 2019

@author: lmidy
"""

l=[1,2,3]

l=[x*2 for x in l]
print(l)


import numpy as np
import datetime as dt

n=2000
tab1=np.arange(n*n).reshape((n,n))
tab2=np.arange(n*n).reshape((n,n),order='F')
#print(tab1.flags,tab2.flags)

a=dt.datetime.now()
tab3=tab1.dot(tab2)
durée=dt.datetime.now()-a
print("durée : ",durée.seconds)


from sklearn.cluster import AgglomerativeClustering
import numpy as np
X = np.array([[1, 2], [1, 4], [1, 0],[4, 2], [4, 4], [4, 0]])