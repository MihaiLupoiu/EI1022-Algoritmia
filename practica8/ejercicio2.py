'''
Created on 04/12/2013

@author: al204332
'''

from random import randrange, seed
seed(0)

def recursos(U, m, v):
    
    def P(n,u):
        if n == 0:
            return 0;
        else:
            return max(P(n-1, u-k) + v[(n-1,k)] for k in range( min(m[n-1], u)) )     
    
    return P(len(m),U)

U = 12 
m = [2,4,2,4,2] 
v = dict( ((i,u), randrange(100)) for i in range(len(m)) for u in range(0,U+1))

print(v)

print(recursos(U, m, v))
