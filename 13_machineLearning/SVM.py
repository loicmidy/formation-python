# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage,fcluster
import numpy as np
import seaborn as sns 
from sklearn import preprocessing
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics
from sklearn.model_selection import KFold,cross_val_score

# chargement des données et leur normalisation
iris = sns.load_dataset("iris")

#X=iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].values
X=iris[['sepal_length', 'sepal_width']].values
y=iris['species'].values

X_scaled = preprocessing.scale(X)

# On découpe notre échantillon en 2 : celui d'entrainement et celui de validation
X_train, X_validation, y_train, y_validation = train_test_split(X_scaled, y, test_size=0.33, random_state=3)

# étape 1 : mise au point du modèle sur échantillon d'entrainement
clf = svm.SVC(kernel='linear', C = 0.1)
clf.fit(X_train,y_train)

y_train_prediction=clf.predict(X_train)
print("Accuracy: ",metrics.accuracy_score(y_train, y_train_prediction))

#scores = cross_val_score(clf,X_train,y_train, cv=KFold(n_splits=3, shuffle=True), scoring='accuracy')
#print("f1_macro: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))


# étape 2 : validation du modèle sur échantillon de validation pas utilisé dans entrainement 
# notamment pour vérifier qu'il n'y a pas over fitting
y_validation_prediction=clf.predict(X_validation)
print("Accuracy: ",metrics.accuracy_score(y_validation, y_validation_prediction))

# étape 3 : faire tourner le modèle sur les autres données (i.e celles pour lesquelles on n'a pas la valeur de Y)