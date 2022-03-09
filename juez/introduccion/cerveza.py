
n=int(input())
output=""
if n >= 46:
    output="MUY BUENA"
elif n >= 36:
    output="BUENA"
elif n >=21:
    output="REGULAR"
elif n>=11:
    output="MALA"
else:
    output="CRUZCAMPO"

print(output)
