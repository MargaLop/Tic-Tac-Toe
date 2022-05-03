from casilla import Casilla


class Tablero:
    lista_casillas = []
    lista_i = len(lista_casillas) - 1

    def __init__(self, rows, columns):
        self.r = rows
        self.c = columns
        self.casilla = []
        for row in range(self.r):
            for col in range(self.c):
                self.casilla.append(Casilla())
    pass

    def dibuja_casilla(self):
        return f"""
+-----
|  {self.lista_i}
"""
