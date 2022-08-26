
from src.Interfaces.Instruccion import Instruccion


class ModificarValor(Instruccion):

    def __init__(self, fila, columna, variable, exp, newValue):
        self.fila = fila
        self.columna = columna
        self.variable = variable
        self.exp = exp
        self.newValue = newValue


    def ejecutar(self, entorno):
        pass