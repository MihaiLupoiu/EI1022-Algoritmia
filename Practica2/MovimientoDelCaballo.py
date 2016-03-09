'''
Created on 02/10/2013

@author: al204332
'''

from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.problems.traversals.breadthfirst import BreadthFirstTraverser

def vecinos(f, c, numFilas, numColumnas):
    resultado = [] 
    for (i, j) in [(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2)]:
        operacion = (f+i, c+j)
        if  (numFilas > operacion[0] >= 0 and numColumnas > operacion[1] >= 0 ):
            resultado.append(operacion)          
    return resultado
        
def horse_graph(rows,cols):
    e=[] #aristas
    
    for f in range(rows):
        for c in range(cols):
            #f,c = vertice
            for v in vecinos(f,c,rows,cols):
                e.append(((f,c),v))
             
    return UndirectedGraph(E=e)

def miTraverseMatriz(g, inicial): 
    res=[]
    salto = 0
    queue = []
    visited = set()
    
    queue.append((inicial,salto)) # aÃ±ado a la cola 
    visited.add(inicial) # aÃ±ado a visitados 
    res.append((inicial, salto))
    
    while (len(queue) > 0):  
        u = queue.pop() #saco el elemento
        vecinos = g.succs(u[0]) # saco vecinos 
        for v in vecinos:
            salto=u[1]+1 # vale 0 porque siempre se saca de lo que habia almacenado en la cola 
            print(salto)
            if (v not in visited): # compruebo si se ha visitado ya y si no lo aÃ±ado
                queue.append((v,salto)) 
                visited.add(v) 
                res.append((v,salto))
    return res 

def devolverValoresRecorrido(grafo, inicio):
    return list(BreadthFirstTraverser().traverse(grafo, inicio))

grafoDelTablero = horse_graph(8, 8)
#print(grafoDelTablero)

#Que casillas podemos alcanzar en 0 o mas movimientos en un tablero de 8x8 si el caballo parte de la posicion (0, 3)
recorrido = devolverValoresRecorrido(grafoDelTablero, (0,3))

# Puede un caballo alcanzar cualquier casilla del tablero de 8x8 desde cualquier otra 
print(len(recorrido)) #Si porque llega a todos los elementos. mismo tamanyo que el grafo

# Partiendo de la posicion (0,0), puede alcanzar cualquier posicion en un tablero de 2x100 

grafoDelTablero = horse_graph(2, 100)
print("Tamanyo de grafo: " + str(len(grafoDelTablero.V)))

dosPOR100 = devolverValoresRecorrido(grafoDelTablero, (0,0))
print("Numero de elementos recorridos: " + str(len(dosPOR100)))

#y en uno de 3x100

grafoDelTablero = horse_graph(3, 100)
print("Tamanyo de grafo: " + str(len(grafoDelTablero.V)))

tresPOR100 = devolverValoresRecorrido(grafoDelTablero, (0,0))
print("Numero de elementos recorridos: " + str(len(tresPOR100)))

print("Matriz de 8x8")
grafoDelTablero = horse_graph(8, 8)
print(miTraverseMatriz(grafoDelTablero, (0,0)))
# 5 2 3 2
# 2 1 4 3
# 3 6 1 2
# 0 3 2 5
