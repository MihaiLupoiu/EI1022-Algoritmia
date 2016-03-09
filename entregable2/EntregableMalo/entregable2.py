'''
Created on 04/11/2013

@author: Myhay
'''
import sys
import re

def redFile (fileName):
    vector = []
    for line in open(fileName,encoding="utf-8"):
        edificio=[]
        cadena=line.split("\n")
        cadena=cadena[0].split(" ")
        
        for i in cadena:
            edificio.append(int(i))
            
        tupla=tuple(edificio)
        vector.append(tupla)
    return vector

#buildings = redFile(sys.argv[1])

buildings = [(1, 10, 3), (2, 5, 5), (3, 6, 3), (4, 7, 5), (10, 10, 3), (9, 4, 6), (20, 8, 4), (22, 6, 6), (25, 10, 2)]

def tamanyoListaResultante(edificios:"lista de edificios", inicio:"inicio de la lista", fin:"fin de la lista"):
    maximo = 0
    medio = (inicio+fin)//2
    
    if((fin - inicio) == 1):
        startPosition = edificios[inicio][0]  
        length = edificios[inicio][2]
        
        maximo = startPosition+length
        return maximo
    
    elif ((fin - inicio) == 2):
        edificio1 = edificios[inicio]
        edificio1Length = edificio1[0] + edificio1[2]
        
        edificio2 = edificios[fin-1]
        edificio2Length = edificio2[0] + edificio2[2]
        
        if(edificio1Length >=  edificio2Length):
            return edificio1Length
        else:
            return edificio2Length
        
    else:
        maximo1 = tamanyoListaResultante(edificios, inicio, medio)
        maximo2 = tamanyoListaResultante(edificios, medio, fin)
        
        if(maximo1 >= maximo2):
            return maximo1
        else:
            return maximo2
        
print(tamanyoListaResultante(buildings,0 , len(buildings)))
    