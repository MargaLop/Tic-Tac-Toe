# from itertools import product


class Casilla:
    # def __init__(self, row, column, jugada='', indice=[], list_r=[], list_c=[]):
    #     self.row = row
    #     self.column = column
    #     self.jugada = jugada
    #     self.indice = indice
    #     self.list_r = list_r
    #     self.list_c = list_r

    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.owner = None

    def guarda_jugada(self, owner):
        self.owner = owner
'''
        for r in range(self.row):
            self.list_r.append(str(r))

        for c in range(self.column):    
            self.list_c.append(str(c))
   
        for i in product(self.list_r, self.list_c): 
            self.indice.append(i[0] + ',' + i[1])
'''
# tableroo = [False,False,False,False,False,False,False,False,False]
