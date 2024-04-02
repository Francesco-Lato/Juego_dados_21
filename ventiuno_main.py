from ventiuno_mesa import MesaJuego
from ventiuno_jugador import Jugador
from ventiuno_dado import Dado
from ventiuno_menu import Menu

ventiuno = Menu('Insertar número jugadores', 'jugar', 'salir', titulo='Ventiuno')
mesa = None


while True:
    ventiuno.mostrar
    opcion = ventiuno.elige()

    if opcion == 1:
        jugadores = int(input('insertar jugadores: '))
        mesa = MesaJuego(jugadores)
        mesa.mostrarJugadores()
    elif opcion == 2:
        if mesa is None:
            print('Antes debe insertar jugador, opción 1 (Insertar número jugadores)')
        if mesa is not None:
            mesa.jugar()
    else:
        print('Adios')
        break


