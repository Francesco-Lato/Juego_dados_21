from typeguard import typechecked
from ventiuno_jugador import Jugador

@typechecked
class MesaJuego:
    def __init__(self, njugadores: int):
        self.__jugadores = []
        self.crear_jugador(njugadores)
        self.puntos_jugadores = {}


    @property
    def jugadores(self):
        return self.__jugadores

    def mostrarJugadores(self):
        print('JUEGO 21')
        print(f'En esta mano van a jugar {len(self.jugadores)} jugadores')
        for jugador in self.jugadores:
            print(f'Jugador con ID: {jugador.id +1}')

    def __str__(self):
        return f'{self.jugadores}, {self.puntos_jugadores}'

    def crear_jugador(self, njugadores: int):
        for i in range(0, njugadores):
            jugador = Jugador(i)
            self.__jugadores.append(jugador)

    def almacenarPuntos(self, jugador: Jugador):
        if jugador.puntos > 21:
            print('Has superado el tope de 21, tu puntuación es = 0')

        self.puntos_jugadores[jugador.id] = jugador.puntos


    def puntos_mano(self, jugador: Jugador):
        if jugador.puntos > 21:
            self.puntos_jugadores[jugador.id] = 0

        else:
            self.puntos_jugadores[jugador.id] = jugador.puntos

    def ganador(self, valores: dict):
        puntos_max = 0
        ganador = []
        for jugador, puntos in valores.items():
            print(f'El jugador {jugador +1} tiene {puntos} puntos')
            if puntos > puntos_max:
                puntos_max = puntos
                ganador = [jugador]
            elif puntos == puntos_max:
                ganador.append(jugador)
        if len(ganador) == 1:
            print(f'El ganador es el jugador {ganador[0]+1} con {puntos_max} puntos')
        else:
            print(f'¡Hay un empate entre los jugadores {", ".join(str(j) for j in ganador)} con {puntos_max} puntos')


    def jugar(self):
        self.mostrarJugadores()
        for jugador in self.__jugadores:
            print(f'El jugador {jugador.id +1} va a tirar los dados.')
            jugador.tirarDados()
            decision = input("¿Quieres volver a tirar los dados? [S/N]: ").upper()
            #if decision == "S" and jugador.puntos >= 21:
            #    print('Ya no puedes tirar los dados')
            while decision == 'S' and jugador.puntos < 21:
                jugador.tirarDados()
                print(jugador.puntos)
                decision = input("¿Quieres volver a tirar los dados? [S/N]: ").upper()
                if decision == "S" and jugador.puntos >= 21:
                    print('Ya no puedes tirar los dados, has superado 21')
                else:
                    continue

            else:
                self.almacenarPuntos(jugador)
                self.puntos_mano(jugador)
                continue

        self.ganador(self.puntos_jugadores)