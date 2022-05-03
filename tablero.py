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

    def make_output_buffer(input_buffer):
        def make_line(position=0, size=80):
            linechars = [
                ['+', '+'],
                ['+', '+'],
                ['+', '+']
            ]

            linechar = linechars[position]

            return ' ' + linechar[0] + '-' * (size + 2) + linechar[1]

        def make_linetext(line, size=80):

            return ' | ' + line.ljust(size) + ' | '

        output_buffer = []

        longest_line = max(input_buffer, key=len)
        line_len = len(longest_line)

        output_buffer.append(make_line(0, line_len))
        first = True
        for line in input_buffer:
            output_buffer.append(make_linetext(line, line_len))
            if first:
                first = False
                output_buffer.append(make_line(1, line_len))

        output_buffer.append(make_line(2, line_len))

        return output_buffer

       


