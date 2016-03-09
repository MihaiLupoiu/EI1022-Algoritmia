import sys
from algoritmia.schemes.divideandconquer import DivideAndConquerSolver, \
    IDivideAndConquerProblem
from skylineviewer import SkylineViewer

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

def grafic(skyline, buildings):
    viewer = SkylineViewer(resultadoSkyline)
    for b in buildings:
        viewer.add_building(b)
    viewer.run()

class Skyline(IDivideAndConquerProblem):
    def __init__(self, bildings: "Lista de edificios"):
        self.bildings = bildings
        
    def is_simple(self) -> "El lenght de la lista de bildings es uno o menos devuelve true":
        return len(self.bildings) <= 1

    def trivial_solution(self) -> "Solucion basica (un edificio)":
       return [self.bildings[0][0],self.bildings[0][1],self.bildings[0][2] + self.bildings[0][0]]

    def divide(self) -> "Iterable<MergesortProblem>":
        yield Skyline(self.bildings[:len(self.bildings)//2])
        yield Skyline(self.bildings[len(self.bildings)//2:])

    def combine(self, s: "Iterable<sorted IList<T>>") -> "sorted IList<T>":
        skyline = []
        sky1, sky2 = tuple(s)
        currentHight1, currentHight2 = 0, 0 
        currentX = 0
        maxH = 0
        i, j = 0, 0
        while i < len(sky1)  and j < len(sky2):
            if sky1[i] < sky2[j]: #comparo x de skyline 1 < x de skyline 2
                currentX = sky1[i]
                if i < len(sky1) - 1:#miro si es el ultimo elemento de sky1 
                    currentHight1 = sky1[i+1] #si no lo es le asigno la alturaMaxima su ultimo valor
                else:#si lo es le asigno la altura maxima 0
                    currentHight1 = 0
                i+=2
            elif sky1[i] > sky2[j]: #comparo x de skyline 1 > x de skyline 2
                currentX = sky2[j]
                if j < len(sky2) - 1 :
                    currentHight2 = sky2[j+1]#si no lo es le asigno la alturaMaxima su ultimo valor
                else:#si lo es le asigno la altura maxima 0
                    currentHight2 = 0
                j+=2
            else: #comparo x de skyline 1 = x de skyline 2
                currentX = sky1[i]
                if i < len(sky1) - 1: #miro si es el ultimo elemento de sky1 
                    currentHight1 = sky1[i+1]#si no lo es le asigno la alturaMaxima su ultimo valor
                else:#si lo es le asigno la altura maxima 0
                    currentHight1 = 0
                if j < len(sky2) - 1 : #miro si es el ultimo elemento de sky2
                    currentHight2 = sky2[j+1]
                else:#si lo es le asigno la altura maxima 0
                    currentHight2 = 0
                i+=2
                j+=2
            maxH = max(currentHight1,currentHight2) # comparo maxima altura
            alturaAnterior = skyline[-1:] #me almaceno la altura anterior del skyline   
            #se compara la altura anterior si es igual a la altura actual, para no volver a anyadirla
            if len(alturaAnterior) == 1 and maxH != alturaAnterior[0]:
                    skyline.append(currentX)
                    skyline.append(maxH)
            else:
                if len(alturaAnterior) != 1:
                    skyline.append(currentX)
                    skyline.append(maxH)
        #añado el resto del skyline que queda
        if i >= len(sky1):
            skyline = skyline + sky2[j:]
        else:
            skyline = skyline + sky1[i:]
        return skyline
# ================================== FINAL =====================================
buildings = readFile(sys.argv[1])
problemSkyline = Skyline(buildings)
resultadoSkyline = DivideAndConquerSolver().solve(problem=problemSkyline)
impSkyline = ""
for imp in resultadoSkyline:
    impSkyline += "{}".format(imp)
    impSkyline += " "
print(impSkyline.rstrip())

if len(sys.argv) == 3 and sys.argv[2] == "-g":
    grafic(resultadoSkyline, buildings)