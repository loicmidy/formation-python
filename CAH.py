# -*- coding: utf-8 -*-
import seaborn as sns 
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.cluster import AgglomerativeClustering


iris = sns.load_dataset("iris")
X=iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].values

X_scaled = preprocessing.scale(X)

cluster = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='ward')  
cluster.fit_predict(X_scaled) 

print(cluster.labels_)  


#ajouter dendogrammes scipy


Y=iris['species'].values