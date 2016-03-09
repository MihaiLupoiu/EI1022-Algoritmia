from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.problems.shortestpaths.length import BreadthFirstShortestPaths
from algoritmia.problems.shortestpaths import Backtracer


#Norte=N,Sud=S,Este=E Oeste=W

def load_labirinth(fichero):
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
               
def movimientos(grafo,vertice):   
    tree = dict(BreadthFirstShortestPaths().one_to_all_backpointers(grafo,vertice))
    distancias={}
    
    for (i,j) in tree:
        
        distancias[(i,j)]=len(Backtracer(tree).backtrace((i,j)))
    return distancias #devuelve un diccionario
  
def sumamatrizes(diccionario1,diccionario2):    
    maximo=0
    mini=max(diccionario1)
    
    for i in (diccionario1):
        if maximo<diccionario2[i]+diccionario1[i]:
            maximo=diccionario2[i]+diccionario1[i]
            mini=i
            
        else:
            if maximo == diccionario2[i]+diccionario1[i]: 
                mini=min(i,mini)                
    return mini
         
    
grafo= load_labirinth('laberinto-5x10.i')
caminoentrada=movimientos(grafo,min(grafo.V))
caminosalida=movimientos(grafo,max(grafo.V))
tesoro=sumamatrizes(caminoentrada,caminosalida)
print("{} {}".format(tesoro[0], tesoro[1])) 
print("{}".format(caminoentrada[tesoro])) 
print("{}".format(caminosalida[tesoro]))   
   
    

    

   
        
    


    