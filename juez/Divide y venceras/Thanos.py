
def guanteinfinito(habitantes,amoche,certificados):
    for i in certificados:
        if i in amoche:
            print(":_(")
        else:
            print(":)")

def aux(amoche,act):
    med = len(amoche) // 2
    if amoche[med] > act:
        aux(amoche[-med:], act)
    elif amoche[med] < act:
        aux(amoche[:-med], act)
    elif amoche[med] == act:
        print(":_(")
    elif len(amoche) == 0:
        print(":)")


def chasquido(habitantes,amoche,certificados):
    med = len(certificados) // 2
    for i in range(len(certificados)):
        act = certificados[i]
        aux(amoche,act)



n = int(input())
habitantes = []
for e in map(int,input().strip().split()):
    habitantes.append(e)

m = int(input())
amoches = []
for e in map(int, input().strip().split()):
    amoches.append(e)
amoches.sort()


p = int(input())
amoche = []
for e in map(int,input().strip().split()):
    amoche.append(e)
amoche.sort()
guanteinfinito(habitantes, amoches, amoche)