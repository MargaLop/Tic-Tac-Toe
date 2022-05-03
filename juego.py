from jugador import Jugador
from tablero import Tablero


class Juego:

    def __init__(self):
        self.reiniciar()

    def juega(self):
        # Decidir jugador activo
        # seleccion de casilla (jugador.introduce_jugada)
        # comprobar si jugador activo gana. posibilidades
        #    - self.ganador()
        #    - O cambiamos jugador activo y repetimos
        #    - O todos los espacios llenos => empate


        pass

    def ganador(self, jugador):
        pass

    def reiniciar(self):
        self.jugadores = (Jugador(False), Jugador(True))
        self.tablero = Tablero()
