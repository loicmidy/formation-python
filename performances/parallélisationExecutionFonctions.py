# -*- coding: utf-8 -*-
import datetime as dt
import time as t

def inc(x):
    t.sleep(2)
    return x + 1

def add(x, y):
    t.sleep(1)
    return x + y


a=dt.datetime.now()

x = inc(1)#2s
y = inc(2)#2s
z = add(x, y)#1s
durée=dt.datetime.now()-a
print("calcul lent de z qui vaut",z," en ",durée.seconds," s")
#comme les 3 lignes sont exécutées séquentiellement la durée totale est 2+2+1=5s




from dask import delayed

a=dt.datetime.now()

#préparation du plan d'exécution
x = delayed(inc)(1)
y = delayed(inc)(2)
z = delayed(add)(x, y)
#exécution
res=z.compute()


durée=dt.datetime.now()-a
print("calcul rapide de z qui vaut ",res," en ",durée.seconds," s")
#les 2 premières lignes sont exécutées en parallèle soit une durée totale de 2s puis la 3e ligne est exécutée en 1s
#la durée totale est de 3s

z.visualize()
