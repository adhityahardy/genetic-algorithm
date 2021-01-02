import random
import math
import copy
# import numpy as np

def Kromosom(sel):
    arrKrom = []
    for i in range(sel):
        arrKrom.append(random.randint(0,1))
    return arrKrom

# def initPop(jumlahpop, gen):
#     populasi = np.random.randint(0,1,(jumlahpop,gen))
#     return populasi

def Populasi(jumlahpop):
    arrPop = []
    for i in range(jumlahpop):
        arrPop.append(Kromosom(8))
    return arrPop

def dekodeKromosom(kromosom):
    # r1min = -1, r1max = 2
    # r2min = -1, r2max = 1

    x1 = -1 + (2-(-1) / (2**-1 + 2**-2 + 2**-3 + 2**-4)) * ((kromosom[0]*2**-1)+(kromosom[1]*2**-2)+(kromosom[2]*2**-3)+(kromosom[3]*2**-4));
    x2 = -1 + (1-(-1) / (2**-1 + 2**-2 + 2**-3 + 2**-4)) * ((kromosom[4]*2**-1)+(kromosom[5]*2**-2)+(kromosom[6]*2**-3)+(kromosom[7]*2**-4));
    return [x1, x2];

def getFitness(fit):
    HitungFitness = dekodeKromosom(fit)
    h = (math.cos(HitungFitness[0])) * (math.sin(HitungFitness[1])) - (HitungFitness[0]/(HitungFitness[1]**2+1))
    resultFit = 1 / h + 0.9
    return resultFit

def getFitnessAll(populasi, SizePop):
    fitAll = []
    for i in range(SizePop):
        fitAll.append(getFitness(populasi[i]))
    return fitAll

def TurnamenSelect(populasi, SizeTur, SizePop):
    BestKrom = []
    for i in range(0, SizeTur-1):
        individu = populasi[random.randint(0, SizeTur-1)]
        if (BestKrom == [] or getFitness(individu) > getFitness(BestKrom)):
            BestKrom = individu
    return BestKrom

def crossOver(parent1, parent2, pc):
    r = random.random()
    if(r <= pc):
        point = random.randint(0,7)
        for i in range(point):
            parent1[i], parent2[i] = parent2[i], parent1[i]
    return parent1, parent2

def mutation(parent1, parent2, pm):
    r = random.random()
    if (r < pm):
        parent1[random.randint(0,7)] = random.randint(0,1)
        parent2[random.randint(0,7)] = random.randint(0,1)
    return parent1, parent2

def getElitisme(fitAll):
    return fitAll.index(max(fitAll))


# jumlahpop = 8
# gen = 4
ukPop = 100
ukTur = 5
pc = 0.6
pm = 0.1
generasi = 20

# populasi = Populasi(ukPop)

# print(populasi)

populasi = Populasi(ukPop)

for i in range(generasi):
    fit = getFitnessAll(populasi, ukPop)
    new_populasi = []

    bestPar = getElitisme(fit)
    new_populasi.append(populasi[bestPar])
    new_populasi.append(populasi[bestPar])
    i = 0
    while (i < ukPop-2):
        parent1 = TurnamenSelect(populasi, ukTur, ukPop)
        parent2 = TurnamenSelect(populasi, ukTur, ukPop)
        while (parent1 == parent2):
            parent2 = TurnamenSelect(populasi, ukTur, ukPop)
        parent1 = copy.deepcopy(parent1)
        parent2 = copy.deepcopy(parent2)
        child = crossOver(parent1, parent2, pc)
        child = mutation(child[0], child[1], pm)
        new_populasi += child
        i += 2
    populasi = new_populasi

fitness = getFitnessAll(populasi, ukPop)
result = getElitisme(fitness)

print('Kromosom terbaik:', populasi[result])
print('Hasil decode    :', dekodeKromosom(populasi[result]))