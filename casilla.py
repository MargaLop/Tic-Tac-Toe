class Casilla:
    def __init__(self, row, column, jugada):
        self.row = row
        self.column = column
        self.jugada = jugada

    def guarda_ficha(self):
        self.buffer =[]
        self.buffer.append(self.jugada)