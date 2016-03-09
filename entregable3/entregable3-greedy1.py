from algoritmia.datastructures.digraphs import UndirectedGraph, WeightingFunction
from math import sqrt
from algoritmia.problems.spanningtrees.interfaces import IMinimumSpanningForestFinder,IMinimumSpanningTreeFinder
from algoritmia.utils import argmin
from algoritmia.datastructures.prioritymaps.heapmap import MinHeapMap

#PRIM-------------
class PrimsMinimumSpanningFinder(IMinimumSpanningTreeFinder, IMinimumSpanningForestFinder):
    def __init__(self, createSet: "Iterable<T> -> ISet<T>"=lambda V: set(), 
                       createMap: "Iterable<T> -> IMap<T, R>"=lambda V: dict()):
        self.createSet = createSet
        self.createMap = createMap

    def minimum_spanning_tree(self, G: "undirected IDigraph<T>", 
            d: "T, T -> R", u: "T") -> "Iterable<(T, T)>":
        added = self.createSet(G.V)
        return self._mst(G, d, u, added)
    
    def _mst(self, G: "undirected IDigraph<T>", 
             d: "T, T -> R", u: "T", added: "set<T>"=None) -> "Iterable<(T, T)>": #[p1
        added.add(u)
        in_frontier_from = self.createMap(G.V)
        for v in sorted(G.succs(u)): in_frontier_from[v] = u
        while len(in_frontier_from) > 0:
            (v, u) = argmin(in_frontier_from.items(), d)
            del in_frontier_from[v]
            added.add(v)
            yield (u, v)
            for w in sorted(G.succs(v)):
                if w not in added and \
                       (w not in in_frontier_from or d(v, w) < d(in_frontier_from[w], w)):
                    in_frontier_from[w] = v #]p1
                    
    def minimum_spanning_forest(self, G: "undirected IDigraph<T>", 
            d: "T, T -> R") -> "Iterable<(T, T)>":
        added = self.createSet(G.V)
        for u in G.V:
            if u not in added:
                for v in self._mst(G, d, u, added):
                    yield v

#------------Prim
#Lectura fichero, creacion de diccionario con aristas y distancias, crecion de vertices creacion de aristas 
def read_file(fichero):
    diccionario={}
    aristas=[]
    vertices=[]
    index = 0
    
    for line in open(fichero,encoding="utf-8"):
        tupla=line.split(" ")
        if len(tupla) == 1:
             vertices = [0]*int(tupla[0])
        else:
            vertices[index] = (float(tupla[0]),float(tupla[1]))
            index+=1
    for i in range(len(vertices)):
        for j in range(i+1,len(vertices)):
            diccionario[(i,j)]=distancia(vertices[i],vertices[j]);
            aristas.append((i,j));
            aristas.append((j,i));
    return diccionario,aristas,vertices
#----Fin lectura
#Calculo distncias------
def distancia(punto1,punto2):
    return round(sqrt(((punto1[0]-punto2[0])*(punto1[0]-punto2[0]))+((punto1[1]-punto2[1])*(punto1[1]-punto2[1]))),3)
#----- Calculo distancia  
    
    
    

diccionario,aristas,vertices=read_file("pruebas-greedy/p00.vjt")

d = WeightingFunction(diccionario, symmetrical=True)
G = UndirectedGraph(E=d.keys())
# Obtencion de recorrido
MST = list(PrimsMinimumSpanningFinder().minimum_spanning_forest(G, d))
#---- Fin Obtencion recorrido
#Arreglo para mostrar por pantalla


lista=[]
for i in MST:
    lista.append(aristas.index(i))

impResultado = ""
for imp in lista:
    impResultado += "{}".format(imp)
    impResultado += " "
print(impResultado.rstrip())


# con este print mostraria el recorrido y el peso
#print('Recorrido: {} \n con peso {}.'.format(impResultado.rstrip(), round(sum (d(u,v) for (u,v) in MST),2)))
#----FIN


