from casilla import Casilla


class Tablero:

    """def __init__(self):

        self.casillas = [
            0, 0, 0,
            0, 0, 0,
            0, 0, 0
        ]"""



    def __init__(self, rows=3, columns=3):
        self.r = rows
        self.c = columns
        self.casillas = []
        contador = 0
        for row in range(self.r):
            for col in range(self.c):
                contador += 1 
                print(f"--{contador}")
                self.casillas.append(Casilla(row, col))

        print(f"Tablero cread de {self.r} x {self.c}")

    def dibujar(self):
        contador = 0

        for row in range(self.r):
            for col in range(self.c):

                contador += 1 



                n = (row * self.c) + col

                #  print(f"row: {row} -- col: {col} --- n: {n}")
                # print(f"++{contador}")
                # print(f"{n} of {len(self.casillas)}")
                
                
                print(self.casillas[n])

        

    def dibuja(self):

        borde = {
            "updown_last": "+-----+\n",
            "updown": "+-----",
            "side_last" :"|     |\n",
            "side": "|     "
        }

        # Creación de "tejado/techo" y de "suelo" de la fila del tablero.
        up_down = borde["updown"] * (self.r - 1) + borde["updown_last"] 

        # Creación de los lados de la fila del tablero.
        paredes = borde["side"] * (self.r - 1) + borde["side_last"]

        fila = up_down + paredes + up_down
        continuacion_fila = paredes + up_down

        tablero = fila + continuacion_fila * (self.c - 1)

        return tablero

# input_que_poner = [0, len()]
if __name__ == "__main__":
    tablero = Tablero(3, 3)
    tablero.dibujar()
    print(tablero.dibuja())