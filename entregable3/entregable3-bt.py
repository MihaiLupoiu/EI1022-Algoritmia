from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.schemes.backtracking import BacktrackingEnumerator
from algoritmia.statespace import IForwardStateSpace
from math import sqrt
import sys


class HamiltonianCycleStateSpace(IForwardStateSpace):#[space
    def __init__(self, G):
        self.G = G
        
    def initial_states(self):
        yield (next(iter(self.G.V)),)
        
    def is_final(self, s):
        return len(s) == len(self.G.V) and (s[-1], s[0]) in self.G.E

    def decide(self, s, v):
        return s + (v,)
    
    def decisions(self, s):
        if len(s) < len(self.G.V):
            for v in self.G.succs(s[-1]):
                if v not in s:
                    yield v #]space

class HamiltonianCycleSolver:#[solver
    def __init__(self):
        self.enumerator = BacktrackingEnumerator(createSolution
                                                 =lambda space, i, d, f: f + (f[0],))
    
    def solve(self, G):
        space = HamiltonianCycleStateSpace(G)
        return self.enumerator.enumerate(space) #]solver
    def find(self,S):
        sol=HamiltonianCycleSolver().solve(S)
        return sol
    
def read_file(fichero):
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
        for j in range(i,len(vertices)):
            aristas.append((vertices[i],vertices[j]));
    aristas.append((vertices[len(vertices)-1],vertices[0]));
    return aristas,vertices

#devuelve la solucion con menor distancia
def mejorresultado(solunciones):
    solucion=next(soluciones)
    distanciamin=calculadistancia(solucion)
    
    for t in soluciones:
       distancia=calculadistancia(t)
       if distancia < distanciamin:
           solucion=t
           distanciamin=distancia
    return solucion
        
#distancia total recorrida
def calculadistancia (solucion):
    i=0
    j=1
    distancia=0
    while(j<len(solucion)):
        distancia+=sqrt(((solucion[i][0]-solucion[j][0])*(solucion[i][0]-solucion[j][0]))+((solucion[i][1]-solucion[j][1])*(solucion[i][1]-solucion[j][1])))
        i+=1
        j+=1
    return distancia

aristas,vertices = read_file("pruebas-bt/p00.vjt")

#aristas,vertices = read_file(sys.argv[1])
grafo=UndirectedGraph(E=aristas)
soluciones=HamiltonianCycleSolver().find(grafo)
solucion=mejorresultado(soluciones)

lista=[]
contador = 0
for i in solucion:
    if contador != len(solucion) - 1:
        lista.append(vertices.index(i))
    else:
        break
    contador+=1

#print(lista)

impResultado = ""
for imp in lista:
    impResultado += "{}".format(imp)
    impResultado += " "
print(impResultado.rstrip())









