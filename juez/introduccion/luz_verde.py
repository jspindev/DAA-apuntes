

jugador, luz ,sensor = input().strip().split()

jugador = int(jugador)

output="CONTINUAR"

if luz == 'r' and sensor == '1':
    output="ELIMINADO"

print("Jugador "+ str(jugador)+ " "+ output)

