'''
Created on 13/11/2013

@author: al204332
'''
def solve1(valores:"vector de valores", pesos:"vector de pesos", capacidad:"entero capacidad maxima mochila"):    
    sorting_permutation = list(reversed(sorted(range(len(valores)), key = lambda i: valores[i]/pesos[i])))
       
    resultado = [0]*len(pesos)
    for i in sorting_permutation:
        resultado[i] = min(1,capacidad/pesos[i])
        capacidad -= resultado[i]*pesos[i]
    return resultado    
        
def benefit(sol:"solucion del solve1", valor:"vector de valores"):    
    valor_total = 0;
    for i in range(len(sol)):
        valor_total += valor[i]*sol[i]
    return valor_total

v, w, W = [60,30,40,20,75], [40,30,20,10,50], 50 # 

sol = solve1(v, w, W)    

#print(sol)

print(sol, benefit(sol, v))
