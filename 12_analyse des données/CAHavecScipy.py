# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage,fcluster
import numpy as np
import seaborn as sns 
from sklearn import preprocessing
import pandas as pd

# chargement des données et leur normalisation
iris = sns.load_dataset("iris")
X=iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].values

X_scaled = preprocessing.scale(X)

# calcul des clusters
Z = linkage(X_scaled, 'ward')
"""
Z comporte une ligne par merge de la forme  [idx1, idx2, dist, sample_count].
idx1 et idx2 sont les id des clusters mergés à cette étape
au début idx1 et idx2 sont les id des observations de base (i.e on merge des clusters élémentaires avec 1 obs)
puis à un moment il y a merge de clusters avec plusieurs lignes
All indices idx >= len(X) actually refer to the cluster formed in Z[idx - len(X)]
"""

# calcul écart de variance inter cluster pour chaque regroupement/dégroupement de cluster
df=pd.DataFrame(Z,columns=['idx1','idx2','dist','sample_count'])
df_fin=df.tail(6)
df_fin.plot(y=["dist"],kind='line')


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

# fcluster form flat clusters from the hierarchical clustering defined by the given linkage matrix
mesClusters=pd.Series(fcluster(Z, 3, criterion='maxclust'))
finalDf = pd.concat([iris, mesClusters], axis = 1)


# utlisation d'un autre critère d'agrégation
Z = linkage(X_scaled, 'single')
df=pd.DataFrame(Z,columns=['idx1','idx2','dist','sample_count'])
df_fin=df.tail(6)
df_fin.plot(y=["dist"],kind='line')



