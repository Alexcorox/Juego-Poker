import random

from typeguard import typechecked
from modulos.Dado import Dado
from typing import Optional
import random

@typechecked
class Jugador:
    def __init__(self, id: int):
        self.__id = self.validarID(id)
        self.__tiros = 0
        self.__dados = []
        self.__crear_dados()
        self.__puntos = 0

    def __crear_dados(self):
        for i in range(0, 5):
            dado = Dado()
            self.__dados.append(dado)

    def validarID(self, id):
        if id < 0:
            raise ValueError('El id debe ser un número positivo')
        return id

    def calcular_puntuacion(self) -> None:
        puntuacion = 0
        caras = {}
        cara_comparada = 1
        repetido = 0

        for i in self.__dados:
            caras[i.cara_actual] = 0

        for i in self.__dados:
            if i.cara_actual == cara_comparada:
                repetido += 1

            cara_comparada += 1
            caras[i.cara_actual] = repetido


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

        self.__puntos = puntuacion

    def __str__(self):
        contador = 0
        for i in self.__dados:
            contador += 1
            print(f"Dado {contador}: {i.cara_actual}")

        return repr(f'Tirada del jugador {self.__id+1}')


    @property
    def id(self):
        return self.__id

    @property
    def tiros(self):
        return self.__tiros

    @property
    def dados(self):
        return self.__dados

    @property
    def puntos(self):
        return self.__puntos

    def tirarDados(self, posiciones: Optional[list] = None):
        if posiciones is None:
            for tiro in self.__dados:
                tiro.cara_actual = random.choice(tiro.caras_dado)
        else:
            for dado in posiciones:
                self.__dados[dado-1].cara_actual = random.choice(self.__dados[1].caras_dado)
