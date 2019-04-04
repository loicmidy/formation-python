# -*- coding: utf-8 -*-
import seaborn as sns 
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.decomposition import PCA
from scipy.cluster.hierarchy import dendrogram, linkage,fcluster
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans

# 1 : CHARGEMENT ET SCALING DATA
iris = sns.load_dataset("iris")
X=iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].values
Y=iris['species'].values

X_scaled = preprocessing.scale(X)

# 2 : ACP
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(X_scaled)
principalDf = pd.DataFrame(data = principalComponents, columns = ['axe1ACP','axe2ACP'])
finalDf = pd.concat([principalDf, iris['species']], axis = 1)

sns.relplot(x="axe1ACP", y="axe2ACP", hue="species", style="species",data=finalDf)

#part de variance expliquée par chaque axe
print(pca.explained_variance_ratio_)


# 3 : CAH
Z = linkage(X_scaled, 'ward')

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

mesClusters=pd.Series(fcluster(Z, 3, criterion='maxclust'),name="numero_cluster_CAH")
finalDf2 = pd.concat([iris,principalDf, mesClusters], axis = 1)

effectifsParCluster=finalDf2.groupby('numero_cluster_CAH')['numero_cluster_CAH'].count()

sns.relplot(x="axe1ACP", y="axe2ACP", hue="numero_cluster_CAH", style="numero_cluster_CAH",data=finalDf2)



# 4 : k means
kmeans = KMeans(n_clusters=3)
kmeans.fit_predict(X_scaled) 
resultatsKmeans=pd.DataFrame(kmeans.labels_,columns=['numero_cluster_kmeans'])
effectifsParClusterKmean2=resultatsKmeans.groupby('numero_cluster_kmeans')['numero_cluster_kmeans'].count()

finalDf3 = pd.concat([finalDf2,resultatsKmeans], axis = 1)
sns.relplot(x="axe1ACP", y="axe2ACP", hue="numero_cluster_kmeans", style="numero_cluster_kmeans",data=finalDf3)


