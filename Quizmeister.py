import requests as req
import json
import random as rand


def Anzahl():
    try:
        Anzahl=int(input("Wie viele Fragen:")) 
        if Anzahl!=int:
            raise ValueError
        else:
            print(Anzahl,"ist eine gute Wahl")
    except ValueError:
        print("Gib mir eine Anzahl")
    
Anzahl()
