
def getBestItem(data, candidates):
    pass

def greedyknapsack(data):

    n= len(data["profit"])
    candidates = set()
    for i in range(n):
        candidates.add(i)

    sol = [0] * n
    freeWeight = data["maxWeight"]
    isSol = False
    while candidates and not isSol :
        bestitem= getBestItem(data, candidates)

n = 5
data = {}

data["profit"] = [20,30,66,40,60]  #rollo videojuego de xexu puto clave 20 de escudo pesa 10 y quieres tener el maximo
data["weight"] = [10,20,30,40,50]
data["maxWeight"] = 100

sol = greedyknapsack(data)

print (sol)