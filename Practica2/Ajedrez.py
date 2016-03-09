from algoritmia.datastructures.digraphs import UndirectedGraph



def horse_graph(rows:"filas", cols:"columnas"):
    aristas= [] 
   
    for f in range(rows):
        for c in range(cols):
           
            for v in vecinos(f,c,rows,cols):
               aristas.append(((f,c),v))
    return UndirectedGraph(E=aristas)           

def vecinos(f,c,row,cols):
    posibles=[(f+1,c+2),(f+1,c-2),(f+2,c-1),(f+2,c+1),(f-1,c-2),(f-1,c+2),(f-2,c-1),(f-2,c+1)]#posibles casillas vecinas
    
    for (i,j) in posibles:     
        if (0 <= i < row and 0<= j < cols):
           yield (i,j)


def mitraverse(grafo, vertice):
    visitados=set()
    queue=[]
    visitados.add(vertice)
    queue.append(vertice)
    yield vertice
    while(len(queue)>0):
        u=queue.pop()
        for v in grafo.succs(u):
            if v not in visitados:
                queue.insert(0,v)
                visitados.add(v)
                yield v
                
def matriz(grafo,vertice):   
    visitados=set()
    queue=[]
    visitados.add(vertice)
    queue.append((vertice,0))
    movimiento=0
    yield (vertice,movimiento)
    while(len(queue)>0):
        u=queue.pop()
        for v in grafo.succs(u[0]):
            movimiento=u[1]+1
            if v not in visitados: 
                queue.insert(0,(v,movimiento))                                 
                visitados.add(v)
                yield(v,movimiento)
        
        
    
        
 #PRuebas          

print(list(mitraverse(horse_graph(8, 8),(0,3))))
print(len(list(mitraverse(horse_graph(8, 8),(0,3)))))#Recorre todo el tablero

print(len(list(mitraverse(horse_graph(2, 100),(0,0))))) #no recorre todo el tablero

print(len(list(mitraverse(horse_graph(3, 100),(0,0))))) #recorre todo el tablero

print(list(mitraverse(horse_graph(8, 8),(0,0))))

print(list(matriz(horse_graph(8, 8),(0,0))))#matriz con movimientos
