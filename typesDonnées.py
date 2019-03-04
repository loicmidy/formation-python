# -*- coding: utf-8 -*-

#hello word
print ("hello word")

#types de données
a=2
print(type(a))

a=2.0
print(type(a))

a="texte"
print(type(a))

a=2+3j
print(type(a))

a=True
print(type(a))

import datetime as dt
a = dt.datetime.now()
print(a.day,a.month,a.year)
print(type(a))

#conversions types de données
print(type( str(2.0) ))

print(type( int("2") ))

print(type( float("2.5") ))

#date => string
a = dt.datetime.now()
b=a.strftime("%H:%M:%S")
print(b)
print(type(b))

#string=>date
b=dt.datetime.strptime('02081977','%d%m%Y')
print(b)
print(type(b))

#The people who made the datetime module also named their class datetime:
#module  class    method
#datetime.datetime.strptime(date, "%Y-%m-%d")
