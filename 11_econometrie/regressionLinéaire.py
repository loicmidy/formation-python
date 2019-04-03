# -*- coding: utf-8 -*-
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import seaborn as sns 
import pandas as pd

baseball=pd.read_sas("C:/Users/lmidy/Documents/GitHub/dataFormationPython/baseball.sas7bdat");
"""
The salaries (Sports Illustrated, April 20, 1987) are for the 1987 season and 
the performance measures are from 1986 (Collier Books, The 1987 Baseball Encyclopedia Update).

BUT : prédire les salaires : Salary ou logSalary
nRBI = A run batted in (RBI), plural runs batted in (RBI or RBIs), is a statistic in baseball and softball that credits a batter for making a play that allows a run to be scored (except in certain situations such as when an error is made on the play)
nBB = walk
YrMajor = Years in the Major Leagues
CrHits = Career Hits
"""

print(baseball.info())

# STATISTIQUES DESCRIPTIVES
# 1 : analyse descriptive de la variable Salaire seule
serieSalaire=baseball['Salary']
print(serieSalaire.describe())#moyenne (535.9) supérieur à médiane (425) donc skew positive
print(serieSalaire.skew())#queue de distribution étalée vers la droite.
print(serieSalaire.kurtosis())

serieSalaireSansValeurManquante=serieSalaire.dropna()
serieSalaireSansValeurManquante.plot(kind='hist',bins=25,color="blue")
serieSalaireSansValeurManquante.plot(kind='box',color="red")
sns.distplot(serieSalaireSansValeurManquante,bins=25)

#passage au log pour traiter le cas des salaires très élevés
serielogSalaire=baseball['logSalary']
print(serielogSalaire.describe())
print(serielogSalaire.skew())
print(serielogSalaire.kurtosis())

serielogSalaireSansValeurManquante=serielogSalaire.dropna()
serielogSalaireSansValeurManquante.plot(kind='hist',bins=25,color="blue")
serielogSalaireSansValeurManquante.plot(kind='box',color="red")
sns.distplot(serielogSalaireSansValeurManquante,bins=25)

#examen de toutes les variables par groupe de deux
baseballvariablesClésSansSalaireManquant=baseball[['logSalary','nHits','nRuns','nRBI','nBB','YrMajor','CrHits']]
baseballvariablesClésSansSalaireManquant.dropna(subset=['logSalary'],inplace=True) 
sns.pairplot(baseballvariablesClésSansSalaireManquant)


# 2 : REGRESSION LINEAIRE (OLS : ordinary least square = MCO moindres carrés ordinaires)
# 2.1 : modèle
modèleOLS = smf.ols('logSalary ~ nHits+nRuns+nRBI+nBB+YrMajor+CrHits', data=baseball).fit()
print(modèleOLS.summary())

model_fitted_y = modèleOLS.fittedvalues # model values
model_residuals = modèleOLS.resid # model residuals

# 2.2 : graphiques de diagnostic
sns.regplot(model_fitted_y,serielogSalaireSansValeurManquante)

# hypothèse 1 : linéarité => pour la vérifier graphique avec Y chapô en abscisse et résidus en ordonnée
# il ne doit pas y avoir de relation entre ces 2 variables si le modèle est OK
#le graphique permet également de détecter l'hétéroscédasticité
sns.residplot(model_fitted_y, model_residuals,lowess=True,scatter_kws={'alpha': 0.5},line_kws={'color': 'red', 'lw': 1, 'alpha': 0.8})
sns.regplot(model_fitted_y, model_residuals)

#hypothèse 2 :
#normal probability plot  is a special case of the Q–Q probability plot for a normal distribution
#en abscisse les quantiles d'une loi normale (0,var = var estimée des résidus) et en ordonnée quantiles des résidus
sm.qqplot(model_residuals,line='r')

#autre façon de faire : vérifier que les résidus suivent une loi normale
sns.distplot(model_residuals)

# 2.3 : détection outliers
sm.graphics.influence_plot(modèleOLS)
print(baseball.iloc[236])

influence = modèleOLS.get_influence()
influenceDataframe = influence.summary_frame()
influenceDataframe.reset_index(inplace = True) 
sns.scatterplot(x="index", y="cooks_d", data=influenceDataframe)
print(influenceDataframe[influenceDataframe['cooks_d']>0.1]['index'])
print(baseball.iloc[282])


# 2.4 : partial régression plot : NE MARCHE PAS BIEN
sm.graphics.plot_partregress_grid(modèleOLS)
baseballvariablesClésSansSalaireManquant['résidus']=model_residuals
sm.graphics.plot_partregress("logSalary", "YrMajor", ["nHits","nRuns","nRBI","nBB","CrHits"], data=baseballvariablesClésSansSalaireManquant)

baseball['YrMajorCarre']=baseball['YrMajor']*baseball['YrMajor']
baseball['CrHitsCarre']=baseball['CrHits']*baseball['CrHits']
modèleOLS = smf.ols('logSalary ~ nHits+nRuns+nRBI+nBB+YrMajor+YrMajorCarre+CrHits+CrHitsCarre', data=baseball).fit()
print(modèleOLS.summary())


