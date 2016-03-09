gimport sys

from algoritmia.schemes.divideandconquer import DivideAndConquerSolver, \
    IDivideAndConquerProblem
#from skylineviewer import SkylineViewer


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

#===============================================================================
# def grafic(skyline, buildings):
#     viewer = SkylineViewer(resultadoSkyline)
#     for b in buildings:
#         viewer.add_building(b)
#     viewer.run()
#===============================================================================

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
                    if maxH == alturaAnterior[0]:
                        #print("i < j parte altura repetida {} {}".format(currentHight1, maxH,0,1))
                        pass
                    else:
                        skyline.append(currentX1);
                        skyline.append(maxH);
                else:
                    skyline.append(currentX1);
                    skyline.append(maxH);
                
                # se puede reducir este trozo =====================
                #y añadir fuera de las comprobaciones
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
                    if maxH == alturaAnterior[0]:
                        #print("i > j parte altura repetida {} {}".format(currentHight2, maxH, 0, 1))
                        pass
                    else:
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
                
                # ===================== prueba ======================
                alturaAnterior = skyline[-1:]
                # se puede reducir este trozo y sacar fuera del while =====================
                if len(alturaAnterior) == 1:
                    if maxH == alturaAnterior[0]:
                        #print("i < j parte altura repetida {} {}".format(currentHight1, maxH,0,1))
                        pass
                    else:
                        skyline.append(currentX1);
                        skyline.append(maxH);
                else:
                    skyline.append(currentX1);
                    skyline.append(maxH);
                
                # ===================== prueba ======================
                
                #skyline.append(currentX1)
                #skyline.append(maxH)
                
                i+=2
                j+=2
            
        if i >= len(sky1):
            skyline = skyline + sky2[j:]
        else:
            skyline = skyline + sky1[i:]
            
        return skyline

# ================================== Pruebas =====================================  
#===============================================================================
# fichero = "ciudad_5_33"
# buildings=readFile("pruebas/"+fichero+".i")
# skylineFichero =readFileResult("pruebas/"+fichero+".o")
# print("Edificios: ")
# print(buildings)
# print("Resuldatos buenos: ")
# print(skylineFichero)
# print(len(skylineFichero))
#===============================================================================

# ============ Prueba Puntual ===============
#buildings=[(81,7,7),(68,16,13)]

#===============================================================================
# problemSkyline = Skyline(buildings)
# resultadoSkyline = DivideAndConquerSolver().solve(problem=problemSkyline)
# print("Final: ")
# print(resultadoSkyline)
# print(len(resultadoSkyline))
# #grafic(resultadoSkyline, buildings)
# print(skylineFichero == resultadoSkyline)
#===============================================================================

# ================================== FINAL =====================================

buildings = readFile(sys.argv[1])
problemSkyline = Skyline(buildings)
resultadoSkyline = DivideAndConquerSolver().solve(problem=problemSkyline)
 
impSkyline = ""
for imp in resultadoSkyline:
    impSkyline += "{}".format(imp)
    impSkyline += " "
     
print(impSkyline.rstrip())


