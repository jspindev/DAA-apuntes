
def explodingkittens(data, m, data_aux):
    riesgo = 0
    beneficio = 0
    ataques = []
    sol = []
    while riesgo < m:
        act_data = data.pop(0)
        ataques.append(act_data[1])
        if riesgo + act_data[3] <= m:
            riesgo += act_data[3]
            beneficio += act_data[2]
        else:
            riesgo_proporcional = m - riesgo
            beneficio += (riesgo_proporcional/act_data[3]) * act_data[2]
            riesgo *= act_data[3]

    print(*ataques)
    #for a in ataques:
   #     sol.append(ataques[a][1])
   # print(*sol, end=" ")


n,m = map(int, input().strip().split())
data = []

for _ in range(n):
    c, r, b = input().strip().split()
    r = int(r)
    b = int(b)
    data.append((r/b, c, b, r))

data_aux = sorted(data)
explodingkittens(data_aux, m, data)
