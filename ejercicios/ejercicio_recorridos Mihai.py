#encoding:utf-8
'''
Created on 05/10/2012

@author: David

IMPORTANTE. LEER CON ATENCIÓN:
  -Este ejercicio es básico e imprescindible. Si tras pelearte con él las HORAS que 
   consideres necesarias no consigues resolverlo, debes asistir a tutorías.
   
  -Para obtener el resultado esperado debes visitar los sucesores de cada vértice
   de forma ordenada (de menor a mayor valor: los vértices son enteros).
'''

from algoritmia.datastructures.digraphs import UndirectedGraph
from queue import Queue

#-------------------------------------------------------------------------------

def mostrar_recorrido_anchura(g, inicial):
    print("mostrar_recorrido_anchura:", end=" ")
    #Código aquí
    cola = Queue();
    visitados = set();
    
    cola.put(inicial);
    visitados.add(inicial);
    print(inicial, end=" ");
    
    while (cola.qsize() > 0 ):
        u = cola.get();
        vecinos = g.succs(u);
        for v in vecinos:
            if (v not in visitados):
                print(v, end=" ");
                cola.put(v);
                visitados.add(v);
    print();
#-------------------------------------------------------------------------------
               
def devolver_recorrido_anchura(g, inicial):
    res=[];
    cola = Queue();
    visitados = set();
    cola.put(inicial); # añado a la cola
    visitados.add(inicial); # añado a visitados
    res.append(inicial) # añado a resultados
    while (cola.qsize() > 0): 
        u = cola.get(); #saco el elemento
        vecinos = g.succs(u); # saco vecinos
        for v in vecinos: 
            if (v not in visitados): # compruebo si se ha visitado ya y si no lo añado
                cola.put(v);
                visitados.add(v);
                res.append(v);
    return res
    
#-------------------------------------------------------------------------------

def mostrar_recorrido_profundidad_preorden(g, inicial):
    print("mostrar_recorrido_profundidad_preorden:", end=" ")
    visitados = set()
    _rec_mostrar_recorrido_profundidad_preorden(g, inicial, visitados)
    print()
    
def _rec_mostrar_recorrido_profundidad_preorden(g, u, visitados):
    #Código aquí
    visitados.add(u);
    print(u, end= " ")
    for v in list(g.preds(u)):
        if (v not in visitados):
            _rec_mostrar_recorrido_profundidad_preorden(g, v, visitados)
    
      
#-------------------------------------------------------------------------------

def devolver_recorrido_profundidad_preorden(g, inicial):
    visitados = set()
    resultado = []
    _rec_devolver_recorrido_profundidad_preorden(g, inicial, visitados, resultado)
    return resultado

def _rec_devolver_recorrido_profundidad_preorden(g, u, visitados, resultado):
    #Código aquí
    resultado.append(u);
    visitados.add(u);
    print(u, end= " ")
    for v in list(g.preds(u)):
        if (v not in visitados):
            _rec_devolver_recorrido_profundidad_preorden(g, v, visitados, resultado);
    
    
#-------------------------------------------------------------------------------

def mostrar_recorrido_profundidad_postorden(g, inicial):
    print("mostrar_recorrido_profundidad_postorden:", end=" ")
    visitados = set()
    _rec_mostrar_recorrido_profundidad_postorden(g, inicial, visitados)
    print()
    
def _rec_mostrar_recorrido_profundidad_postorden(g, u, visitados):
    #Código aquí
    visitados.add(u);
    for v in g.succs(u):
        if (v not in visitados):
            _rec_mostrar_recorrido_profundidad_postorden(g, v, visitados);
    print(u, end=" ");
      
#-------------------------------------------------------------------------------

def devolver_recorrido_profundidad_postorden(g, inicial):
    visitados = set()
    resultado = []
    _rec_devolver_recorrido_profundidad_postorden(g, inicial, visitados, resultado)
    return resultado

def _rec_devolver_recorrido_profundidad_postorden(g, u, visitados, resultado):
    #Código aquí
    visitados.add(u);
    for v in g.succs(u):
        if (v not in visitados):
            _rec_devolver_recorrido_profundidad_postorden(g, v, visitados, resultado)
    resultado.append(u);
    
#-------------------------------------------------------------------------------

#programa principal

e = [(2,1),(2,5),(2,6),(1,5),(1,6),(1,3),(3,7),(3,4),(4,7)]
g = UndirectedGraph(E=e)

print("RESULTADOS ESPERADOS:")
print("""mostrar_recorrido_anchura: 2 1 5 6 3 4 7 
devolver_recorrido_anchura: [2, 1, 5, 6, 3, 4, 7]
mostrar_recorrido_profundidad_preorden: 2 1 3 4 7 5 6 
devolver_recorrido_profundidad_preorden: [2, 1, 3, 4, 7, 5, 6]
mostrar_recorrido_profundidad_postorden: 7 4 3 5 6 1 2 
devolver_recorrido_profundidad_postorden: [7, 4, 3, 5, 6, 1, 2]
""")

print("RESULTADOS OBTENIDOS:")             
mostrar_recorrido_anchura(g, 2)
print("devolver_recorrido_anchura:",devolver_recorrido_anchura(g,2))
mostrar_recorrido_profundidad_preorden(g, 2)
print("devolver_recorrido_profundidad_preorden:",devolver_recorrido_profundidad_preorden(g,2))
mostrar_recorrido_profundidad_postorden(g, 2)
print("devolver_recorrido_profundidad_postorden:",devolver_recorrido_profundidad_postorden(g,2))
