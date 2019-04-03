# -*- coding: utf-8 -*-
import numpy as np
import seaborn as sns 
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import logit
#hack pour faire marcher le code car sinon AttributeError: module 'scipy.stats' has no attribute 'chisqprob'
stats.chisqprob = lambda chisq, df: stats.chi2.sf(chisq, df)


# 1 : import et conversions
adultèreFeminin = sm.datasets.fair.load_pandas().data
print( sm.datasets.fair.NOTE)
print(adultèreFeminin.info())
print(adultèreFeminin.describe(include='all')) 
adultèreFeminin['rate_marriage']=adultèreFeminin['rate_marriage'].astype(str)
adultèreFeminin['religious']=adultèreFeminin['religious'].astype(str)
adultèreFeminin['educ']=adultèreFeminin['educ'].astype(str)
adultèreFeminin['occupation']=adultèreFeminin['occupation'].astype(str)
adultèreFeminin['occupation_husb']=adultèreFeminin['occupation_husb'].astype(str)
adultèreFeminin['affair'] = (adultèreFeminin['affairs'] > 0).astype(int)
adultèreFeminin.drop(['affairs'], axis=1,inplace=True)

"""
Variable name definitions:

        rate_marriage   : How rate marriage, 1 = very poor, 2 = poor, 3 = fair,
                        4 = good, 5 = very good
        age             : Age
        yrs_married     : No. years married. Interval approximations. See
                        original paper for detailed explanation.
        children        : No. children
        religious       : How relgious, 1 = not, 2 = mildly, 3 = fairly,
                        4 = strongly
        educ            : Level of education, 9 = grade school, 12 = high
                        school, 14 = some college, 16 = college graduate,
                        17 = some graduate school, 20 = advanced degree
        occupation      : 1 = student, 2 = farming, agriculture; semi-skilled,
                        or unskilled worker; 3 = white-colloar; 4 = teacher
                        counselor social worker, nurse; artist, writers;
                        technician, skilled worker, 5 = managerial,
                        administrative, business, 6 = professional with
                        advanced degree
        occupation_husb : Husband's occupation. Same as occupation.
        affairs         : measure of time spent in extramarital affairs
"""

# 2 : statistiques descriptives
sns.catplot(x="religious", y="affair", kind="bar", data=adultèreFeminin)
sns.catplot(x="rate_marriage", y="affair", kind="bar", data=adultèreFeminin)
sns.catplot(x="children", y="affair", kind="bar", data=adultèreFeminin)
sns.catplot(x="educ", y="affair", kind="bar", data=adultèreFeminin)
sns.catplot(x="occupation", y="affair", kind="bar", data=adultèreFeminin)
sns.catplot(x="occupation_husb", y="affair", kind="bar", data=adultèreFeminin)
sns.catplot(x="age", y="affair", kind="bar", data=adultèreFeminin)
sns.catplot(x="yrs_married", y="affair", kind="bar", data=adultèreFeminin)


# 3 : MODELE
modeleLogitAdultere=logit("affair ~  C(rate_marriage) + age + yrs_married + C(religious)", adultèreFeminin).fit()
print(modeleLogitAdultere.summary())

#calcul des odds ratio
parametres = modeleLogitAdultere.params
parametres.name='paramètres'
oddRatios=np.exp(parametres)
oddRatios.name='odd ratios'
intervallesConfiance=modeleLogitAdultere.conf_int()
ensemble=pd.concat([parametres,intervallesConfiance,oddRatios],axis=1)

#calcul des effets marginaux
margeff = modeleLogitAdultere.get_margeff()
print(margeff.summary())

#Akaike information criterion
print(modeleLogitAdultere.aic)

#prédiction
respondent1000 = adultèreFeminin.iloc[[1000]]
modeleLogitAdultere.predict(respondent1000)
modeleLogitAdultere.predict(x2)
 
