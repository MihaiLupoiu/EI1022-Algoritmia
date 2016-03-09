


def solve(v,w,W):

    x=[0]*len(w) #vector de resultados
    for i in range(len(w)):
        x[i]=min(1,W/w[i])
        W-=x[i]*w[i]
    return x



def solve2(v,w,W) :
    n = len(v)
    sorting_permutation = list(reversed(sorted(range(n), key =lambda i: v[i]/w[i])))
#     sorting_permutation = list(sorted(range(n), key =lambda i: -v[i]/w[i]))
    x = [0] * len(w)
    for i in sorting_permutation:
        x[i] = min(1, W /w[i])
        W -= x[i] *w[i]
        
    return x
    
def benefit(sol,v):
    beneficio=0
    for i in range(len(v)):
        beneficio+=sol[i]*v[i]
    return beneficio



v,w,W=[60,30,40,20,75],[40,30,20,10,50],50
sol=solve(v,w,W)
print(sol,benefit(sol,v))
sol2=solve2(v,w,W)
print(sol2,benefit(sol2,v))