# -*- coding: utf-8 -*-
from sklearn import preprocessing
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import KFold,cross_val_score

# chargement des données et leur normalisation
url = ('https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wdbc.data')
names = ['id_number', 'diagnosis', 'radius_mean',
         'texture_mean', 'perimeter_mean', 'area_mean',
         'smoothness_mean', 'compactness_mean',
         'concavity_mean','concave_points_mean',
         'symmetry_mean', 'fractal_dimension_mean',
         'radius_se', 'texture_se', 'perimeter_se',
         'area_se', 'smoothness_se', 'compactness_se',
         'concavity_se', 'concave_points_se',
         'symmetry_se', 'fractal_dimension_se',
         'radius_worst', 'texture_worst',
         'perimeter_worst', 'area_worst',
         'smoothness_worst', 'compactness_worst',
         'concavity_worst', 'concave_points_worst',
         'symmetry_worst', 'fractal_dimension_worst']


cancersPoumons = pd.read_csv(url, names=names)
# Setting 'id_number' as our index
cancersPoumons.set_index(['id_number'], inplace = True)
# Converted to binary to help later on with models and plots
cancersPoumons['diagnosis'] = cancersPoumons['diagnosis'].map({'M':1, 'B':0})

X=cancersPoumons.iloc[:,2:].values
y=cancersPoumons['diagnosis'].values

X_scaled = preprocessing.scale(X)

# On découpe notre échantillon en 2 : celui d'entrainement et celui de validation
X_train, X_validation, y_train, y_validation = train_test_split(X_scaled, y, test_size=0.33, random_state=30)

# étape 1 : mise au point du modèle sur échantillon d'entrainement
clf = RandomForestClassifier(random_state=42,n_estimators=100,oob_score = True)
clf.fit(X_train,y_train)

# k fold validation sur échantillon entrainement
scores = cross_val_score(clf,X_train,y_train, cv=KFold(n_splits=3, shuffle=True), scoring='f1_macro')
print("f1_macro: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))


# étape 2 : validation du modèle sur échantillon de validation pas utilisé dans entrainement 
# notamment pour vérifier qu'il n'y a pas over fitting
y_validation_prediction=clf.predict(X_validation)
print("f1_macro: ",metrics.f1_score(y_validation, y_validation_prediction))

resultats_validation = pd.concat([pd.Series(y_validation,name='y_validation'),pd.Series(y_validation_prediction,name='y_validation_prediction')],axis=1)
# Create confusion matrix
cm_resultats_validation=pd.crosstab(resultats_validation['y_validation'], resultats_validation['y_validation_prediction'], rownames=['y_validation'], colnames=['y_validation_prediction'])
print("cm_resultats_validation ")
print(cm_resultats_validation)

# étape 3 : faire tourner le modèle sur les autres données (i.e celles pour lesquelles on n'a pas la valeur de Y)

