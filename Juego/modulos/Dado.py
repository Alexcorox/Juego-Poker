
class Dado:

    """
    Esta clase simplente se encarga de crear el objeto dado
    """
    def __init__(self):
        self.__caras_dado = [1, 2, 3, 4, 5, 6]
        self.__cara_actual = 0

    @property
    def cara_actual(self):
        return self.__cara_actual

    @property
    def caras_dado(self):
        return self.__caras_dado

    @cara_actual.setter
    def cara_actual(self, cara_nueva: int):
        self.__cara_actual = cara_nueva

    def __repr__(self):
        return f"{self.cara_actual}"
