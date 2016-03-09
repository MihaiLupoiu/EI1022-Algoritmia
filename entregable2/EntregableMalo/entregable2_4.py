from abc import ABCMeta, abstractmethod
from test.test_iterlen import len

class IDivideAndConquerProblem(metaclass=ABCMeta): #[intro
    @abstractmethod
    def is_simple(self) -> "bool": pass
        
    @abstractmethod
    def trivial_solution(self) -> "Solution": pass

    @abstractmethod
    def divide(self) -> "Iterable<IDivideAndConquerProblem>": pass

    @abstractmethod
    def combine(self, solutions: "Iterable<Solution>") -> "Solution": pass

class DivideAndConquerSolver:
    def solve(self, problem: "IDivideAndConquerProblem") -> "Solution":
        if problem.is_simple():
            return problem.trivial_solution()
        else:
            return problem.combine(self.solve(p) for p in problem.divide()) #] intro


from msilib.schema import Billboard

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

class Skyline(IDivideAndConquerProblem):
    def __init__(self, bildings: "Lista de edificios"):
        self.bildings = bildings
        
    def is_simple(self) -> "El lenght de la lista de bildings es uno o menos devuelve true":
        return len(self.bildings) <= 1

    def trivial_solution(self) -> "Solucion basica (un edificio)":
        skyline = []
        
        start = self.bildings[0][0]
        hight = self.bildings[0][1]
        final = self.bildings[0][2]+start
        skyline.append(start)
        skyline.append(hight)
        skyline.append(final)
        
        return skyline

    def divide(self) -> "Iterable<MergesortProblem>":
        yield Skyline(self.bildings[:len(self.bildings)//2])
        yield Skyline(self.bildings[len(self.bildings)//2:])

    def combine(self, s: "Iterable<sorted IList<T>>") -> "sorted IList<T>":
        skyline = []
        sky1, sky2 = tuple(s)
        
        currentHight1, currentHight2 = 0, 0 
        
        i, j = 0, 0
        
        while i < len(sky1)  and j < len(sky2):
            
            if sky1[i] < sky2[j]:
                currentX = sky1[i]
                if i < len(sky1) - 1:
                    currentHight1 = sky1[i+1]
                else:
                    #print("altura = o cuando sky[i] = {}".format(sky1[i]),0)
                    currentHight1 = 0
                maxHight = currentHight1;
                if currentHight2 > maxHight:
                    #print("cambiado la altura maxima")
                    maxHight = currentHight2
                
                skyline.append(currentX)
                skyline.append(maxHight)
                    
                i += 2
            else:   
                currentX = sky2[j]
                if j < len(sky2) - 1 :
                    currentHight2 = sky2[j+1]
                else:
                    #print("altura = o cuando sky2[j] = {}".format(sky2[j]),0)
                    currentHight2 = 0
                    
                maxHight = currentHight2;
                if currentHight1 > maxHight:
                    maxHight = currentHight1
                
                skyline.append(currentX)
                skyline.append(maxHight)
                
                j += 2
           
            #===================================================================
            # print("Skyline 1: {}".format(sky1, 0))
            # print("i = " + str(i))
            # print("Pos1: {} _ CurrentHight1: {}".format(sky1[i - 1 ], currentHight1, 0, 1))
            #  
            # print("Skyline 2: {}".format(sky2, 0))
            # print("j = " + str(j))
            # print("Pos2: {} _ CurrentHight2: {}".format(sky2[j - 2],currentHight2, 0, 1))
            #===================================================================
            
            #eliminar los duplicados
            
            skyline_nuevo = []
            index = 0
            pos_h_anterior = (0,0)
            while index in range(len(skyline) +1) :
                #print("indice = " + str(index))
                if index == 2 or index > 3:
                    if pos_h_anterior[1] != skyline[index - 1]:      
                        pos_h_anterior = (skyline[index-2],skyline[index-1])
                        #print(pos_h_anterior)
                        skyline_nuevo.append(pos_h_anterior[0])
                        skyline_nuevo.append(pos_h_anterior[1])
                index += 2
                
            #print("Casi Final") 
            #print(skyline_nuevo) 
            #skyline_nuevo   
        
              
        while i < len(sky1): 
            #print("Restante A: {}".format(sky1[i],0) )
            #skyline.append(sky1[i]) 
            skyline_nuevo.append(sky1[i])
            #print(skyline_nuevo)
            i += 1;
        while j < len(sky2): 
            #print("Restante B: {}".format(sky2[j],0) )
            #skyline.append(sky2[j]) 
            skyline_nuevo.append(sky2[j])
            #print(skyline_nuevo)
            j += 1;
        
        print("Returned skyline = {}".format(skyline_nuevo,0))           
        
        return skyline_nuevo

     
#buildings=[(1,10,3),(2,5,5), (3,6,3), (4,7,5), (10,10,3),(9,4,6), (20,8,4),(22, 6, 6),(25,10,2)]

#fichero = "ciudad_20_19"
#buildings=redFile("pruebas/"+fichero+".i")
#skyline =redFileResult("pruebas/"+fichero+".o")
#print("Edificios: ")
#print(buildings)
#print("Resuldatos buenos: ")
#print(skyline)
#print(len(skyline))
#buildings=[(1,10,3),(2,5,5), (3,6,3), (4,7,5), (10,10,3),(9,4,6), (20,8,4),(22, 6, 6),(25,10,2)]
buildings=[(81,7,7),(68,16,13)]

problemSkyline = Skyline(buildings)
resultadoSkyline = DivideAndConquerSolver().solve(problem=problemSkyline)
#print("Final: ")
#print(resultadoSkyline)
#print(len(resultadoSkyline))