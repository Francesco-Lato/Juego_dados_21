from typeguard import typechecked

@typechecked
class Dado:
    def __init__(self):
        self.__cara = 1

    @property
    def cara(self):
        return self.__cara

    @cara.setter
    def cara(self, cara):
        if cara < 1 or cara > 6:
            raise ValueError('Error en el valor de la cara del dado')
        else:
            self.__cara = cara
















