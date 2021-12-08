#Gauss' circle problem: define how many points of a square grid are within a sphere which's center is the center of said grid
#Approximated solution: as the distance between points decreases, the number of points within the sphere increases,
#approximating: sphere's area / square's area

#For a a sphere of radius R, the grid will be side 2R
#Thus, (2 * pi * R*R) / (2R * 2R)

#Problema do circulo de Gauss: definir quantos pontos de um grid quadrado estao dentro de uma esfera cujo centro está no centro do grid
#Solucao aproximada: a medida que a distancia entre pontos diminui, o número de pontos na esfera aumenta
#aproximando: area da esfera / area do quadrado

#Sendo o raio da esfera = R, logo, o lado do quadrado = 2R
#Ou seja, (2 * pi * R*R) / (2R * 2R)

import math

class position:

    def __init__(self, x, y):
        self.x=x
        self.y=y

#simple pythagoras
def distance(pos1, pos2):

    x=math.fabs(pos1.x-pos2.x)
    y=math.fabs(pos1.y-pos2.y)

    x=x*x
    y=y*y

    return math.sqrt(x+y)

def genMatrix(size):

    matrix=[]

    for i in range(size):
        for j in range(size):

            pos = position(i,j)

            matrix.append(pos)

    return matrix

##########

num = 99

razoes=[]
razoes.append(1)

def calcular(size):

    count=0
    radius=(size-1)/2

    matriz = genMatrix(size)
    centro = position(radius, radius)

    #in case you wanna offset the sphere
    #centro.x=centro.x+0.5
    #centro.y=centro.y+0.5

    for i in matriz:

        dist = distance(i, centro)

        inRange = dist <= radius

        if inRange:
            count=count+1

    ratio = count / len(matriz)

    lastRatio = razoes[len(razoes)-1]
    conv = ratio / lastRatio

    if conv > 1:
        conv = lastRatio / ratio

    ratiostr ="%.6f" % (ratio*100)
    convstr = "%.6f" % conv
    
    razoes.append(ratio)

    print("Size",size,"x",size,".   ",count,"out of",len(matriz),"in radius.    Or:",ratiostr,"% .Convergence:",convstr)    

for i in range(3,num):
    calcular(i)

print("")