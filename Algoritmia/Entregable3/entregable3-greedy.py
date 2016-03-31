from algoritmia.datastructures.digraphs import UndirectedGraph, WeightingFunction
from math import sqrt
from algoritmia.problems.spanningtrees import PrimsMinimumSpanningFinder
from algoritmia.problems.traversals.interfaces import IDigraphDepthFirstTraverser
from algoritmia.datastructures.queues.fifo import Fifo
from algoritmia.datastructures.queues.lifo import Lifo
from itertools import dropwhile
import sys


class DepthFirstTraverser(IDigraphDepthFirstTraverser): #[iterative
    def __init__(self, createLifo=lambda V: Lifo(),
                       createSet=lambda V: set()):
        self.createLifo = createLifo
        self.createSet = createSet
        
    def traverse(self, G: "IDigraph<T>", u: "T", preorder_visitor: "T, T -> S"=None,
                 postorder_visitor: "T, T -> S"=None):
        if preorder_visitor == postorder_visitor == None:
            preorder_visitor = lambda u, v: v
        visited = self.createSet(G.V)
        stack = self.createLifo(G.V)
        return self._traverse(G, u, preorder_visitor, postorder_visitor, visited, stack)
    
    def _traverse(self, G: "IDigraph<T>", u: "T", preorder_visitor: "T, T -> S", 
                  postorder_visitor: "T, T -> S",
                  visited: "ISet<T>", stack: "ILifo<T>"):
        visited.add(u)
        stack.push(((u, u), (v for v in sorted(G.succs(u)))))
        if preorder_visitor != None:
            yield preorder_visitor(u, u)
        while len(stack) > 0:
            ((u, v), succs) = stack.pop()
            succs = dropwhile(lambda w: w in visited, succs)
            w = next(succs, None)
            if w != None:
                stack.push(((u, v), succs))
                stack.push(((v, w), (x for x in sorted(G.succs(w)))))
                visited.add(w)
                if preorder_visitor != None:
                    yield preorder_visitor(v, w)
            else:
                if postorder_visitor != None:
                    yield postorder_visitor(u, v)

    def full_traverse(self, G: "IDigraph<T>", 
                  preorder_visitor: "T, T -> S"=None, 
                  postorder_visitor: "T, T -> S"=None):
        if preorder_visitor == postorder_visitor == None:
            preorder_visitor = lambda u, v: v
        visited = self.createSet(G.V)
        stack = self.createLifo(G.V)
        for v in G.V:
            if v not in visited:
                for w in self._traverse(G, v, preorder_visitor, postorder_visitor, visited, stack): 
                    yield w  #]iterative



#Lectura fichero, creacion de diccionario con aristas y distancias, crecion de vertices creacion de aristas 
def readFile(fichero):
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
            distan=distancia(vertices[i],vertices[j])
            diccionario[(i,j)]=distan
            diccionario[(j,i)]=distan
            
    return diccionario,vertices

def distancia(punto1,punto2):
    return sqrt(((punto1[0]-punto2[0])*(punto1[0]-punto2[0]))+((punto1[1]-punto2[1])*(punto1[1]-punto2[1])))
 
def mejorSolucion(grafoPrim):
    j=0
    for inici in grafoPrim.V:
        distan=0
        solucio=list(DepthFirstTraverser().traverse(grafoPrim, inici))
        if (j==0):
            mejorDistancia=0
            for i in range(len(solucio)-1):
                mejorDistancia+=diccionario[(solucio[i],solucio[i+1])]
            mejorDistancia+=diccionario[(solucio[len(solucio)-1],solucio[0])]
            solucion=solucio
        
        else:
            for i in range(len(solucio)-1):
                distan+=diccionario[(solucio[i],solucio[i+1])]
            distan+=diccionario[(solucio[len(solucio)-1],solucio[0])]
            if distan<mejorDistancia:
                mejorDistancia=distan
                solucion=solucio
        j+=1
    return solucion
    

#diccionario,vertices=readFile("pruebas-greedy/p00.vjt")

diccionario,vertices=readFile(sys.argv[1])

d = WeightingFunction(diccionario)
G = UndirectedGraph(E=d.keys())
MST = list(PrimsMinimumSpanningFinder().minimum_spanning_forest(G, d))
grafoPrim=UndirectedGraph(E=MST)
solucion=mejorSolucion(grafoPrim)   
 

impResultado = ""
for imp in solucion:
    impResultado += "{}".format(imp)
    impResultado += " "
print(impResultado.rstrip()) 
