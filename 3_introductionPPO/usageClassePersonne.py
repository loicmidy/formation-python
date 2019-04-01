# -*- coding: utf-8 -*-

import personne as per

loicM=per.Personne("loïc","Midy")
print (loicM.getIdentite())

guilhemD=per.Personne.creerPersonne("guilhem|deschamp")
print (guilhemD.getIdentite())