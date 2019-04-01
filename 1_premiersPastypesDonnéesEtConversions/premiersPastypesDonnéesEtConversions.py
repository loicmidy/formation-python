# -*- coding: utf-8 -*-

#hello word
print ("hello word")

#types de données
a=2
print(a,type(a))

a=2.0
print(a,type(a))

a="texte"
print(a,type(a))

a=2+3j
print(a,type(a))

a=True
print(a,type(a))

import datetime as dt
a = dt.datetime.now()
print(a.day,a.month,a.year)
print(a,type(a))

#conversions (synonymes : transtypage/cast en Anglais) types de données
a=str(2.0)
print(a,type(a))


a=int(2.9)
print(a,type(a))# la conversion flottant vers entier prend la partie entière et pas l'arrondi le plus proche


a= int("2")
print(a,type(a))

a=  float("2.5")
print(a,type(a))

#date => string
a = dt.datetime.now()
b=a.strftime("%H:%M:%S")
print(b,type(b))

#string=>date
b=dt.datetime.strptime('02081977','%d%m%Y')
print(b,type(b))

#The people who made the datetime module also named their class datetime:
#module  class    method
#datetime.datetime.strptime(date, "%Y-%m-%d")
