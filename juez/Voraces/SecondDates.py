
def date(data_aux,k):
    young=[]
    old=[]
    for i in range(k):
        young.append(data_aux[i][1])
    for i in range(k):
        data_aux.remove(data_aux[0])
    n=len(data_aux)
    for v in range(n):
        old.append(data_aux[v][1])
    print(*young)
    print(*old)

n,k= map(int,input().strip().split())
data = []
for _ in range(n):
    c, a = input().strip().split()
    a = int(a)
    data.append((a, c))

data_aux = sorted(data)

date(data_aux,k)
