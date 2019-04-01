# -*- coding: utf-8 -*-
def concatenationSpeciale(texte1,texte2):
    """documentation textuelle de la fonction"""
    return texte1+" - "+texte2

def factorielle(n):
    if n==1 :return 1
    else: return n*factorielle(n-1)