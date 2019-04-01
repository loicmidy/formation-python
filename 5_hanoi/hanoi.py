# -*- coding: utf-8 -*-

def hanoi(depart,arrivee,intermediaire,nombreDisques):
    if nombreDisques==1: print(depart,"=>",arrivee)
    else:
       hanoi(depart,intermediaire,arrivee,nombreDisques-1) 
       print(depart,"=>",arrivee)
       hanoi(intermediaire,arrivee,depart,nombreDisques-1) 
    

hanoi("A","C","B",3)