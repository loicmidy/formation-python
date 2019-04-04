# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage,fcluster
import numpy as np
import seaborn as sns 
from sklearn import preprocessing
import pandas as pd

iris = sns.load_dataset("iris")
X=iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].values

X_scaled = preprocessing.scale(X)

Z = linkage(X_scaled, 'ward')

# dendrogram complet
plt.figure(figsize=(25, 10))
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('sample index')
plt.ylabel('distance')
dendrogram(Z)
plt.show()

# dendrogram tronqué
plt.title('Hierarchical Clustering Dendrogram (truncated)')
plt.xlabel('sample index')
plt.ylabel('distance')
dendrogram(
    Z,
    truncate_mode='lastp',  # show only the last p merged clusters
    p=12,  # show only the last p merged clusters
)
plt.show()

mesClusters=pd.Series(fcluster(Z, 3, criterion='maxclust'))
finalDf = pd.concat([iris, mesClusters], axis = 1)