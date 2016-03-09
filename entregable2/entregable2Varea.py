from algoritmia.schemes.divideandconquer import IDivideAndConquerProblem
from algoritmia.schemes.divideandconquer import DivideAndConquerSolver
import sys
 
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
  
  
class Skyline(IDivideAndConquerProblem): 
    def __init__(self, edificios: "Lista de edificios"): 
        self.edificios = edificios 
    
    def is_simple(self) -> "El lenght de la lista de edificios es uno o menos devuelve true": 
        return len(self.edificios) <= 1
    
    def trivial_solution(self) -> "Solucion basica (un edificio)":  
        return [self.edificios[0][0],self.edificios[0][1],self.edificios[0][2] + self.edificios[0][0]]
  
    def divide(self) -> "Iterable<MergesortProblem>": 
        yield Skyline(self.edificios[:len(self.edificios)//2]) 
        yield Skyline(self.edificios[len(self.edificios)//2:]) 
        
    def combine(self, s: "Iterable<sorted IList<T>>") -> "sorted IList<T>":
        skyline = []
        sky1, sky2 = tuple(s)
        currentHight1, currentHight2 = 0, 0 
        currentX1, currentX2 = 0, 0
        i, j = 0, 0
        while i < len(sky1)  and j < len(sky2):
            if sky1[i] < sky2[j]:
                currentX1 = sky1[i]
                if i < len(sky1) - 1:
                    currentHight1 = sky1[i+1]
                else:
                    currentHight1 = 0
                maxH = currentHight1
                if currentHight2 > maxH:
                    maxH = currentHight2
                #hacer algo con las alturas repetidas (no introducirlas)
                alturaAnterior = skyline[-1:]
                # se puede reducir este trozo y sacar fuera del while =====================
                if len(alturaAnterior) == 1:
                    if maxH != alturaAnterior[0]:
                        skyline.append(currentX1);
                        skyline.append(maxH);
                else:
                    skyline.append(currentX1);
                    skyline.append(maxH);
                i+=2        
            elif sky1[i] > sky2[j]:
                currentX2 = sky2[j]
                
                if j < len(sky2) - 1 :
                    currentHight2 = sky2[j+1]
                else:
                    currentHight2 = 0
                    
                maxH = currentHight2
                if currentHight1 > maxH:
                    maxH = currentHight1
                #hacer algo con las alturas repetidas (no introducirlas)
                alturaAnterior = skyline[-1:]
                if len(alturaAnterior) == 1:
                    if maxH != alturaAnterior[0]:
                        skyline.append(currentX2);
                        skyline.append(maxH);
                else:
                    skyline.append(currentX2);
                    skyline.append(maxH);
                j+=2                
            else:
                currentX1 = sky1[i]
                #miro si es el ultimo elemento de sky1 y asigno altura a 0
                if i < len(sky1) - 1:
                    currentHight1 = sky1[i+1]
                else:
                    currentHight1 = 0
                #miro si es el ultimo elemento de sky2 y asigno altura a 0
                currentX2 = sky2[j]
                if j < len(sky2) - 1 :
                    currentHight2 = sky2[j+1]
                else:
                    currentHight2 = 0
                # comparo maximo
                maxH = currentHight1
                if currentHight2 > maxH:
                    maxH = currentHight2
                alturaAnterior = skyline[-1:]
                if len(alturaAnterior) == 1:
                    if maxH != alturaAnterior[0]:
                        skyline.append(currentX1);
                        skyline.append(maxH);
                else:
                    skyline.append(currentX1);
                    skyline.append(maxH);              
                i+=2
                j+=2
        #salimos del while    
        if i >= len(sky1):
            skyline = skyline + sky2[j:]
        else:
            skyline = skyline + sky1[i:]
            
        return skyline

buildings = readFile(sys.argv[1])
resultadoSkyline = DivideAndConquerSolver().solve(Skyline(buildings)) 
impSkyline = ""
for imp in resultadoSkyline:
    impSkyline += "{}".format(imp)
    impSkyline += " "     
print(impSkyline.rstrip())
