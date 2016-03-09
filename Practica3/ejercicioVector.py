'''
Created on 30/10/2013

@author: al204332
'''


def funcion(a:"vector",i:"pos inicial",j:"pos fin"):
    
    medio = (i+j)//2
    
    #print("a = ", a[medio])
    #print("Medio = ", medio)
    
    if(a[medio] == medio):
        #print("fin = ", a[medio])
        return medio
    
    elif(a[medio] > medio ):
        #print("descarto la parte derecha")
        return funcion(a, i, medio)
    
    else:
        #print("descarto la parte izquierda")
        return funcion(a, medio+1, j)
        

    
a = [-10,-5,1,3,6]

resultado = funcion(a, 0, len(a))

print(resultado)