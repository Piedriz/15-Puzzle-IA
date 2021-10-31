
import copy


class Tablero:
    def __init__(self, arg, parent=None, depth=0):
        self.estado = arg
        self._findx()
        self.hijos = []
        self.backtrack = parent
        self.profundidade = depth


    def __hash__(self):
        return hash(''.join(self.estado))

    def __copy__(self):
        return Tablero(self.estado)

    def __str__(self):
        text = """┌──┬──┬──┬──┐
│{}│{}│{}│{}│
├──┼──┼──┼──┤
│{}│{}│{}│{}│
├──┼──┼──┼──┤
│{}│{}│{}│{}│
├──┼──┼──┼──┤
│{}│{}│{}│{}│
└──┴──┴──┴──┘""" \
            .format(self.estado[0].rjust(2, '0'), self.estado[1].rjust(2, '0'), self.estado[2].rjust(2, '0'),
                    self.estado[3].rjust(2, '0'),
                    self.estado[4].rjust(2, '0'), self.estado[5].rjust(2, '0'), self.estado[6].rjust(2, '0'),
                    self.estado[7].rjust(2, '0'),
                    self.estado[8].rjust(2, '0'), self.estado[9].rjust(2, '0'), self.estado[10].rjust(2, '0'),
                    self.estado[11].rjust(2, '0'),
                    self.estado[12].rjust(2, '0'), self.estado[13].rjust(2, '0'), self.estado[14].rjust(2, '0'),
                    self.estado[15].rjust(2, '0')).replace("00", "  ")
        return text

    def __repr__(self):
        return str(self.estado)

    def __eq__(self, other):
        return self.estado == other

    def _findx(self):
        i = 0
        while self.estado[i] != '0':
            i += 1
        self.x, self.y = (int(i / 4), i % 4)

  

    # Definiendo los movimientos
    def _left(self):
        move = copy.deepcopy(self.estado)
        btrack = copy.deepcopy(self.backtrack)
        if btrack is None:
            btrack = ['Izquierda']
        else:
            btrack.append('Izquierda')
        if self.y != 0:
            move[self.x * 4 + self.y] = move[self.x * 4 + self.y - 1]
            move[self.x * 4 + self.y - 1] = '0'
            tleft = Tablero(move, parent=btrack, depth=self.profundidade + 1)
            self.hijos.append(tleft)

    def _right(self):
        move = copy.deepcopy(self.estado)
        btrack = copy.deepcopy(self.backtrack)
        if btrack is None:
            btrack = ['Derecha']
        else:
            btrack.append('Derecha')
        if self.y != 3:
            move[self.x * 4 + self.y] = move[self.x * 4 + self.y + 1]
            move[self.x * 4 + self.y + 1] = '0'
            tright = Tablero(move, parent=btrack, depth=self.profundidade + 1)
            self.hijos.append(tright)

    def _up(self):
        move = copy.deepcopy(self.estado)
        btrack = copy.deepcopy(self.backtrack)
        if btrack is None:
            btrack = ['Arriba']
        else:
            btrack.append('Arriba')
        if self.x != 0:
            move[self.x * 4 + self.y] = move[(self.x - 1) * 4 + self.y]
            move[(self.x - 1) * 4 + self.y] = '0'
            tup = Tablero(move, parent=btrack, depth=self.profundidade + 1)
            self.hijos.append(tup)

    def _down(self):
        move = copy.deepcopy(self.estado)
        btrack = copy.deepcopy(self.backtrack)
        if btrack is None:
            btrack = ['Abajo']
        else:
            btrack.append('Abajo')
        if self.x != 3:
            move[self.x * 4 + self.y] = move[(self.x + 1) * 4 + self.y]
            move[(self.x + 1) * 4 + self.y] = '0'
            tdown = Tablero(move, parent=btrack, depth=self.profundidade + 1)
            self.hijos.append(tdown)

    def moves(self):
        if self.profundidade > 1:
            last = self.backtrack[self.profundidade-1]
        else:
            last = "0"
        if last != "Derecha":
            self._left()
        if last != "Izquierda":
            self._right()
        if last != "Abajo":
            self._up()
        if last != "Arriba":
            self._down()
        return self.hijos
