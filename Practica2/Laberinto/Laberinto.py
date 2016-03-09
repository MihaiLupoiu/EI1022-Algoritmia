'''
Created on 16/10/2013

@author: al204332
'''
from random import shuffle
import algoritmia.datastructures.mergefindsets
from algoritmia.datastructures.mergefindsets.mergefindset import MergeFindSet
from algoritmia.datastructures.digraphs import UndirectedGraph
from labyrinthviewer import *


numFilas = 5
numColumnas = 10 

v = [(i,j) for i in range (numFilas) for j in range(numColumnas)]

w = []

for (i,j) in v:
    if i < numFilas - 1:
        w.append(((i,j),(i+1,j)))
    if j < numColumnas - 1:
        w.append(((i,j),(i,j+1)))
shuffle(w)

#===============================================================================
# print(w)
# print(len(w))
#===============================================================================

e = []

mfset = MergeFindSet()

for vertice in v:
    mfset.add(vertice)

for pares in w:
    if(mfset.find(pares[0]) != mfset.find(pares[1])):
        mfset.merge(pares[0], pares[1])
        e.append(pares)
        
#===============================================================================
# print(len(e))
# print(e)
#===============================================================================

grafo = UndirectedGraph(E=e)
print(grafo)

lv = LabyrinthViewer(grafo, cell_size=100,margin=50,show_io=True)

lv.run()