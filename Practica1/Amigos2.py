'''
Created on 30/09/2013

@author: admin
'''
from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.problems.connectedcomponents import GraphTraversalConnectedComponentsFinder

def leeFichero(fichero):
    lista = []
    for line in open(fichero,encoding="utf-8"):
        tupla = line.split("#")
        tupla[1] = tupla[1].replace("\n","")
        lista.append(tupla)
    return (lista)

def creaGrafo(lista):
    vertices = set()
    for tupla in lista:
        vertices.add(tupla[0])
        vertices.add(tupla[1])
    grafo = UndirectedGraph(vertices,lista)   
    
    return(grafo) 

def componentesConexos (grafo): 
    a = GraphTraversalConnectedComponentsFinder()
    return a.connected_components(grafo)   

def muestraGrupos (grupo):
    for i in grupo:
        print(i)
aristas = leeFichero("amigos.txt")
grafo = creaGrafo(aristas)
grupos = componentesConexos(grafo)
muestraGrupos(grupos)




    
        

