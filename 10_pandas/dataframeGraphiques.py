# -*- coding: utf-8 -*-
import pandas as pd
import seaborn as sns 

#1 : INTRODUCTION QUARTET D'ASCOMBE avec seaborn
anscombe = sns.load_dataset("anscombe")
anscombe.groupby("dataset").mean()
anscombe.groupby("dataset").std()
anscombe.groupby("dataset").corr()


sns.lmplot("x", "y", data=anscombe[anscombe['dataset']=='I'])
sns.lmplot("x", "y", data=anscombe[anscombe['dataset']=='II'])
sns.lmplot("x", "y", data=anscombe[anscombe['dataset']=='III'])
sns.lmplot("x", "y", data=anscombe[anscombe['dataset']=='IV'])


# 2 : GRAPHIQUES BASIQUES AVEC PLOT
tips = sns.load_dataset("tips")

tips.plot(y=["tip","size"],kind='line',subplots=True)

pourboireMoyenEtnbFumeurparSexe=tips.groupby('sex').agg({'smoker': lambda row: row.value_counts()['Yes'],'tip': lambda row: sum(row) / len(row)})
print(pourboireMoyenEtnbFumeurparSexe)
pourboireMoyenEtnbFumeurparSexe.plot(kind='bar')


#analyse variable tip
tips.plot(y="tip",kind='hist', bins=50,color="blue")
tips.plot(y="tip",kind='box',color="blue")
boxplot = tips.boxplot(column=['tip'],by='sex')

#analyse variable tip pourcentage de bill
tips['tip_pct']=tips['tip']/tips['total_bill']*100
tips.plot(y="tip_pct",kind='hist', bins=50,color="blue")
tips['tip_pct'].plot.density()
#on utilise une fonction de seaborn pour afficher conjointement les deux graphiques
sns.distplot(tips['tip_pct'],bins=50)

#recherche de variables corrélées à tip
tips.plot(x="size",y="tip",kind='scatter')
tips.plot(x="total_bill",y="tip",kind='scatter')
sns.relplot(x="total_bill", y="tip", hue="smoker", style="smoker",data=tips);
sns.relplot(x="total_bill", y="tip", hue="smoker",col="time", data=tips);
sns.relplot(x="total_bill", y="tip", size="size", data=tips);

#matrice de nuages de points => très utile avant économétrie
iris = sns.load_dataset("iris")
sns.pairplot(iris)
sns.pairplot(iris, hue="species")



titanic = sns.load_dataset("titanic")
survieParClasseEtSexe=titanic.groupby(['sex','pclass',]).agg({'survived': lambda row: row.value_counts()[1]})
print(survieParClasseEtSexe)
effectifsParClasseEtSexe=titanic.groupby(['sex','pclass',])['sex'].count()
print(effectifsParClasseEtSexe)
sns.catplot(x="sex", y="survived", hue="class", kind="bar", data=titanic)

