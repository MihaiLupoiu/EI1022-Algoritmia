from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.problems.shortestpaths.length import BreadthFirstShortestPaths
from algoritmia.problems.shortestpaths import Backtracer
#from labyrinthviewer import LabyrinthViewer
import sys

#Norte=N,Sud=S,Este=E Oeste=W

def load_labyrinth(fichero):
    aristas=[]
    posicion=(0,0)
    for line in open(fichero,encoding="utf-8"): 
        tupla=line.split(" ")
        for v in range(len(tupla)):
            if 'n' not in tupla[v]:
                aristas.append((posicion,(posicion[0]-1,posicion[1])))
            if 's' not in tupla[v]:
                aristas.append((posicion,(posicion[0]+1,posicion[1])))
            if 'e' not in tupla[v]:
                aristas.append((posicion,(posicion[0],posicion[1]+1)))
            if 'w' not in tupla[v]:
                aristas.append((posicion,(posicion[0],posicion[1]-1)))
            posicion=(posicion[0],posicion[1]+1)
        posicion=(posicion[0]+1,0)
    return UndirectedGraph(E=aristas) 
                 
#===============================================================================
# def mostrar_laberinto(grafo,tesoro):
# #     graph = UndirectedGraph(E=grafo.E)
#     
#     lv = LabyrinthViewer(grafo, cell_size=30, margin=10, show_io=True)
# 
#     dict1 = dict(BreadthFirstShortestPaths().one_to_all_backpointers(grafo, min(grafo.V)))
#     dict2 = dict(BreadthFirstShortestPaths().one_to_all_backpointers(grafo, max(grafo.V)))
#     
#     pos_treasure = (tesoro[0],tesoro[1])
#     p1 = Backtracer(dict1).backtrace(tesoro)
#     p2 = Backtracer(dict2).backtrace(tesoro)
#    # p1 = [(0, 0), (1, 0), (1, 1), (1, 2), (0, 2), (0, 3), (1, 3), (1, 4), (0, 4), (0, 5), (0, 6), (0, 7), (1, 7), (1, 8), (2, 8), (2, 7), (2, 6), (1, 6), (1, 5), (2, 5), (2, 4), (2, 3), (3, 3), (4, 3), (4, 2), (4, 1), (4, 0), (3, 0), (2, 0), (2, 1), (2, 2), (3, 2), (3, 1)]
#    # p2 = [(3, 1), (3, 2), (2, 2), (2, 1), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (4, 9)]
# 
#     lv.set_treasure_pos(pos_treasure)
#     lv.add_path(p1,'red', 0)
#     lv.add_path(p2,'green', 2)
#     
#     lv.run()
#     
#===============================================================================
def visitor (fnt,dst):
    return dst
    
def dictAnchura (grafo,inicial):   
    visitados=set()
    queue=[]
    visitados.add(inicial)
    queue.append((inicial,0))
    movimiento=0
    diccionario={}
    diccionario[(inicial)] =0
    
    while(len(queue)>0):
        u=queue.pop()
        for v in grafo.succs(u[0]):
            movimiento=u[1]+1
            if v not in visitados: 
                #queue.insert(0,(v,movimiento))   #FIFO          
                queue.append((v,movimiento))                
                visitados.add(v)
                a,b = visitor(u,v)
                diccionario[(a,b)] = movimiento
    return diccionario

grafo= load_labyrinth(sys.argv[1])
#grafo = load_labyrinth("pruebas/laberinto-5x10.i")


inicialEntrada = min(grafo.V)
inicialSalida = max(grafo.V)
M1 = (dictAnchura(grafo,inicialEntrada))
M2 = (dictAnchura(grafo,inicialSalida))

maximo = 0
posicionMin = inicialSalida
for i in M1:
    if maximo < M1[i] + M2[i]:
        maximo = M1[i] + M2[i]
        posicionMin= i 
    else:
        if  maximo == M1[i] + M2[i]:
            posicionMin = min(posicionMin,i)
            
print("{} {}".format(posicionMin[0], posicionMin[1])) 
print("{}".format(M1[posicionMin])) 
print("{}".format(M2[posicionMin]))                  