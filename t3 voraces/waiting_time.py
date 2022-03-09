import random
import sys


def getBestTask(candidates, tasks):
    bestTimeTask = sys.maxsize
    bestTask = 0
    for c in candidates:
        time = tasks[c]
        if time < bestTimeTask:
            bestTimeTask = time
            bestTask = c

    return bestTask


def greedyWaitingTime(tasks):
    candidates = set()  # creamos un conjunto
    n = len(tasks)
    for i in range(n):
        candidates.add(i)  # añade task en candidatos en forma de conjunto

    sol = []  # un algoritmo voraz siempre empieza por una solucion vacia
    while candidates:
        bestTask = getBestTask(candidates, tasks)
        candidates.remove(bestTask)
        sol.append(bestTask)
    return sol


n = 10
tasks = []

for i in range(n):
    tasks.append(random.uniform(44, 140))
print(tasks)

sol = greedyWaitingTime(tasks)
print(sol)
sumWaitingTime = 0
for j in range(len(sol)):
    print(str(sol[j]), end=" ")
    i = 0
    acum = 0
    while i <= j:
        acum += tasks[i]
        i += 1
    sumWaitingTime += acum

print(sumWaitingTime)