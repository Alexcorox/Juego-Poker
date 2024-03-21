from Juego.modulos.Jugador import Jugador
from typeguard import typechecked


@typechecked
class Mesa:
    """
    Esta clase es la encargada de la logica del juego, es decir crea los jugadores y el orden en el que juegan
    Como parametro recibe el numero de jugadores que van a jugar.
    """
    def __init__(self, njugadores: int):
        self.__jugadores = []  # Lista donde se almacenaran los jugadores
        self.__puntuaciones_jugadores = {}  # Diccionario donde almacenaremos el jugador y cuanta puntuacion tiene en una ronda
        self.__rondas_jugadores = {}  # Diccionario donde almacenaremos las rondas ganadas de cada jugador
        self.__crear_jugador(njugadores)  # Llamada a metodo privado para crear jugadores

    def __crear_jugador(self, njugadores: int):
        for i in range(0, njugadores):  # Bucle para crear jugadores hasta llegar a la cantidad indicada
            jugador = Jugador(i)  # Creacion de usuario pasandole una id
            self.__jugadores.append(jugador)  # Se añade el jugador a la lista de jugadores
            self.__puntuaciones_jugadores[i] = 0  # Se inicializa la id en el diccionario y se añade valor inicial 0
            self.__rondas_jugadores[i] = 0

    def jugar(self):
        turno = 1  # Se crea variable para controlar el turno en el que nos encontramos
        max_turno = 5  # Numero maximo de turnos
        id_ganador = 0  # Se inicializa la id del ganador y se asigna como valor inicial 0

        while turno <= max_turno:  # Mientras que no se supere el maximo de turnos
            puntuacion_max = 0  # Se inicializa la puntuacion maxima de la ronda
            print(f"Estamos en la ronda {turno}")
            print("===================================================")
            for jugador in self.__jugadores:
                input(f"Jugador {jugador.id+1} pulse intro para lanzar los dados")
                print("")
                jugador.tirar_dados()
                print(jugador)
                print("")
                decision = input("¿Quieres volver a tirar los dados? [S/n]: ")

                # Comprobacion para ver si el usuario quiere volver a tirar los dados
                if decision.lower() == "s" or decision == "":
                    dados_a_cambiar = []  # Se crea una lista para almacenar los dados a cambiar
                    ndados = 1  # Se crea una variable para comprobar cuantos dados quiere cambiar usuario
                    while True:
                        dado = int(input("Indique el dado a cambiar segun la posicion o introduzca 0 para salir: "))

                        if dado == 0 or ndados >= 5:
                            break

                        if dado >= 1 and dado <= 6 and dado not in dados_a_cambiar:
                            ndados += 1
                            dados_a_cambiar.append(dado)

                    jugador.tirar_dados(dados_a_cambiar)
                    print("")
                    print(jugador)
                    print("")

                jugador.calcular_puntuacion()
                self.__puntuaciones_jugadores[jugador.id] = jugador.puntos  # Actualizamos el diccionario con los puntos del jugador

            for ganador in self.__puntuaciones_jugadores:  # Recorremos el diccionario de las puntuaciones
                id_jugador = ganador
                puntuacion_jugador = self.__puntuaciones_jugadores[ganador]

                # Comprobamos si la puntacion del jugador actual es mayor a la del jugador con mayor puntuacion
                if puntuacion_jugador > puntuacion_max:
                    # Si es asi, almacenamos el id del ganador
                    puntuacion_max = puntuacion_jugador
                    id_ganador = id_jugador

            # En el diccionario de rondas ganadas agregamos un ronda al id del ganador
            self.__rondas_jugadores[id_ganador] += 1

            print("===================================================")
            print(f"El ganador de la ronda {turno} es el jugador {id_ganador+1}")
            print("===================================================")
            turno += 1  # Sumamos 1 ronda

        puntuacion_max = 0  # Le asignamos el valor 0 puntuacion max

        # Recorremos el diccionario de las rondas ganadas
        for ganador in self.__rondas_jugadores:
            puntuacion_jugador = self.__rondas_jugadores[ganador]

            # Comprobamos si las rondas del jugador actual es mayor a la del jugador con mayor rondas
            if puntuacion_jugador > puntuacion_max:
                # Si es asi, almacenamos el id del ganador
                puntuacion_max = puntuacion_jugador
                id_ganador = ganador

        print(f"El ganador del juego es {id_ganador+1} ")
