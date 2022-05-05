from jugador import Jugador
from tablero import Tablero

class Juego:

    def choose_marker(self, marker):
        
        self.marker = str('')
        while marker != 'X' and marker !='O':
            marker = input("Player1! Please choose 'X' or 'O' as your marker: ").upper()

            player1 = marker

            if player1 == 'X':
                player2 = 'O'
            else:
                player2 = 'X'
    
    
        print('Player1', player1)
        print('Player2', player2)

        return(player1, player2)
    
    def reset(self):
        self.turno = 0
        self.tablero = Tablero()


    def juega(self):
         
        playAgain = True
        while playAgain:
            self.reset()
            while self.tablero.quedanCeldasLibres():
                self.tablero.dibuja(self.jugadores)
                jugador = self.jugadores[self.turno % 2]
                jugador.elige(self.tablero)
                self.turno += 1

                if self.tablero.hayJugadaGanadora():
                    pre =("    Felicidades jugador [ ")
                    post =(" ]! Has ganado")
                    print(f"{pre}{jugador.token}{post}")
                    break

            if not self.tablero.hayJugadaGanadora():
                print ("\n    EMPATE: Habéis llegado al final sin que gane nadie.")

            playAgain = self.yesOrNo()
            if playAgain:
                print("\n    Gracias por repetir, está claro que te diviertes")
        

