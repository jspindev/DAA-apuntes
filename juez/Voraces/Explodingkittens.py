
# no se si es waiting time o mochila sindeo el risgo lo maximo que me cuadra

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

n,m = map(int, input().strip().split()) #m riesgo
data = {}
data["attack"]=[]
data["profit"]=[]
data["weight"]=[]
ataque=[]
profit=[]
weight=[]
for i in range(n):
    c, r, b = input().strip().split()
    ataque.append(c)
    profit.append(b)
    weight.append(r)
data["attack"]=ataque
data["profit"]=profit
data["weight"]=weight
data["maxWeight"] = m

(sol, val) = greedyknapsack(data)

print(*sol)