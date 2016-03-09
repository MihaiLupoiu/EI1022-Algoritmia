from algoritmia.utils import infinity
import sys


def Kfactorizacion(inicial,final,K):
    
    dic={}
    back={}
    def S(n,k):
        if (n,k) in dic:
            return dic[(n,k)]
        if k==0 and n==1:
            b= (0,None)
        else:
            if k==0 and n!=1:
                b = (infinity,None)
            else:
                b =min((( S(( n // j), k-1) + j), ((n//j, k-1), j)) for j in divisores if n % j==0)
        dic[(n,k)],back[(n,k)]=b
        return dic[(n,k)]
    
    for i in range(inicial,final+1):
        divisores=[1]
        for j in range (2,i//2+1):
            if i%j==0:
                divisores.append(j)
        divisores.append(i)
        
        S(i,K)
        pos=(i,K)
        desglose=[]
        while back[pos]!=None:
            pos,d=back[pos]
            desglose.append(d)
        desglose.append(i)
        desglose.reverse()
        
        impResultado = ""
        for imp in desglose:
            impResultado += "{}".format(imp)
            impResultado += " "
        print(impResultado.rstrip())

inicio=int(sys.argv[1])
fin=int(sys.argv[2])
K=int(sys.argv[3])
Kfactorizacion(inicio, fin, K)

