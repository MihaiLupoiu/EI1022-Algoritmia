'''
Created on 04/12/2013

@author: al204332
'''

def mochila (v, w, W):
    def B(n,c):
        if n == 0:
            return 0
        elif w[n-1] <= c:
            return max(B(n-1,c), B(n-1,c-w[n-1]) + v[n-1])
        else:
            return B(n-1,c)
    return B(len(v),W)


W = 6 
v = [90,75,60,20,10] 
w = [4,3,3,2,2]

#print(mochila(v,w,W) )

Beneficio = 135 
Objetos = [0,1,1,0,0]


# version vevolviendo lista de objetos por hacer
def mochilaLista (v, w, W):
    def B2(n,c):
        lista = []
        if n == 0:
            return (0,lista + [0])
        elif w[n-1] <= c:
            b1 = B2(n-1,c)
            b2 = B2(n-1,c-w[n-1]) + v[n-1] 
            maximo = max(b1[0], b2[0])
            if b1 == maximo:
                return (b1[0],lista+[0])
            else:
                return (b2[0], lista+[1])
        else:
            return (B2(n-1,c),lista + [0])
    return B2(len(v),W)

W = 6 
v = [90,75,60,20,10] 
w = [4,3,3,2,2]

#print(mochilaLista(v, w, W) )

#=================================================================================

#version completa varea 

#===============================================================================
# def mochilaConMem (v, w, W):
#     diccionario = {}
#     def B(n,c):
#         if (n,c) in diccionario:
#             return diccionario[(n,c)]
#         else:
#             if n == 0:
#                 diccionario[(n,c)] = 0
#                 return 0
#             elif w[n-1] <= c:
#                 b = max(B(n-1,c), B(n-1,c-w[n-1]) + v[n-1])
#                 diccionario[(n,c)] = b
#                 return b
#             else:
#                 b = B(n-1,c)
#                 diccionario[(n,c)] = b
#                 return b
#     return B(len(v),W)
#===============================================================================

# version reducida

def mochilaConMem (v, w, W):
    diccionario = {}
    def B(n,c):
        if (n,c) in diccionario:
            return diccionario[(n,c)]
        else:
            if n == 0:
                b = 0
            elif w[n-1] <= c:
                b = max(B(n-1,c), B(n-1,c-w[n-1]) + v[n-1])
            else:
                b = B(n-1,c)
            diccionario[(n,c)] = b
            return b
    return B(len(v),W)

W = 6 
v = [90,75,60,20,10] 
w = [4,3,3,2,2]

#print( mochilaConMem(v,w,W) )

# version iterativa
#===============================================================================

def mochilaConMemIter (v, w, W):
    dic = {}
    for c in range(W + 1): 
        dic[(0,c)] = 0
        
    for n in range(1, len(v) + 1):
        for c in range(W + 1):
            if(w[n-1] <= c):
                dic[(n,c)] = max(dic[(n-1,c)], dic[ (n-1,c-w[n-1]) ] + v[n-1])
            else:
                dic[(n,c)] = dic[(n-1,c)]
                
    return dic[(len(v),W)]

W = 6 
v = [90,75,60,20,10] 
w = [4,3,3,2,2]

print( mochilaConMemIter(v,w,W) )

#===============================================================================
