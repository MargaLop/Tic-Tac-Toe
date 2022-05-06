'''class Jugador:
    fichas = ["cruz", "raya"]
    inicio = ""

    def __init__(self, ficha=False):
        self.ficha = self.fichas[0] if ficha else self.fichas[1]
        # self.inicio = inicio

    def introduce_jugada(self):
        userInput = input("seleccione una ficha cruz/raya")

    def movimiento(self, ficha, contador):
        nueva_lista = []
        contador += 1
        jugada = nueva_lista.append(ficha)
        # when (ficha == [0] and ficha == [0]):
'''
from colorhelper import rojo, verde, azul
from tablero import Tablero

class Jugador:
    def __init__(self, token, valor):
        self._token = token
        self.valor = valor
        self.color = rojo if self.valor == 1 else azul

    def get_token(self):
        self.Tablero[row][column] = Jugador
        return self.color(self._token)

    def set_token(self, token):
        player = 'X' if self.get_random_first_player() == 1 else 'O'
        while True:
            print(f"Player {player} turn")
        self._token = token

    def del_token(self):
        del self._token

    token = property(get_token, set_token, del_token)

    def elige(self, tablero):

        def humanToMachine(casillaElegida):
            return int(casillaElegida) - 1

        def validarEntrada(tablero, casillaElegida):
            if not casillaElegida.isdigit():
                print("    Eso no parece una jugada válida")
                return False

            celdaElegida = humanToMachine(casillaElegida)
            if celdaElegida not in range(0, 9):
                print("    Eso parece estar fuera del tablero")
                return False

            if not tablero.estaDisponibleLaCelda(celdaElegida):
                print("    Esa casilla ya está ocupada")
                return False

            return True

        def solicitaJugada():

            return input(f"\n    jugador [ {self.token} ] elige pos: ")

        casillaElegida = solicitaJugada()
        while not validarEntrada(tablero, casillaElegida):
            casillaElegida = solicitaJugada()

        celdaElegida = humanToMachine(casillaElegida)


        def is_player_win(self, Jugador):
            win = None

        n = len(self.board)

        # checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != Jugador:
                    win = False
                    break
            if win:
                return win

        # checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != Jugador:
                    win = False
                    break
            if win:
                return win

        # checking diagonals
        win = True
        for i in range(n):
            if self.board[i][i] != Jugador:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != Jugador:
                win = False
                break
        if win:
            return win
        return False

        for row in self.Teclado:
            for item in row:
                if item == '-':
                    return False
        return True





        tablero.introduce(self, celdaElegida)