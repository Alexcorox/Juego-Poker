"""

"""
from modulos.Jugador import Jugador
from typeguard import typechecked


@typechecked
class Mesa:
    def __init__(self, njugadores: int):
        self.__jugadores = []
        self.__puntuaciones_jugadores = {}
        self.__rondas_jugadores = {}
        self.__crear_jugador(njugadores)

    def __crear_jugador(self, njugadores: int):
        for i in range(0, njugadores):
            jugador = Jugador(i)
            self.__jugadores.append(jugador)
            self.__puntuaciones_jugadores[i] = 0
            self.__rondas_jugadores[i] = 0

    def jugar(self):
        turno = 1
        max_turno = 2
        id_ganador = 0

        while turno <= max_turno:
            turno += 1
            puntuacion_max = 0

            for jugador in self.__jugadores:
                jugador.tirarDados()
                print(jugador)
                decision = input("¿Quieres volver a tirar los dados? [S/n]: ")

                if decision == "S" or decision == "":
                    dados_a_cambiar = []
                    while True:
                        dado = int(input("Indique el dado a cambiar segun la posicion:"))

                        if dado >= 1 and dado <= 6:
                            dados_a_cambiar.append(dado)

                        if dado == 0:
                            break

                    jugador.tirarDados(dados_a_cambiar)
                    print(jugador)

                jugador.calcular_puntuacion()
                self.__puntuaciones_jugadores[jugador.id] = jugador.puntos

            for ganador in self.__puntuaciones_jugadores:
                id_jugador = ganador
                puntuacion_jugador = self.__puntuaciones_jugadores[ganador]

                if puntuacion_jugador > puntuacion_max:
                    puntuacion_max = puntuacion_jugador
                    id_ganador = id_jugador

            self.__rondas_jugadores[id_ganador] += 1

            print("===================================================")
            print(f"El ganador de la ronda {turno-1} es el jugador {id_ganador+1}")
            print("===================================================")

        puntuacion_max = 0
        for ganador in self.__puntuaciones_jugadores:
            puntuacion_jugador = self.__rondas_jugadores[ganador]

            if puntuacion_jugador > puntuacion_max:
                puntuacion_max = puntuacion_jugador
                id_ganador = ganador

        print(f"El ganador del juego es {id_ganador+1} ")




