# -*- coding: utf-8 -*-
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

