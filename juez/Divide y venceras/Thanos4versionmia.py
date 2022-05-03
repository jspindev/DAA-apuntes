
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
        print(":)")
    elif len(amoche) == 0:
        print(":_)")


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
certificados = []
for e in map(int,input().strip().split()):
    certificados.append(e)
certificados.sort()


#guanteinfinito(habitantes, amoches, certificados)
chasquido(habitantes, amoches, certificados)