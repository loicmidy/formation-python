# -*- coding: utf-8 -*-

class Personne:
    def __init__(self,nom,prenom):
        self.nom=nom
        self.prenom=prenom
    
    #une fonction liée à la classe Personne (self en paramètre)
    def getIdentite(self):
        return self.nom,self.prenom

    #une fonction non liée à la classe
    def creerPersonne(chaine):
        nom,prenom=chaine.split("|")
        return Personne(nom,prenom)