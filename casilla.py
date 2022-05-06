class Casilla:

    def __init__(self, row, column):
        self.row = row
        self.col = column
        self.owner = None

    def guarda_jugada(self, owner):
        self.owner = owner
    
    #comprobar que posicion es la casilla actual.
    def comprobar_posicion (self,row,column):
        while self.owner == None:
            if row == self.row and column == self.col:
                return True
            else:
                return False 

    def esta_disponible(self):
        if self.owner == None:
            return True
        else:
            return False

    def __str__(self):
        # return f"[{self.row}, {self.column}] ññ"
        return self.owner if self.owner else "·"

