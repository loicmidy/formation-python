# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 14:41:05 2019
on met ici le commentaire de niveau commentaires.py
@author: lmidy
"""


class Personne:
    def __init__(self,nom,prenom):
        """documentation du constructeur d'objets Personne"""
        self.nom=nom
        self.prenom=prenom
    
    
    def getIdentite(self):
        """documentation de la méthode getIdentite"""
        return self.nom,self.prenom