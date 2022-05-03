class Jugador:
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
