def isFeasible(data, bestItem, freeWeight):
    return (freeWeight - data['weight'][bestItem]) >= 0

def getBestItem(data, candidates):
    bestRatio = 0
    bestItem = -1
    for c in candidates:
        r = data['profit'][c] / data['weight'][c]
        if r > bestRatio:
            bestRatio = r
            bestItem = c
    return bestItem


def greedyknapsack(data):

    n= len(data["profit"])
    candidates = set()
    for i in range(n):
        candidates.add(i)
    sol = [0] * n

    freeWeight = data["maxWeight"]
    isSol = False
    val = 0
    while candidates and not isSol :
        bestItem= getBestItem(data, candidates)
        candidates.remove(bestItem)
        if isFeasible(data, bestItem, freeWeight):
            sol[bestItem] = 1.0
            val += data['profit'][bestItem]
            freeWeight -= data['weight'][bestItem]
        else:
            sol[bestItem] =  freeWeight /data['weight'][bestItem]
            val += data['profit'][bestItem] * sol[bestItem]
            isSol = True
    return sol, val

n = 5
data = {}

data["profit"] = [20,30,66,40,60]  #rollo videojuego de xexu puto clave 20 de escudo pesa 10 y quieres tener el maximo
data["weight"] = [10,20,30,40,50]
data["maxWeight"] = 100

(sol,val) = greedyknapsack(data)

print (sol)