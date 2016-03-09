


def redFile (fileName):
    vector = []
    for line in open(fileName,encoding="utf-8"):
        edificio=[]
        cadena=line.split("\n")
        cadena=cadena[0].split(" ")
        
        for i in cadena:
            edificio.append(int(i))
            
        tupla=tuple(edificio)
        vector.append(tupla)
    return vector

def redFileResult (fileName):
    for line in open(fileName,encoding="utf-8"):
        edificio=[]
        cadena=line.split("\n")
        cadena=cadena[0].split(" ")
        
        for i in cadena:
            edificio.append(int(i))
            
        
    return edificio





def is_simple(s):
    return len(s)<=1

def trivial_solution(s):
    lista=[]
    lista.append(s[0][0])
    lista.append(s[0][1])
    lista.append(s[0][0]+s[0][2])
    return lista

def divide(s):
    return (s[:len(s)//2], s[len(s)//2:])

def combina(izquierda,derecha):
    lista=[]
    i=0
    j=0
    h1=0
    h2=0
    posxizquierda=0
    posxderecha=0
    #print("izquierda={}".format(izquierda))
    #print("derecha={}".format(derecha))
    while((i<len(izquierda)) and (j<len(derecha))):
        posxizquierda=izquierda[i]
        posxderecha=derecha[j]
        #print("posxderecha={}".format(posxderecha))
        #print("posxizquierda={}".format(posxizquierda))
        if posxizquierda<posxderecha:
            if i<len(izquierda)-1:
                h1=izquierda[i+1]
        else:
            if posxizquierda>posxderecha:
                if j<len(derecha)-1:
                    h2=derecha[j+1]
            else:
                if i<len(izquierda)-1:
                    h1=izquierda[i+1]
                if j<len(derecha)-1:
                    h2=derecha[j+1]
            
        #print("h1={}".format(h1))
        #print("h2={}".format(h2))           
        if h1>h2:
            lista.append(izquierda[i])
            if i<len(izquierda)-1:
                
                lista.append(h1)
                
                        
        
                if j<len(derecha)-1:
                   
                    if derecha[j]==izquierda[i]:
                            j=j+2
                    else:
                        if derecha[j+2]==izquierda[i+2]:
                            j=j+2
            i=i+2
        else:        
            if h1<h2 :
                
                lista.append(derecha[j])
                if j<len(derecha)-1:
                    
                    lista.append(h2) 
                            

                    if i<len(izquierda)-1:
                        
                        if izquierda[i]==derecha[j]:
                            i=i+2
                        else:                        
                            if izquierda[i+2]==derecha[j+2]:
                                i=i+2

                j=j+2
            else: 
               
                        
                  
                if h1 ==0 and h2==0:
                    if posxderecha<posxizquierda:
                        lista.append(posxderecha)
                        lista.append(0)
                        j=j+2
                        
                    else:
                        lista.append(posxizquierda)
                        lista.append(0)
                        i=i+2
                else:
                    if h1==0 or h2==0:
                        if posxderecha<posxizquierda:
                            lista.append(posxderecha)
                            j=j+2
                        else:
                            lista.append(posxizquierda)
                            i=i+2
                                
                    else:
                        if posxderecha<posxizquierda:
                            lista.append(posxizquierda)
                            i=i+2
                        else:
                            lista.append(posxderecha)
                            j=j+2
                    
            
        #print(lista) 
    t=i
    u=j
    while(t<len(izquierda)):
        
        if izquierda[t]>lista[len(lista)-1]:
            if t==0:
                lista.append(0)
                lista.append(izquierda[t]) 
            else:
                lista.append(izquierda[t-1])
                lista.append(izquierda[t])
        t=t+2
    
    while(u<len(derecha)):
        
        if derecha[u]>lista[len(lista)-1]:
            if u==0:
                lista.append(0)
                lista.append(derecha[u])
            else:
                lista.append(derecha[u-1])
                lista.append(derecha[u])
        u=u+2
       
        
    
       
    return lista

def definecontorno(s:"list()edificio"):
    lista=[]
    if is_simple(s): 
        return trivial_solution(s)
    else: 
        lista=divide(s)
        return combina(definecontorno(lista[0]), definecontorno(lista[1]))      




buildings=redFile("pruebas/ciudad_10000_0.i")
skyline =redFileResult("pruebas/ciudad_10000_0.o")

print(buildings)
print("profesor={},{}".format(skyline,len(skyline)))
print("mio     ={},{}".format(definecontorno(buildings),len(definecontorno(buildings))))


