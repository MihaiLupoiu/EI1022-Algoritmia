'''
Created on 13/11/2013

@author: al204332
'''
def solve1(valores, pesos, capacidad):    
    resultado = [0]*len(pesos)
    for i in range(len(pesos)):
        resultado[i] = min(1,capacidad/pesos[i])
        capacidad -= resultado[i]*pesos[i]
    return resultado    
        
#===============================================================================
# def benefit(sol, v):    
#     pass
#===============================================================================

v, w, W = [60,30,40,20,75], [40,30,20,10,50], 50 

sol    =    solve1(v, w, W)    

#print(sol, benefit(sol,    v))

print(sol)