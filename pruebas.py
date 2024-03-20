from modulos.Jugador import Jugador

j1 = Jugador

def __calcular_puntuaciones(jugador: 'Jugador') -> int:
    puntuacion = 0
    caras = {}
    for i in jugador.dados:
        caras[i.id_dados] = 0

    for i in jugador.dados:
        if i.id_dados in caras:
            caras[i.id_dados] += 1
    npares = 0
    ntrio = 0
    ncuartetos = 0
    nquinteto = 0
    valores = caras.values()
    if 2 in valores:
        npares += 1
    if 3 in valores:
        ntrio += 1
    if 4 in valores:
        ncuartetos += 1
    if 5 in valores:
        nquinteto += 1
    # Calculo la puntuación
    if nquinteto == 1:
        puntuacion += 8
    elif ncuartetos == 1:
        puntuacion += 7
    elif ntrio == 1 and npares == 1:
        puntuacion += 6
    elif ntrio == 1 and nquinteto == 0 and ncuartetos == 0 and ntrio == 0 and npares == 0:
        puntuacion += 3
    elif ntrio == 0 and nquinteto == 0 and ncuartetos == 0 and ntrio == 0 and npares == 2:
        puntuacion += 2
    elif ntrio == 0 and nquinteto == 0 and ncuartetos == 0 and ntrio == 0 and npares == 0:
        puntuacion += 1
    else:
        dados = 0
        for i in valores:
            dados += i
        if dados == 15:
            puntuacion += 4
        if dados == 20:
            puntuacion += 5

    return puntuacion

if __name__ == '__main__':
    print(j1)
    print(__calcular_puntuaciones(j1))
