"""
Archivo principal en el cual se escriben las llamadas a la mesa
"""
from modulos.Mesa import Mesa

print("===================================================")
print("Bienvenido al juego de poker")
print("===================================================")
while True:
    jugadores = int(input("Porfavor, introduzca cuantos jugadores van a jugar: "))
    print("")

    mesa = Mesa(jugadores)
    mesa.jugar()

    print("")
    jugar_otra_vez = input("¿Jugar otra partida? [S/n]: ")

    if jugar_otra_vez.lower() == "n" or jugar_otra_vez.lower() != "s" and jugar_otra_vez != "":
        break

print("")
print("Finalizando el juego")
