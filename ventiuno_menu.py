class Menu:
    """Clase Menú"""
    def __init__(self, *opciones, titulo='--- Menu ---'):
        self.__opciones = list(opciones)
        self.__titulo = titulo

    def insertar_opciones(self, opcion):
        self.__opciones.append(opcion)

    @property
    def size_menu(self):
        return len(self.__opciones)

    @property
    def mostrar(self):
        print(self.__titulo)
        for i in range(self.size_menu):
            print(f'{i+1}. {self.__opciones[i].title()}')
        print('------------')

    def elige(self):
        opcion = int(input('Elige opción: '))
        while True:
            if opcion < 1 or opcion > self.size_menu: #1 <= opcion >= self.size_menu (opcion debe estr entre 1 y el len de opciones)
                opcion = int(input('Elige opción: '))
            else:
                return opcion