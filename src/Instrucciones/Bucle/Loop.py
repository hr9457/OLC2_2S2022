from src.Interfaces.Instruccion import Instruccion


class Loop(Instruccion):

    def __init__(self, fila, columna, nodo):
        self.fila = fila
        self.columna = columna
        self.nodo = nodo


    def ejecutar(self, entorno):
        pass
