#calcetines -> 1
#pantalon -> 2
#camisa -> 3
#zapatos -> 4
#cinturon -> 5
#jersey -> 6
from collections import deque

grafo=[
    [],
    [4],
    [4,5],
    [5,6],
    [],
    [],
    []
]
def top_sort_visit(data, k):
    data["state"][k] = "VISITED"
    data["time"]=data["time"]+1
    #data["time"] +=1
    data["d"][k]=data["time"]
    for adj in data["graph"][k]:
        if data["state"][adj] == "NOT VISITED":
            top_sort_visit(data,adj)

    data["state"][k] =="FINISH"
    data["time"] += 1
    data["f"][k] = data["time"]

    data["list"].appendleft(k)

def top_sort(g):
    n = len(g)
    data={
        "graph":g,
        "state": dict(),
        "d":dict(), #descubrimiento
        "f":dict(), #fin
        "time": 0,
        "list":deque() #solucion
    }
    for k in g.keys():
        data["state"][k] = "NOT VISITED"
        data["d"][k] = 0
        data["f"][k] = 0

    for k in g.keys():
        if data["state"][k] == "NOT VISITED":
            top_sort_visit(data,k)
    #print(g.keys())

    print(data["list"])


#g=dict() es un diccionario un array pero indexado con lo que tu quieras de indice
g ={
    "calcetines":["zapatos"],
    "pantalon":["zapatos","cinturon"],
    "camisa":["cinturon","jersey"],
    "zapatos":[],
    "cinturon":[],
    "jersey":[]
}

print(g["calcetines"])


top_sort(g)