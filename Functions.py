
import time 
from collections import deque


class MinHeap:
    def __init__(self, goalstate, comparar):
        self.datos = [None]
        self.tamaño = 0
        self.comparador = comparar
        self.goalstate = goalstate

    def __len__(self):
        return self.tamaño

    def __contains__(self, item):
        return item in self.datos

    def __str__(self):
        return str(self.datos)

    def _compare(self, x, y):
        x = self.comparador(self.datos[x], self.goalstate)
        y = self.comparador(self.datos[y], self.goalstate)

        if x < y:
            return True
        else:
            return False

    def getpos(self, x):
        for i in range(self.tamaño+1):
            if x == self.datos[i]:
                return i
        return None

    def _upHeap(self, i):
        while i > 1 and self._compare(i, int(i/2)):
            self._swap(i, int(i/2))
            i = int(i/2)

    def _downHeap(self, i):
        tamaño = self.tamaño
        while 2*i <= tamaño:
            j = 2*i
            if j < tamaño and self._compare(j+1, j):
                j += 1
            if self._compare(i, j):
                break
            self._swap(i, j)
            i = j

    def _swap(self, i, j):
        t = self.datos[i]
        self.datos[i] = self.datos[j]
        self.datos[j] = t

    def push(self, x):
        self.tamaño += 1
        self.datos.append(x)
        self._upHeap(self.tamaño)

    def pop(self):
        if self.tamaño < 1:
            return None
        t = self.datos[1]
        self.datos[1] = self.datos[self.tamaño]
        self.datos[self.tamaño] = t
        self.tamaño -= 1
        self._downHeap(1)
        self.datos.pop()
        return t

    def peek(self):
        if self.tamaño < 1:
            return None
        return self.datos[1]


# comparadores
def hamming(inicialState, goalstate):
    inicial = inicialState.estado
    goal = goalstate.estado
    depth = inicialState.profundidade
    sum = 0
    for x, y in zip(goal, inicial):
        if x != y and x != '0':
            sum += 1
    return sum + depth


def manhattan(inicialState, goalstate):
    inicial = inicialState.estado
    goal = goalstate.estado
    depth = inicialState.profundidade
    sum = 0
    for i in range(16):
        if goal[i] == '0':
            continue
        x1, y1 = (int(i / 4), i % 4)
        for j in range(16):
            if goal[i] == inicial[j]:
                x2, y2 = (int(j / 4), j % 4)
                sum += abs(x1 - x2) + abs(y1 - y2)
                break
    return sum + depth

#Algoritmos

# Primero en Anchura
def bfs(inicialState, goalstate):
  
    total_nos = 1
    frontera = deque()
    frontera.append(inicialState)

    while len(frontera) > 0:
        state = frontera.popleft()

        if goalstate == state:
            return state.backtrack, total_nos
        for Hijo in state.moves():
            total_nos += 1
            frontera.append(Hijo)
        del(state)
    return False, total_nos


#Primero el mejor
def guloso(inicialState, goalstate, comparador):
    total_nos = 1
    state = inicialState

    while state != goalstate:
        Hijos = state.moves()
        state = Hijos.pop()
        for x in Hijos:
            total_nos += 1
            if comparador(x, goalstate) < comparador(state, goalstate):
                state = x

    return state.backtrack, total_nos

#A*
def astar(inicialState, goalstate, comparador):
    total_nos = 1
    frontera = MinHeap(goalstate, comparador)
    frontera.push(inicialState)
    visitados = set()

    while len(frontera) > 0:
        state = frontera.pop()
        visitados.add(state)

        if goalstate == state:
            return state.backtrack, total_nos

        for Hijo in state.moves():
            total_nos += 1
            if Hijo not in frontera and Hijo not in visitados:
                frontera.push(Hijo)
            elif Hijo in frontera:
                i = frontera.getpos(Hijo)
                if frontera.datos[i].profundidade > Hijo.profundidade:
                    frontera.datos[i] = Hijo
                    frontera._upHeap(i)

    return False, total_nos
