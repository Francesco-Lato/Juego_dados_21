from typeguard import typechecked
import random
from ventiuno_dado import Dado
import time

@typechecked
class Jugador:
    def __init__(self, id: int):
        self.__id = id
        self.__puntos = 0
        self.__dados = []
        self.crearDados()

    @property
    def id(self):
        return self.__id

    @property
    def dados(self):
        return self.__dados

    @property
    def puntos(self):
        return self.__puntos

    @puntos.setter
    def puntos(self, puntos):
        self.__puntos = puntos

    def crearDados(self):
        for i in range(2):
            d = Dado()
            self.dados.append(d)

    def tirarDados(self):
        suma_tiro = 0
        for i, tiro in enumerate(self.dados, start=1):
            tiro.cara = random.randint(1, 6)
            print('...tirando dados')
            time.sleep(2)
            print(f'Dado {i} = {tiro.cara}')
            suma_tiro += tiro.cara
        print(f'TOTAL tiro: {suma_tiro}')
        self.puntos += suma_tiro
        print(f'Total: {self.puntos}')
        return self.puntos


    def verDados(self):
        print("Valores de los dados:")
        for i, dado in enumerate(self.dados, start=1):
            print(f"Dado {i}: {dado.cara}")