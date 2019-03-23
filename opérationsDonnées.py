# -*- coding: utf-8 -*-

#opérations nombres
b=2**3/33#division exacte
print(b)

b=2**3//3#partie entière
print(b)

#opérations chaines de caractères
phrase="123456789"
print(phrase[2:])#on enlève les 2 premiers caractères
print(phrase[:6])#on va jusqu'au 6e caractères (donc on enlève les suivants)

plusieursMotsSeparésParPipe="voici|plusieurs|mots"
print(plusieursMotsSeparésParPipe.split("|"))

plusieursMotsConcaténés="voici "+"plusieurs "+"mots"
print(plusieursMotsConcaténés)

#re est le module pour traiter les expressions régulières
import re
resultat=re.sub("^M ","", "M MIDYM ")#remplacer M espace lorsque c'est en début de mot par rien (donc supprimer 'M ')
print(resultat)

#opérations dates
import datetime as dt
import time as t
a=dt.datetime.now()
t.sleep(2)
durée=dt.datetime.now()-a
print(durée.seconds)