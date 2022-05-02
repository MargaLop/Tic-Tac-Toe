from jinja2 import ChoiceLoader
# from casilla import Casilla


class Tablero:
    def __init__(self, rows, columns):
        self.r = rows
        self.c = columns
        self.casilla = []
        for row in range(self.r):
            for col in range(self.c):
                self.casilla.append(Casilla())
    pass

    def dibujaCasilla(self, altura, ancho):
        altura = 5
        ancho = 5
        buffer_casilla = ""
        celda = ancho * altura
        print("""+-----+-----+-----+")
        |     |     |     |")
        +-----+-----+-----+")
        |     |     |     |")
        +-----+-----+-----+")
        |     |     |     |")
        +-----+-----+-----+""")

