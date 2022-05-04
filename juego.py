from  random import randint
from jugador import Jugador
from tablero import Tablero


class Juego:

    def __init__(self):
        self.reiniciar()

    def juega(self):
        # Decidir jugador activo
        jugador = randint(0, 1)
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

#reinicio. mira a ver si te interesa.
        while True:
            question = input("¿Quieres jugar de nuevo? y or n\n")
            if question == "y":
                print("GLHF")
                self.board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
                self.run()
            elif question == "n":
                print("¡Nos vemos proximamente!")
                quit()
            else:
                print("Esta opción valida")
