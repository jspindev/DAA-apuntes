#repartir pizzas
#en voraces hay que crear siempre un set

def getBestItem(datam, candidates):
    bestProfit = 0
    bestItem = -1
    for c in candidates:
        profit = data["profit"][c]
        if profit > bestProfit:
            bestProfit = profit
            bestItem = c
    return bestItem

def isFeasible(shcedule, pos):
    return shcedule[pos] == -1

def greedySchedule(data):
    n = len(data["profit"])
    candidates = set()
    for i in range(n):
        candidates.add(i)
    lastDate = max(data["deadLine"])
    schedule = [-1] * (lastDate + 1)
    while candidates:
        bestItem = getBestItem(data, candidates)
        candidates.remove(bestItem)
        i = data["deadLine"][bestItem]
        found = False
        while i >= 0 and not found:
            if isFeasible(schedule,i):
                schedule[i] = bestItem
                found = True
            i -= 1
    return schedule

#Prog. Principal
data = {
    "profit" : [50,10,15,30],
    "deadLine" : [2,1,2,1]
}

schedule = greedySchedule(data)
print(schedule)