class Casilla:
    def __init__(self,jugada):
        self.jugada = jugada

    def guarda_jugada(self,buffer =[]):
        self.buffer = buffer
        self.buffer.append(self.jugada)

