class Casilla:
    def __init__(self, row, column, jugada='',buffer =[]):
        self.row = row
        self.column = column
        self.jugada = jugada
        self.buffer = buffer

    def guarda_ficha(self,jugada):
        self.jugada = jugada
        self.buffer.apend(self.jugada)
        