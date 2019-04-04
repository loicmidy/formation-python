# -*- coding: utf-8 -*-
import seaborn as sns 
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.cluster import AgglomerativeClustering
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram

def plot_dendrogram(model, **kwargs):

    # Children of hierarchical clustering
    children = model.children_

    # Distances between each pair of children
    # Since we don't have this information, we can use a uniform one for plotting
    distance = np.arange(children.shape[0])

    # The number of observations contained in each cluster level
    no_of_observations = np.arange(2, children.shape[0]+2)

    # Create linkage matrix and then plot the dendrogram
    linkage_matrix = np.column_stack([children, distance, no_of_observations]).astype(float)

    # Plot the corresponding dendrogram
    dendrogram(linkage_matrix, **kwargs)





iris = sns.load_dataset("iris")
X=iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].values

X_scaled = preprocessing.scale(X)

cluster = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='ward')  
cluster.fit_predict(X_scaled) 

print(cluster.labels_)  
df=pd.DataFrame(cluster.labels_,columns=['numero_cluster'])
effectifsParCluster2=df.groupby('numero_cluster')['numero_cluster'].count()

finalDf3 = pd.concat([iris, df], axis = 1)


# ATTENTION CE DENDOGRAMME SEMBLE FAUX ! 
plt.title('Hierarchical Clustering Dendrogram')
plot_dendrogram(cluster, labels=cluster.labels_)
plt.show()







