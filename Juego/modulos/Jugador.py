from typeguard import typechecked
from Juego.modulos.Dado import Dado
from typing import Optional
import random


@typechecked
class Jugador:
    """
        Esta clase es la que contiene los metodos de jugador y su funcionamiento.
        Como parametro recibe el id del jugador.
    """
    def __init__(self, id_jugador: int):
        self.__id = self.__validar_id(id_jugador)  # Se verifica la id del jugador antes de asignarla
        self.__dados = []  # Lista donde se almacenaran los dados
        self.__crear_dados()  # Llamada al metodo privado crear los dados
        self.__puntos = 0  # Puntuacion del jugador

    def __crear_dados(self):
        # Se crean 5 dados y se añaden a la lista de dados
        for i in range(0, 5):
            dado = Dado()
            self.__dados.append(dado)

    @staticmethod
    def __validar_id(id_jugador):
        if id_jugador < 0:
            raise ValueError('El id debe ser un número positivo')
        return id_jugador

    @property
    def id(self):
        return self.__id

    @property
    def dados(self):
        return self.__dados

    @property
    def puntos(self):
        return self.__puntos

    def calcular_puntuacion(self) -> None:
        puntuacion = 0
        caras = {}

        for i in self.__dados:
            if i.cara_actual in caras:
                continue
            caras[i.cara_actual] = 0

        for i in self.__dados:
            if i.cara_actual in caras:
                caras[i.cara_actual] += 1
            else:
                continue

        npares = 0
        ntrio = 0
        ncuartetos = 0
        nquinteto = 0
        valores = caras.values()
        for i in valores:
            if i == 5:
                nquinteto += 1
            if i == 4:
                ncuartetos += 1
            if i == 3:
                ntrio += 1
            if i == 2:
                npares += 1
        if npares > 1:
            npares = 0
            ncuartetos += 1
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

        self.__puntos = puntuacion

    def tirar_dados(self, posiciones: Optional[list] = None):
        # Si no se ha recibido posiciones (es decir el usuario no ha hecho una segunda tirada)
        if posiciones is None:
            for tiro in self.__dados:  # Recorremos la lista de los dados y escogemos una nueva cara
                tiro.cara_actual = random.choice(tiro.caras_dado)
        else:  # Si posiciones si tiene valor (hay segunda tirada)
            for dado in posiciones:  # Recorremos la lista de las posiciones
                # Cambiamos la cara de de los dados que el usuario ha elegido
                self.__dados[dado-1].cara_actual = random.choice(self.__dados[0].caras_dado)

    def __str__(self):
        contador = 0
        # Se recorre la lista de los dados y se muestra el numero del dao y su cara actual
        for i in self.__dados:
            contador += 1
            print(f"Dado {contador}: {i.cara_actual}")
        print("")

        return f"Tirada del jugador {self.__id+1}"
