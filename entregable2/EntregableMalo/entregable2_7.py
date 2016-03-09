'''
Created on 11/11/2013

@author: admin
'''
'''
Created on 09/11/2013

@author: admin
'''
from algoritmia.schemes.divideandconquer import IDivideAndConquerProblem
from algoritmia.schemes.divideandconquer import DivideAndConquerSolver
import sys



# from test.test_iterlen import len
  
  
#===============================================================================
# class DivideAndConquerSolver: 
#     def solve(self, problem: "IDivideAndConquerProblem") -> "Solution": 
#         if problem.is_simple(): 
#             return problem.trivial_solution() 
#         else: 
#             return problem.combine(self.solve(p) for p in problem.divide())  
#   
#   
#===============================================================================

  
def readFile (fileName): 
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
  
def readFileResult (fileName): 
    for line in open(fileName,encoding="utf-8"): 
        edificio=[] 
        cadena=line.split("\n") 
        cadena=cadena[0].split(" ") 
          
        for i in cadena: 
            edificio.append(int(i)) 
              
    return edificio 
  
class Skyline(IDivideAndConquerProblem): 
    def __init__(self, edificios: "Lista de edificios"): 
        self.edificios = edificios 
          
    def is_simple(self) -> "El lenght de la lista de edificios es uno o menos devuelve true": 
        return len(self.edificios) <= 1
  
    def trivial_solution(self) -> "Solucion basica (un edificio)": 
        skyline = [] 
          
        start = self.edificios[0][0] 
        hight = self.edificios[0][1] 
        final = self.edificios[0][2] + start 
        skyline.append(start) 
        skyline.append(hight) 
        skyline.append(final) 
  
        return skyline 
  
    def divide(self) -> "Iterable<MergesortProblem>": 
        yield Skyline(self.edificios[:len(self.edificios)//2]) 
        yield Skyline(self.edificios[len(self.edificios)//2:]) 
        
    
    #def combine(self, s: "Iterable<sorted IList<T>>") -> "sorted IList<T>":
     #   return 1
        #=======================================================================
        # skyline = []
        # sky1,sky2 = tuple(s)
        # print("combine",sky1)
        # print("combine",sky2)
        # i,j = 0,0
        # print ("i",i)
        # print("j",j)    
        # 
        # skyline.append(min(sky1[0],sky2[0]))
        # 
        # print ("skyline",skyline)
        # 
        #=======================================================================
       
    def combine(self, s: "Iterable<sorted IList<T>>") -> "sorted IList<T>":
        
        lista=[]
        izquierda,derecha = tuple(s)
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

        
            
#buildings=[(1,10,3),(2,5,5), (3,6,3), (4,7,5), (10,10,3),(9,4,6), (20,8,4),(22, 6, 6),(25,10,2)] 
  
# fichero = "c"
#buildings=readFile("pruebas/"+fichero+".i") 
#skyline =readFileResult("pruebas/"+fichero+".o") 
#print("Edificios: ") 
#print(buildings) 
#print("Resuldatos buenos: ") 
#print(skyline) 
  
buildings = readFile(sys.argv[1])
#buildings = readFile("pruebas/ciudad_5_1.i")



resultadoSkyline = DivideAndConquerSolver().solve(Skyline(buildings)) 
var=""
for elem  in range(len(resultadoSkyline)-1):
    var += str(resultadoSkyline[elem]) + " "
var+=str(resultadoSkyline[len(resultadoSkyline)-1])
print (var)
   # print(resultadoSkyline[elem],end =" ")
